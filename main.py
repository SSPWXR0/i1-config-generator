#!/usr/bin/env python3
from __future__ import annotations

import os
import random
import sys

import yaml
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

from systemspecific import i1_domestic, i1_domestic_watt, i1_weatherscan, i2_domestic
from utils.LFRecord_operations import (
    get_timezone_by_location_id,
    prompt_for_nearby_locations,
    prompt_for_location,
    search_and_select_location,
    search_location_auto,
    LocationRecord,
)
from utils.map_utils import (
    get_all_mapcut_coordinates,
    get_projection_for_system,
    get_product_sizes_for_system,
    MAP_PRODUCT_SIZES,
    MAP_PRODUCT_SIZES_WATT,
    MAP_PRODUCT_SIZES_WEATHERSCAN,
)

VERSION = "2.0-2026-01-26"

SystemType = Literal["domestic", "domesticWATT", "weatherscan", "i2"]

SYSTEM_DISPLAY_NAMES: dict[SystemType, str] = {
    "domestic": "IntelliStar 1 Domestic (Pre-WATT, 2003-2013)",
    "domesticWATT": "IntelliStar 1 Domestic Enhanced/WATT (2013-2015) [Experimental]",
    "weatherscan": "IntelliStar 1 Weatherscan (2003-2022)",
    "i2": "IntelliStar 2 / XD / HD",
}

SYSTEM_FILE_SUFFIXES: dict[SystemType, tuple[str, str]] = {
    "domestic": ("_i1_config.py", "py"),
    "domesticWATT": ("_i1watt_config.py", "py"),
    "weatherscan": ("_wxscan_config.py", "py"),
    "i2": ("_i2_config.xml", "xml"),
}


def print_banner() -> None:
    print("=" * 65)
    print("       IntelliStar Configuration Generator")
    print(f"       Created by @sspwxr (raii) - Version {VERSION}")
    print("=" * 65)


def quote_list(items: list[str]) -> str:
    return ", ".join(f"'{item}'" for item in items if item)


@dataclass
class AggregatedConfig:
    location_id: str = ""
    nearby_location_ids: list[str] = field(default_factory=list)
    coop_ids: list[str] = field(default_factory=list)
    tecci_ids: list[str] = field(default_factory=list)
    zone_ids: list[str] = field(default_factory=list)
    county_ids: list[str] = field(default_factory=list)
    county_names: dict[str, str] = field(default_factory=dict)
    obs_stations: list[str] = field(default_factory=list)
    climate_ids: list[str] = field(default_factory=list)
    airport_ids: list[str] = field(default_factory=list)
    full_time_zone: str = ""
    name: str = ""
    state_code: str = ""
    country_code: str = ""
    lat: float | None = None
    lon: float | None = None

    def add_record(self, record: LocationRecord) -> None:
        if not self.location_id:
            self.location_id = record.loc_id

        if record.loc_id and record.loc_id not in self.nearby_location_ids:
            self.nearby_location_ids.append(record.loc_id)

        if not self.state_code and record.state_code:
            self.state_code = record.state_code

        if not self.country_code and record.country_code:
            self.country_code = record.country_code

        if record.coop_id and record.coop_id not in self.coop_ids:
            self.coop_ids.append(record.coop_id)

        for tecci in record.teccis:
            if tecci not in self.tecci_ids:
                self.tecci_ids.append(tecci)

        if record.obs_station and record.obs_station not in self.obs_stations:
            self.obs_stations.append(record.obs_station)

        if record.zone_id and record.zone_id not in self.zone_ids:
            self.zone_ids.append(record.zone_id)

        if record.full_time_zone and not self.full_time_zone:
            self.full_time_zone = record.full_time_zone

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


def select_input_mode() -> Literal["manual", "yaml"]:
    print("\nHow would you like to provide location data?")
    print("  1. Load from input.yaml file")
    print("  2. Manual entry via prompts")
    
    while True:
        choice = input("\nEnter choice (1 or 2). Default is 1: ").strip()
        if choice == "1" or choice == "":
            return "yaml"
        if choice == "2":
            return "manual"


def select_system_type() -> SystemType:
    print("\nSelect the system type to generate a config for:")
    print("  1. Domestic IntelliStar (Pre-WATT, 2003-2013)")
    print("  2. Domestic IntelliStar Enhanced/WATT (2013-2015) [Experimental]")
    print("  3. Weatherscan IntelliStar (2003-2022)")
    print("  4. IntelliStar 2 / XD / HD")
    
    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        if choice == "1":
            return "domestic"
        if choice == "2":
            return "domesticWATT"
        if choice == "3":
            return "weatherscan"
        if choice == "4":
            return "i2"
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

def write_default_input_yaml() -> None:
    contents = """
userLocaleInput:
  locations:
    mainLocation:
      applicable: # the systems on which this location set can be used.
        - i1_domestic
        - i1_domesticWATT
        - i1_weatherscan
        - i2_domestic
      name: Saskatoon # Primary location name. Used on all systems as the default location for weather presentations.
      state: SK

    nearbyLocations:
      applicable:
        - i1_domestic
        - i1_domesticWATT
        - i1_weatherscan
        - i2_domestic
      locations: # Secondary nearby locations for weather presentations. On all I1 systems except WATT, these are displayed in a list after the main current conditions and on the LDL.
      # on all systems with WATT, these are used on the Lower Display Line.
        - name: Warman
          state: SK
        - name: Prince Albert
          state: SK
        - name: Melfort
          state: SK
        - name: Yorkton
          state: SK
        - name: North Battleford
          state: SK
        - name: Lloydminster
          state: AB
        - name: Humboldt
          state: SK
        - name: Outlook
          state: SK
    MapCities:
      applicable:
        - i2_domestic
      reuseNearbyLocations: false # If true, uses the nearby locations as the cities shown on the map display. If false, uses the specified locations below.
      locations: # Cities to be shown on the map display.
        - name: Martensville
          state: SK
        - name: Outlook
          state: SK
        - name: North Battleford
          state: SK
        - name: Lloydminster
          state: AB
        - name: Prince Albert
          state: SK
        - name: Regina Beach
          state: SK
        - name: Dundurn
          state: SK
        - name: Watrous
          state: SK
    MetroMapCities:
      applicable:
        - i2_domestic
      reuseNearbyLocations: false # If true, uses the nearby locations as the cities shown on the metro map display. If false, uses the specified locations below.
      locations: # Cities to be shown on the metro map display.
        - name: Warman
          state: SK
        - name: Martensville
          state: SK
        - name: Biggar
          state: SK
        - name: Osler
          state: SK
        - name: Langham
          state: SK
        - name: Hague
          state: SK
        - name: Rosthern
          state: SK
        - name: Vanscoy
          state: SK
    RegionalMapCities:
      applicable:
        - i2_domestic
      reuseNearbyLocations: false # If true, uses the nearby locations as the cities shown on the regional map display. If false, uses the specified locations below.
      locations: # Cities to be shown on the regional map display.
        - name: North Battleford
          state: SK
        - name: Lloydminster
          state: AB
        - name: Prince Albert
          state: SK
        - name: Yorkton
          state: SK
        - name: Melfort
          state: SK
        - name: Humboldt
          state: SK
        - name: Melville
          state: SK
        - name: Tisdale
          state: SK
    SummerGetawayLocations: # no one has gotten these to work lol. max 3.
      applicable:
        - i2_domestic
      reuseNearbyLocations: false
      locations: []

    WinterGetawayLocations: # no one has gotten these to work lol. max 3.
      applicable:
        - i2_domestic
      reuseNearbyLocations: false
      locations: []

    airportLocations: # no one has gotten these to work lol
      applicable:
        - i1_domestic
        - i1_domesticWATT
        - i2_domestic
      locations: []

    travelDestinations: # no one has gotten these to work lol
      applicable:
        - i1_domesticWATT
        - i1_domestic
      locations:
        - name: Edmonton
          state: AB
        - name: Calgary
          state: AB
        - name: Vancouver
          state: BC

    snowboardLocations: # no one has gotten these to work lol
      applicable:
        - i1_domestic
      locations: []
"""
    with open("input.yaml", "w") as f:
        f.write(contents.strip())


def load_input_yaml() -> dict | None:
    input_path = Path("input.yaml")
    if not input_path.exists():
        print(f"\nError: {input_path} not found.")
        print("Creating a sample input.yaml file... Please edit it with your location data and re-run the program.")
        write_default_input_yaml()
        return None
    
    try:
        with open(input_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except yaml.YAMLError as e:
        print(f"\nError parsing input.yaml: {e}")
        return None

def process_locations_from_yaml(
    data: dict,
    system_type: SystemType
) -> tuple[AggregatedConfig, list[LocationRecord]] | None:
    locations_data = data.get("userLocaleInput", {}).get("locations", {})
    
    main_loc_data = locations_data.get("mainLocation", {})
    main_name = main_loc_data.get("name", "")
    main_state = main_loc_data.get("state", "")
    
    if not main_name:
        print("\nError: No main location name specified in input.yaml.")
        return None
    
    print(f"\nSearching for main location: {main_name}, {main_state}")
    main_record_data = search_location_auto(main_name, main_state)
    
    if main_record_data is None:
        print(f"  ✗ No results found for '{main_name}, {main_state}'")
        return None
    
    config = AggregatedConfig()
    all_records: list[LocationRecord] = []
    
    main_location_name = main_record_data.get('prsntNm', main_name)
    main_lat = _parse_float(main_record_data.get('lat'))
    main_lon = _parse_float(main_record_data.get('long'))
    
    config.name = main_location_name
    config.lat = main_lat
    config.lon = main_lon
    config.state_code = main_record_data.get('stCd', main_state)
    config.country_code = main_record_data.get('cntryCd', '')
    
    main_record = LocationRecord.from_db_record(main_record_data, name=main_location_name)
    all_records.append(main_record)
    config.add_record(main_record)
    
    loc_id_short = main_record.loc_id[:8] if main_record.loc_id else 'N/A'
    print(f"  ✓ Found: {main_location_name} (ID: {loc_id_short})")
    print(f"    Coordinates: {main_lat}, {main_lon}")
    
    nearby_data = locations_data.get("nearbyLocations", {})
    nearby_list = nearby_data.get("locations", [])
    
    processed_loc_ids = {main_record.loc_id}
    
    print(f"\nProcessing {len(nearby_list)} nearby locations...")
    for nearby_loc in nearby_list:
        nearby_name = nearby_loc.get("name", "")
        nearby_state = nearby_loc.get("state", "")
        
        if not nearby_name:
            continue
        
        nearby_record_data = search_location_auto(nearby_name, nearby_state)
        
        if nearby_record_data is None:
            print(f"  ⚠ Not found: {nearby_name}, {nearby_state}")
            continue
        
        loc_id = nearby_record_data.get('locId', '')
        if loc_id in processed_loc_ids:
            print(f"  ⚠ Duplicate skipped: {nearby_name}")
            continue
        
        processed_loc_ids.add(loc_id)
        record = LocationRecord.from_db_record(
            nearby_record_data,
            name=nearby_record_data.get('prsntNm', nearby_name)
        )
        all_records.append(record)
        config.add_record(record)
        loc_id_short = loc_id[:8] if loc_id else 'N/A'
        print(f"  ✓ {record.name} (ID: {loc_id_short})")
    
    return config, all_records


def process_locations_manual(system_type: SystemType) -> tuple[AggregatedConfig, list[LocationRecord]] | None:
    main_record_data = prompt_for_location()
    
    if main_record_data is None:
        print("No location selected. Exiting.")
        return None
    
    main_location_name = main_record_data.get('prsntNm', '')
    main_lat = _parse_float(main_record_data.get('lat'))
    main_lon = _parse_float(main_record_data.get('long'))
    main_state = main_record_data.get('stCd', '')
    main_country = main_record_data.get('cntryCd', '')
    location_id = main_record_data.get('locId', '')
    
    nearby = prompt_for_nearby_locations(max_nearby=8, main_location_id=location_id)
    
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
    
    main_record = LocationRecord.from_db_record(main_record_data, name=main_location_name)
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
        print(f"  OBS STATION: {record.obs_station}")
        print(f"  Coop ID: {record.coop_id}")
        print(f"  Zone ID: {record.zone_id}")
        print(f"  Airport ID: {record.airport_id}")
    
    return config, all_records


def _parse_float(value) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def compile_i1_interest_list(config: AggregatedConfig, system_type: SystemType) -> str:
    if system_type == "weatherscan":
        return i1_weatherscan.compile_interest_list(config)
    if system_type == "domesticWATT":
        raise NotImplementedError("domesticWATT not yet implemented - use domestic for now")
    return i1_domestic.compile_interest_list(config)


def compile_i1_currentconditions(
    config: AggregatedConfig,
    all_records: list[LocationRecord],
    system_type: SystemType
) -> str:
    if system_type == "weatherscan":
        return i1_weatherscan.compile_currentconditions(config, all_records)
    if system_type == "domesticWATT":
        raise NotImplementedError("domesticWATT not yet implemented - use domestic for now")
    raise NotImplementedError("Use generate_domestic_config for domestic")


def compile_i1_forecast(config: AggregatedConfig, system_type: SystemType) -> str:
    if system_type == "weatherscan":
        return i1_weatherscan.compile_forecast(config)
    if system_type == "domesticWATT":
        raise NotImplementedError("domesticWATT not yet implemented - use domestic for now")
    raise NotImplementedError("Use generate_domestic_config for domestic")


def compile_i1_metadata(config: AggregatedConfig, system_type: SystemType) -> str | list[str | int]:
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
        "GENERICABLE SUCKS",
        "I HATE ROGERS XFINITY",
        "DECENTRALIZE TELECOMMUNICATIONS",
        "meowwww",
    ]
    
    random_cable_name = random.choice(random_cable_names)
    
    if system_type == "weatherscan":
        return i1_weatherscan.compile_metadata(config, random_cable_name, random_star_id)
    if system_type == "domesticWATT":
        raise NotImplementedError("domesticWATT not yet implemented - use domestic for now")
    raise NotImplementedError("Use generate_domestic_config for domestic")


def compile_i1_airport_data(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    airport_records = [r for r in all_records if r.airport_id]
    
    airport_ids = [r.airport_id for r in airport_records]
    airport_names = [r.name for r in airport_records]
    airport_teccis = [r.teccis[0] if r.teccis else "" for r in airport_records]
    
    return f"""scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = [{quote_list(airport_ids)}]
d.airportLocName = [{quote_list(airport_names)}]
d.obsStation = [{quote_list(airport_teccis)}]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)"""


def compile_i1_airport_delays(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    airport_records = [r for r in all_records if r.airport_id]
    
    if not airport_records:
        return ""
    
    airport_ids = [r.airport_id for r in airport_records[:3]]
    airport_teccis = [r.teccis[0] if r.teccis else "" for r in airport_records[:3]]
    airport_names = [r.name + " Arpt" for r in airport_records[:3]]
    display_flags = [1] * len(airport_ids)
    
    return f"""d = twc.Data()
d.airportId = [{quote_list(airport_ids)}]
d.obsStation = [{quote_list(airport_teccis)}]
d.locName = [{quote_list(airport_names)}]
d.displayFlag = {display_flags}
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)"""


def compile_i1_travel_forecast(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    if len(all_records) < 2:
        return ""
    
    travel_records = all_records[1:4]
    loc_names = [r.name for r in travel_records]
    coop_ids = [r.coop_id for r in travel_records if r.coop_id]
    
    if not coop_ids:
        return ""
    
    return f"""d = twc.Data()
d.locName = [{quote_list(loc_names[:len(coop_ids)])}]
d.coopId = [{quote_list(coop_ids)}]
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)"""


def compile_i1_scmt_removes(system_type: SystemType) -> str:
    if system_type == "weatherscan":
        return i1_weatherscan.compile_scmt_removes()
    if system_type == "domesticWATT":
        raise NotImplementedError("domesticWATT not yet implemented - use domestic for now")
    raise NotImplementedError("Use generate_domestic_config for domestic")


def compile_i1_bulletin_override() -> str:
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
    return """scmtRemove('Config.1.VocalLocalSchedule')
d = twc.Data()
d.OffTimes = ( )
dsm.set('Config.1.VocalLocalSchedule', d, 0, 1)
#
scmtRemove('Config.1.Ldl_LASCrawl')
scmtRemove('Config.1.LASCrawl')"""


def compile_i1_non_image_maps() -> str:
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
    return i1_weatherscan.compile_packages(config)


def compile_wxscan_airport_data(config: AggregatedConfig, all_records: list[LocationRecord]) -> str:
    return i1_weatherscan.compile_airport_data(config, all_records)


def compile_i1_map_data(
    config: AggregatedConfig,
    all_records: list[LocationRecord],
    system_type: SystemType
) -> str:
    if config.lat is None or config.lon is None:
        return "# MAP DATA SKIPPED - No lat/lon available for primary location"
    
    lines: list[str] = []
    lines.append("#")
    lines.append("# MAP DATA CONFIGURATION")
    lines.append("# Generated from primary location coordinates")
    lines.append(f"# Lat: {config.lat}, Lon: {config.lon}")
    lines.append(f"# System: {SYSTEM_DISPLAY_NAMES.get(system_type, system_type)}")
    lines.append("#")
    
    primary_name = config.name if config.name else "Location"
    
    map_sizes = get_product_sizes_for_system(system_type)
    projection = get_projection_for_system(system_type)
    mapcuts = get_all_mapcut_coordinates(config.lat, config.lon, map_sizes, projection)
    
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
    
    if system_type == "domesticWATT":
        font_name = "Akko-Bold"
    elif system_type == "weatherscan":
        font_name = "Frutiger_Bold"
    else:
        font_name = "Interstate-Bold"
    
    product_params = _get_product_params_for_system(system_type)
    
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
        size = map_sizes[product_name]
        
        datacut = calc_datacut_coord(cut_x, cut_y, size[0], size[1])
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
        lines.append(f"               ('{font_name}',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),")
        lines.append(f"              ( ( ({center_pos[0]-16},{center_pos[1]-9}),'{primary_name}',),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"             (")
        lines.append(f"               ('{font_name}',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),")
        lines.append(f"              ( ( ({center_pos[0]-16},{center_pos[1]-9}),'{primary_name}',),")
        lines.append(f"              ),")
        lines.append(f"             ),")
        lines.append(f"        ],")
        lines.append(vector_style)
        lines.append(f")")
        lines.append(f"dsm.set('Config.1.{product_name}', d, 0)")
        lines.append("")
    
    lines.append("#")
    lines.append("# Map and Radar Interest Lists")
    lines.append("#")
    
    if system_type == "weatherscan":
        lines.extend(_get_weatherscan_interest_lists())
    else:
        lines.extend(_get_domestic_interest_lists(system_type))
    
    lines.append("# END OF MAPS")
    lines.append("# commit for map stuff to avoid missing updates")
    lines.append("ds.commit()")
    
    return "\n".join(lines)


def _get_product_params_for_system(system_type: SystemType) -> dict:
    base_params = {
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
    
    if system_type == "domesticWATT":
        base_params.update({
            "Local_SummaryFS": {
                "datacutType": "radar.us",
                "mapFinalSize": (720, 277),
                "dataFinalSize": (720, 277),
                "mapMilesSize": (141, 54),
            },
            "LFLocal_LocalDoppler": {
                "datacutType": "radar.us",
                "mapFinalSize": (788, 338),
                "dataFinalSize": (788, 338),
                "mapMilesSize": (154, 66),
            },
            "Local_MetroRadarFS": {
                "datacutType": "radar.us",
                "mapFinalSize": (720, 268),
                "dataFinalSize": (720, 268),
                "mapMilesSize": (127, 47),
            },
            "Local_Satellite": {
                "datacutType": "radarSatellite.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (291, 194),
            },
            "Local_RegionalRadarFS": {
                "datacutType": "radar.us",
                "mapFinalSize": (720, 268),
                "dataFinalSize": (720, 268),
                "mapMilesSize": (388, 144),
            },
        })
    elif system_type == "weatherscan":
        base_params = {
            "Radar_LocalDoppler": {
                "datacutType": "radar.us",
                "mapFinalSize": (240, 137),
                "dataFinalSize": (240, 137),
                "mapMilesSize": (141, 97),
            },
            "Local_LocalDoppler": {
                "datacutType": "radar.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (141, 94),
            },
            "Local_RadarSatelliteComposite": {
                "datacutType": "radarSatellite.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_RegionalForecastConditions": {
                "datacutType": "forecast.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (564, 376),
            },
            "Local_FrostFreezeWarnings": {
                "datacutType": "frostFreeze.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_SnowfallQpfForecast": {
                "datacutType": "snowfallQpfForecast.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_NationalTravelWeather": {
                "datacutType": "travelWeather.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_EstimatedPrecipitation": {
                "datacutType": "estimatedPrecip.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_PrecipitationQpfForecast": {
                "datacutType": "precipQpfForecast.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
            "Local_PalmerDroughtSeverity": {
                "datacutType": "palmerDrought.us",
                "mapFinalSize": (720, 480),
                "dataFinalSize": (720, 480),
                "mapMilesSize": (127, 85),
            },
        }
    
    return base_params


def _get_domestic_interest_lists(system_type: SystemType) -> list[str]:
    lines = []
    lines.append("wxdata.setInterestList('mercator.us','1',['radar.us',])")
    
    if system_type == "domesticWATT":
        lines.append("wxdata.setInterestList('lambert.us','1',['radarSatellite.us',])")
        lines.append("wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite',])")
        lines.append("wxdata.setInterestList('radar.us.cuts','1',['Config.1.LFLocal_LocalDoppler','Config.1.Local_SummaryFS','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_MetroRadarFS','Config.1.Local_RegionalRadarFS','Config.1.Local_RegionalDopplerRadar',])")
        lines.append("wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])")
        lines.append("wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us',])")
    else:
        lines.append("wxdata.setInterestList('radar.us.cuts','1',['Config.1.NationalLdl_DopplerRadar','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])")
        lines.append("wxdata.setInterestList('mapData','1',['mercator.us',])")
        lines.append("wxdata.setInterestList('imageData','1',['radar.us',])")
    
    return lines


def _get_weatherscan_interest_lists() -> list[str]:
    lines = []
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
    return lines


def compile_full_config(
    config: AggregatedConfig,
    all_records: list[LocationRecord],
    system_type: SystemType
) -> str:
    if system_type == "i2":
        return i2_domestic.compile_config(config)
    
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
        "GENERICABLE SUCKS",
        "I HATE ROGERS XFINITY",
        "DECENTRALIZE TELECOMMUNICATIONS",
        "meowwww",
    ]
    random_cable_name = random.choice(random_cable_names)

    timezone = get_timezone_by_location_id(all_records[0].loc_id)
    
    if system_type == "domestic":
        return i1_domestic.generate_domestic_config(
            config, all_records, random_cable_name, random_star_id, timezone
        )
    
    if system_type == "domesticWATT":
        
        return i1_domestic_watt.generate_domestic_watt_config(
            config, all_records, random_cable_name, random_star_id, timezone
        )
    
    sections: list[str] = []
    start_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    
    sections.append(f"# Created on {start_time}")
    sections.append(f"# SCMT Configuration File for {SYSTEM_DISPLAY_NAMES[system_type]}")
    sections.append(f"# Generated by IntelliStar Config Generator v{VERSION} by @sspwxr (raii)")
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
    
    if system_type == "weatherscan":
        sections.append("dsm.set('scmt_configType', 'wxscan',0)")
        sections.append("dsm.set('scmt.ProductTypes',['None'], 0)")
    
    sections.append("#")
    sections.append(f"wxdata.setTimeZone('{get_timezone_by_location_id(all_records[0].loc_id)}')")
    sections.append("#")
    
    if system_type == "weatherscan":
        sections.append(compile_i1_scmt_removes(system_type))
        sections.append(compile_i1_map_data(config, all_records, system_type))
        sections.append("#")
        sections.append(compile_i1_interest_list(config, system_type))
        sections.append(compile_i1_metadata(config, system_type))
        sections.append("#")
        sections.append(compile_wxscan_airport_data(config, all_records))
        sections.append("#")
        sections.append(compile_i1_bulletin_override())
        sections.append("#")
        sections.append(compile_i1_vocal_schedule())
        sections.append("#")
        sections.append(compile_wxscan_packages(config))
        sections.append("#")
        sections.append(compile_i1_currentconditions(config, all_records, system_type))
        sections.append("#")
        sections.append(compile_i1_forecast(config, system_type))
        sections.append("#")
        sections.append(compile_i1_travel_forecast(config, all_records))
        sections.append("#")
    
    end_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
    sections.append("Log.info('scmt config completed')")
    sections.append(f"# Finished generation on {end_time}")
    
    return "\n".join(sections)


def print_config_summary(config: AggregatedConfig, all_records: list[LocationRecord]) -> None:
    print("\n")
    print("AGGREGATED CONFIGURATION")
    print("=" * 65)
    print(f"  Primary Location: {config.name}")
    print(f"  Coordinates: ({config.lat}, {config.lon})")
    print(f"  State/Country: {config.state_code}, {config.country_code}")
    print("-" * 65)
    print(f"  Total locations processed: {len(all_records)}")
    print(f"  Airport IDs: {config.airport_ids}")
    print(f"  Coop IDs: {config.coop_ids}")
    print(f"  TECCI IDs: {config.tecci_ids}")
    print(f"  OBS STATION IDs: {config.obs_stations}")
    print(f"  Zone IDs: {config.zone_ids}")
    print(f"  County IDs: {config.county_ids}")
    print(f"  Climate IDs: {config.climate_ids}")
    print("=" * 65)


def generate_output_filename(config: AggregatedConfig, system_type: SystemType) -> str:
    # {type}_{platform}_{location}_{state}.py

    if not system_type == "i2":
        platform = "i1"
    else:
        platform = "i2"
    
    safe_name = config.name.replace(' ', '_').replace('/', '_').replace('\\', '_')
    filename = f"{system_type}_{platform}_{safe_name}_{config.state_code}.py"
    return os.path.join("output", filename)

def main() -> None:
    print_banner()
    
    input_mode = select_input_mode()
    
    system_type = select_system_type()
    print(f"\nGenerating config for: {SYSTEM_DISPLAY_NAMES[system_type]}")
    
    if input_mode == "yaml":
        yaml_data = load_input_yaml()
        if yaml_data is None:
            sys.exit(1)
        
        result = process_locations_from_yaml(yaml_data, system_type)
        if result is None:
            sys.exit(1)
        
        config, all_records = result
    else:
        result = process_locations_manual(system_type)
        if result is None:
            sys.exit(1)
        
        config, all_records = result
    
    print_config_summary(config, all_records)
    
    print(f"\n{SYSTEM_DISPLAY_NAMES[system_type].upper()} CONFIG")
    print(f"Generated for: {config.name.upper()}")
    print("=" * 65)
    
    full_config = compile_full_config(config, all_records, system_type)
    output_filename = generate_output_filename(config, system_type)
    
    Path("output").mkdir(exist_ok=True)
    
    with open(output_filename, 'w') as f:
        f.write(full_config)
    
    print(f"\n✓ Configuration saved to: {output_filename}")
    print(f"  Total lines: {len(full_config.splitlines())}")
    print(f"  File size: {len(full_config)} bytes")


if __name__ == "__main__":
    main()
