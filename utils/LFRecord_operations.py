from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

DB_PATH = Path("./LFRecord.db")

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
            return tz.get(init_fetch["tmZnAbbr"], "CST")
        if country_code == "CA":
            return tz_canada.get(init_fetch["stCd"], "America/Regina")
        if country_code == "MX":
            return tz_mexico.get(init_fetch["stCd"], "America/Mexico_City")
        else:
            gmtDiff = init_fetch["gmtDiff"] / 1
            return f"Etc/GMT{'+' if gmtDiff < 0 else '-'}{abs(int(gmtDiff))}"

    return "CST6CDT"


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

def search_records_by_name_and_state(search_term: str, state_code: str | None = None) -> dict | None:
    query = "SELECT * FROM LFRecord WHERE prsntNm LIKE ?"
    params = [f"%{search_term}%"]

    if state_code:
        query += " AND stCd = ?"
        params.append(state_code)

    query += " ORDER BY prsntNm LIMIT 20"

    with get_db_connection() as conn:
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()

    matches = [dict(row) for row in rows]

    if not matches:
        return None

    if len(matches) == 1:
        return matches[0]

    print(f"Multiple matches found ({len(matches)}):")
    for idx, record in enumerate(matches, 1):
        loc_id = record.get('locId', '')[:8] if record.get('locId') else ''
        print(f"  [{idx}] {record.get('prsntNm', '')}, {record.get('stCd', '')} {record.get('cntryCd', '')} (ID: {loc_id})")

    while True:
        selection = input(f"Select (1-{len(matches)}): ").strip()
        
        try:
            sel_idx = int(selection) - 1
            if 0 <= sel_idx < len(matches):
                return matches[sel_idx]
            else:
                print(f"Invalid selection. Enter 1-{len(matches)}")
        except ValueError:
            print(f"Invalid input. Enter a number")


def search_location_auto(name: str, state_code: str | None = None) -> dict | None:
    query = "SELECT * FROM LFRecord WHERE prsntNm LIKE ?"
    params = [f"%{name}%"]

    if state_code:
        query += " AND stCd = ?"
        params.append(state_code)

    query += " ORDER BY prsntNm LIMIT 20"

    with get_db_connection() as conn:
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()

    matches = [dict(row) for row in rows]

    if not matches:
        return None

    if len(matches) == 1:
        return matches[0]

    for record in matches:
        if record.get('prsntNm', '').lower() == name.lower():
            return record

    for record in matches:
        loc_id = record.get('locId', '')
        if loc_id and loc_id.startswith('CN') or loc_id.startswith('US'):
            return record

    return matches[0]


def search_and_select_location(prompt: str, allow_skip: bool = False, show_coords: bool = False) -> dict | None:

    location_name = input(prompt).strip()
    
    if not location_name:
        if allow_skip:
            print("    Skipped")
        else:
            print("No location name provided")
        return None
    
    if ', ' in location_name:
        parts = location_name.rsplit(', ', 1)
        location_name = parts[0].strip()
        state_code = parts[1].strip().upper()
    elif ',' in location_name:
        parts = location_name.rsplit(',', 1)
        location_name = parts[0].strip()
        state_code = parts[1].strip().upper()
    else:
        state_code = None
    
    matches: list[dict] = search_records_by_name(location_name) if state_code is None else []
    if state_code is not None:
        result = search_records_by_name_and_state(location_name, state_code)
        matches = [result] if result else []
    
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


def prompt_for_nearby_locations(max_nearby: int = 7, main_location_id: str | None = None) -> list[dict]:

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
            if main_location_id and record.get('locId') == main_location_id:
                print(f"    Skipped: This is the main location, cannot be added as nearby")
                continue
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
                        if main_location_id and record.get('locId') == main_location_id:
                            print(f"    Cannot select: This is the main location")
                            continue
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
    full_time_zone: str = ""
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
            full_time_zone=record.get("tmZnNm", ""),
            lat=lat,
            lon=lon,
        )
