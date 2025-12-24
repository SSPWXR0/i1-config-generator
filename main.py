"""
Weather Location Configuration Generator

Searches for locations, prompts for nearby cities,
and queries local database records.
"""

from __future__ import annotations

from logging import config
import math
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator
import json

DB_PATH = Path("./LFRecord.db")

with open('./pixelToLatLon.json') as f:
    PIXEL_TO_LATLON = json.load(f)

DOMESTIC_CALIBRATION = PIXEL_TO_LATLON["domestic"]
WEATHERSCAN_CALIBRATION = PIXEL_TO_LATLON["weatherscan"]

_LON_SCALE = 0.0018435216
_LON_OFFSET = -132.836645
_LAT_SCALE = 0.0000390509
_LAT_OFFSET = 0.285417

MAP_PRODUCT_SIZES: dict[str, tuple[int, int]] = {
    "Radar_LocalDoppler": (1440, 822),
    "NationalLdl_DopplerRadar": (1440, 821),
    "Local_MetroDopplerRadar": (1440, 960),
    "Local_MetroForecastMap": (1440, 960),
    "Local_MetroObservationMap": (1440, 960),
    "Local_RegionalDopplerRadar": (3456, 2304),
    "Local_RegionalForecastMap": (5760, 3840),
    "Local_RegionalObservationMap": (5760, 3840),
}

BASEMAP_TILES = {
    "ne": {"width": 19718, "height": 10336, "x_min": 19703, "y_min": 0},
    "nw": {"width": 19703, "height": 10336, "x_min": 0, "y_min": 0},
    "se": {"width": 19718, "height": 10500, "x_min": 19703, "y_min": 10336},
    "sw": {"width": 19703, "height": 10500, "x_min": 0, "y_min": 10336},
}
MERCATOR_MAX_X = 39421
MERCATOR_MAX_Y = 20836

def _lat_to_mercator_y(lat: float) -> float:
    lat_rad = math.radians(lat)
    return math.log(math.tan(math.pi / 4 + lat_rad / 2))


def _mercator_y_to_lat(y: float) -> float:
    return math.degrees(2 * math.atan(math.exp(y)) - math.pi / 2)


def pixel_to_latlon(x: int, y: int) -> tuple[float, float]:

    lon = x * _LON_SCALE + _LON_OFFSET
    mercator_y = y * _LAT_SCALE + _LAT_OFFSET
    lat = _mercator_y_to_lat(mercator_y)
    return (lat, lon)


def latlon_to_pixel(lat: float, lon: float) -> tuple[int, int]:

    x = (lon - _LON_OFFSET) / _LON_SCALE
    mercator_y = _lat_to_mercator_y(lat)
    y = (mercator_y - _LAT_OFFSET) / _LAT_SCALE
    return (round(x), round(y))


def get_tiles_for_coordinate(x: int, y: int) -> list[str]:

    tiles = []
        
    if x < 19703:
        if y < 10336:
            tiles.append("nw")
        else:
            tiles.append("sw")
    else:
        if y < 10336:
            tiles.append("ne")
        else:
            tiles.append("se")
    
    return tiles


def clamp_mapcut_coordinate(cut_x: int, cut_y: int, width: int, height: int) -> tuple[int, int]:

    clamped_x = max(0, cut_x)
    clamped_y = max(0, cut_y)
    
    if clamped_x + width > MERCATOR_MAX_X:
        clamped_x = MERCATOR_MAX_X - width
    
    if clamped_y + height > MERCATOR_MAX_Y:
        clamped_y = MERCATOR_MAX_Y - height
    
    return (clamped_x, clamped_y)


def get_mapcut_coordinate(lat: float, lon: float, product_name: str) -> tuple[int, int]:

    center = latlon_to_pixel(lat, lon)
    size = MAP_PRODUCT_SIZES.get(product_name, (1440, 960))
    cut_x = center[0] - size[0] // 2
    cut_y = center[1] - size[1] // 2
    
    cut_x, cut_y = clamp_mapcut_coordinate(cut_x, cut_y, size[0], size[1])
    
    return (cut_x, cut_y)


def get_all_mapcut_coordinates(lat: float, lon: float) -> dict[str, tuple[int, int]]:

    return {
        product: get_mapcut_coordinate(lat, lon, product)
        for product in MAP_PRODUCT_SIZES
    }

print("=" * 60)
print("IntelliStar Configuration Generator")
print("Created by @sspwxr (raii), version 1-2025-12-20")
print("=" * 60)

@contextmanager
def get_db_connection(db_path: Path = DB_PATH) -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def get_timezone_by_location_id(location_id: str) -> str | None:
    tz = {
        "CST": "CST6CDT",
        "MST": "MST7MDT",
        "PST": "PST8PDT",
        "EST": "EST5EDT",
        "AKST": "AKST9AKDT",
        "HST": "HST10",
    }
    tz_canada = {
        "AB": "America/Edmonton",
        "BC": "America/Vancouver",
        "MB": "America/Winnipeg",
        "NB": "America/Moncton",
        "NL": "America/St_Johns",
        "NS": "America/Halifax",
        "ON": "America/Toronto",
        "PE": "America/Halifax",
        "QC": "America/Montreal",
        "SK": "America/Regina",
        "YT": "America/Whitehorse",
    }
    tz_mexico = {
        "AG": "America/Mexico_City",
        "BC": "America/Tijuana",
        "BS": "America/Mazatlan",
        "CC": "America/Merida",
        "CS": "America/Mexico_City",
        "CH": "America/Chihuahua",
        "CL": "America/Mexico_City",
        "CM": "America/Mexico_City",
        "DG": "America/Monterrey",
        "GT": "America/Mexico_City",
        "GR": "America/Mexico_City",
        "HG": "America/Mexico_City",
        "JA": "America/Mexico_City",
        "EM": "America/Mexico_City",
        "MI": "America/Mexico_City",
        "MO": "America/Mexico_City",
        "NA": "America/Mazatlan",
        "NL": "America/Monterrey",
        "OA": "America/Mexico_City",
        "PU": "America/Mexico_City",
        "QT": "America/Mexico_City",
        "QR": "America/Cancun",
        "SL": "America/Mexico_City",
        "SI": "America/Mazatlan",
        "SO": "America/Hermosillo",
        "TB": "America/Mexico_City",
        "TM": "America/Monterrey",
        "TL": "America/Mexico_City",
        "VE": "America/Mexico_City",
        "YU": "America/Merida",
        "ZA": "America/Mexico_City",
    }


    with get_db_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM LFRecord WHERE locId = ?",
            (location_id,)
        )
        init_fetch = cursor.fetchone()

    if init_fetch is not None:
        country_code = init_fetch["cntryCd"]
        if country_code == "US":
            return tz.get(init_fetch["stCd"], "CST")
        if country_code == "CA":
            return tz_canada.get(init_fetch["stCd"], "America/Regina")
        if country_code == "MX":
            return tz_mexico.get(init_fetch["stCd"], "America/Mexico_City")
        return "CST6CDT"

    timezone = row["timeZone"]
    print(f"Found timezone: {timezone}")
    return timezone

def get_record_by_location_id(location_id: str) -> dict | None:
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


def search_records_by_name(search_term: str) -> list[dict]:

    with get_db_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM LFRecord WHERE prsntNm LIKE ? ORDER BY prsntNm LIMIT 20",
            (f"%{search_term}%",)
        )
        rows = cursor.fetchall()

    return [dict(row) for row in rows]


def search_and_select_location(prompt: str, allow_skip: bool = False, show_coords: bool = False) -> dict | None:

    location_name = input(prompt).strip()
    
    if not location_name:
        if allow_skip:
            print("    Skipped")
        else:
            print("No location name provided")
        return None
    
    matches = search_records_by_name(location_name)
    
    if not matches:
        print(f"    No results found for '{location_name}' in database")
        return None
    
    if len(matches) == 1:
        record = matches[0]
        loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
        print(f"    Found: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
        if show_coords:
            print(f"    Coordinates: {record.get('lat', 'N/A')}, {record.get('long', 'N/A')}")
        return record
    
    print(f"    Multiple matches found ({len(matches)}):")
    print("    Make sure to select locIds like 'CNST0000' for the best data consistency!")
    for idx, record in enumerate(matches, 1):
        loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
        print(f"      [{idx}] {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
    
    skip_text = ", or 'skip'" if allow_skip else ""
    while True:
        selection = input(f"    Select (1-{len(matches)}{skip_text}): ").strip()
        
        if allow_skip and selection.lower() == 'skip':
            print("    Skipped")
            return None
        
        try:
            sel_idx = int(selection) - 1
            if 0 <= sel_idx < len(matches):
                record = matches[sel_idx]
                print(f"    Selected: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')}")
                if show_coords:
                    print(f"    Coordinates: {record.get('lat', 'N/A')}, {record.get('long', 'N/A')}")
                return record
            else:
                print(f"    Invalid selection. Enter 1-{len(matches)}")
        except ValueError:
            print(f"    Invalid input. Enter a number")


def prompt_for_nearby_locations(max_nearby: int = 7) -> list[dict]:

    nearby_locations = []
    
    print(f"\nEnter up to {max_nearby} nearby locations (press Enter to skip, 'back' to go back):")
    
    i = 0
    while i < max_nearby:
        location_name = input(f"  Nearby location {i + 1}: ").strip()
        
        if not location_name:
            print("    Skipped")
            i += 1
            continue
        
        if location_name.lower() == 'back':
            if nearby_locations:
                removed = nearby_locations.pop()
                i -= 1
                print(f"    Removed: {removed.get('prsntNm', 'Unknown')}")
            else:
                print("    Nothing to go back to")
            continue
        
        matches = search_records_by_name(location_name)
        
        if not matches:
            print(f"    No results found for '{location_name}' in database")
            continue
        
        if len(matches) == 1:
            record = matches[0]
            nearby_locations.append(record)
            print(f"    Found: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {record.get('locId', '')[:8]})")
            i += 1
        else:
            print(f"    Multiple matches found ({len(matches)}):")
            print("    Make sure to select locIds like 'CNST0000' for the best data consistency!")
            for idx, record in enumerate(matches, 1):
                loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
                print(f"      [{idx}] {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
            
            while True:
                selection = input(f"    Select (1-{len(matches)}, or 'skip'): ").strip()
                
                if selection.lower() == 'skip':
                    print("    Skipped")
                    break
                
                try:
                    sel_idx = int(selection) - 1
                    if 0 <= sel_idx < len(matches):
                        record = matches[sel_idx]
                        nearby_locations.append(record)
                        print(f"    Selected: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')}")
                        i += 1
                        break
                    else:
                        print(f"    Invalid selection. Enter 1-{len(matches)}")
                except ValueError:
                    print(f"    Invalid input. Enter a number or 'skip'")
    
    return nearby_locations


def prompt_for_location() -> dict | None:
    return search_and_select_location("Enter the location name: ", allow_skip=False, show_coords=True)

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


def get_cityticker_travel_cities(state_code: str, country_code: str) -> str:
    """Get CityTicker travel cities based on region.
    
    Maps states/provinces to regions and returns appropriate travel cities.
    """
    # Define region mappings
    southeast_us = ['FL', 'GA', 'AL', 'MS', 'LA', 'SC', 'NC', 'TN', 'KY', 'VA', 'WV', 'AR']
    northeast_us = ['NY', 'NJ', 'PA', 'CT', 'MA', 'RI', 'NH', 'VT', 'ME', 'DE', 'MD', 'DC']
    midwest_us = ['OH', 'MI', 'IN', 'IL', 'WI', 'MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS']
    southwest_us = ['TX', 'OK', 'NM', 'AZ']
    california = ['CA']
    northwest_us = ['WA', 'OR', 'ID', 'MT', 'WY']
    rocky_mountain = ['CO', 'UT', 'NV']
    
    # Canadian regions
    maritimes = ['NS', 'NB', 'PE', 'NL']
    quebec = ['QC']
    ontario = ['ON']
    prairies = ['MB', 'SK', 'AB']
    british_columbia = ['BC']
    territories = ['YT', 'NT', 'NU']
    
    if country_code == "CA":
        if state_code in maritimes:
            return """d = twc.Data()
d.obsStation = ['T71437008','CYUL','T71300001','T71398004','T71705002','T71609000',]
d.locName = ['Toronto','Montreal','Ottawa','Halifax','Moncton','Saint John',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Toronto','Montreal','Ottawa','Halifax','Moncton','Saint John',]
d.coopId = ['71624000','71627000','71628000','71395000','71706000','71609000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in british_columbia:
            return """d = twc.Data()
d.obsStation = ['CYVR','T71799002','CYXX','CYLW','T71896004','T71887000',]
d.locName = ['Vancouver','Victoria','Abbotsford','Kelowna','Prince George','Kamloops',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Vancouver','Victoria','Abbotsford','Kelowna','Prince George','Kamloops',]
d.coopId = ['71892000','71799000','71108000','71203000','71896000','71887000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in prairies:
            return """d = twc.Data()
d.obsStation = ['CYYC','T71123000','T71513001','T71863000','T71579003','T71251001',]
d.locName = ['Calgary','Edmonton','Saskatoon','Regina','Winnipeg','Lethbridge',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Calgary','Edmonton','Saskatoon','Regina','Winnipeg','Lethbridge',]
d.coopId = ['71877000','71123000','71866000','71863000','71852000','71874000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in quebec:
            return """d = twc.Data()
d.obsStation = ['CYUL','T71578001','CYVO','CYHU','CYMX','CYUY',]
d.locName = ['Montreal','Quebec City','Val-d\\'Or','St. Hubert','Mirabel','Rouyn',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Montreal','Quebec City','Val-d\\'Or','St. Hubert','Mirabel','Rouyn',]
d.coopId = ['71627000','71714000','71725000','71371000','71626000','71733000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        else:
            # Default Canada (Ontario and territories)
            return """d = twc.Data()
d.obsStation = ['T71437008','CYUL','CYVR','T71300001','CYYC','T71579003',]
d.locName = ['Toronto','Montreal','Vancouver','Ottawa','Calgary','Winnipeg',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Toronto','Montreal','Vancouver','Ottawa','Calgary','Winnipeg',]
d.coopId = ['71624000','71627000','71892000','71628000','71877000','71852000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
    else:
        # US regions
        if state_code in southeast_us:
            return """d = twc.Data()
d.obsStation = ['T72219029','T72202000','T72205000','T72327008','T72314004','T72231015',]
d.locName = ['Atlanta','Miami','Orlando','Nashville','Charlotte','New Orleans',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Miami','Orlando','Nashville','Charlotte','New Orleans',]
d.coopId = ['72219013','72202012','72205012','72327013','72314013','72231012',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in northeast_us:
            return """d = twc.Data()
d.obsStation = ['T72503193','T72509060','T72408054','T72405034','T72406000','T72507009',]
d.locName = ['New York','Boston','Philadelphia','Washington','Baltimore','Providence',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York','Boston','Philadelphia','Washington','Baltimore','Providence',]
d.coopId = ['72503094','72509014','72408013','72405093','72406093','72507014',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in california:
            return """d = twc.Data()
d.obsStation = ['T72295000','T72494028','T72290012','T74509014','T72494029','T72483024',]
d.locName = ['Los Angeles','San Francisco','San Diego','San Jose','Oakland','Sacramento',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Los Angeles','San Francisco','San Diego','San Jose','Oakland','Sacramento',]
d.coopId = ['72295000','72294093','72290023','72293090','72294090','72283093',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in northwest_us:
            return """d = twc.Data()
d.obsStation = ['T72793000','T72698008','T72681000','T72785004','T72772024','T72773011',]
d.locName = ['Seattle','Portland','Boise','Spokane','Bozeman','Missoula',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Seattle','Portland','Boise','Spokane','Bozeman','Missoula',]
d.coopId = ['72793024','72698024','72681024','72785024','72677024','72773024',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in midwest_us:
            return """d = twc.Data()
d.obsStation = ['T72530000','T72537001','T72658005','T72524092','T72438000','T72446003',]
d.locName = ['Chicago','Detroit','Minneapolis','Cleveland','Indianapolis','Kansas City',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Chicago','Detroit','Minneapolis','Cleveland','Indianapolis','Kansas City',]
d.coopId = ['72530094','72537094','72658014','72524094','72438093','72446093',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in southwest_us:
            return """d = twc.Data()
d.obsStation = ['T72259000','T72243023','T72278000','T72253000','T72365000','T72270000',]
d.locName = ['Dallas','Houston','Phoenix','San Antonio','Albuquerque','El Paso',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas','Houston','Phoenix','San Antonio','Albuquerque','El Paso',]
d.coopId = ['72258053','72243012','72278023','72253012','72365023','72270023',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif state_code in rocky_mountain:
            return """d = twc.Data()
d.obsStation = ['T72469009','T72572028','T72386000','T72466000','T72476000','T72464000',]
d.locName = ['Denver','Salt Lake City','Las Vegas','Colorado Springs','Grand Junction','Pueblo',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Denver','Salt Lake City','Las Vegas','Colorado Springs','Grand Junction','Pueblo',]
d.coopId = ['72565003','72572024','72386023','72566093','72576093','72564003',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif country_code == "US":
            # Default US (general national cities)
            return """d = twc.Data()
d.obsStation = ['T72503193','T72295000','T72530000','T72259000','T72469009','T72219029',]
d.locName = ['New York','Los Angeles','Chicago','Dallas','Denver','Atlanta',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York','Los Angeles','Chicago','Dallas','Denver','Atlanta',]
d.coopId = ['72503094','72295000','72530094','72258053','72565003','72219013',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
        elif country_code == "MX":
            # Mexico travel cities (only Monterrey has TECCI)
            return """d = twc.Data()
d.obsStation = ['MMMX','MMGL','T76393000','MMTJ','MMUN','MMPR',]
d.locName = ['Mexico City','Guadalajara','Monterrey','Tijuana','Cancun','Puerto Vallarta',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Mexico City','Guadalajara','Monterrey','Tijuana','Cancun','Puerto Vallarta',]
d.coopId = ['76679000','76612000','76394000','76188000','76595000','76654000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""


def get_cityticker_obs_stations(state_code: str, country_code: str) -> list[str]:
    """Get CityTicker obsStation IDs for interest list based on region.
    
    Returns a list of obsStation IDs for the travel cities.
    Prioritizes TECCI format (T + coopId) where available from LFRecord.db,
    falls back to ICAO airport codes when no TECCI exists.
    """
    # Define region mappings (same as get_cityticker_travel_cities)
    southeast_us = ['FL', 'GA', 'AL', 'MS', 'LA', 'SC', 'NC', 'TN', 'KY', 'VA', 'WV', 'AR']
    northeast_us = ['NY', 'NJ', 'PA', 'CT', 'MA', 'RI', 'NH', 'VT', 'ME', 'DE', 'MD', 'DC']
    midwest_us = ['OH', 'MI', 'IN', 'IL', 'WI', 'MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS']
    southwest_us = ['TX', 'OK', 'NM', 'AZ']
    california = ['CA']
    northwest_us = ['WA', 'OR', 'ID', 'MT', 'WY']
    rocky_mountain = ['CO', 'UT', 'NV']
    
    # Canadian regions
    maritimes = ['NS', 'NB', 'PE', 'NL']
    quebec = ['QC']
    ontario = ['ON']
    prairies = ['MB', 'SK', 'AB']
    british_columbia = ['BC']
    territories = ['YT', 'NT', 'NU']
    
    if country_code == "CA":
        if state_code in maritimes:
            # Toronto, Montreal, Ottawa, Halifax, Moncton, Saint John - TECCIs from LFRecord
            return ['T71437008', 'CYUL', 'T71300001', 'T71398004', 'T71705002', 'T71609000']
        elif state_code in quebec:
            # Montreal, Quebec City, Val-d'Or, St. Hubert, Mirabel, Rouyn
            return ['CYUL', 'T71578001', 'CYVO', 'CYHU', 'CYMX', 'CYUY']
        elif state_code in ontario:
            # Toronto, Ottawa, Hamilton, London, Thunder Bay, Sudbury
            return ['T71437008', 'T71300001', 'CYHM', 'CYXU', 'CYQT', 'CYSB']
        elif state_code in prairies:
            # Calgary, Edmonton, Saskatoon, Regina, Winnipeg, Lethbridge
            return ['CYYC', 'T71123000', 'T71513001', 'T71863000', 'T71579003', 'T71251001']
        elif state_code in british_columbia:
            # Vancouver, Victoria, Abbotsford, Kelowna, Prince George, Kamloops
            return ['CYVR', 'T71799002', 'CYXX', 'CYLW', 'T71896004', 'T71887000']
        elif state_code in territories:
            # Whitehorse, Yellowknife, Iqaluit, Dawson City, Inuvik, Norman Wells
            return ['CYXY', 'CYZF', 'CYFB', 'CYDA', 'CYEV', 'CYVQ']
        else:
            # Default Canadian cities - Toronto, Montreal, Vancouver, Ottawa, Calgary, Winnipeg
            return ['T71437008', 'CYUL', 'CYVR', 'T71300001', 'CYYC', 'T71579003']
    elif country_code == "MX":
        # Mexico City, Guadalajara, Monterrey, Tijuana, Cancun, Puerto Vallarta
        # Only Monterrey has TECCI
        return ['MMMX', 'MMGL', 'T76393000', 'MMTJ', 'MMUN', 'MMPR']
    else:
        # US regions - TECCIs from LFRecord where available
        if state_code in southeast_us:
            # Atlanta, Miami, Orlando, Nashville, Charlotte, New Orleans
            return ['T72219029', 'T72202000', 'T72205000', 'T72327008', 'T72314004', 'T72231015']
        elif state_code in northeast_us:
            # New York, Boston, Philadelphia, Washington, Baltimore, Providence
            return ['T72503193', 'T72509060', 'T72408054', 'T72405034', 'T72406000', 'T72507009']
        elif state_code in midwest_us:
            # Chicago, Detroit, Minneapolis, Cleveland, Indianapolis, Kansas City
            return ['T72530000', 'T72537001', 'T72658005', 'T72524092', 'T72438000', 'T72446003']
        elif state_code in southwest_us:
            # Dallas, Houston, Phoenix, San Antonio, Albuquerque, El Paso
            return ['T72259000', 'T72243023', 'T72278000', 'T72253000', 'T72365000', 'T72270000']
        elif state_code in california:
            # Los Angeles, San Francisco, San Diego, San Jose, Oakland, Sacramento
            return ['T72295000', 'T72494028', 'T72290012', 'T74509014', 'T72494029', 'T72483024']
        elif state_code in northwest_us:
            # Seattle, Portland, Boise, Spokane, Bozeman, Missoula
            return ['T72793000', 'T72698008', 'T72681000', 'T72785004', 'T72772024', 'T72773011']
        elif state_code in rocky_mountain:
            # Denver, Salt Lake City, Las Vegas, Colorado Springs, Grand Junction, Pueblo
            return ['T72469009', 'T72572028', 'T72386000', 'T72466000', 'T72476000', 'T72464000']
        else:
            # Default US (general national cities) - NYC, LA, Chicago, Dallas, Denver, Atlanta
            return ['T72503193', 'T72295000', 'T72530000', 'T72259000', 'T72469009', 'T72219029']


def compile_i1_interest_list(config: AggregatedConfig, system_type: str = "domestic") -> str:
    
    if system_type == "weatherscan":
        # International coop IDs for Canada and Mexico forecasts (static)
        intl_coop_ids = [
            # Canada
            '71182000', '71627001', '71852000', '71879001', '71892001', '71913000', '71936000', '71966000',
            # Mexico
            '76255000', '76393000', '76405000', '76595000', '76679001',
        ]
        
        # CityTicker obsStation IDs based on region
        cityticker_obs = get_cityticker_obs_stations(config.state_code, config.country_code)
        
        # Combine all coop IDs
        all_coop_ids = list(config.coop_ids) + intl_coop_ids
        # Combine all obsStation IDs
        all_obs_ids = list(config.tecci_ids) + cityticker_obs
        
        output_interest_list = f"""wxdata.setInterestList('airportId','1',[{quote_list(config.airport_ids) if config.airport_ids else ''}])
wxdata.setInterestList('coopId','1',[{quote_list(all_coop_ids)}])
wxdata.setInterestList('pollenId','1',[])
wxdata.setInterestList('obsStation','1',[{quote_list(all_obs_ids)}])
wxdata.setInterestList('metroId','1',[])
wxdata.setInterestList('climId','1',[{quote_list(config.climate_ids)}])
wxdata.setInterestList('zone','1',[{quote_list(config.zone_ids)}])
wxdata.setInterestList('aq','1',[])
wxdata.setInterestList('skiId','1',[])
wxdata.setInterestList('county','1',[{quote_list(config.county_ids)}])"""
    else:
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

def compile_i1_currentconditions(config: AggregatedConfig, all_records: list[LocationRecord], system_type: str = "domestic") -> str:
    loc_name = config.name
    loc_names = [record.name for record in all_records[:2]]
    
    if system_type == "weatherscan":
        # Get travel cities based on country
        travel_cities_output = get_cityticker_travel_cities(config.state_code, config.country_code)
        
        # Weatherscan uses different current conditions products
        output_current_conditions = f"""d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.locName = [{quote_list(loc_names)}]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.locName = [{quote_list(loc_names)}]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.locName = [{quote_list(loc_names)}]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:4])}]
d.locName = [{quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[4:8]) if len(config.tecci_ids) > 4 else quote_list(config.tecci_ids[:4])}]
d.locName = [{quote_list([record.name for record in all_records[4:8]]) if len(all_records) > 4 else quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:4])}]
d.locName = [{quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[4:8]) if len(config.tecci_ids) > 4 else quote_list(config.tecci_ids[:4])}]
d.locName = [{quote_list([record.name for record in all_records[4:8]]) if len(all_records) > 4 else quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:10])}]
d.locName = [{quote_list([record.name for record in all_records[:10]])}]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
""" + get_cityticker_travel_cities(config.state_code, config.country_code) + f"""
#
d = twc.Data()
d.obsStation = '{config.tecci_ids[0] if config.tecci_ids else ""}'
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.climId = '{config.climate_ids[0] if config.climate_ids else ""}'
d.latitude = {config.lat}
d.longitude = {config.lon}
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)"""
    else:
        # Domestic IntelliStar
        output_current_conditions = f"""d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.locName = [{quote_list([loc_name, loc_name][:len(config.tecci_ids[:2])])}]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.locName = [{quote_list([loc_name, loc_name][:len(config.tecci_ids[:2])])}]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.schedule = [((11,22,16,0,0), (11,24,16,0,0)),((12,15,16,0,0), (1,5,16,0,0)),((5,18,16,0,0), (9,3,16,0,0)),]
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
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.obsLocName = [{quote_list([loc_name, loc_name][:len(config.tecci_ids[:2])])}]
dsm.set('Config.1.Ldl_CurrentApparentTemp', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_CurrentCeiling', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentDewpoint', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentGusts', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentHumidity', d, 0, 1)
ds.commit()
dsm.set('Config.1.Ldl_CurrentPressure', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentSkyTemp', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentVisibility', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentWinds', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:2]) if config.tecci_ids else ""}]
d.obsLocName = [{quote_list([loc_name, loc_name][:len(config.tecci_ids[:2])])}]
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
d.climId = '{config.climate_ids[0] if config.climate_ids else ""}'
d.latitude = {config.lat}
d.longitude = {config.lon}
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids)}]
d.climId = ['{config.climate_ids[0] if config.climate_ids else ""}']
d.latitude = {config.lat}
d.longitude = {config.lon}
d.locName = [{quote_list([record.name for record in all_records[:1]])}]
d.coopId = [{quote_list(config.coop_ids[:1])}]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.1.Local_RecordHighLow', d, 0, 1)
#
d = twc.Data()
d.obsStation = '{config.tecci_ids[0] if config.tecci_ids else ""}'
d.locName = '{loc_name.upper()}'
d.heatIndexThreshold = 102
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
d = twc.Data()
d.zone = '{config.zone_ids[0] if config.zone_ids else ""}'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
d = twc.Data()
d.crawlRate = 3
dsm.set('Config.1.Ldl_HurricaneWatch', d, 0, 1)
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_LocalStarIDMessage', d, 0, 1)
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_NationalStarIDMessage', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(config.tecci_ids[:8])}]
d.locName = [{quote_list([record.name for record in all_records[:8]])}]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
d = twc.Data()
d.activeVocalCue = 1
dsm.set('Config.1.Local_RegionalDopplerRadar', d, 0, 1)"""
    return output_current_conditions

def compile_i1_forecast(config: AggregatedConfig, system_type: str = "domestic") -> str:
    loc_name = config.name
    
    if system_type == "weatherscan":
        # Weatherscan forecast products
        output_forecast = f"""d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name} Area'
d.zone = '{config.zone_ids[0] if config.zone_ids else ""}'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Weatherscan'
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Garden.0.Local_GardeningForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 1
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Toronto','London','Paris',]
d.coopId = ['71624000','03772000','07149000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Cancun','Tokyo','Sydney',]
d.coopId = ['76595000','47671000','94767000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Berlin','Rome','Hong Kong',]
d.coopId = ['10384000','16239000','45005000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.2', d, 0, 1)
#
"""
    else:
        # Domestic IntelliStar forecast products
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
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
d = twc.Data()
d.locName = ['{loc_name.upper()}']
d.coopId = ['{config.coop_ids[0] if config.coop_ids else ""}']
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Ldl_ExtendedForecast', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
d = twc.Data()
d.coopId = '{config.coop_ids[0] if config.coop_ids else ""}'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.1.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.1.Ldl_SummaryForecast', d, 0, 1)
#
"""
    return output_forecast

def compile_i1_metadata(config: AggregatedConfig, system_type: str = "domestic") -> str:
    """Generate metadata configuration settings."""
    county_list = [(cid, cname) for cid, cname in config.county_names.items()]
    county_list_str = str(county_list) if county_list else "[]"

    import random

    random_star_id = random.randint(100000, 999999)

    random_cable_names = [
        "I HATE COMCAST CORPORATION",
        "NOT MARICOM",
        "FOREST CLEARING COMMUNICATIONS",
        "WHO CARES ABOUT THIS THEY ARE ALL OWNED BY ONE BIG CORPORATION ANYWAYS",
        "OPEN YOUR MIND. OPEN YOUR EYES",
        "STEVEN HERE",
        "FEMBOYTELECOM",
        "GENERICABLE INC.",
        "WHOLLY OWNED BY MIST WEATHER MEDIA",
        "ZESTNETTV",
        "ZACHNET TV",
        "The67TV",
        "HI MY NAME IS AUSTIN AND IM A PEDOPHILE, INC",
        "GENERICABLE SUCKS",
        "I HATE ROGERS XFINITY",
        "DECENTRALIZE OUR TELECOMMUNICATIONS",
        "meowwww",
    ]

    random_cable_name = random.choice(random_cable_names)
    
    if system_type == "weatherscan":
        output_metadata = f"""dsm.set('dmaCode','None', 0)
dsm.set('headendName','WXS - {config.name.upper()} - WXS', 0)
dsm.set('cableSystemName','{random_cable_name},', 0)
dsm.set('onAirName','{random_cable_name},', 0)
dsm.set('msoName','{random_cable_name}', 0)
dsm.set('secondaryObsStation','{config.tecci_ids[1] if len(config.tecci_ids) > 1 else config.tecci_ids[0] if config.tecci_ids else ""}', 0)
dsm.set('primaryClimoStation','{config.climate_ids[0] if config.climate_ids else ""}', 0)
dsm.set('stateCode','{config.state_code}', 0)
dsm.set('primaryCoopId','{config.coop_ids[0] if config.coop_ids else ""}', 0)
dsm.set('primarylat',{config.lat}, 0)
dsm.set('primaryCounty','{config.county_ids[0] if config.county_ids else ""}', 0)
dsm.set('primaryObsStation','{config.tecci_ids[0] if config.tecci_ids else ""}', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',{config.lon}, 0)
dsm.set('primaryForecastName','{config.name}', 0)
dsm.set('primaryZone','{config.zone_ids[0] if config.zone_ids else ""}', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('countryCode','{config.country_code}', 0)
dsm.set('headendId','{random_star_id}', 0)
"""

    else:
        output_metadata = f"""dsm.set('Config.1.countyNameList',{county_list_str}, 0)
dsm.set('headendName','DOM - {config.name.upper()} - DOM', 0)
dsm.set('cableSystemName','{random_cable_name},', 0)
dsm.set('onAirName','{random_cable_name},', 0)
dsm.set('msoName','{random_cable_name}', 0)
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
dsm.set('headendId','{random_star_id}', 0)

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


def compile_i1_airport_delays(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    """Generate airport delay conditions configuration."""
    airport_records = [r for r in all_records if r.airport_id]
    
    if not airport_records:
        return ""
    
    airport_ids = [r.airport_id for r in airport_records[:3]]
    airport_teccis = [r.teccis[0] if r.teccis else "" for r in airport_records[:3]]
    airport_names = [r.name + " Arpt" for r in airport_records[:3]]
    display_flags = [1] * len(airport_ids)
    
    output = f"""d = twc.Data()
d.airportId = [{quote_list(airport_ids)}]
d.obsStation = [{quote_list(airport_teccis)}]
d.locName = [{quote_list(airport_names)}]
d.displayFlag = {display_flags}
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)"""
    return output


def compile_i1_travel_forecast(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    """Generate travel forecast configuration."""
    if len(all_records) < 2:
        return ""
    
    travel_records = all_records[1:4]
    loc_names = [r.name for r in travel_records]
    coop_ids = [r.coop_id for r in travel_records if r.coop_id]
    
    if not coop_ids:
        return ""
    
    output = f"""d = twc.Data()
d.locName = [{quote_list(loc_names[:len(coop_ids)])}]
d.coopId = [{quote_list(coop_ids)}]
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)"""
    return output


def compile_i1_scmt_removes(system_type: str) -> str:
    domestic_products = [
        'Config.1.Local_OutdoorActivityForecast',
        'Config.1.Ldl_LocalStarIDMessage',
        'Config.1.Ldl_HurricaneWatch',
        'Config.1.Local_Climatology',
        'Config.1.Cc_CurrentConditions',
        'Config.1.Local_RadarSatelliteComposite',
        'Config.1.Local_NWSHeadlines',
        'Config.1.Ldl_AirportDelayConditions',
        'Config.1.Ldl_CurrentApparentTemp',
        'Config.1.Ldl_UVForecast',
        'Config.1.Ldl_AirQualityForecast',
        'Config.1.Local_EventForecast',
        'Config.1.Local_GetawayForecast',
        'Config.1.Local_LocalObservations',
        'Config.1.TimeTemp_Default',
        'Config.1.Local_TrafficReport',
        'Config.1.Local_TextForecast',
        'Config.1.Ldl_NationalStarIDMessage',
        'Config.1.Ldl_TravelForecast',
        'Config.1.Ldl_SunriseSunset',
        'Config.1.Local_SchoolDayWeather',
        'Config.1.Fcst_TextForecast',
        'Config.1.Local_RecordHighLow',
        'Config.1.Ldl_ExtendedForecast',
        'Config.1.Local_7DayForecast',
        'Config.1.Local_ExtendedForecast',
        'Config.1.Fcst_ExtendedForecast',
        'Config.1.Local_MarineForecast',
        'Config.1.Local_AirQualityForecast',
        'Config.1.Local_HeatSafetyTips',
        'Config.1.Local_Almanac',
        'Config.1.Ldl_TrafficTripTimes',
        'Config.1.Fcst_DaypartForecast',
        'Config.1.Local_CurrentConditions',
        'Config.1.Local_TrafficOverview',
        'Config.1.Local_Tides',
        'Config.1.Local_DaypartForecast',
        'Config.1.Local_TrafficFlow',
        'Config.1.Ldl_CurrentMTDPrecip',
    ]
    weatherscan_products = [
        'Config.1.Travel.LasCrawl_Default',
        'Config.1.Ski.LasCrawl_Default',
        'Config.1.Golf.LasCrawl_Default',
        'Config.1.BoatAndBeach.LasCrawl_Default',
        'Config.1.Health.LasCrawl_Default',
        'Config.1.Traffic.LasCrawl_Default',
        'Config.1.SpanishCore.LasCrawl_Default',
        'Config.1.International.LasCrawl_Default',
        'Config.1.Core.LasCrawl_Default',
        'Config.1.Garden.LasCrawl_Default',
        'Config.1.Airport.LasCrawl_Default',
        'Config.1.LasCrawl_Default',
        'Config.1.Core2Spanish.LasCrawl_Default',
        'Config.1.Core2.LasCrawl_Default',
        'Config.1.Core5.LasCrawl_Default',
        'Config.1.Core4Spanish.LasCrawl_Default',
        'Config.1.Core3.LasCrawl_Default',
        'Config.1.Core1.LasCrawl_Default',
        'Config.1.Core4.LasCrawl_Default',
        'Config.1.LocalBroadcaster.LasCrawl_Default',
        'Config.1.Health.0.Local_SunSafetyFacts.0',
        'Config.1.Airport.0.Local_NationalAirportConditions.0',
        'Config.1.Airport.0.Fcst_DaypartForecast.0',
        'Config.1.Core4.0.Local_CurrentConditions.0',
        'Config.1.Ski.0.Cc_LongCurrentConditions.0',
        'Config.1.Airport.0.Local_NationalAirportConditions.1',
        'Config.1.Traffic.0.Local_TrafficReport.0',
        'Config.1.Ski.0.Local_SkiConditions.0',
        'Config.1.Core4.0.Fcst_DaypartForecast.0',
        'Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0',
        'Config.1.Travel.0.Fcst_TextForecast.0',
        'Config.1.Traffic.0.Fcst_ExtendedForecast.0',
        'Config.1.Traffic.0.Local_TrafficFlow.0',
        'Config.1.Core1.0.Local_LocalObservations.0',
        'Config.1.Core3.0.Fcst_DaypartForecast.0',
        'Config.1.Airport.0.Fcst_ExtendedForecast.0',
        'Config.1.Airport.0.Local_LocalAirportConditions.1',
        'Config.1.Health.0.Cc_ShortCurrentConditions.0',
        'Config.1.Garden.0.Fcst_DaypartForecast.0',
        'Config.1.Core5.0.Cc_LongCurrentConditions.0',
        'Config.1.Core5.0.Local_MenuBoard.0',
        'Config.1.Traffic.0.Fcst_TextForecast.0',
        'Config.1.SevereCore2.0.Local_SevereWeatherMessage.0',
        'Config.1.SevereCore1A.0.Local_CurrentConditions.0',
        'Config.1.Core2.0.Local_DaypartForecast.0',
        'Config.1.CityTicker_AirportDelays.0',
        'Config.1.Airport.0.Local_LocalAirportConditions.2',
        'Config.1.Travel.0.Fcst_DaypartForecast.0',
        'Config.1.Ski.0.Fcst_DaypartForecast.0',
        'Config.1.Traffic.0.Local_PackageIntro.0',
        'Config.1.Health.0.Cc_LongCurrentConditions.0',
        'Config.1.International.0.Local_InternationalDestinations.3',
        'Config.1.International.0.Cc_LongCurrentConditions.0',
        'Config.1.Core1.0.Cc_LongCurrentConditions.0',
        'Config.1.Core3.0.Cc_LongCurrentConditions.0',
        'Config.1.Cc_ShortCurrentConditions.0',
        'Config.1.Core3.0.Local_WeatherBulletin.0',
        'Config.1.CityTicker_LocalCitiesCurrentConditions.0',
        'Config.1.Fcst_DaypartForecast.0',
        'Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0',
        'Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0',
        'Config.1.SevereCore1B.0.Local_CurrentConditions.0',
        'Config.1.Core1.0.Local_TextForecast.0',
        'Config.1.Core3.0.Local_CurrentConditions.0',
        'Config.1.Core2.0.Fcst_DaypartForecast.0',
        'Config.1.Garden.0.Local_Promo.0',
        'Config.1.Traffic.0.Cc_ShortCurrentConditions.0',
        'Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0',
        'Config.1.Core1.0.Fcst_ExtendedForecast.0',
        'Config.1.Core1.0.Local_MenuBoard.0',
        'Config.1.Core2.0.Local_CurrentConditions.0',
        'Config.1.SevereCore2.0.Local_WeatherBulletin.0',
        'Config.1.Core2.0.Fcst_ExtendedForecast.0',
        'Config.1.Core4.0.Local_WeatherBulletin.0',
        'Config.1.Core3.0.Cc_ShortCurrentConditions.0',
        'Config.1.International.0.Fcst_ExtendedForecast.0',
        'Config.1.Travel.0.Fcst_ExtendedForecast.0',
        'Config.1.SevereCore1A.0.Fcst_DaypartForecast.0',
        'Config.1.Fcst_TextForecast.0',
        'Config.1.Airport.0.Local_PackageIntro.0',
        'Config.1.Health.0.Local_Promo.0',
        'Config.1.Core4.0.Cc_ShortCurrentConditions.0',
        'Config.1.Airport.0.Cc_LongCurrentConditions.0',
        'Config.1.International.0.Local_PackageIntro.0',
        'Config.1.Core5.0.Fcst_DaypartForecast.0',
        'Config.1.Ski.0.Local_SkiConditions.2',
        'Config.1.Core4.0.Fcst_ExtendedForecast.0',
        'Config.1.Health.0.Local_HealthForecast.0',
        'Config.1.CityTicker_TravelCitiesForecast.0',
        'Config.1.SevereCore1B.0.Local_ExtendedForecast.0',
        'Config.1.Core4.0.Fcst_TextForecast.0',
        'Config.1.Garden.0.Fcst_TextForecast.0',
        'Config.1.SevereCore2.0.Fcst_ExtendedForecast.0',
        'Config.1.Core3.0.Local_TextForecast.0',
        'Config.1.Airport.0.Fcst_TextForecast.0',
        'Config.1.Airport.0.Local_LocalAirportConditions.0',
        'Config.1.SevereCore1B.0.Fcst_DaypartForecast.0',
        'Config.1.SevereCore1B.0.Local_WeatherBulletin.0',
        'Config.1.Core1.0.Local_CurrentConditions.0',
        'Config.1.SevereCore1A.0.Local_WeatherBulletin.0',
        'Config.1.Core4.0.Local_DaypartForecast.0',
        'Config.1.Health.0.Local_PackageIntro.0',
        'Config.1.Health.0.Local_OutdoorActivityForecast.0',
        'Config.1.SevereCore2.0.Fcst_TextForecast.0',
        'Config.1.Core4.0.Cc_LongCurrentConditions.0',
        'Config.1.Core3.0.Local_MenuBoard.0',
        'Config.1.Core5.0.Fcst_ExtendedForecast.0',
        'Config.1.Core2.0.Fcst_TextForecast.0',
        'Config.1.Core2.0.Local_ExtendedForecast.0',
        'Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0',
        'Config.1.Ski.0.Local_SkiConditions.3',
        'Config.1.SevereCore1A.0.Local_TextForecast.0',
        'Config.1.Garden.0.Fcst_ExtendedForecast.0',
        'Config.1.Ski.0.Cc_ShortCurrentConditions.0',
        'Config.1.Core2.0.Local_MenuBoard.0',
        'Config.1.Health.0.Fcst_ExtendedForecast.0',
        'Config.1.International.0.Local_InternationalDestinations.1',
        'Config.1.SevereCore1A.0.Local_ExtendedForecast.0',
        'Config.1.International.0.Local_InternationalDestinations.4',
        'Config.1.Core1.0.Local_Almanac.0',
        'Config.1.International.0.Cc_ShortCurrentConditions.0',
        'Config.1.Airport.0.Local_LocalAirportConditions.3',
        'Config.1.Traffic.0.Local_TrafficOverview.0',
        'Config.1.SevereCore2.0.Cc_LongCurrentConditions.0',
        'Config.1.Health.0.Local_AllergyReport.0',
        'Config.1.SevereCore1A.0.Local_LocalObservations.0',
        'Config.1.Core2.0.Cc_LongCurrentConditions.0',
        'Config.1.SevereCore1A.0.Fcst_TextForecast.0',
        'Config.1.Core5.0.Fcst_TextForecast.0',
        'Config.1.Ski.0.Local_SunSafetyFacts.0',
        'Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0',
        'Config.1.Core2.0.Cc_ShortCurrentConditions.0',
        'Config.1.Core1.0.Fcst_TextForecast.0',
        'Config.1.Core5.0.Cc_ShortCurrentConditions.0',
        'Config.1.Travel.0.Local_Destinations.1',
        'Config.1.Cc_LongCurrentConditions.0',
        'Config.1.CityTicker_LocalCitiesForecast.0',
        'Config.1.Travel.0.Cc_LongCurrentConditions.0',
        'Config.1.Traffic.0.SmLocal_TrafficSponsor.0',
        'Config.1.Ski.0.Local_PackageIntro.0',
        'Config.1.Ski.0.Fcst_TextForecast.0',
        'Config.1.Garden.0.Cc_LongCurrentConditions.0',
        'Config.1.Travel.0.Local_Destinations.0',
        'Config.1.Garden.0.Local_PackageIntro.0',
        'Config.1.CityTicker_TravelCitiesCurrentConditions.0',
        'Config.1.International.0.Local_InternationalDestinations.0',
        'Config.1.Airport.0.Local_NationalAirportConditions.3',
        'Config.1.Core1.0.Local_WeatherBulletin.0',
        'Config.1.Traffic.0.Cc_LongCurrentConditions.0',
        'Config.1.Health.0.Local_SunSafetyFacts.1',
        'Config.1.International.0.Fcst_DaypartForecast.0',
        'Config.1.Core1.0.Local_LocalObservations.1',
        'Config.1.Airport.0.Local_NationalAirportConditions.2',
        'Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0',
        'Config.1.Core2.0.Local_WeatherBulletin.0',
        'Config.1.International.0.Fcst_TextForecast.0',
        'Config.1.Ski.0.Local_SkiConditions.1',
        'Config.1.Fcst_ExtendedForecast.0',
        'Config.1.SevereCore1B.0.Local_DaypartForecast.0',
        'Config.1.Travel.0.Local_PackageIntro.0',
        'Config.1.International.0.Local_InternationalDestinations.2',
        'Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0',
        'Config.1.Garden.0.Local_GardeningForecast.0',
        'Config.1.Core3.0.Fcst_TextForecast.0',
        'Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0',
        'Config.1.Travel.0.Cc_ShortCurrentConditions.0',
        'Config.1.Ski.0.Fcst_ExtendedForecast.0',
        'Config.1.Core3.0.Fcst_ExtendedForecast.0',
        'Config.1.International.0.Local_InternationalDestinations.5',
        'Config.1.Travel.0.Local_Destinations.2',
        'Config.1.SevereCore2.0.Fcst_DaypartForecast.0',
        'Config.1.Airport.0.Cc_ShortCurrentConditions.0',
        'Config.1.Health.0.Local_UltravioletIndex.0',
        'Config.1.Garden.0.Cc_ShortCurrentConditions.0',
        'Config.1.Core1.0.Cc_ShortCurrentConditions.0',
        'Config.1.Core1.0.Local_NetworkIntro.0',
        'Config.1.Core1.0.Local_ExtendedForecast.0',
        'Config.1.Health.0.Local_AirQualityForecast.0',
        'Config.1.Core4.0.Local_ExtendedForecast.0',
        'Config.1.SevereCore1B.0.Fcst_TextForecast.0',
        'Config.1.SevereCore1A.0.Local_LocalObservations.1',
        'Config.1.Health.0.Fcst_TextForecast.0',
        'Config.1.Core1.0.Fcst_DaypartForecast.0',
        'Config.1.Traffic.0.Fcst_DaypartForecast.0',
        'Config.1.Health.0.Fcst_DaypartForecast.0',
        'Config.1.Core4.0.Local_MenuBoard.0',
        'Config.1.Ski.0',
    ]
    
    lines = [f"scmtRemove('{product}')" for product in (domestic_products if system_type == "domestic" else weatherscan_products)]
    return "\n".join(lines)


def compile_i1_bulletin_override() -> str:
    """Generate bulletin and override configuration."""
    return """#
# BLOCK BEGIN
d = twc.Data()
dsm.set('Config.1.Override', d, 0)
d = twc.Data()
d.activeVocal = 1
dsm.set('Config.1.Bulletin_Default', d, 0)
# BLOCK END
#
d = twc.Data()
d.sponsorLogo = ''
dsm.set('Config.1', d, 0, 1)"""


def compile_i1_vocal_schedule() -> str:
    """Generate vocal local schedule configuration."""
    return """scmtRemove('Config.1.VocalLocalSchedule')
d = twc.Data()
d.OffTimes = ( )
dsm.set('Config.1.VocalLocalSchedule', d, 0, 1)
#
scmtRemove('Config.1.Ldl_LASCrawl')
scmtRemove('Config.1.LASCrawl')"""


def compile_i1_non_image_maps() -> str:
    """Generate non-image maps configuration."""
    return """#
#  Non Image Maps
#
d = [
'Config.1.Local_MetroForecastMap',
'Config.1.Local_MetroObservationMap',
'Config.1.Local_RegionalForecastMap',
'Config.1.Local_RegionalObservationMap',
]
dsm.set('Config.1.nonImageMaps', d, 0)"""


def compile_wxscan_packages(config: AggregatedConfig) -> str:
    """Generate weatherscan package definitions."""
    loc_name = config.name
    output = f"""#
scmtRemove('Config.1.Ski.0')
d = twc.Data()
d.bkgImage = 'ski_bg'
d.packageTitle = 'Ski & Snow'
d.packageFlavor = 1
d.shortPackageTitle = 'SKI'
dsm.set('Config.1.Ski.0', d, 0, 1)
scmtRemove('Config.1.Garden.0')
d = twc.Data()
d.bkgImage = 'garden_bg'
d.packageTitle = 'Garden'
d.packageFlavor = 1
d.shortPackageTitle = 'GARDEN'
dsm.set('Config.1.Garden.0', d, 0, 1)
scmtRemove('Config.1.SevereCore1B.0')
d = twc.Data()
d.bkgImage = 'severe_core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'YOUR LOCAL FORECAST'
dsm.set('Config.1.SevereCore1B.0', d, 0, 1)
scmtRemove('Config.1.SevereCore1A.0')
d = twc.Data()
d.bkgImage = 'severe_core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'YOUR LOCAL FORECAST'
dsm.set('Config.1.SevereCore1A.0', d, 0, 1)
scmtRemove('Config.1.International.0')
d = twc.Data()
d.bkgImage = 'international_bg'
d.packageTitle = 'International Forecast'
d.packageFlavor = 3
d.shortPackageTitle = 'INTERNATIONAL'
dsm.set('Config.1.International.0', d, 0, 1)
scmtRemove('Config.1.SevereCore2.0')
d = twc.Data()
d.bkgImage = 'severe_core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'YOUR LOCAL FORECAST'
dsm.set('Config.1.SevereCore2.0', d, 0, 1)
scmtRemove('Config.1.Airport.0')
d = twc.Data()
d.bkgImage = 'airport_bg'
d.packageTitle = 'Airport Conditions'
d.packageFlavor = 3
d.shortPackageTitle = 'AIRPORT'
dsm.set('Config.1.Airport.0', d, 0, 1)
scmtRemove('Config.1.Core5.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 0
d.shortPackageTitle = '{loc_name.upper()} RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = '{loc_name.upper()}'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = '{loc_name.upper()}'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = '{loc_name.upper()}'
dsm.set('Config.1.Core2.0', d, 0, 1)
scmtRemove('Config.1.Travel.0')
d = twc.Data()
d.bkgImage = 'travel_bg'
d.packageTitle = 'Travel Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'TRAVEL'
dsm.set('Config.1.Travel.0', d, 0, 1)
scmtRemove('Config.1.Core1.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = '{loc_name.upper()}'
dsm.set('Config.1.Core1.0', d, 0, 1)
scmtRemove('Config.1.Traffic.0')
d = twc.Data()
d.activeCc_LongCurrentConditions = 0
d.activeCc_ShortCurrentConditions = 0
d.activeFcst_DaypartForecast = 0
d.activeFcst_ExtendedForecast = 0
d.activeFcst_TextForecast = 0
d.activeLocal_PackageIntro = 1
d.activeLocal_TrafficFlow = 1
d.activeLocal_TrafficOverview = 1
d.activeLocal_TrafficReport = 1
d.activeSmLocal_TrafficSponsor = 1
d.bkgImage = 'traffic_bg'
d.packageTitle = 'Traffic Report'
d.packageFlavor = 3
d.shortPackageTitle = 'TRAFFIC'
dsm.set('Config.1.Traffic.0', d, 0, 1)
scmtRemove('Config.1.Health.0')
d = twc.Data()
d.bkgImage = 'health_bg'
d.packageTitle = 'Weather & Your Health'
d.packageFlavor = 2
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = '{loc_name}'
d.bkgImage = 'neighborhood_bg'
d.affiliateName = 'Weatherscan'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'garden_intro_bg'
dsm.set('Config.1.Garden.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'international_intro_bg'
dsm.set('Config.1.International.0.Local_PackageIntro.0', d, 0, 1)
#
"""
    return output


def compile_wxscan_airport_data(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    """Generate weatherscan airport data configuration."""
    airport_records = [r for r in all_records if r.airport_id]
    
    if not airport_records:
        return ""
    
    # Get first few airports for local conditions
    local_airports = airport_records[:2]
    airport_ids = [r.airport_id for r in local_airports]
    airport_teccis = [r.teccis[0] if r.teccis else "" for r in local_airports]
    airport_names = [r.name for r in local_airports]
    
    output = f"""#
d = twc.Data()
d.airportId = [{quote_list(airport_ids)}]
d.obsStation = [{quote_list(airport_teccis)}]
d.locName = [{quote_list(airport_names)}]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
"""
    # Add individual local airport conditions
    for i, record in enumerate(local_airports):
        output += f"""d = twc.Data()
d.airportId = '{record.airport_id}'
d.obsStation = '{record.teccis[0] if record.teccis else ""}'
d.locName = '{record.name}'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.{i}', d, 0, 1)
#
"""
    return output

def compile_full_config(config: AggregatedConfig, all_records: list[LocationRecord], system_type: str = "domestic") -> str:
    from datetime import datetime

    secret_hehe = "#"
    
    sections = []
    
    start_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    if "Oct 10" in start_time:
        import base64
        secret_hehe = base64.b64decode("I+KghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghAoj4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCECg==").decode('utf-8')
    
    sections.append(f"# Created on {start_time}")
    sections.append(f"# SCMT Configuration File for IntelliStar 1 {system_type.capitalize()}")
    sections.append("# Generated by IntelliStar Config Generator by @sspwxr (raii)")
    sections.append("#")
    sections.append("#")
    sections.append(secret_hehe)
    sections.append("#")
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
    if system_type == "domestic":
        sections.append(f"dsm.set('scmt_configType', 'domestic',0)")
        sections.append("dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)")
    if system_type == "weatherscan":
        sections.append(f"dsm.set('scmt_configType', 'wxscan',0)")
        sections.append("dsm.set('scmt.ProductTypes',['None'], 0)")
    sections.append("#")
    sections.append(f"wxdata.setTimeZone('{get_timezone_by_location_id(all_records[0].loc_id)}')")
    sections.append("#")
    if system_type == "domestic":
        sections.append(compile_i1_map_data(config, all_records))
        sections.append("#")
        sections.append(compile_i1_interest_list(config, "domestic"))
        sections.append(compile_i1_metadata(config, "domestic"))
        sections.append("#")
        sections.append(compile_i1_airport_data(config, all_records))
        sections.append("#")
        sections.append(compile_i1_bulletin_override())
        sections.append("#")
        sections.append(compile_i1_vocal_schedule())
        sections.append("#")
        sections.append(compile_i1_scmt_removes(system_type="domestic"))
        sections.append("#")
        sections.append(compile_i1_non_image_maps())
        sections.append("#")
        sections.append("#")
        sections.append(compile_i1_currentconditions(config, all_records, "domestic"))
        sections.append("#")
        sections.append(compile_i1_forecast(config, "domestic"))
        sections.append("#")
        sections.append(compile_i1_airport_delays(config, all_records))
        sections.append("#")
        sections.append(compile_i1_travel_forecast(config, all_records))
        sections.append("#")
    if system_type == "weatherscan":
        sections.append(compile_i1_scmt_removes(system_type="weatherscan"))
        sections.append(compile_i1_map_data(config, all_records, "weatherscan"))
        sections.append("#")
        sections.append(compile_i1_interest_list(config, "weatherscan"))
        sections.append(compile_i1_metadata(config, "weatherscan"))
        sections.append("#")
        sections.append(compile_wxscan_airport_data(config, all_records))
        sections.append("#")
        sections.append(compile_i1_bulletin_override())
        sections.append("#")
        sections.append(compile_i1_vocal_schedule())
        sections.append("#")
        sections.append(compile_wxscan_packages(config))
        sections.append("#")
        sections.append(compile_i1_currentconditions(config, all_records, "weatherscan"))
        sections.append("#")
        sections.append(compile_i1_forecast(config, "weatherscan"))
        sections.append("#")
        sections.append(compile_i1_travel_forecast(config, all_records))
        sections.append("#")
    
    end_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    sections.append("Log.info('scmt config completed')")
    sections.append(f"# Finished generation on {end_time}")
    
    return "\n".join(sections)


def compile_i1_map_data(config: AggregatedConfig, all_records: list[LocationRecord], system_type: str = "domestic") -> str:
    """
    Generate map data configurations for all map products.
    
    This creates the wxdata.setMapData() and dsm.set() calls for each map product,
    calculating mapcut coordinates from the primary location's lat/lon.
    """
    if config.lat is None or config.lon is None:
        return "# MAP DATA SKIPPED - No lat/lon available for primary location"
    
    lines = []
    lines.append("#")
    lines.append("# MAP DATA CONFIGURATION")
    lines.append("# Generated from primary location coordinates")
    lines.append(f"# Lat: {config.lat}, Lon: {config.lon}")
    lines.append("#")
    
    primary_name = config.name if config.name else "Location"
    
    mapcuts = get_all_mapcut_coordinates(config.lat, config.lon)

    standard_vectors = [
        'mercator.us.ushighways.vg',
        'mercator.us.counties.vg',
        'mercator.us.states.vg',
        'mercator.us.coastlines.vg',
        'mercator.us.statehighways.vg',
        'mercator.us.otherroutes.vg',
        'mercator.us.interstates.vg',
    ]
    vectors_str = ",".join([f"'{v}'" for v in standard_vectors])
    
    vector_style = """  vector = [
             (( 6,(20,20,20,96),1,),(('statehighways',),),),
             (( 6,(20,20,20,96),1,),(('ushighways',),),),
             (( 6,(20,20,20,96),1,),(('interstates',),),),
             (( 6,(20,20,20,96),1,),(('otherroutes',),),),
             (( 1,(20,20,20,255),2,),(('counties',),),),
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 1,(20,20,20,255),2,),(('coastlines',),),),
             (( 3,(130,130,130,255),2,),(('statehighways',),),),
             (( 3,(130,130,130,255),2,),(('ushighways',),),),
             (( 3,(130,130,130,255),2,),(('interstates',),),),
             (( 3,(130,130,130,255),2,),(('otherroutes',),),),
             ],"""
    
    product_params = {
        "Radar_LocalDoppler": {
            "datacutType": "radar.us",
            "mapFinalSize": (240, 137),
            "dataFinalSize": (240, 137),
            "mapMilesSize": (141, 97),
        },
        "NationalLdl_DopplerRadar": {
            "datacutType": "radar.us",
            "mapFinalSize": (193, 110),
            "dataFinalSize": (193, 110),
            "mapMilesSize": (141, 97),
        },
        "Local_MetroDopplerRadar": {
            "datacutType": "radar.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (127, 102),
        },
        "Local_MetroForecastMap": {
            "datacutType": "forecast.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (141, 94),
        },
        "Local_MetroObservationMap": {
            "datacutType": "observation.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (141, 94),
        },
        "Local_RegionalDopplerRadar": {
            "datacutType": "radar.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (339, 226),
        },
        "Local_RegionalForecastMap": {
            "datacutType": "forecast.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (564, 376),
        },
        "Local_RegionalObservationMap": {
            "datacutType": "observation.us",
            "mapFinalSize": (720, 480),
            "dataFinalSize": (720, 480),
            "mapMilesSize": (564, 376),
        },
    }
    
    def calc_datacut_coord(mapcut_x: int, mapcut_y: int, size_w: int, size_h: int) -> tuple[int, int]:
        center_x = mapcut_x + size_w // 2
        center_y = mapcut_y + size_h // 2
        radar_x = int(center_x / 9.4)
        radar_y = int(center_y / 9.4)
        return (radar_x, radar_y)
    
    for product_name, (cut_x, cut_y) in mapcuts.items():
        if product_name not in product_params:
            continue
            
        params = product_params[product_name]
        size = MAP_PRODUCT_SIZES[product_name]
        
        # Calculate datacutCoordinate (approximate)
        datacut = calc_datacut_coord(cut_x, cut_y, size[0], size[1])
        
        # Estimate datacutSize based on mapMilesSize ratio
        datacut_size = (int(params["mapMilesSize"][0] * 1.25), int(params["mapMilesSize"][1] * 1.05))
        
        lines.append(f"#")
        lines.append(f"# {product_name} (MAP DATA)")
        lines.append(f"#")
        lines.append(f"d = twc.Data(mapName='mercator.us.bfg',")
        lines.append(f"             mapcutCoordinate=({cut_x},{cut_y}),")
        lines.append(f"             mapcutSize=({size[0]},{size[1]}),")
        lines.append(f"             mapFinalSize={params['mapFinalSize']},")
        lines.append(f"             mapMilesSize={params['mapMilesSize']},")
        lines.append(f"             datacutType='{params['datacutType']}',")
        lines.append(f"             datacutCoordinate={datacut},")
        lines.append(f"             datacutSize={datacut_size},")
        lines.append(f"             dataFinalSize={params['dataFinalSize']},")
        lines.append(f"             dataOffset=(0,0),")
        lines.append(f"             vectors=[{vectors_str},],")
        lines.append(f")")
        lines.append(f"wxdata.setMapData('Config.1.{product_name}', d, 0)")
        lines.append(f"#")
        lines.append(f"# {product_name} (PRODUCT DATA)")
        lines.append(f"#")
        
        # Calculate center position for locator dot (center of the final map size)
        final_w, final_h = params["mapFinalSize"]
        center_pos = (final_w // 2, final_h // 2)
        
        lines.append(f"d = twc.Data(")
        lines.append(f"  tiffImage = [")
        lines.append(f"             (")
        lines.append(f"               ('locatorDotSmallOutline',0,2,1,),")
        lines.append(f"              ( ( {center_pos},),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"             (")
        lines.append(f"               ('locatorDotSmall',0,1,0,),")
        lines.append(f"              ( ( {center_pos},),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"        ],")
        lines.append(f"  textString = [")
        lines.append(f"             (")
        lines.append(f"               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),")
        lines.append(f"              ( ( ({center_pos[0]-16},{center_pos[1]-9}),'{primary_name}',),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"             (")
        lines.append(f"               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),")
        lines.append(f"              ( ( ({center_pos[0]-16},{center_pos[1]-9}),'{primary_name}',),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"        ],")
        lines.append(vector_style)
        lines.append(f")")
        lines.append(f"dsm.set('Config.1.{product_name}', d, 0)")
        lines.append("")
    
    # Add the interest lists for map/radar data binding
    lines.append("#")
    lines.append("# Map and Radar Interest Lists")
    lines.append("#")
    
    if system_type == "weatherscan":
        # Add static international forecast maps (Canada and Mexico)
        lines.append("# MAP: 240")
        lines.append("# Local_InternationalForecast (MAP DATA) - Canada")
        lines.append("#")
        lines.append("d = twc.Data(mapName='lambert.ca.tif',")
        lines.append("             mapcutCoordinate=(0,3),")
        lines.append("             mapcutSize=(720,480),")
        lines.append("             mapFinalSize=(720,480),")
        lines.append("             mapMilesSize=(3635,2907),")
        lines.append(")")
        lines.append("wxdata.setMapData('Config.1.International.0.Local_InternationalForecast.0', d, 0)")
        lines.append("#")
        lines.append("# Local_InternationalForecast (PRODUCT DATA) - Canada")
        lines.append("#")
        lines.append("d = twc.Data(")
        lines.append("  fcstIcon = [")
        lines.append("             (")
        lines.append("               (0,1,0,),")
        lines.append("               ( ( '71182000',(574,186),),")
        lines.append("                 ( '71627001',(538,92),),")
        lines.append("                 ( '71852000',(365,93),),")
        lines.append("                 ( '71879001',(241,140),),")
        lines.append("                 ( '71892001',(132,103),),")
        lines.append("                 ( '71913000',(374,189),),")
        lines.append("                 ( '71936000',(247,234),),")
        lines.append("                 ( '71966000',(125,285),),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append("  fcstValue = [")
        lines.append("             (")
        lines.append("               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),1,0,),")
        lines.append("               ( ( '71182000',(571,226),),")
        lines.append("                 ( '71627001',(535,132),),")
        lines.append("                 ( '71852000',(362,133),),")
        lines.append("                 ( '71879001',(238,180),),")
        lines.append("                 ( '71892001',(129,143),),")
        lines.append("                 ( '71913000',(371,229),),")
        lines.append("                 ( '71936000',(244,274),),")
        lines.append("                 ( '71966000',(122,325),),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append("  textString = [")
        lines.append("             (")
        lines.append("               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),1,0,1,),")
        lines.append("               ( ( (510,260),'Churchill Falls',),")
        lines.append("                 ( (497,166),'Montreal',),")
        lines.append("                 ( (322,167),'Winnipeg',),")
        lines.append("                 ( (194,214),'Edmonton',),")
        lines.append("                 ( (84,177),'Vancouver',),")
        lines.append("                 ( (335,263),'Churchill',),")
        lines.append("                 ( (192,308),'Yellowknife',),")
        lines.append("                 ( (90,359),'Dawson',),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append(")")
        lines.append("dsm.set('Config.1.International.0.Local_InternationalForecast.0', d, 0)")
        lines.append("# MAP: 246")
        lines.append("# Local_InternationalForecast (MAP DATA) - Mexico")
        lines.append("#")
        lines.append("d = twc.Data(mapName='mercator.mx.tif',")
        lines.append("             mapcutCoordinate=(0,3),")
        lines.append("             mapcutSize=(720,480),")
        lines.append("             mapFinalSize=(720,480),")
        lines.append("             mapMilesSize=(2979,1831),")
        lines.append(")")
        lines.append("wxdata.setMapData('Config.1.International.0.Local_InternationalForecast.1', d, 0)")
        lines.append("#")
        lines.append("# Local_InternationalForecast (PRODUCT DATA) - Mexico")
        lines.append("#")
        lines.append("d = twc.Data(")
        lines.append("  fcstIcon = [")
        lines.append("             (")
        lines.append("               (0,1,0,),")
        lines.append("               ( ( '76255000',(206,261),),")
        lines.append("                 ( '76393000',(346,201),),")
        lines.append("                 ( '76405000',(222,166),),")
        lines.append("                 ( '76595000',(570,121),),")
        lines.append("                 ( '76679001',(368,95),),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append("  fcstValue = [")
        lines.append("             (")
        lines.append("               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),1,0,),")
        lines.append("               ( ( '76255000',(203,301),),")
        lines.append("                 ( '76393000',(343,241),),")
        lines.append("                 ( '76405000',(211,206),),")
        lines.append("                 ( '76595000',(567,161),),")
        lines.append("                 ( '76679001',(365,135),),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append("  textString = [")
        lines.append("             (")
        lines.append("               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),1,0,1,),")
        lines.append("               ( ( (165,335),'Guaymas',),")
        lines.append("                 ( (298,275),'Monterrey',),")
        lines.append("                 ( (188,240),'La Paz',),")
        lines.append("                 ( (538,195),'Cancun',),")
        lines.append("                 ( (315,169),'Mexico City',),")
        lines.append("               ),")
        lines.append("             ),")
        lines.append("        ],")
        lines.append(")")
        lines.append("dsm.set('Config.1.International.0.Local_InternationalForecast.1', d, 0)")
        lines.append("#")
        # Weatherscan interest lists
        lines.append("wxdata.setInterestList('lambert.us','1',['precipQpfForecast.us','estimatedPrecip.us','travelWeather.us','snowfallQpfForecast.us','palmerDrought.us','frostFreeze.us','radarSatellite.us',])")
        lines.append("wxdata.setInterestList('mercator.us','1',['radar.us',])")
        lines.append("#")
        lines.append("#")
        lines.append("wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])")
        lines.append("wxdata.setInterestList('precipQpfForecast.us.cuts','1',['Config.1.Garden.0.Local_PrecipitationQpfForecast.0',])")
        lines.append("wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0',])")
        lines.append("wxdata.setInterestList('estimatedPrecip.us.cuts','1',['Config.1.Garden.0.Local_EstimatedPrecipitation.0',])")
        lines.append("wxdata.setInterestList('frostFreeze.us.cuts','1',['Config.1.Garden.0.Local_FrostFreezeWarnings.0',])")
        lines.append("wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])")
        lines.append("wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])")
        lines.append("wxdata.setInterestList('palmerDrought.us.cuts','1',['Config.1.Garden.0.Local_PalmerDroughtSeverity.0',])")
        lines.append("#")
        lines.append("wxdata.setInterestList('mapData','1',['lambert.ca','mercator.us','mercator.mx','lambert.us',])")
        lines.append("#")
        lines.append("wxdata.setInterestList('imageData','1',['frostFreeze.us','palmerDrought.us','radarSatellite.us','snowfallQpfForecast.us','precipQpfForecast.us','radar.us','travelWeather.us','estimatedPrecip.us',])")
    else:
        # Domestic interest lists
        lines.append("wxdata.setInterestList('mercator.us','1',['radar.us',])")
        lines.append("wxdata.setInterestList('radar.us.cuts','1',['Config.1.NationalLdl_DopplerRadar','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])")
        lines.append("wxdata.setInterestList('mapData','1',['mercator.us',])")
        lines.append("wxdata.setInterestList('imageData','1',['radar.us',])")
    
    lines.append("# END OF MAPS")
    lines.append("# commit for map stuff to avoid missing updates")
    lines.append("ds.commit()")
    
    return "\n".join(lines)


def main() -> None:
    """Main entry point for the configuration generator."""
    
    # Prompt for system type
    print("\nSelect the system type to generate a config for:")
    print("  1. Domestic IntelliStar")
    print("  2. Weatherscan IntelliStar")
    while True:
        system_choice = input("Enter choice (1 or 2): ").strip()
        if system_choice == "1":
            system_type = "domestic"
            break
        elif system_choice == "2":
            system_type = "weatherscan"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    print(f"\nGenerating config for: {system_type.upper()}")
    
    main_record_data = prompt_for_location()
    
    if main_record_data is None:
        print("No location selected. Exiting.")
        return

    main_location_name = main_record_data.get('prsntNm', '')
    main_lat = main_record_data.get('lat')
    main_lon = main_record_data.get('long')
    main_state = main_record_data.get('stCd', '')
    main_country = main_record_data.get('cntryCd', '')
    location_id = main_record_data.get('locId', '')

    if main_lat:
        try:
            main_lat = float(main_lat)
        except (ValueError, TypeError):
            main_lat = None
    if main_lon:
        try:
            main_lon = float(main_lon)
        except (ValueError, TypeError):
            main_lon = None

    nearby = prompt_for_nearby_locations(max_nearby=8)
    
    print(f"\nNearby locations entered: {len(nearby)}")
    for record in nearby:
        print(f"  - {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')}")

    config = AggregatedConfig()
    all_records: list[LocationRecord] = []

    config.name = main_location_name
    config.lat = main_lat
    config.lon = main_lon
    config.state_code = main_state
    config.country_code = main_country

    print(f"\nMain Location ID: {location_id[:8] if location_id else 'N/A'}")
    
    main_record = LocationRecord.from_db_record(
        main_record_data, 
        name=main_location_name
    )
    all_records.append(main_record)
    config.add_record(main_record)
    print(f"  Database record found")
    print(f"  TECCIs: {main_record.teccis}")
    print(f"  Coop ID: {main_record.coop_id}")
    print(f"  Zone ID: {main_record.zone_id}")
    print(f"  Airport ID: {main_record.airport_id}")

    processed_loc_ids = {location_id}
    
    for record_data in nearby:
        loc_id = record_data.get('locId', '')
        name = record_data.get('prsntNm', '')
        
        if loc_id in processed_loc_ids:
            print(f"\nSkipping duplicate: {name} (ID: {loc_id[:8]})")
            continue
        
        processed_loc_ids.add(loc_id)
        
        print(f"\nAdding: {name} (ID: {loc_id[:8]})")
        record = LocationRecord.from_db_record(record_data, name=name)
        all_records.append(record)
        config.add_record(record)
        print(f"  TECCIs: {record.teccis}")
        print(f"  Coop ID: {record.coop_id}")
        print(f"  Zone ID: {record.zone_id}")
        print(f"  Airport ID: {record.airport_id}")

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
    
    if system_type == "domestic":
        print(f"DOMESTIC INTELLISTAR CONFIG GENERATED FOR {config.name.upper()}")
        print("=" * 60)
        full_config = compile_full_config(config, all_records, system_type="domestic")
        output_filename = f"output/{config.name.replace(' ', '_').replace('/', '_')}_i1_config.py"
    else:
        print(f"WEATHERSCAN INTELLISTAR CONFIG GENERATED FOR {config.name.upper()}")
        print("=" * 60)
        full_config = compile_full_config(config, all_records, system_type="weatherscan")
        output_filename = f"output/{config.name.replace(' ', '_').replace('/', '_')}_wxscan_config.py"
    
    Path("output").mkdir(exist_ok=True)
    
    with open(output_filename, 'w') as f:
        f.write(full_config)
    
    print(f"\nConfiguration saved to: {output_filename}")
    print(f"Total lines: {len(full_config.splitlines())}")

if __name__ == "__main__":
    main()
