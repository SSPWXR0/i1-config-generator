"""
Nearby location finder module.

This module finds nearby locations within a certain radius from a primary location.
It queries the LFRecord database and uses haversine distance to filter results.

Algorithm:
1. From primary location, get lat/lon
2. Find locations in cardinal directions (N, E, S, W) within the radius
3. Optionally find locations in between (NE, SE, SW, NW)
4. Return a set of LocationRecords within the specified radius

This is experimental and may need refinement for different geographic regions.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from utils.LFRecord_operations import get_db_connection, LocationRecord

if TYPE_CHECKING:
    from typing import Sequence

EARTH_RADIUS_KM = 6371.0
EARTH_RADIUS_MI = 3958.8

KM_TO_MI = 0.621371
MI_TO_KM = 1.60934


class Direction(Enum):
    NORTH = 0
    NORTHEAST = 45
    EAST = 90
    SOUTHEAST = 135
    SOUTH = 180
    SOUTHWEST = 225
    WEST = 270
    NORTHWEST = 315


@dataclass
class NearbyResult:
    record: LocationRecord
    distance_km: float
    bearing: float

    @property
    def distance_mi(self) -> float:
        return self.distance_km * KM_TO_MI

    @property
    def direction(self) -> Direction:
        normalized = self.bearing % 360
        if normalized < 22.5 or normalized >= 337.5:
            return Direction.NORTH
        elif normalized < 67.5:
            return Direction.NORTHEAST
        elif normalized < 112.5:
            return Direction.EAST
        elif normalized < 157.5:
            return Direction.SOUTHEAST
        elif normalized < 202.5:
            return Direction.SOUTH
        elif normalized < 247.5:
            return Direction.SOUTHWEST
        elif normalized < 292.5:
            return Direction.WEST
        else:
            return Direction.NORTHWEST


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS_KM * c


def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    dlon = math.radians(lon2 - lon1)

    x = math.sin(dlon) * math.cos(lat2_rad)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(
        lat2_rad
    ) * math.cos(dlon)

    bearing = math.atan2(x, y)
    return (math.degrees(bearing) + 360) % 360


def get_bounding_box(
    lat: float, lon: float, radius_km: float
) -> tuple[float, float, float, float]:
    lat_delta = radius_km / 111.0
    lon_delta = radius_km / (111.0 * math.cos(math.radians(lat)))

    min_lat = lat - lat_delta
    max_lat = lat + lat_delta
    min_lon = lon - lon_delta
    max_lon = lon + lon_delta

    return min_lat, max_lat, min_lon, max_lon


def find_all_nearby(
    primary_lat: float,
    primary_lon: float,
    radius_km: float = 150.0,
    exclude_loc_ids: set[str] | None = None,
    limit: int = 50,
) -> list[NearbyResult]:
    if exclude_loc_ids is None:
        exclude_loc_ids = set()

    min_lat, max_lat, min_lon, max_lon = get_bounding_box(
        primary_lat, primary_lon, radius_km * 1.2
    )

    query = """
        SELECT * FROM LFRecord 
        WHERE lat IS NOT NULL 
          AND long IS NOT NULL
          AND CAST(lat AS REAL) BETWEEN ? AND ?
          AND CAST(long AS REAL) BETWEEN ? AND ?
        ORDER BY prsntNm
        LIMIT 500
    """

    with get_db_connection() as conn:
        cursor = conn.execute(query, (min_lat, max_lat, min_lon, max_lon))
        rows = cursor.fetchall()

    results: list[NearbyResult] = []

    for row in rows:
        record_dict = dict(row)
        loc_id = record_dict.get("locId", "")

        if loc_id in exclude_loc_ids:
            continue

        try:
            rec_lat = float(record_dict.get("lat", 0))
            rec_lon = float(record_dict.get("long", 0))
        except (ValueError, TypeError):
            continue

        if rec_lat == primary_lat and rec_lon == primary_lon:
            continue

        distance = haversine_distance(primary_lat, primary_lon, rec_lat, rec_lon)

        if distance > radius_km:
            continue

        bearing = calculate_bearing(primary_lat, primary_lon, rec_lat, rec_lon)

        location_record = LocationRecord.from_db_record(record_dict)
        results.append(NearbyResult(record=location_record, distance_km=distance, bearing=bearing))

    results.sort(key=lambda x: x.distance_km)
    return results[:limit]


def find_cardinal_locations(
    primary_lat: float,
    primary_lon: float,
    radius_km: float = 150.0,
    exclude_loc_ids: set[str] | None = None,
    include_intercardinal: bool = False,
) -> dict[Direction, NearbyResult | None]:
    all_nearby = find_all_nearby(
        primary_lat, primary_lon, radius_km, exclude_loc_ids, limit=200
    )

    if include_intercardinal:
        directions = list(Direction)
    else:
        directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

    result: dict[Direction, NearbyResult | None] = {d: None for d in directions}

    for nearby in all_nearby:
        direction = nearby.direction

        if direction not in result:
            continue

        if result[direction] is None:
            result[direction] = nearby

    return result


def find_nearby_by_location_record(
    primary: LocationRecord,
    radius_km: float = 150.0,
    limit: int = 8,
) -> list[NearbyResult]:
    if primary.lat is None or primary.lon is None:
        return []

    return find_all_nearby(
        primary.lat,
        primary.lon,
        radius_km,
        exclude_loc_ids={primary.loc_id},
        limit=limit,
    )


def find_nearby_for_config(
    primary_lat: float,
    primary_lon: float,
    primary_loc_id: str,
    radius_km: float = 200.0,
    max_locations: int = 8,
    prefer_canonical_ids: bool = True,
) -> list[LocationRecord]:
    all_nearby = find_all_nearby(
        primary_lat,
        primary_lon,
        radius_km,
        exclude_loc_ids={primary_loc_id},
        limit=100,
    )

    if prefer_canonical_ids:
        canonical = [
            n for n in all_nearby
            if n.record.loc_id.startswith(("CN", "US", "MX", "CAXX", "USXX"))
        ]
        non_canonical = [
            n for n in all_nearby
            if not n.record.loc_id.startswith(("CN", "US", "MX", "CAXX", "USXX"))
        ]
        all_nearby = canonical + non_canonical

    selected: list[LocationRecord] = []
    seen_names: set[str] = set()

    for nearby in all_nearby:
        if len(selected) >= max_locations:
            break

        name_key = nearby.record.name.lower()
        if name_key in seen_names:
            continue

        seen_names.add(name_key)
        selected.append(nearby.record)

    return selected


def find_distributed_nearby(
    primary_lat: float,
    primary_lon: float,
    primary_loc_id: str,
    radius_km: float = 200.0,
    max_locations: int = 8,
) -> list[LocationRecord]:
    cardinal = find_cardinal_locations(
        primary_lat,
        primary_lon,
        radius_km,
        exclude_loc_ids={primary_loc_id},
        include_intercardinal=True,
    )

    selected: list[LocationRecord] = []
    seen_ids: set[str] = set()

    priority_order = [
        Direction.NORTH,
        Direction.SOUTH,
        Direction.EAST,
        Direction.WEST,
        Direction.NORTHEAST,
        Direction.SOUTHWEST,
        Direction.SOUTHEAST,
        Direction.NORTHWEST,
    ]

    for direction in priority_order:
        if len(selected) >= max_locations:
            break

        result = cardinal.get(direction)
        if result and result.record.loc_id not in seen_ids:
            seen_ids.add(result.record.loc_id)
            selected.append(result.record)

    if len(selected) < max_locations:
        all_nearby = find_all_nearby(
            primary_lat,
            primary_lon,
            radius_km,
            exclude_loc_ids=seen_ids | {primary_loc_id},
            limit=max_locations - len(selected),
        )
        for nearby in all_nearby:
            if len(selected) >= max_locations:
                break
            if nearby.record.loc_id not in seen_ids:
                seen_ids.add(nearby.record.loc_id)
                selected.append(nearby.record)

    return selected


def print_nearby_summary(
    primary_name: str,
    results: Sequence[NearbyResult],
) -> None:
    print(f"\nNearby locations for {primary_name}:")
    print("-" * 60)
    for i, result in enumerate(results, 1):
        dir_name = result.direction.name
        print(
            f"  {i:2}. {result.record.name:25} "
            f"{result.distance_km:6.1f} km ({result.distance_mi:5.1f} mi) "
            f"{dir_name:10} (ID: {result.record.loc_id[:8]})"
        )
    print("-" * 60)