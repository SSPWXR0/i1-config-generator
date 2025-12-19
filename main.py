"""
Weather Location Configuration Generator

Searches for locations, finds nearby cities using BFS traversal,
and queries local database records.
"""

from __future__ import annotations

import asyncio
import math
import sqlite3
from collections import deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterator

import aiohttp
import requests

API_KEY = "e1f10a1e78da46f5b10a1e78da96f525"
DB_PATH = Path("./LFRecord.db")

BASE_URL = "https://api.weather.com/v3"
LOCATION_SEARCH_ENDPOINT = f"{BASE_URL}/location/search"
NEARBY_ENDPOINT = f"{BASE_URL}/location/near"

EXCLUDED_STATION_KEYWORDS = frozenset([
    "Rcs", "East", "PFRA", "CS", "AWS", "Marine", "CDA", "West", "(Autob)"
])


class DistanceUnit(Enum):
    """Supported distance units for calculations."""
    KILOMETERS = "m"
    MILES = "e"
    MILES_ALT = "h"
    METERS = "s"


@dataclass
class SearchConfig:
    """Configuration for nearby city search."""
    max_distance: float = 500.0
    max_results: int = 8
    min_spacing: float = 2.0


@dataclass(frozen=True)
class Coordinates:
    """Immutable geographic coordinates."""
    latitude: float
    longitude: float

    @property
    def as_tuple(self) -> tuple[float, float]:
        return (self.latitude, self.longitude)


@dataclass
class City:
    """Represents a city/location with geographic data."""
    name: str
    state_province: str
    country: str
    coords: Coordinates
    distance_to_origin: float = 0.0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "stateProvince": self.state_province,
            "country": self.country,
            "lat": self.coords.latitude,
            "lon": self.coords.longitude,
            "distToOrigin": self.distance_to_origin
        }

@contextmanager
def get_db_connection(db_path: Path = DB_PATH) -> Iterator[sqlite3.Connection]:
    """Context manager for database connections with automatic cleanup."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def get_record_by_location_id(location_id: str) -> dict | None:
    """
    Retrieve a record from LFRecord.db by location ID.

    Args:
        location_id: The location ID to search for.

    Returns:
        Dictionary of record data, or None if not found.
    """
    with get_db_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM LFRecord WHERE locId = ?",
            (location_id,)
        )
        row = cursor.fetchone()

    if row is None:
        return None

    record = dict(row)
    print(f"Found record: {record}")
    return record

class WeatherAPIClient:
    """Client for Weather.com API interactions."""

    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key

    def search_location(self, query: str) -> dict:
        """
        Search for a location by name.

        Args:
            query: Location name to search for.

        Returns:
            JSON response with location data.
        """
        params = {
            "query": query,
            "locationType": "city",
            "language": "en-US",
            "format": "json",
            "apiKey": self.api_key
        }
        response = requests.get(LOCATION_SEARCH_ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()

    async def fetch_nearby_locations(
        self,
        session: aiohttp.ClientSession,
        coords: Coordinates
    ) -> dict:
        """
        Fetch nearby observation stations for given coordinates.

        Args:
            session: Active aiohttp session.
            coords: Geographic coordinates to search around.

        Returns:
            JSON response with nearby location data.
        """
        url = (
            f"{NEARBY_ENDPOINT}"
            f"?geocode={coords.latitude},{coords.longitude}"
            "&product=observation"
            "&format=json"
            f"&apiKey={self.api_key}"
        )
        async with session.get(url) as response:
            return await response.json()

def vincenty_distance(
    point1: Coordinates,
    point2: Coordinates,
    unit: DistanceUnit = DistanceUnit.MILES
) -> float:
    """
    Calculate geodesic distance using Vincenty's inverse formula (WGS-84).

    Args:
        point1: First geographic point.
        point2: Second geographic point.
        unit: Desired output unit.

    Returns:
        Distance between points in specified unit.

    Raises:
        RuntimeError: If formula fails to converge.
    """
    SEMI_MAJOR_AXIS = 6378137.0
    FLATTENING = 1 / 298.257223563
    SEMI_MINOR_AXIS = (1 - FLATTENING) * SEMI_MAJOR_AXIS

    φ1 = math.radians(point1.latitude)
    φ2 = math.radians(point2.latitude)
    L = math.radians(point2.longitude - point1.longitude)

    U1 = math.atan((1 - FLATTENING) * math.tan(φ1))
    U2 = math.atan((1 - FLATTENING) * math.tan(φ2))

    sin_U1, cos_U1 = math.sin(U1), math.cos(U1)
    sin_U2, cos_U2 = math.sin(U2), math.cos(U2)

    λ = L
    max_iterations = 100

    for _ in range(max_iterations):
        sin_λ = math.sin(λ)
        cos_λ = math.cos(λ)

        sin_σ = math.sqrt(
            (cos_U2 * sin_λ) ** 2 +
            (cos_U1 * sin_U2 - sin_U1 * cos_U2 * cos_λ) ** 2
        )

        if sin_σ == 0:
            return 0.0

        cos_σ = sin_U1 * sin_U2 + cos_U1 * cos_U2 * cos_λ
        σ = math.atan2(sin_σ, cos_σ)

        sin_α = (cos_U1 * cos_U2 * sin_λ) / sin_σ
        cos2_α = 1 - sin_α ** 2

        if cos2_α == 0:
            cos_2σm = 0
        else:
            cos_2σm = cos_σ - (2 * sin_U1 * sin_U2) / cos2_α

        C = (FLATTENING / 16) * cos2_α * (4 + FLATTENING * (4 - 3 * cos2_α))

        λ_prev = λ
        λ = L + (1 - C) * FLATTENING * sin_α * (
            σ + C * sin_σ * (
                cos_2σm + C * cos_σ * (-1 + 2 * cos_2σm ** 2)
            )
        )

        if abs(λ - λ_prev) <= 1e-12:
            break
    else:
        raise RuntimeError("Vincenty's formula failed to converge")

    u2 = cos2_α * (SEMI_MAJOR_AXIS ** 2 - SEMI_MINOR_AXIS ** 2) / (SEMI_MINOR_AXIS ** 2)
    A = 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))

    Δσ = B * sin_σ * (
        cos_2σm + (B / 4) * (
            cos_σ * (-1 + 2 * cos_2σm ** 2) -
            (B / 6) * cos_2σm * (-3 + 4 * sin_σ ** 2) * (-3 + 4 * cos_2σm ** 2)
        )
    )

    distance_meters = SEMI_MINOR_AXIS * A * (σ - Δσ)

    conversions = {
        DistanceUnit.KILOMETERS: distance_meters / 1000,
        DistanceUnit.MILES: distance_meters / 1609.344,
        DistanceUnit.MILES_ALT: distance_meters / 1609.344,
        DistanceUnit.METERS: distance_meters,
    }
    return conversions.get(unit, distance_meters)

@dataclass
class NearbyCityFinder:
    """BFS-based finder for nearby cities within distance constraints."""

    origin: Coordinates
    origin_name: str
    config: SearchConfig = field(default_factory=SearchConfig)
    api_client: WeatherAPIClient = field(default_factory=WeatherAPIClient)

    async def find(self) -> list[City]:
        """
        Find nearby cities using breadth-first search.
        Continues searching aggressively until max_results is reached.

        Returns:
            List of nearby cities sorted by distance.
        """
        nearby_cities: list[City] = []
        visited_coords: set[tuple[float, float]] = set()
        queue: deque[Coordinates] = deque([self.origin])
        search_attempts = 0
        max_attempts = 50

        async with aiohttp.ClientSession() as session:
            while queue and len(nearby_cities) < self.config.max_results and search_attempts < max_attempts:
                search_attempts += 1
                current = queue.popleft()
                cities_from_location = await self._process_location(
                    session, current, nearby_cities, visited_coords
                )

                for city in cities_from_location:
                    if len(nearby_cities) < self.config.max_results:
                        nearby_cities.append(city)
                        queue.append(city.coords)
                    else:
                        break

                if len(queue) < 3 and len(nearby_cities) < self.config.max_results:
                    for city in nearby_cities[-min(3, len(nearby_cities)):]:
                        queue.append(city.coords)

        return sorted(nearby_cities, key=lambda c: c.distance_to_origin)

    async def _process_location(
        self,
        session: aiohttp.ClientSession,
        coords: Coordinates,
        existing_cities: list[City],
        visited: set[tuple[float, float]]
    ) -> list[City]:
        """Process a location and extract valid nearby cities."""
        data = await self.api_client.fetch_nearby_locations(session, coords)
        locations = data.get("location", {})

        candidates: list[City] = []
        names = locations.get("stationName", [])

        for i, name in enumerate(names):
            city = self._extract_city(locations, i, name)
            if city and self._is_valid_city(city, existing_cities, visited):
                visited.add(city.coords.as_tuple)
                candidates.append(city)

        return candidates

    def _extract_city(
        self,
        locations: dict,
        index: int,
        name: str
    ) -> City | None:
        """Extract city data from API response at given index."""
        if name == self.origin_name:
            return None

        if any(kw in name for kw in EXCLUDED_STATION_KEYWORDS):
            return None

        try:
            coords = Coordinates(
                latitude=locations["latitude"][index],
                longitude=locations["longitude"][index]
            )
            distance = round(vincenty_distance(coords, self.origin))

            return City(
                name=name,
                state_province=locations.get("adminDistrictCode", [""])[index] or "",
                country=locations.get("countryCode", [""])[index],
                coords=coords,
                distance_to_origin=distance
            )
        except (IndexError, KeyError):
            return None

    def _is_valid_city(
        self,
        city: City,
        existing: list[City],
        visited: set[tuple[float, float]]
    ) -> bool:
        """Check if city meets all validity criteria."""
        if city.coords.as_tuple in visited:
            return False

        max_dist = self.config.max_distance
        if len(existing) < self.config.max_results // 2:
            max_dist *= 2
        
        if city.distance_to_origin > max_dist:
            return False

        if existing:
            min_spacing = self.config.min_spacing
            if len(existing) >= self.config.max_results * 0.75:
                min_spacing = min_spacing / 2
                
            for existing_city in existing:
                spacing = vincenty_distance(city.coords, existing_city.coords)
                if spacing < min_spacing:
                    return False

        return True


async def get_nearby_cities(
    location_data: dict,
    max_distance: float = 500,
    max_results: int = 8,
    min_spacing: float = 2,
) -> list[dict]:
    """
    Find nearby cities for a given location.

    Args:
        location_data: Location data from search API.
        max_distance: Maximum distance from origin in miles.
        max_results: Maximum number of cities to return.
        min_spacing: Minimum distance between cities in miles.

    Returns:
        List of nearby city dictionaries.
    """
    loc = location_data["location"]
    origin = Coordinates(
        latitude=loc["latitude"][0],
        longitude=loc["longitude"][0]
    )
    origin_name = loc["city"][0]

    finder = NearbyCityFinder(
        origin=origin,
        origin_name=origin_name,
        config=SearchConfig(
            max_distance=max_distance,
            max_results=max_results,
            min_spacing=min_spacing
        )
    )

    cities = await finder.find()
    return [city.to_dict() for city in cities]

def prompt_for_location() -> dict:
    """Prompt user for location and return search results."""
    location_name = input("Enter the location name: ")
    client = WeatherAPIClient()
    
    try:
        result = client.search_location(location_name)
        
        if not result or 'location' not in result:
            print(f"ERROR: No results found for '{location_name}'")
            print(f"Raw API response: {result}")
            raise ValueError(f"Location '{location_name}' not found")
        
        loc = result.get('location', {})
        if not loc.get('city') or len(loc.get('city', [])) == 0:
            print(f"ERROR: Location data is empty for '{location_name}'")
            print(f"Raw location data: {loc}")
            raise ValueError(f"No location data for '{location_name}'")
        
        print(f"✓ Found: {loc.get('city', [''])[0]}, {loc.get('adminDistrictCode', [''])[0]} {loc.get('countryCode', [''])[0]}")
        print(f"  Location ID: {loc.get('locId', [''])[0][:8]}")
        print(f"  Coordinates: {loc.get('latitude', [0])[0]}, {loc.get('longitude', [0])[0]}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ ERROR searching for location '{location_name}':")
        print(f"   {str(e)}")
        print(f"\nTip: Try being more specific (e.g., 'Dildo, NL' or 'Dildo, Newfoundland')")
        raise

@dataclass
class LocationRecord:
    """Parsed location record with relevant fields for config generation."""
    loc_id: str
    name: str
    coop_id: str | None = None
    teccis: list[str] = field(default_factory=list)
    zone_id: str | None = None
    county_id: str | None = None
    county_name: str | None = None
    climate_id: str | None = None
    airport_id: str | None = None
    obs_station: str | None = None
    state_code: str | None = None
    country_code: str | None = None
    lat: float | None = None
    lon: float | None = None

    @classmethod
    def from_db_record(cls, record: dict, name: str = "") -> "LocationRecord":
        """Parse a database record into a LocationRecord."""

        teccis = []
        for key in ("primTecci",):
            if record.get(key):
                teccis.append(record[key])

        lat = None
        lon = None
        if record.get("lat"):
            try:
                lat = float(record["lat"])
            except (ValueError, TypeError):
                pass
        if record.get("long"):
            try:
                lon = float(record["long"])
            except (ValueError, TypeError):
                pass

        return cls(
            loc_id=record.get("locId", ""),
            name=name or record.get("prsntNm", ""),
            coop_id=record.get("coopId"),
            teccis=teccis,
            zone_id=record.get("zoneId"),
            county_id=record.get("cntyId"),
            county_name=record.get("cntyNm"),
            climate_id=record.get("cliStn"),
            airport_id=record.get("arptId"),
            obs_station=record.get("obsStn"),
            state_code=record.get("stCd"),
            country_code=record.get("cntryCd"),
            lat=lat,
            lon=lon,
        )


def quote_list(items: list[str]) -> str:
    """Format list items as quoted strings."""
    return ", ".join(f"'{item}'" for item in items if item)


@dataclass
class AggregatedConfig:
    """Aggregated configuration data from all locations."""
    coop_ids: list[str] = field(default_factory=list)
    tecci_ids: list[str] = field(default_factory=list)
    zone_ids: list[str] = field(default_factory=list)
    county_ids: list[str] = field(default_factory=list)
    county_names: dict[str, str] = field(default_factory=dict)
    climate_ids: list[str] = field(default_factory=list)
    airport_ids: list[str] = field(default_factory=list)
    name: str = ""
    state_code: str = ""
    country_code: str = ""
    lat : float | None = None
    lon : float | None = None

    def add_record(self, record: LocationRecord) -> None:
        """Add a location record's data to the aggregated config."""

        if not self.state_code and record.state_code:
            self.state_code = record.state_code
        
        if not self.country_code and record.country_code:
            self.country_code = record.country_code

        if record.coop_id and record.coop_id not in self.coop_ids:
            self.coop_ids.append(record.coop_id)

        for tecci in record.teccis:
            if tecci not in self.tecci_ids:
                self.tecci_ids.append(tecci)

        if record.zone_id and record.zone_id not in self.zone_ids:
            self.zone_ids.append(record.zone_id)

        if record.county_id and record.county_id not in self.county_ids:
            self.county_ids.append(record.county_id)
            if record.county_name:
                self.county_names[record.county_id] = record.county_name

        if record.climate_id and record.climate_id not in self.climate_ids:
            self.climate_ids.append(record.climate_id)

        if record.airport_id and record.airport_id not in self.airport_ids:
            self.airport_ids.append(record.airport_id)
        
        if self.lat is None and record.lat is not None:
            self.lat = record.lat
        if self.lon is None and record.lon is not None:
            self.lon = record.lon


def compile_i1_interest_list(config: AggregatedConfig) -> str:
    
    output_interest_list = f"""wxdata.setInterestList('airportId','1',[{quote_list(config.airport_ids) if config.airport_ids else ''}])
wxdata.setInterestList('coopId','1',[{quote_list(config.coop_ids)}])
wxdata.setInterestList('indexId','1',[''])
#wxdata.setInterestList('pollenId','1',[])
wxdata.setInterestList('obsStation','1',[{quote_list(config.tecci_ids)}])
wxdata.setInterestList('climId','1',[{quote_list(config.climate_ids)}])
wxdata.setInterestList('zone','1',[{quote_list(config.zone_ids)}])
#wxdata.setInterestList('aq','1',[])
wxdata.setInterestList('skiId','1',[])
wxdata.setInterestList('county','1',[{quote_list(config.county_ids)}])"""
    
    return output_interest_list

def compile_i1_currentconditions(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    loc_name = config.name
    output_current_conditions = f"""d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.locName = ['{loc_name}']
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.locName = ['{loc_name}']
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
d = twc.Data()
d.climId = '{config.climate_ids[0] if config.climate_ids else ""}'
d.latitude = {config.lat}
d.longitude = {config.lon}
dsm.set('Config.1.Ldl_SunriseSunset', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.obsLocName = ['{loc_name}']
dsm.set('Config.1.Ldl_CurrentApparentTemp', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['{config.tecci_ids[0] if config.tecci_ids else ""}']
d.obsLocName = ['{loc_name}']
dsm.set('Config.1.Ldl_CurrentMTDPrecip', d, 0, 1)
#
d = twc.Data()
d.obsStation = '{config.tecci_ids[0] if config.tecci_ids else ""}'
d.climId = ['{config.climate_ids[0] if config.climate_ids else ""}']
d.latitude = {config.lat}
d.longitude = {config.lon}
d.locName = '{loc_name.upper()}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Local_Climatology', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids)}]
d.locName = [{quote_list([record.name for record in all_records])}]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)"""
    return output_current_conditions

def compile_i1_forecast(config: AggregatedConfig) -> str:
    loc_name = config.name
    output_forecast = f"""d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
d = twc.Data()
d.location = '{loc_name.upper()}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name.upper()}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = '{loc_name.upper()}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{config.name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.1.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.1.Ldl_SummaryForecast', d, 0, 1)
#
"""
    return output_forecast

def compile_i1_metadata(config: AggregatedConfig) -> str:
    """Generate metadata configuration settings."""
    county_list = [(cid, cname) for cid, cname in config.county_names.items()]
    county_list_str = str(county_list) if county_list else "[]"
    
    output_metadata = f"""dsm.set('Config.1.countyNameList',{county_list_str}, 0)
dsm.set('dmaCode','None', 0)
dsm.set('secondaryObsStation','{config.tecci_ids[1] if len(config.tecci_ids) > 1 else config.tecci_ids[0] if config.tecci_ids else ""}', 0)
dsm.set('primaryClimoStation','{config.climate_ids[0] if config.climate_ids else ""}', 0)
dsm.set('primaryIndexId','{config.airport_ids[0] if config.airport_ids else ""}', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','{config.state_code}', 0)
dsm.set('primaryAqStation','None', 0)
dsm.set('primPollenSiteName','{config.name}', 0)
dsm.set('primaryCoopId','{config.coop_ids[0] if config.coop_ids else ""}', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','{config.airport_ids[0] if config.airport_ids else ""}', 0)
dsm.set('primaryCounty','{config.county_ids[0] if config.county_ids else ""}', 0)
dsm.set('primaryObsStation','{config.tecci_ids[0] if config.tecci_ids else ""}', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','{config.airport_ids[0] if config.airport_ids else ""}', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',{config.lon}, 0)
dsm.set('primaryLat',{config.lat}, 0)
dsm.set('primaryForecastName','{config.name}', 0)
dsm.set('primaryZone','{config.zone_ids[0] if config.zone_ids else ""}', 0)
dsm.set('climoRegion','3', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('countryCode','{config.country_code}', 0)"""
    return output_metadata

def compile_i1_airport_data(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    """Generate airport data tag configuration."""
    airport_records = [r for r in all_records if r.airport_id]
    
    airport_ids = [r.airport_id for r in airport_records]
    airport_names = [r.name for r in airport_records]
    airport_teccis = [r.teccis[0] if r.teccis else "" for r in airport_records]
    
    output = f"""scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = [{quote_list(airport_ids)}]
d.airportLocName = [{quote_list(airport_names)}]
d.obsStation = [{quote_list(airport_teccis)}]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)"""
    return output

def compile_full_config(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    """Compile all configuration sections into a complete file."""
    from datetime import datetime
    
    sections = []
    
    start_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    sections.append(f"# Created on {start_time}")
    sections.append("# SCMT Configuration File for IntelliStar 1 Domestic")
    sections.append("# Generated by IntelliStar Config Generator by @sspwxr (raii)")
    sections.append("Log.info('scmt config started')")
    sections.append("#")
    sections.append("def scmtRemove(key):")
    sections.append("    try:")
    sections.append("        dsm.remove(key)")
    sections.append("    except:")
    sections.append("        pass")
    sections.append("#")
    sections.append("")
    sections.append("#")
    sections.append("# Beginning of SCMT deployment")
    sections.append("import os")
    sections.append("dsm.set('scmt_configType', 'domestic',0)")
    sections.append("dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)")
    sections.append("#")
    sections.append(compile_i1_interest_list(config))
    sections.append(compile_i1_metadata(config))
    sections.append("#")
    sections.append(compile_i1_airport_data(config, all_records))
    sections.append("#")
    sections.append("#")
    sections.append(compile_i1_currentconditions(config, all_records))
    sections.append("#")
    sections.append(compile_i1_forecast(config))
    sections.append("#")
    
    end_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    sections.append("Log.info('scmt config completed')")
    sections.append(f"# Finished generation on {end_time}")
    
    return "\n".join(sections)

def main() -> None:
    """Main entry point for the configuration generator."""
    locale_data = prompt_for_location()

    main_location_name = locale_data["location"]["city"][0]
    main_lat = locale_data["location"]["latitude"][0]
    main_lon = locale_data["location"]["longitude"][0]
    main_state = locale_data["location"].get("adminDistrictCode", [""])[0]
    main_country = locale_data["location"].get("countryCode", [""])[0]

    nearby = asyncio.run(get_nearby_cities(locale_data))
    print(f"\nNearby cities ({len(nearby)} found):")
    for city in nearby:
        print(f"  - {city['name']}, {city['stateProvince']} "
              f"({city['distToOrigin']} miles)")

    config = AggregatedConfig()
    all_records: list[LocationRecord] = []

    config.name = main_location_name
    config.lat = main_lat
    config.lon = main_lon
    config.state_code = main_state
    config.country_code = main_country

    location_id = locale_data["location"]["locId"][0][:8]
    print(f"\nMain Location ID: {location_id}")
    
    main_record_data = get_record_by_location_id(location_id)
    if main_record_data:
        main_record = LocationRecord.from_db_record(
            main_record_data, 
            name=main_location_name
        )
        all_records.append(main_record)
        config.add_record(main_record)
        print(f"  ✓ Database record found")
        print(f"  TECCIs: {main_record.teccis}")
        print(f"  Coop ID: {main_record.coop_id}")
        print(f"  Zone ID: {main_record.zone_id}")
        print(f"  Airport ID: {main_record.airport_id}")
    else:
        print(f"  ⚠ No database record found for {main_location_name}")
        print(f"  → Will use data from nearby locations")

    client = WeatherAPIClient()
    processed_loc_ids = {location_id}
    
    for city in nearby:
        try:
            search_result = client.search_location(city['name'] + ", " + city['country'])
            loc_id = search_result['location']['locId'][0][:8]
            
            if loc_id in processed_loc_ids:
                print(f"\nSkipping duplicate: {city['name']} (ID: {loc_id})")
                continue
            
            processed_loc_ids.add(loc_id)
            
            print(f"\nLooking up: {city['name']} (ID: {loc_id})")
            record_data = get_record_by_location_id(loc_id)
            
            if record_data:
                record = LocationRecord.from_db_record(record_data, name=city['name'])
                all_records.append(record)
                config.add_record(record)
                print(f"  TECCIs: {record.teccis}")
                print(f"  Coop ID: {record.coop_id}")
                print(f"  Zone ID: {record.zone_id}")
                print(f"  Airport ID: {record.airport_id}")
            else:
                print(f"  No record found")
        except Exception as e:
            print(f"  Error looking up {city['name']}: {e}")

    print("\n")
    print("AGGREGATED CONFIGURATION")
    print("=" * 60)
    print(f"Total locations processed: {len(all_records)}")
    print(f"Airport IDs: {config.airport_ids}")
    print(f"Coop IDs: {config.coop_ids}")
    print(f"TECCI IDs: {config.tecci_ids}")
    print(f"Zone IDs: {config.zone_ids}")
    print(f"County IDs: {config.county_ids}")
    print(f"Climate IDs: {config.climate_ids}")

    print("\n")
    print(f"INTELLISTAR CONFIG GENERATED FOR {config.name.upper()}")
    print("=" * 60)
    
    full_config = compile_full_config(config, all_records)
    
    output_filename = f"output/{config.name.replace(' ', '_').replace('/', '_')}_i1_config.py"
    Path("output").mkdir(exist_ok=True)
    
    with open(output_filename, 'w') as f:
        f.write(full_config)
    
    print(f"\nConfiguration saved to: {output_filename}")
    print(f"Total lines: {len(full_config.splitlines())}")
    print("\nPreview (first 50 lines):")
    print("-" * 60)
    preview_lines = full_config.splitlines()[:50]
    for line in preview_lines:
        print(line)
    if len(full_config.splitlines()) > 50:
        print(f"\n... ({len(full_config.splitlines()) - 50} more lines)")

if __name__ == "__main__":
    main()
