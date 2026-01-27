from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import AggregatedConfig
    from utils.LFRecord_operations import LocationRecord


def quote_list(items: list[str]) -> str:
    return ", ".join(f"'{item}'" for item in items if item)


def get_cityticker_travel_cities(state_code: str, country_code: str) -> str:
    southeast_us = ['FL', 'GA', 'AL', 'MS', 'LA', 'SC', 'NC', 'TN', 'KY', 'VA', 'WV', 'AR']
    northeast_us = ['NY', 'NJ', 'PA', 'CT', 'MA', 'RI', 'NH', 'VT', 'ME', 'DE', 'MD', 'DC']
    midwest_us = ['OH', 'MI', 'IN', 'IL', 'WI', 'MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS']
    southwest_us = ['TX', 'OK', 'NM', 'AZ']
    california = ['CA']
    northwest_us = ['WA', 'OR', 'ID', 'MT', 'WY']
    rocky_mountain = ['CO', 'UT', 'NV']
    
    maritimes = ['NS', 'NB', 'PE', 'NL']
    quebec = ['QC']
    prairies = ['MB', 'SK', 'AB']
    british_columbia = ['BC']
    
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
            return """d = twc.Data()
d.obsStation = ['MMMX','MMGL','T76393000','MMTJ','MMUN','MMPR',]
d.locName = ['Mexico City','Guadalajara','Monterrey','Tijuana','Cancun','Puerto Vallarta',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Mexico City','Guadalajara','Monterrey','Tijuana','Cancun','Puerto Vallarta',]
d.coopId = ['76679000','76612000','76394000','76188000','76595000','76654000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)"""
    return ""


def get_cityticker_obs_stations(state_code: str, country_code: str) -> list[str]:
    southeast_us = ['FL', 'GA', 'AL', 'MS', 'LA', 'SC', 'NC', 'TN', 'KY', 'VA', 'WV', 'AR']
    northeast_us = ['NY', 'NJ', 'PA', 'CT', 'MA', 'RI', 'NH', 'VT', 'ME', 'DE', 'MD', 'DC']
    midwest_us = ['OH', 'MI', 'IN', 'IL', 'WI', 'MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS']
    southwest_us = ['TX', 'OK', 'NM', 'AZ']
    california = ['CA']
    northwest_us = ['WA', 'OR', 'ID', 'MT', 'WY']
    rocky_mountain = ['CO', 'UT', 'NV']
    maritimes = ['NS', 'NB', 'PE', 'NL']
    quebec = ['QC']
    ontario = ['ON']
    prairies = ['MB', 'SK', 'AB']
    british_columbia = ['BC']
    territories = ['YT', 'NT', 'NU']
    
    if country_code == "CA":
        if state_code in maritimes:
            return ['T71437008', 'CYUL', 'T71300001', 'T71398004', 'T71705002', 'T71609000']
        elif state_code in quebec:
            return ['CYUL', 'T71578001', 'CYVO', 'CYHU', 'CYMX', 'CYUY']
        elif state_code in ontario:
            return ['T71437008', 'T71300001', 'CYHM', 'CYXU', 'CYQT', 'CYSB']
        elif state_code in prairies:
            return ['CYYC', 'T71123000', 'T71513001', 'T71863000', 'T71579003', 'T71251001']
        elif state_code in british_columbia:
            return ['CYVR', 'T71799002', 'CYXX', 'CYLW', 'T71896004', 'T71887000']
        elif state_code in territories:
            return ['CYXY', 'CYZF', 'CYFB', 'CYDA', 'CYEV', 'CYVQ']
        else:
            return ['T71437008', 'CYUL', 'CYVR', 'T71300001', 'CYYC', 'T71579003']
    elif country_code == "MX":
        return ['MMMX', 'MMGL', 'T76393000', 'MMTJ', 'MMUN', 'MMPR']
    else:
        if state_code in southeast_us:
            return ['T72219029', 'T72202000', 'T72205000', 'T72327008', 'T72314004', 'T72231015']
        elif state_code in northeast_us:
            return ['T72503193', 'T72509060', 'T72408054', 'T72405034', 'T72406000', 'T72507009']
        elif state_code in midwest_us:
            return ['T72530000', 'T72537001', 'T72658005', 'T72524092', 'T72438000', 'T72446003']
        elif state_code in southwest_us:
            return ['T72259000', 'T72243023', 'T72278000', 'T72253000', 'T72365000', 'T72270000']
        elif state_code in california:
            return ['T72295000', 'T72494028', 'T72290012', 'T74509014', 'T72494029', 'T72483024']
        elif state_code in northwest_us:
            return ['T72793000', 'T72698008', 'T72681000', 'T72785004', 'T72772024', 'T72773011']
        elif state_code in rocky_mountain:
            return ['T72469009', 'T72572028', 'T72386000', 'T72466000', 'T72476000', 'T72464000']
        else:
            return ['T72503193', 'T72295000', 'T72530000', 'T72259000', 'T72469009', 'T72219029']


def compile_interest_list(config: "AggregatedConfig") -> str:
    intl_coop_ids = [
        '71182000', '71627001', '71852000', '71879001', '71892001', '71913000', '71936000', '71966000',
        '76255000', '76393000', '76405000', '76595000', '76679001',
    ]
    
    cityticker_obs = get_cityticker_obs_stations(config.state_code, config.country_code)
    
    all_coop_ids = list(config.coop_ids) + intl_coop_ids
    all_obs_ids = list(config.tecci_ids) + cityticker_obs
    
    return f"""wxdata.setInterestList('airportId','1',[{quote_list(config.airport_ids) if config.airport_ids else ''}])
wxdata.setInterestList('coopId','1',[{quote_list(all_coop_ids)}])
wxdata.setInterestList('pollenId','1',[])
wxdata.setInterestList('obsStation','1',[{quote_list(all_obs_ids)}])
wxdata.setInterestList('metroId','1',[])
wxdata.setInterestList('climId','1',[{quote_list(config.climate_ids)}])
wxdata.setInterestList('zone','1',[{quote_list(config.zone_ids)}])
wxdata.setInterestList('aq','1',[])
wxdata.setInterestList('skiId','1',[])
wxdata.setInterestList('county','1',[{quote_list(config.county_ids)}])"""


def compile_currentconditions(config: "AggregatedConfig", all_records: list["LocationRecord"]) -> str:
    loc_name = config.name
    loc_names = [record.name for record in all_records[:2]]
    obs_stations_for_current = []
    for record in all_records:
        if record.teccis and record.teccis[0]:
            obs_stations_for_current.append(record.teccis[0])
        elif record.obs_station:
            obs_stations_for_current.append(record.obs_station)

    return f"""d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:2])}]
d.locName = [{quote_list(loc_names)}]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:2])}]
d.locName = [{quote_list(loc_names)}]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:2])}]
d.locName = [{quote_list(loc_names)}]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:4])}]
d.locName = [{quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[4:8]) if len(obs_stations_for_current) > 4 else quote_list(obs_stations_for_current[:4])}]
d.locName = [{quote_list([record.name for record in all_records[4:8]]) if len(all_records) > 4 else quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:4])}]
d.locName = [{quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[4:8]) if len(obs_stations_for_current) > 4 else quote_list(obs_stations_for_current[:4])}]
d.locName = [{quote_list([record.name for record in all_records[4:8]]) if len(all_records) > 4 else quote_list([record.name for record in all_records[:4]])}]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = [{quote_list(obs_stations_for_current[:10])}]
d.locName = [{quote_list([record.name for record in all_records[:10]])}]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
""" + get_cityticker_travel_cities(config.state_code, config.country_code) + f"""
#
d = twc.Data()
d.obsStation = '{obs_stations_for_current[0] if obs_stations_for_current else ""}'
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


def compile_forecast(config: "AggregatedConfig") -> str:
    loc_name = config.name
    return f"""d = twc.Data()
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


def compile_metadata(config: "AggregatedConfig", random_cable_name: str, random_star_id: int) -> str:
    return f"""dsm.set('dmaCode','None', 0)
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


def compile_packages(config: "AggregatedConfig") -> str:
    loc_name = config.name
    return f"""#
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


def compile_airport_data(config: "AggregatedConfig", all_records: list["LocationRecord"]) -> str:
    airport_records = [r for r in all_records if r.airport_id]
    
    if not airport_records:
        return ""
    
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
    for i, record in enumerate(local_airports):
        output += f"""d = twc.Data()
d.airportId = '{record.airport_id}'
d.obsStation = '{record.teccis[0] if record.teccis else ""}'
d.locName = '{record.name}'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.{i}', d, 0, 1)
#
"""
    return output


def compile_travel_forecast(config: "AggregatedConfig", all_records: list["LocationRecord"]) -> str:
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


def compile_scmt_removes() -> str:
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
    
    lines = [f"scmtRemove('{product}')" for product in weatherscan_products]
    return "\n".join(lines)
