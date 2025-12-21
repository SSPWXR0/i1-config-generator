"""
Weather Location Configuration Generator

Searches for locations, prompts for nearby cities,
and queries local database records.
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

DB_PATH = Path("./LFRecord.db")

print("=" * 60)
print("IntelliStar Configuration Generator")
print("Created by @sspwxr (raii), version 1-2025-12-20")
print("=" * 60)

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


def search_records_by_name(search_term: str) -> list[dict]:
    """
    Search LFRecord.db for records matching a name.

    Args:
        search_term: The name to search for (uses LIKE matching).

    Returns:
        List of matching records as dictionaries.
    """
    with get_db_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM LFRecord WHERE prsntNm LIKE ? ORDER BY prsntNm LIMIT 20",
            (f"%{search_term}%",)
        )
        rows = cursor.fetchall()

    return [dict(row) for row in rows]


def prompt_for_nearby_locations(max_nearby: int = 7) -> list[dict]:
    """
    Prompt user for nearby location names, searching LFRecord database directly.

    Args:
        max_nearby: Maximum number of nearby locations to prompt for.

    Returns:
        List of matching database records as dictionaries.
    """
    nearby_locations = []
    
    print(f"\nEnter up to {max_nearby} nearby locations (press Enter to skip, 'back' to go back):")
    
    i = 0
    while i < max_nearby:
        location_name = input(f"  Nearby location {i + 1}: ").strip()
        
        if not location_name:
            print(f"    Skipped")
            i += 1
            continue
        
        if location_name.lower() == 'back':
            if nearby_locations:
                removed = nearby_locations.pop()
                i -= 1
                print(f"    Removed: {removed.get('prsntNm', 'Unknown')}")
            else:
                print(f"    Nothing to go back to")
            continue
        
        # Search the database directly
        matches = search_records_by_name(location_name)
        
        if not matches:
            print(f"    No results found for '{location_name}' in database")
            continue
        
        if len(matches) == 1:
            # Single match - use it directly
            record = matches[0]
            nearby_locations.append(record)
            print(f"    Found: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {record.get('locId', '')[:8]})")
            i += 1
        else:
            # Multiple matches - ask user to select
            print(f"    Multiple matches found ({len(matches)}):")
            for idx, record in enumerate(matches, 1):
                loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
                print(f"      [{idx}] {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
            
            while True:
                selection = input(f"    Select (1-{len(matches)}, or 'skip'): ").strip()
                
                if selection.lower() == 'skip':
                    print(f"    Skipped")
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
    """Prompt user for location and return database record, searching LFRecord database directly."""
    location_name = input("Enter the location name: ").strip()
    
    if not location_name:
        print("No location name provided")
        return None
    
    # Search the database directly (same as nearby locations)
    matches = search_records_by_name(location_name)
    
    if not matches:
        print(f"No results found for '{location_name}' in database")
        return None
    
    if len(matches) == 1:
        # Single match - use it directly
        record = matches[0]
        loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
        print(f"Found: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
        print(f"  Coordinates: {record.get('lat', 'N/A')}, {record.get('long', 'N/A')}")
        return record
    else:
        # Multiple matches - ask user to select
        print(f"Multiple matches found ({len(matches)}):")
        for idx, record in enumerate(matches, 1):
            loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
            print(f"  [{idx}] {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")
        
        while True:
            selection = input(f"Select (1-{len(matches)}): ").strip()
            
            try:
                sel_idx = int(selection) - 1
                if 0 <= sel_idx < len(matches):
                    record = matches[sel_idx]
                    print(f"Selected: {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')}")
                    print(f"  Coordinates: {record.get('lat', 'N/A')}, {record.get('long', 'N/A')}")
                    return record
                else:
                    print(f"Invalid selection. Enter 1-{len(matches)}")
            except ValueError:
                print(f"Invalid input. Enter a number")

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
    
    travel_records = all_records[1:4]  # Use 2nd through 4th records for travel
    loc_names = [r.name for r in travel_records]
    coop_ids = [r.coop_id for r in travel_records if r.coop_id]
    
    if not coop_ids:
        return ""
    
    output = f"""d = twc.Data()
d.locName = [{quote_list(loc_names[:len(coop_ids)])}]
d.coopId = [{quote_list(coop_ids)}]
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)"""
    return output


def compile_i1_scmt_removes() -> str:
    """Generate scmtRemove calls for all products."""
    products = [
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
    
    lines = [f"scmtRemove('{product}')" for product in products]
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

def compile_full_config(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    from datetime import datetime

    secret_hehe = "#"
    
    sections = []
    
    start_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    if "Oct 10" in start_time:
        import base64
        secret_hehe = base64.b64decode("I+KghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghAoj4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCECiPioITioITioITioILioITioJDioITioITioITioJDioITioITioILioITioJDioITioITioITioITioITiooDio6Dio7bio7bio7/io7/io7/io7fio7bio7bio6Tio4DioYDioITioITioITioITioITioITioILioITioJDioITioITioILioITioJDioITioITioILioITioJDioITioKDioIQKI+KghOKghOKhgOKgoOKgkOKghOKghOKggeKghOKhgOKgkOKghOKgkOKgiOKghOKghOKghOKghOKjgOKjtOKjv+Kjv+Kjv+Kjv+Kjv+Kiv+Kjv+Kiv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjt+KjpuKhgOKghOKghOKghOKghOKggeKigOKgiOKghOKgiOKghOKhgOKggeKghOKhiOKghOKgoOKghOKghAoj4qCE4qCE4qCE4qGA4qCE4qGA4qCI4qCE4qGA4qCE4qGA4qCQ4qCE4qCE4qCE4qCE4qKA4qO04qO/4qO/4qG/4qO/4qK94qO+4qO94qK/4qO64qGv4qO34qO74qO94qO74qOf4qO/4qO/4qO/4qO/4qOm4qGA4qCE4qCE4qCE4qCE4qGA4qCQ4qCI4qCE4qCE4qCE4qCC4qCE4qCE4qCE4qCQ4qCECiPioITioITioIHioITioITiooDioITioIHioITioITiooDioITioITioITioITiooDio77io7/io7/ior/iob3ioa/io7/ior7io5/io7/io7Pior/iob3io77io7rio7Pio7vio7rio73io7viob/io7/io7/io6bioITioITioITioITioITioITioITioILioIHioITioJDioITioYDioITioIQKI+KghOKghOKgguKghOKggeKghOKghOKgkOKgiOKghOKghOKghOKghOKghOKghOKjv+Kjv+Kjv+Kjr+Kiv+KjveKju+KjveKjv+Kjv+Kjr+Kjv+Kjv+Kjv+Kjt+Kju+KiruKjl+Khr+KjnuKhvuKhueKhteKju+Kjv+Kjh+KghOKghOKghOKgguKghOKghOKgoOKgkOKghOKgguKghOKigOKghOKghAoj4qCE4qCE4qCC4qCI4qCE4qCI4qCE4qCE4qCC4qCE4qCB4qCE4qCE4qCE4qO44qO/4qO/4qO/4qO/4qG/4qG+4qOz4qK/4qK/4qK/4qC/4qC/4qCf4qCf4qCf4qC/4qOv4qG+4qOd4qOX4qOv4qKq4qKO4qKX4qOv4qO/4qOH4qCE4qCE4qCE4qCE4qKA4qCE4qKA4qCg4qCE4qCI4qCE4qCE4qGACiPioITioITioILioITioYjioITioKDioITioKDioJDioIjioITioITioITioIvioInioIHioJHioIHioonio4HioYHioIHioIHioITioITioITioITioITioITioITiooniorvior3io57ior7io5XiopXiop3ioo7io7/io7/ioYDioITioITioITioITiooDioITioITioYDioJDioIjioITioIQKI+KghOKghOKgguKggeKghOKghOKghOKghOKghOKghOKigOKghOKghOKghOKhp+KgoOKhgOKgkOKgguKjuOKjv+Kiv+KilOKilOKipOKiiOKgoeKhseKjqeKipOKitOKjnuKjvuKjveKivuKjveKjuuKhleKhleKhleKhveKjv+Kjv+Kgn+KituKghOKghOKghOKghOKghOKghOKgoOKghOKgguKghAoj4qCE4qCE4qCC4qCE4qCQ4qCE4qCg4qCE4qCE4qCC4qCE4qCE4qCE4qCE4qO/4qGz4qGE4qGi4qGC4qO/4qO/4qKv4qOr4qKX4qO94qOz4qGj4qOX4qKv4qOf4qO/4qO/4qK/4qG94qOz4qKX4qG34qO74qGO4qKO4qKO4qO/4qGH4qC74qOm4qCD4qCE4qCE4qCE4qGA4qCC4qCg4qCE4qCC4qCECiPioITioITioILioIjioITioJDioITioKDioITioITioILioITioITioITiob/ioZ3ioZzio5zio6zio7/io7/io7/io7fio6/iorrioLviobvio5ziopTioKHiopPiop3iopXioo/iopfioo/ioq/iobPioZ3iobjiobjio7jio6fioYDio7nio6DioITioITioITioYDioJDiooDioJDioIjioIQKI+KghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKjh+KiquKijuKhp+Khm+Kgm+Kgi+Kgi+KgieKgmeKjqOKjruKjpuKiheKhg+Kgh+KhleKhjOKhquKhqOKiuOKiqOKio+Kgq+KhqOKiquKiuOKgsOKjv+Kjh+KjvuKhnuKghOKghOKghOKghOKghOKghOKghOKghOKghAoj4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qKR4qGV4qG14qG74qOV4qCE4qCE4qCE4qCU4qGc4qGX4qGf4qOf4qK/4qKu4qKG4qGR4qKV4qOV4qKO4qKu4qGq4qGO4qGq4qGQ4qKF4qKH4qKj4qC54qGb4qO/4qGF4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCECiPioITioITioITioITioITioITioITioITioITioITioITioITioITioITiorjioo7ioKrioYrio4Tio7Dio7Dio7Xio5Xio67io6Lio7PiobjioajioKrioajioILioITioJHioo/ioJfioo3ioKrioaLioqPiooPioKrioYLio7nio73io7/io7fioYTioITioITioITioITioITioITioITioIQKI+KghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKghOKhuOKgkOKgneKgi+Kgg+KgoeKhleKgrOKgjuKgrOKgqeKgseKimeKjmOKjkeKjgeKhiOKghOKghOKhleKijOKiiuKiquKguOKhmOKhnOKijOKgouKjuOKjvuKiv+Kjv+Kjv+KhgOKghOKghOKghOKghOKghOKghOKghAoj4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qGO4qOQ4qCy4qKS4qKa4qKb4qKb4qKb4qKb4qCb4qCd4qGL4qGr4qKJ4qCq4qGx4qCh4qCE4qCg4qKj4qKR4qCx4qGo4qGK4qGO4qKc4qKQ4qCF4qK84qG+4qOf4qO/4qO/4qO34qCR4qCQ4qKG4qGk4qOE4qCE4qCECiPioITiooLioJDioJDioYDioKHioITioIXioIjioITioIHioITioITio6DioYPioaLioKjiooDiooLiopDiopDiooTioJHioIziooziooLioKLioKHioZHioZjioozioKDioZjioYzioo7ioJzioYzioo7ioJzioYzioKLioKjiobjio7/iob3io7/io7/io7/io6PioITioqrioqrio7rioYTioIQKI+KghOKgguKghOKhgeKghOKgguKhgeKgiOKhgOKgguKjgeKitOKgi+KggeKhouKhkeKhqOKikOKikOKijOKgouKjguKio+KgqeKhguKhouKhkeKhkeKhjOKinOKgsOKhqOKiquKimOKglOKhseKimOKglOKhkeKgqOKiiOKgkOKivOKht+Kjv+Kju+Kit+Kir+KiguKgo+KhmOKglOKhouKiv+KhgAoj4qCE4qCF4qCC4qGA4qCC4qKB4qCE4qCE4qKA4qKO4qKO4qCC4qCE4qCE4qGi4qGD4qGi4qKK4qKU4qKi4qCj4qGq4qGi4qKj4qCq4qGi4qGR4qGV4qGc4qGc4qGM4qKO4qKi4qCx4qCo4qGC4qGR4qCo4qCE4qCB4qGC4qGo4qO64qG94qGv4qGr4qCj4qCh4qCi4qKR4qKI4qCC4qCM4qGG4qOnCiPioITioILioIHioITioIjioITioITioITiopjiopziopXioITioITio7DiobjioJDioIzioIbioofioI7ioY7ioo7ioo7ioo7ioo7ioo7ioo7ioI7ioY7ioarioJjioIzioILioIHioIHioITiooDioITiooTioqLioprioq7ioo/ioJ7ioajiooLioJXioInioIzioaDioILioIzioozioKLio7oKI+KghOKjgOKjpOKjtOKjtuKjtuKjtuKiluKhp+KhkeKgrOKhgOKigOKhr+Khg+KhjOKgiOKgiOKghOKghOKgiOKghOKghOKghOKghOKghOKgguKggeKghOKghOKghOKghOKghOKghOKihOKiguKiouKiseKiseKiseKgseKioeKikeKgjOKiguKgoeKgoOKgoeKgoeKhguKgheKileKigeKiiuKijgoj4qO/4qO/4qK/4qG/4qCf4qCJ4qCE4qCB4qKw4qKM4qCq4qOA4qG44qCo4qKC4qCM4qGK4qKE4qKC4qCg4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qCE4qKA4qCg4qKQ4qKo4qOY4qKU4qK14qCx4qGD4qGD4qGV4qG44qCQ4qGB4qCM4qGQ4qGo4qCo4qKK4qCM4qGi4qKR4qKF4qCq4qGw4qGxCiPio4/io67io6Tio6Tio6TioaTioITioK7ioo/ioKfio6PioqPioo7ioKjioITioITioKjioorioqrioqrioavioarioYrioZDioZDioZDioYzioazioarioario47iopfioZXioY7ioaPioIPiooXioIrioIbioKHioKDioYHioKLioZHioZDioozioozioKLioZHioYzioobioo7ioI7ioKrioIgKI+Khv+KhneKgr+Kij+Kgk+KghOKghOKigOKikOKgiOKhjuKhjuKhjuKghOKgiOKghOKgoeKiguKgguKhleKhleKhleKgleKijOKijOKiouKiseKiuOKhuOKjquKiruKho+Khk+KgjOKgoOKikeKgoeKiiOKgjOKijOKiguKgquKgqOKhguKjiuKgouKhouKio+KiseKguOKgkeKggeKghOKhgOKiggoj4qCB4qOI4qOA4qOA4qOA4qGA4qCE4qKQ4qCU4qCQ4qKo4qKi4qKj4qCK4qKA4qCo4qCo4qKQ4qCQ4qG44qG44qGq4qGx4qGR4qGM4qGG4qGH4qGH4qOP4qKu4qKq4qKq4qCK4qCE4qKR4qKQ4qCo4qGQ4qKM4qCi4qGq4qGY4qKM4qCi4qGi4qKj4qCq4qCK4qCE4qCE4qKA4qCC4qCB4qCE4qKCCiPio7/io7/io7/io7/ioIvioITioITioITioIzioKjioITioaPioZHiooXioITioITioKjiopDioKjiorDiorHioqPioqPioqriorjioqjioZrio57iopzioo7ioo7ioo7ioKrioJDioITioYbioaPioarioYrioarioYLioarioZjioYzioY7ioIrioITioZDioIjioYDiooLioIjioITioYHioYIKI+Khn+Kgn+KgneKgg+KghOKghOKghOKghOKijOKgquKghOKho+KgiuKghOKjt+KjhOKghOKghOKgjOKiuOKiuOKgseKhseKhoeKho+Kho+Khs+KhleKhh+Khh+Khh+KgpeKgkeKghOKioeKikeKgleKilOKikeKglOKhjOKhhuKgh+KggeKhgOKghOKggeKghOKiguKgkOKgoOKgiOKghOKiguKgkAoj4qOg4qOk4qO04qOk4qGk4qCE4qCE4qCE4qKQ4qCF4qCF4qGK4qCM4qCE4qO/4qO/4qO34qOk4qOk4qOC4qOF4qOR4qCw4qCo4qCi4qKR4qOV4qOc4qOY4qOo4qOm4qOl4qOs4qCE4qKQ4qKF4qKK4qKi4qKh4qCj4qCD4qCE4qGQ4qCg4qCE4qGC4qCh4qKI4qCg4qCI4qCE4qCh4qCI4qCE4qCoCiPio7/io7/io7/ioZ/ioITioITioITioITioITioozioKLioqjioKjioITiorniopvior/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ior/ioJ/ioITiorDiorDiorHioJHioIHiooDioJDioYDioILioITioKHioJDioJDioYDioILioYHioIzioKDioIHioIziopAKI+Khn+KgneKgiOKghOKghOKghOKghOKghOKgguKgoOKhkeKhseKikOKghOKiuOKhsuKhoOKghOKgieKgmeKgu+Kgv+Kjv+Kgv+Kgv+Kim+Kgq+KhqeKhs+KjuOKgvuKggeKigOKiouKgo+Kgg+KghOKgoOKgkOKhgOKgguKghOKgoeKgiOKghOKhgeKgguKghOKgoeKgkOKiiOKgoOKggeKgjOKgoAoj4qCE4qCE4qOA4qOk4qOk4qOA4qGA4qCE4qCC4qCE4qCQ4qKM4qCG4qKV4qCI4qOX4qKl4qKj4qKh4qKR4qKM4qGi4qGi4qKF4qKH4qKH4qKv4qK+4qG94qCD4qKA4qCU4qGF4qCB4qCE4qCE4qCo4qKA4qCh4qCQ4qCI4qCE4qCh4qKI4qCQ4qGA4qCF4qCM4qCg4qCB4qGC4qCE4qCh4qKI4qCQCiPio77io7/ior/iob/iob/ioIfioITioITioITioYDiooDioKLioK3ioobioKbiob/iobfiobfiobXiobfiobfio7Xior3ioa7io7fior3iob3ioZPioKTioKTioJXioYHioKDioITioIXioITioIXioITioILioIzioKDioKHioIjioITiooLioJDioKDioKjioKDioIHioITiooLioKHioJDioYg=").decode('utf-8')

    if "Jun 07" in start_time:
        import base64
        secret_hehe = base64.b64decode("I+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khv+Kgv+Kim+Kjm+KjqeKjreKjreKjreKjreKjmeKjqeKjreKjreKjreKjreKjmeKjm+Kgu+Kiv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qG/4qCf4qOL4qO14qO24qO/4qO/4qO/4qO/4qO/4qC/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qG34qOm4qOZ4qC74qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/iob/ioovio7Tio7/io7/ioZ/iob/iorvio7/io7/ioZ/io7/ioLjio7/ioZnio7/io7/io4fiorvio7/io7/io7/io7/io7/io7fio43iobvio7fio6ziobvio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khv+Kio+KjtuKiv+Khv+Kii+KgjeKisOKgg+KjvuKjv+Kjv+KioeKjv+KhhuKiv+Kjp+KgueKjv+Kjv+KjhuKiu+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KjpuKhueKjt+KjjOKgu+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qCP4qO04qG/4qGh4qCL4qG04qKj4qCi4qCD4qO84qO/4qO/4qKD4qO+4qO/4qGH4qOM4qC74qO34qGI4qC74qK/4qOm4qGZ4qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO34qOM4qK/4qO34qGc4qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioovio7zioZ/ioIHioITio6jioJ7ioYHiooDio77io7/iob/iooPio77io7/ioo/io7Tio7/io7fio67io5nioYLioITioKjiopnioYLioJnioLvior/io7/io7/io7/io7/io7/io6fioZnior/io4biorvio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khn+KjuOKjv+Kgg+KjtOKjtuKjv+KgluKjo+KjvuKjv+Kgn+KjoeKhvuKgn+Kjq+KjvOKjv+Kjv+Kjv+Kjv+Kjv+Kjt+KjtuKjpOKjvOKjt+KjtuKjpuKjrOKjmeKhu+Kiv+Kjv+Kjv+Kjv+Kjt+KjnOKgv+KjjuKiu+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qG/4qKg4qO/4qOv4qO84qG/4qKf4qOh4qO+4qC/4qKb4qOh4qOk4qO04qO24qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO34qOs4qGZ4qO/4qO/4qO/4qO34qO24qOG4qC54qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPio7/io7/io7/io7/io7/io7/io7/io7/io7/ioIPio77io7/io7/io6bio6Tio6TiooDio7bio77iopvioa3ioJDioJLioJLioKzioZvior/io7/io7/iorjio7/io7/ioYzio7/io7/iob/ioovioIXioJLioJDioJLioqzioZ3ior/io7fioZjio7/io7/io7/io7/io7/io7fioZzior/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KiuOKjv+Kjv+Kjv+Kjv+Kjv+Kig+KjvuKjv+KhoeKhj+KggOKgkOKggOKgguKggOKjiOKjvOKjv+Khh+KivuKjv+Kjv+KhhuKiv+Kjv+Kjp+KjgOKggOKgsOKgoOKgheKggOKiueKhjuKjv+Kjt+KhmOKjv+Kjv+Kjv+Kjv+Kjv+Khv+Kgt+KgrOKimeKiu+Kiv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qK44qO/4qO/4qO/4qO/4qGP4qO84qO/4qO/4qO/4qG/4qC24qC24qC24qKe4qOr4qO84qO/4qCf4qOh4qOt4qO24qOm4qO94qOM4qC74qO/4qOm4qOZ4qGy4qC24qC24qC24qK/4qO/4qO/4qO/4qOn4qC44qO/4qO/4qO/4qO/4qO/4qOm4qOk4qOt4qGt4qKA4qO/4qO/4qO/4qO/4qO/CiPio7/io7/ioZ/iorvio7/io7/io7/io7/ioY/io7jio7/io7/io7/iob/ioqDio7/io7/io7/io7/io7/io7/io7/io7/io7/ioJ/ioovio7Tiob/ioJPioLnio7/ioY/ioJnioL/iorfio47iorviobvio7/io7/io7/io7/io7/io7/io7/io7/io7/ioYbiorvio7/io7/io7/io7/io7/ioZ/ioonio5LioYHio7zio7/io7/io7/iob8KI+Kjv+Kjv+Kjt+KgoOKjieKhm+Kgv+Kim+KjoOKjv+Kjv+Kjv+Kjv+Khh+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khv+Kii+KjteKjv+KjpuKjm+KjoOKjtOKjvuKjv+Kjt+KjtuKjpOKjm+Kjm+KjvOKjv+KjpuKjmeKiv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjt+KiuOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khv+KioeKjv+Kjv+Kjv+Khv+Kgngoj4qO/4qCL4qKb4qC34qCN4qCb4qK74qO/4qO/4qO/4qO/4qO/4qO/4qKw4qO/4qO/4qO/4qO/4qO/4qG/4qOr4qO24qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO34qON4qK74qO/4qO/4qO/4qO/4qO/4qK44qO/4qO/4qO/4qO/4qO/4qO/4qG/4qOh4qO+4qO/4qO/4qO/4qO/4qGMCiPio7/ioIDioKbiobvior/io7/io7/io7/io7/io7/io7/io7/io5/iorjio7/io7/io7/io7/ioo/io7Tio7/io7/io7/ioL/ioJ/ioJvio5vioZvioInioInio4nioInioIniopvio5vioJvioZvioL/ioL/io7/io7/io7/io7fiobnio7/io7/io7/io7/iorjio7/io7/io7/io7/ioJ/io6vioLTioJ/io7vio7/io7/io7/iob/ioIEKI+Kjv+KjhuKgs+KjpuKjpOKjveKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjl+KiuOKjv+Kjv+Kjv+Kgh+KjvuKjv+Khn+Kgi+KggOKjrOKioeKjtuKjjuKjsOKjv+Kjv+KjgOKjvuKjv+Kjt+KjseKjtuKhjuKjpeKhlOKhguKijeKiv+Kjv+Kjt+KiueKjv+Kjv+Khn+KiuOKjv+Kjv+Kgv+Kjt+KhtuKgluKjq+KjtOKjv+Khv+Kgj+KggeKggOKgkgoj4qO/4qO/4qCj4qCc4qC74qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qC44qO/4qO/4qGP4qK44qO/4qGP4qKg4qK44qKH4qO/4qK74qO/4qO/4qO/4qO/4qO/4qGb4qO/4qO/4qO/4qK/4qO/4qC/4qO/4qOH4qO/4qKI4qCC4qK54qO/4qGM4qO/4qO/4qGH4qO/4qG/4qCb4qCm4qCE4qOA4qO/4qG/4qCJ4qCB4qCA4qCA4qCA4qCA4qCACiPio7/io7/io7fio6zioZDioLvior/ior/io7/io7/io7/io7/io7/ioYbiorvio7/io7/iorjio7/ioIDioobioobioKPioI3ioIDioIDioIDioIjioInioIDioIDioIDioIDioIDioIDioIDioIDioIDiopLio4vioJ/ioYTioIjio7/ioYfio7/iob/iorDiob/iooHio7bio6Tio43ioLvioIHioIDioIDioIDioIDio4Dio6Dio4Dio4AKI+Kjv+Kjv+Kjv+Kjv+Kjt+KjgOKgqOKivOKjv+Kjv+Kjv+Kjv+Kjv+Kjp+KguOKjv+Kjv+KiuOKjv+KggOKgmOKgiuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgieKgkOKggeKggOKjv+Kio+Kjv+Kgh+KhvOKig+KjvOKjv+Kjv+Kjv+KjpuKhkOKituKjtuKjtOKjtuKjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qO34qO24qOk4qOt4qOt4qOE4qCZ4qK/4qOG4qK74qO/4qGM4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOv4qO84qG/4qKA4qO04qO/4qO/4qO/4qO/4qGP4qK/4qO34qOE4qGZ4qK+4qO/4qO/4qO/4qO/4qO/CiPio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioJ/ioqDioYbiorLio6zioYjio7/io7/io7/ioYTioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorjio7/io7/ioYfio77io7/io7/io7/io7/io7/io7/iorjio7/io7/io7/ioYTior/io7/io7/io7/io78KI+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kgn+KjoOKjvuKjv+Kjt+KguOKjv+Khh+Kiu+Kjv+Kjv+Khh+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjuOKjv+Kjv+KioOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khj+KjvOKjv+Kjv+Kjv+Khh+KguOKjv+Kjv+Kjv+Kjvwoj4qO/4qO/4qO/4qO/4qO/4qO/4qG/4qCb4qCw4qO/4qO/4qO/4qO/4qOG4qK54qO/4qC44qO/4qO/4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qO/4qO/4qGf4qO44qO/4qO/4qO/4qO/4qO/4qGf4qOw4qO/4qO/4qO/4qG/4qKB4qO34qOk4qG54qO/4qO/CiPio7/io7/io7/io7/ioZ/ioonio7Tio77io4bioLnio7/io7/io7/io7/io4bioLvioYbio7/io7/io7/ioYTioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioqDio7/io7/ioIfio7/io7/io7/io7/iob/ioovio7Tio7/io7/io7/ioJ/io6Dio77io7/io7/io7fioYzior8KI+Kjv+Kjv+Kjv+Kgi+KjtOKjv+Kjv+Kjv+Kjv+Kjt+KhiOKgu+Kjv+Kjv+Kjv+Kjv+Kjp+KiuOKjv+Kjv+Khh+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKiuOKjv+Kjv+KisOKjv+Kjv+Kjv+Kjv+Kjt+Kjv+Kjv+Kjv+Khv+Kig+KjtOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+KhjAoj4qO/4qO/4qKD4qO+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qOm4qGI4qC74qO/4qO/4qO/4qGI4qO/4qO/4qOn4qKg4qKk4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC04qCG4qO+4qO/4qGP4qO44qO/4qO/4qO/4qO/4qO/4qO/4qG/4qKL4qO04qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPio7/ioIfio77io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7bio4zioLvior/ioYfior/io7/io7/ioLDior/ioYLioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDio7/ioIfio7/io7/ioYfio7/io7/io7/io7/io7/iob/ioovio7Tio77io7/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+Khv+KiuOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjt+KjtuKjpuKiuOKjv+Kjv+KhhOKiv+Kjn+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjm+Kgu+KiuOKjv+Kjv+KigeKjv+Kjv+Kjv+Kgn+KjgeKjtOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qGH4qO+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGA4qO/4qO/4qOH4qCZ4qOr4qOk4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC44qC/4qGH4qO44qO/4qGf4qK44qC/4qKL4qOl4qO+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPioIfio7/io7/io7/io7/io7/io4bioLjio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioYfiorvio7/io7/ioYTioL/io6/ioYTioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiobvio7/iooDio7/io7/ioY/io6Dio77io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+KggOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+KhgOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjt+KiuOKjv+Kjv+Kjh+KisOKjv+Kil+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKitOKjp+KgmeKiuOKjv+Kjv+Kgg+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qCw4qO/4qO/4qO/4qO/4qO/4qO/4qOn4qC44qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGI4qO/4qO/4qO/4qOG4qKj4qO/4qKD4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qOA4qKw4qOn4qC74qKh4qO/4qO/4qO/4qKw4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPioJjio7/io7/io7/io7/io7/io7/io7/ioYbiorvio7/io7/io7/io7/io7/io7/io7/io7/io7/ioYfior/io7/io6/ioLvio6bioInior/ioYfio7/iobfio7biorLio7/ioZ7io7/ioLrioJ/io6Dior/io7/io7/ioYfio7jio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io78KI+KgiOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KhhOKiu+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KguOKjv+Kjv+Kjt+KhmeKit+KjpuKjlOKjiOKgieKgm+KgqeKgm+KigeKjieKjtOKhvuKii+KjvOKjv+Kjn+KigOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjvwoj4qGE4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGE4qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGG4qK74qO/4qO/4qO/4qO34qOt4qOb4qC74qC/4qC/4qC/4qC/4qC/4qKb4qOr4qO04qO/4qO/4qO/4qCH4qO84qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/CiPioYfio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioYTioLnio7/io7/io7/io7/io7/io7/io7/io7/ioYzioL/io7/io7/io7/io7/io7/iob/io7/io7/io7/io7/ior/ior/io7/io7/io7/iob/ioI/io7zio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io78=").decode('utf-8')

    if "Apr 20" in secret_hehe:
        import base64
        secret_hehe = base64.b64decode("II+KggOKggOKigOKhoOKgtOKgkuKgkuKimuKjk+KjsuKjtuKjpuKjpOKjgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qO04qOv4qO24qO24qG+4qC/4qCb4qOL4qOJ4qOl4qOk4qK24qG+4qO/4qO24qOE4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPiorjio7vio63iorXio7bio7Lior/io7vio5/io7/ioL7io73ioq/iob/io7Xioq/iob/io7fio4TioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KiuuKjv+KjnuKiv+KjvuKgn+Kgm+KgieKgieKgieKgieKgmeKgu+Kjv+KjveKir+Kjn+Kjs+Kiv+Kjt+KhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCY4qO34qOv4qO/4qCB4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC74qO/4qK+4qO94qO74qOe4qO34qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIjioLvio7/io4bioYDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorniob/io57io6fio5/iob7io4fioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKgieKgm+KgkuKggOKggOKggOKggOKggOKggOKggOKggOKggOKjv+Kjn+KhvuKjreKjn+Kjv+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK74qO+4qO94qOz4qOf4qO+4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio7/io5/iob7io6fio5/io77ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio4Dio4DioKTioKTioJLioJLioKDioKTio4DioYDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKioOKjv+Kjr+Kjn+Kit+Kjq+Khn+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKhoOKikuKjieKgpeKggOKgkuKgguKgieKggeKggOKghOKggOKgieKgkeKgpuKjhOKhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qO+4qOf4qG+4qOt4qK/4qO94qCD4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qCe4qCJ4qCB4qCA4qKA4qCA4qCC4qKA4qCC4qCI4qCg4qCA4qKB4qCI4qCA4qCE4qCA4qCI4qCT4qCm4qOE4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qOACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDio77io5/iob7io73ioq/io5/ioY/ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorDio7nioIDioIDiobDioIPioIDioYDioILioojioIDioKDioIjiooDioIDioYHioITioIjioYDioKDioIHioKDioIjioJDioIDioYDioIDioJnioKLio4TioIDioIDioIDioIDioIDioIDio4DioKTio57ioL3ioZ4KI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKioOKjvuKjn+KhvuKjveKir+Kjn+KgnuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjv+KggOKjp+KgnOKggeKigOKgkOKggOKhkOKggOKhgOKgguKgkOKggOKgoOKggOKhgOKgguKigOKgkOKggOKggeKisOKhjOKggOKhgOKggeKgoOKggeKggOKgmeKgouKjgOKgpOKgluKgi+Kgk+KgieKigOKjvuKghwoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qO04qO/4qOf4qG+4qO94qKv4qO/4qCL4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qK/4qCA4qC44qGG4qCA4qCC4qKA4qCC4qKA4qCQ4qCA4qCg4qCB4qKI4qCA4qCQ4qCA4qGQ4qCA4qCg4qCI4qKQ4qKu4qO34qCA4qCA4qCM4qCA4qCE4qCB4qCg4qCA4qKA4qCA4qCg4qCA4qCE4qKC4qO+4qGf4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioqDio77io7/io7Pioq/io7/io7nioJ/ioIHioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio4DiobTior7ioZvioIDioYDioLniopfioK7io4TioYDioKDioIDioIzioIDioZDioIDioKDioIHioKDioIDioITio6HioJbioInio7zio7vioILioIjiooDioJDioIDioIzioIDioZDioIDioYDioILioITio6LioZ/iob7ioIHioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKjtOKjv+Kjn+KhvuKjveKhu+KgnuKggeKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKit+KggOKiuOKhl+KggOKgoOKigOKggOKhgOKggOKgieKgm+KgkuKgtuKgtuKgtuKgluKgm+KggeKigOKgkuKgieKhgOKgoOKisOKjt+Khj+KipOKjrOKjpOKjpOKirOKjgOKhkOKggOKghOKigOKikOKhvOKih+Khv+KggeKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qO+4qO/4qO74qK+4qG94qCL4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qCz4qOk4qOA4qCg4qCB4qCA4qCE4qCA4qCM4qKA4qCQ4qCg4qCA4qGA4qCA4qCE4qCQ4qCI4qCA4qGA4qCC4qCA4qO04qO/4qCf4qCA4qCA4qCZ4qKz4qG+4qCu4qO34qOd4qG74qC24qG04qKv4qO54qG/4qCB4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDiorjio7/io7Piob/ioIvioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorDio7/io7/io7/io7fio77io6bio6zio4Tio4Dio4DioYLioJDioIDioojioIDioILioojioIDioITioKDioInioJ/ioIHioYDioKDiooHio4Lio4DiobzioILioIDioInioJnioLviorfio6fioJ/ioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKiuOKjv+KhveKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKigOKjv+Kjv+Kjv+KjveKjv+Kjv+Kgj+Kiv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KjtuKjtuKjtuKjtuKjvuKjv+Kjv+Kjv+Kjv+Kjv+KhhOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qK/4qGH4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qO/4qO/4qO/4qO/4qO/4qG/4qCA4qK44qO/4qO/4qOf4qOb4qC74qK/4qO/4qGf4qCA4qK44qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qOH4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioLnio4bioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio7/io7/io7/io7/io7/io7/io7/io6Tio6/io7/io7/io7/io7/io7fio7/io7/io4fioIDiooDio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgs+KghOKhgOKggOKggOKggOKhoOKjpOKjpOKjpOKgpOKgpOKgpOKgpOKgpOKgpOKgpOKgpOKgpOKgpOKgpOKipOKjgOKjgOKjgOKjgOKjgOKhgOKggOKggOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+KjreKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kiv+Kjv+KjpuKjvuKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCB4qCA4qKw4qO+4qK/4qO94qO74qGH4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCJ4qCJ4qCJ4qCJ4qCZ4qCb4qCb4qCb4qCb4qCb4qO/4qGf4qCb4qC/4qK/4qO/4qO/4qO/4qO/4qOv4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioJjio7/io5/io77io7PioYfioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio4Dio4Dio4Dio4Dio4Dio4Dio4Dio4Dio4Dio4zio4Dio4Dio6Dio6Tio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/iob/ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgm+KgmuKgm+KgkuKgkuKgm+KgkuKgkuKggOKggOKgiOKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKiu+Kjv+Kjv+Kjv+Kjv+Kgn+Kjv+Kiv+Kjv+Kiv+Khv+Kjv+Kjv+Kjv+Kjv+Kjv+Kiv+Khv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kgh+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKI4qG/4qGf4qO94qCP4qCA4qCY4qK/4qOm4qCv4qOd4qOz4qOb4qG84qOz4qKr4qO/4qO94qG+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGf4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiobTio4/io7Pio7nioY/ioIDioJDiooDioIDioIjioJvioLfioLbioKfioL7ioLfioL/iorvioZfioIniornio7/io7/io7/io7/io7/io7/ioZ/ioqDio6DioYDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKhv+KhnOKipuKjv+KggOKigOKggeKioOKjpOKjgeKgoOKggOKjuOKjhOKggOKhgOKigOKgiOKiu+KjpuKhgOKgu+Kjv+Kjv+Kjv+Kjv+Kgn+Kiv+KhjOKgmeKjo+KjhOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC54qOf4qO84qGP4qCA4qCg4qKA4qO+4qO/4qO/4qGE4qO84qO/4qO/4qOG4qCA4qCE4qCQ4qCA4qK74qO34qOE4qCJ4qC54qCL4qCB4qCA4qGA4qK74qOm4qCA4qKT4qGi4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioJjior/ioYfioIDioZDiorjio7/io7/io7/io7/io7/io7/io7/io7/ioIDioKDioIjioIDioITioJvio77io7fioITioIDioILioIHioYDioITiorvio7fioYDioKvio7fioYDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjp+KggOKigOKgmOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KggOKigOKgguKggeKgoOKjuOKgn+KggeKggOKghOKggeKgoOKggOKgoOKiiOKjv+Khv+KjhuKgmOKis+KhhOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKg4qO/4qGA4qKA4qCg4qC54qO/4qO/4qO/4qO/4qO/4qO/4qGH4qCA4qGA4qCE4qCI4qGA4qK/4qOE4qGA4qCM4qCA4qGI4qCA4qKE4qOx4qKv4qO/4qOf4qG94qO34qOE4qCY4qKF4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDiob7ioofiobfio4TioIDioYDioJnioL/io7/io7/io7/io7/ioIfioIDioYDioITioILiooDioqjio7/io7/io7fio6bio7Tio7jio6/io73io77ioZ/io77ior3io7Pior/io6bioYDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjvOKij+Khs+KjjuKhneKjs+KjhOKggOKhgOKgiOKgmeKgv+Kgi+KggOKhgOKghOKggOKgguKhgOKiuOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KjveKjq+KjvuKgn+Kgi+KggeKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK84qOL4qKu4qC14qOa4qG84qGx4qKO4qGf4qOm4qOQ4qCA4qCg4qCA4qCQ4qCA4qCg4qCI4qCA4qCE4qK44qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qC34qCL4qCB4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIjioLvio67io53iobLio5Xioavior3iobjiopbio63io5vioLbio6Tio4HioIjioIDioITioIHioKDiorjio7/io7/io7/io7/io7/io7/ioIPioIHioYfioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKigOKjtOKjvuKjv+Kjv+Kjt+Kjp+Kjj+Kjp+Kim+KhvOKipuKhueKjmuKhpeKij+Khn+Kjs+KipuKjnOKisuKgvOKju+Kjn+Kjn+Kjv+Kjv+Kjv+KjtuKjvuKgl+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGP4qCJ4qCb4qCb4qCb4qCb4qCb4qCb4qK74qO+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGP4qCB4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIjioJnioL/io7/io7/io7/io7/io7/ioJ/ioIHioIDioIDioIDioIDioIDioIDioIDiorjio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io4fioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggeKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKiuOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KjpuKhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAoj4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC74qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGE4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACiPioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIjioLvior/io7/io7/io7/io7/io7/io7/io7/io7/iob/ioIfioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAKI+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgieKgm+Kgm+Kgm+Kgm+Kgm+KgieKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggA==").decode("utf-8")

    sections.append(f"# Created on {start_time}")
    sections.append("# SCMT Configuration File for IntelliStar 1 Domestic")
    sections.append("# Generated by IntelliStar Config Generator by @sspwxr (raii)")
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
    sections.append("dsm.set('scmt_configType', 'domestic',0)")
    sections.append("dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)")
    sections.append("#")
    sections.append(compile_i1_interest_list(config))
    sections.append(compile_i1_metadata(config))
    sections.append("#")
    sections.append(compile_i1_airport_data(config, all_records))
    sections.append("#")
    sections.append(compile_i1_bulletin_override())
    sections.append("#")
    sections.append(compile_i1_vocal_schedule())
    sections.append("#")
    sections.append(compile_i1_scmt_removes())
    sections.append("#")
    sections.append(compile_i1_non_image_maps())
    sections.append("#")
    sections.append("#")
    sections.append(compile_i1_currentconditions(config, all_records))
    sections.append("#")
    sections.append(compile_i1_forecast(config))
    sections.append("#")
    sections.append(compile_i1_airport_delays(config, all_records))
    sections.append("#")
    sections.append(compile_i1_travel_forecast(config, all_records))
    sections.append("#")
    
    end_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    sections.append("Log.info('scmt config completed')")
    sections.append(f"# Finished generation on {end_time}")
    
    return "\n".join(sections)

def main() -> None:
    """Main entry point for the configuration generator."""
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

    # Convert lat/lon to float if they exist
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

    nearby = prompt_for_nearby_locations(max_nearby=7)
    
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
    
    # Main location is already a full database record
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
    
    # Nearby locations are already full database records
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
