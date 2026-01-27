import math
from typing import NamedTuple

MERCATOR_MAX_X = 39421
MERCATOR_MAX_Y = 20836


class ProjectionConstants(NamedTuple):
    lon_scale: float
    lon_offset: float
    lat_scale: float
    lat_offset: float


DOMESTIC_PROJECTION = ProjectionConstants(
    lon_scale=0.001843629904,
    lon_offset=-132.415309106784,
    lat_scale=0.000038650000,
    lat_offset=0.290263290208,
)

# WATT uses the same basemap as pre-WATT domestic, so projection is identical
WATT_PROJECTION = DOMESTIC_PROJECTION

# Weatherscan also uses the same US Mercator basemap
WEATHERSCAN_PROJECTION = DOMESTIC_PROJECTION

_LON_SCALE = DOMESTIC_PROJECTION.lon_scale
_LON_OFFSET = DOMESTIC_PROJECTION.lon_offset
_LAT_SCALE = DOMESTIC_PROJECTION.lat_scale
_LAT_OFFSET = DOMESTIC_PROJECTION.lat_offset

BASEMAP_TILES = {
    "ne": {"width": 19718, "height": 10336, "x_min": 19703, "y_min": 0},
    "nw": {"width": 19703, "height": 10336, "x_min": 0, "y_min": 0},
    "se": {"width": 19718, "height": 10500, "x_min": 19703, "y_min": 10336},
    "sw": {"width": 19703, "height": 10500, "x_min": 0, "y_min": 10336},
}

MAP_PRODUCT_SIZES = {
    "Radar_LocalDoppler": (1440, 822),
    "NationalLdl_DopplerRadar": (1440, 821),
    "Local_MetroDopplerRadar": (1440, 960),
    "Local_MetroForecastMap": (1440, 960),
    "Local_MetroObservationMap": (1440, 960),
    "Local_RegionalDopplerRadar": (3456, 2304),
    "Local_RegionalForecastMap": (5760, 3840),
    "Local_RegionalObservationMap": (5760, 3840),
}

MAP_PRODUCT_SIZES_WATT = {
    "Radar_LocalDoppler": (1440, 822),
    "Local_SummaryFS": (1440, 554),
    "LFLocal_LocalDoppler": (1576, 677),
    "Local_MetroDopplerRadar": (1440, 960),
    "Local_MetroRadarFS": (1440, 537),
    "Local_MetroObservationMap": (1512, 1008),
    "Local_MetroForecastMap": (1512, 1008),
    "Local_RegionalForecastMap": (6192, 4128),
    "Local_RegionalObservationMap": (6192, 4128),
    "Local_Satellite": (2979, 1986),
    "Local_RegionalRadarFS": (3960, 1475),
    "Local_RegionalDopplerRadar": (3960, 2640),
}

MAP_PRODUCT_SIZES_WEATHERSCAN = {
    "Radar_LocalDoppler": (1440, 822),
    "Local_LocalDoppler": (1440, 960),
    "Local_RadarSatelliteComposite": (1296, 864),
    "Local_RegionalForecastConditions": (5760, 3840),
    "Local_FrostFreezeWarnings": (1296, 864),
    "Local_SnowfallQpfForecast": (1296, 864),
    "Local_NationalTravelWeather": (1296, 864),
    "Local_EstimatedPrecipitation": (1296, 864),
    "Local_PrecipitationQpfForecast": (1296, 864),
    "Local_PalmerDroughtSeverity": (1296, 864),
}

def _lat_to_mercator_y(lat: float) -> float:
    lat_rad = math.radians(lat)
    return math.log(math.tan(math.pi / 4 + lat_rad / 2))

def _mercator_y_to_lat(y: float) -> float:
    return math.degrees(2 * math.atan(math.exp(y)) - math.pi / 2)

def pixel_to_latlon(x: int, y: int, projection: ProjectionConstants = DOMESTIC_PROJECTION) -> tuple[float, float]:
    lon = x * projection.lon_scale + projection.lon_offset
    mercator_y = y * projection.lat_scale + projection.lat_offset
    lat = _mercator_y_to_lat(mercator_y)
    return (lat, lon)

def latlon_to_pixel(lat: float, lon: float, projection: ProjectionConstants = DOMESTIC_PROJECTION) -> tuple[int, int]:
    x = (lon - projection.lon_offset) / projection.lon_scale
    mercator_y = _lat_to_mercator_y(lat)
    y = (mercator_y - projection.lat_offset) / projection.lat_scale
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

def get_mapcut_coordinate(
    lat: float,
    lon: float,
    product_name: str,
    product_sizes: dict[str, tuple[int, int]] = MAP_PRODUCT_SIZES,
    projection: ProjectionConstants = DOMESTIC_PROJECTION
) -> tuple[int, int]:
    center = latlon_to_pixel(lat, lon, projection)
    size = product_sizes.get(product_name, (1440, 960))
    cut_x = center[0] - size[0] // 2
    cut_y = center[1] - size[1] // 2
    
    cut_x, cut_y = clamp_mapcut_coordinate(cut_x, cut_y, size[0], size[1])
    
    return (cut_x, cut_y)

def get_all_mapcut_coordinates(
    lat: float,
    lon: float,
    product_sizes: dict[str, tuple[int, int]] = MAP_PRODUCT_SIZES,
    projection: ProjectionConstants = DOMESTIC_PROJECTION
) -> dict[str, tuple[int, int]]:
    return {
        product: get_mapcut_coordinate(lat, lon, product, product_sizes, projection)
        for product in product_sizes
    }


def get_projection_for_system(system_type: str) -> ProjectionConstants:
    if system_type == "domesticWATT":
        return WATT_PROJECTION
    elif system_type == "weatherscan":
        return WEATHERSCAN_PROJECTION
    return DOMESTIC_PROJECTION


def get_product_sizes_for_system(system_type: str) -> dict[str, tuple[int, int]]:
    if system_type == "domesticWATT":
        return MAP_PRODUCT_SIZES_WATT
    elif system_type == "weatherscan":
        return MAP_PRODUCT_SIZES_WEATHERSCAN
    return MAP_PRODUCT_SIZES
