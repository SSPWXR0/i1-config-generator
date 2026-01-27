# Created on Fri Oct 17 14:49:42 GMT 2014
Log.info('scmt config started')
# EXP: 1519
# VIW: 11039
# CLN: 14645
#
def scmtRemove(key):
    try:
        dsm.remove(key)
    except:
        pass
#

#
# Beginning of SCMT deployment
import os
dsm.set('scmt_configType', 'domestic',0)
dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)
#
dsm.set('Scmt.PlatformType', 'IntelliStar', 0)
#Short-cast sound effect
scmtRemove('Config.1.SoundFxSchedule')
d = twc.Data()
d.OffTimes = ((0,23),)
dsm.set('Config.1.SoundFxSchedule', d, 0, 1)
#
scmtRemove('Config.1.Local_TextForecast.0')
scmtRemove('Config.1.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.Local_SchoolDayWeather.0')
scmtRemove('Config.1.Local_TrafficReport.0')
scmtRemove('Config.1.Local_TrafficFlow.0')
scmtRemove('Config.1.Radar_LocalDoppler.0')
scmtRemove('Config.1.Local_MetroDopplerRadar.0')
scmtRemove('Config.1.Local_MetroForecastMap.0')
scmtRemove('Config.1.Local_RadarSatelliteComposite.0')
scmtRemove('Config.1.Local_RegionalForecastMap.0')
scmtRemove('Config.1.Local_RegionalObservationMap.0')
scmtRemove('Config.1.Local_AirQualityForecast.0')
scmtRemove('Config.1.Local_Almanac.0')
scmtRemove('Config.1.Local_Climatology.0')
scmtRemove('Config.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Local_EventForecast.0')
scmtRemove('Config.1.Local_7DayForecast.0')
scmtRemove('Config.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Local_GetawayForecast.0')
scmtRemove('Config.1.Local_HeatSafetyTips.0')
scmtRemove('Config.1.Local_RegionalDopplerRadar.0')
scmtRemove('Config.1.Local_LocalObservations.0')
scmtRemove('Config.1.Local_MarineForecast.0')
scmtRemove('Config.1.Local_TrafficOverview.0')
scmtRemove('Config.1.Cc_CurrentConditions.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.5')
scmtRemove('Config.1.Ldl_AirportDelayConditions.0')
scmtRemove('Config.1.Ldl_AirQualityForecast.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.0')
scmtRemove('Config.1.Ldl_TravelForecast.0')
scmtRemove('Config.1.Ldl_UVForecast.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.1')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.2')
scmtRemove('Config.1.Ldl_TrafficTripTimes.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.3')
scmtRemove('Config.1.TimeTemp_Default.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.4')
scmtRemove('Config.1.Ldl_Almanac.0')
scmtRemove('Config.1.Ldl_DailyForecast.0')
scmtRemove('Config.1.Ldl_3DayForecast.0')
scmtRemove('Config.1.Ldl_HourlyForecast.0')
scmtRemove('Config.1.Ldl_CurrentObs.0')
scmtRemove('Config.1.Ldl_CurrentObs.1')
scmtRemove('Config.1.Ldl_CurrentObs.2')
scmtRemove('Config.1.Ldl_CurrentObs.3')
scmtRemove('Config.1.Ldl_StarIDMessag.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.5')
scmtRemove('Config.1.Local_NWSHeadlines.0')
scmtRemove('Config.1.Local_Tides.0')
scmtRemove('Config.1.Local_RecordHighLow.0')
scmtRemove('Config.1.Local_Satellite.0')
scmtRemove('Config.1.Local_MetroObservationMap.0')
scmtRemove('Config.1.Ldl_HurricaneWatch.0')
scmtRemove('Config.1.NationalLdl_DopplerRadar.0')
scmtRemove('Config.1.NationalLdl_RadarSatellite.0')
scmtRemove('Config.1.NationalLdl_WeatherBulletin.0')
scmtRemove('Config.1.NationalLdl_5DayForecast.0')
scmtRemove('Config.1.NationalLdl_5DayForecast.1')
scmtRemove('Config.1.NationalLdl_5DayForecast.2')
scmtRemove('Config.1.NationalLdl_5DayForecast.3')
scmtRemove('Config.1.NationalLdl_5DayForecast.4')
scmtRemove('Config.1.NationalLdl_5DayForecast.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.0')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.1')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.2')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.3')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.4')
scmtRemove('Config.1.LFLocal_LocalDoppler.0')
scmtRemove('Config.1.LFLocal_Almanac.0')
scmtRemove('Config.1.LFCc_CurrentConditions.0')
scmtRemove('Config.1.LFLocal_NWSHeadlines.0')
scmtRemove('Config.1.LFLocal_ExtendedForecast.0')
scmtRemove('Config.1.LFLocal_TextForecast.0')
scmtRemove('Config.1.LFLocal_HourlyForecast.0')
#
# MAP: 81361
# LFLocal_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19094,8020),
             mapcutSize=(1776,763),
             mapFinalSize=(398,171),
             mapMilesSize=(173,97),
             datacutType='radar.us',
             datacutCoordinate=(1940,645),
             datacutSize=(217,93),
             dataFinalSize=(398,171),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.LFLocal_LocalDoppler', d, 0)
#
# LFLocal_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (114,81),),
                ( (249,137),),
                ( (92,27),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (114,81),),
                ( (249,137),),
                ( (92,27),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (81,95),'McKinney',),
                ( (256,149),'Paris',),
                ( (109,27),'Dallas',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (81,95),'McKinney',),
                ( (256,149),'Paris',),
                ( (109,27),'Dallas',),
              ),
             ),
        ],
  vector = [
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
             ],
)
dsm.set('Config.1.LFLocal_LocalDoppler', d, 0)
# MAP: 121116
# Local_SummaryFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18672,7846),
             mapcutSize=(2316,891),
             mapFinalSize=(338,130),
             mapMilesSize=(247,114),
             datacutType='radar.us',
             datacutCoordinate=(1888,623),
             datacutSize=(284,110),
             dataFinalSize=(338,130),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.interstates.vg','mercator.us.otherroutes.vg',],
)
wxdata.setMapData('Config.1.Local_SummaryFS', d, 0)
#
# Local_SummaryFS (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (121,41),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (105,67),'Dallas',),
              ),
             ),
        ],
  vector = [
             (( 2,(101,152,191,255),2,),(('counties',),),),
             (( 3,(101,152,191,255),2,),(('states',),),),
             (( 1,(146,182,209,255),2,),(('coastlines',),),),
             (( 3,(179,180,168,255),2,),(('statehighways',),),),
             (( 4,(152,153,139,255),2,),(('ushighways',),),),
             (( 4,(152,153,139,255),2,),(('interstates',),),),
             (( 2,(179,180,168,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_SummaryFS', d, 0)
# MAP: 74065
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18127,7533),
             mapcutSize=(3049,1740),
             mapFinalSize=(240,137),
             mapMilesSize=(325,222),
             datacutType='radar.us',
             datacutCoordinate=(1821,585),
             datacutSize=(374,213),
             dataFinalSize=(240,137),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Radar_LocalDoppler', d, 0)
#
# Radar_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (113,63),),
                ( (160,83),),
                ( (105,28),),
                ( (107,44),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (113,63),),
                ( (160,83),),
                ( (105,28),),
                ( (107,44),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (80,77),'McKinney',),
                ( (167,95),'Paris',),
                ( (115,20),'Waxahachie',),
                ( (124,44),'Dallas',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (80,77),'McKinney',),
                ( (167,95),'Paris',),
                ( (115,20),'Waxahachie',),
                ( (124,44),'Dallas',),
              ),
             ),
        ],
  vector = [
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
             ],
)
dsm.set('Config.1.Radar_LocalDoppler', d, 0)
# MAP: 77007
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18791,7651),
             mapcutSize=(1624,1083),
             mapFinalSize=(720,480),
             mapMilesSize=(173,139),
             datacutType='radar.us',
             datacutCoordinate=(1903,600),
             datacutSize=(199,132),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroDopplerRadar', d, 0)
#
# Local_MetroDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (596,154),'20',),
                ( (219,126),'35W',),
                ( (619,304),'30',),
                ( (265,306),'35E',),
                ( (348,244),'635',),
                ( (66,206),'20',),
                ( (393,91),'45',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (219,126),'35W',),
                ( (265,306),'35E',),
                ( (348,244),'635',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (370,347),'75',),
                ( (126,327),'287',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (370,347),'75',),
                ( (126,327),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (596,154),'20',),
                ( (619,304),'30',),
                ( (66,206),'20',),
                ( (393,91),'45',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (269,246),),
                ( (312,237),),
                ( (187,227),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (303,274),),
                ( (312,181),),
                ( (248,338),),
                ( (198,215),),
                ( (262,261),),
                ( (490,309),),
                ( (446,177),),
                ( (362,325),),
                ( (383,221),),
                ( (340,288),),
                ( (387,255),),
                ( (319,133),),
                ( (328,223),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (303,274),),
                ( (312,181),),
                ( (248,338),),
                ( (198,215),),
                ( (262,261),),
                ( (490,309),),
                ( (446,177),),
                ( (362,325),),
                ( (383,221),),
                ( (340,288),),
                ( (387,255),),
                ( (319,133),),
                ( (328,223),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (269,246),),
                ( (312,237),),
                ( (187,227),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (201,292),'Carrollton',),
                ( (322,163),'DeSoto',),
                ( (173,341),'Denton',),
                ( (151,198),'Fort Worth',),
                ( (158,264),'Grapevine',),
                ( (510,312),'Greenville',),
                ( (465,162),'Kaufman',),
                ( (382,328),'McKinney',),
                ( (407,218),'Mesquite',),
                ( (360,291),'Plano',),
                ( (407,258),'Rowlett',),
                ( (262,116),'Waxahachie',),
                ( (305,206),'Dallas',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (201,292),'Carrollton',),
                ( (322,163),'DeSoto',),
                ( (173,341),'Denton',),
                ( (151,198),'Fort Worth',),
                ( (158,264),'Grapevine',),
                ( (510,312),'Greenville',),
                ( (465,162),'Kaufman',),
                ( (382,328),'McKinney',),
                ( (407,218),'Mesquite',),
                ( (360,291),'Plano',),
                ( (407,258),'Rowlett',),
                ( (262,116),'Waxahachie',),
                ( (305,206),'Dallas',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 4,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 4,(130,130,130,255),2,),(('statehighways',),),),
             (( 4,(130,130,130,255),2,),(('ushighways',),),),
             (( 4,(130,130,130,255),2,),(('interstates',),),),
             (( 4,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroDopplerRadar', d, 0)
# MAP: 116051
# Local_MetroRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18849,7889),
             mapcutSize=(1624,605),
             mapFinalSize=(620,231),
             mapMilesSize=(173,77),
             datacutType='radar.us',
             datacutCoordinate=(1910,629),
             datacutSize=(199,74),
             dataFinalSize=(620,231),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.interstates.vg','mercator.us.otherroutes.vg',],
)
wxdata.setMapData('Config.1.Local_MetroRadarFS', d, 0)
#
# Local_MetroRadarFS (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignGray',0,2,0,),'Tungsten-Medium',18,(235,235,235,255),1,-20,(),),
              ( ( (491,45),'20',),
                ( (164,29),'35W',),
                ( (550,178),'30',),
                ( (206,175),'35E',),
                ( (37,89),'20',),
                ( (297,32),'45',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (86,193),'287',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (246,64),),
                ( (190,200),),
                ( (148,92),),
                ( (398,174),),
                ( (360,60),),
                ( (289,187),),
                ( (310,98),),
                ( (270,155),),
                ( (367,94),),
                ( (61,99),),
                ( (261,100),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (222,40),'DeSoto',),
                ( (114,191),'Denton',),
                ( (96,65),'Fort Worth',),
                ( (411,151),'Greenville',),
                ( (334,38),'Kaufman',),
                ( (309,190),'McKinney',),
                ( (307,118),'Mesquite',),
                ( (208,158),'Plano',),
                ( (387,78),'Terrell',),
                ( (35,125),'Weatherford',),
                ( (191,105),'Dallas',),
              ),
             ),
        ],
  vector = [
             (( 2,(101,152,191,255),2,),(('counties',),),),
             (( 3,(101,152,191,255),2,),(('states',),),),
             (( 1,(146,182,209,255),2,),(('coastlines',),),),
             (( 3,(179,180,168,255),2,),(('statehighways',),),),
             (( 4,(152,153,139,255),2,),(('ushighways',),),),
             (( 4,(152,153,139,255),2,),(('interstates',),),),
             (( 2,(179,180,168,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroRadarFS', d, 0)
# MAP: 71648
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(2769,731),
             mapcutSize=(2032,1355),
             mapFinalSize=(720,480),
             mapMilesSize=(1949,1317),
             datacutType='radarSatellite.us',
             datacutCoordinate=(530,31),
             datacutSize=(1044,699),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Local_RadarSatelliteComposite', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RadarSatelliteComposite', d, 0)
# MAP: 77481
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18977,7940),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(100,80),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (208,89),'35W',),
                ( (409,224),'635',),
                ( (412,87),'35E',),
                ( (230,279),'35W',),
                ( (348,263),'35E',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (87,357),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (616,244),'30',),
                ( (76,148),'20',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72249002',(195,137),),
                ( '72249017',(324,78),),
                ( '72249024',(116,252),),
                ( '72259000',(309,190),),
                ( '72259014',(433,132),),
                ( '72259031',(431,264),),
                ( '72259036',(519,178),),
                ( '72259038',(267,306),),
                ( '72259052',(529,311),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72249002',(192,173),),
                ( '72249017',(321,114),),
                ( '72249024',(113,288),),
                ( '72259000',(306,226),),
                ( '72259014',(430,168),),
                ( '72259031',(428,300),),
                ( '72259036',(516,214),),
                ( '72259038',(264,342),),
                ( '72259052',(526,347),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (145,209),'Ft. Worth',),
                ( (275,150),'Arlington',),
                ( (92,324),'Boyd',),
                ( (281,262),'Irving',),
                ( (403,204),'Dallas',),
                ( (404,336),'Plano',),
                ( (480,250),'Garland',),
                ( (231,378),'Denton',),
                ( (478,383),'McKinney',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),1,),(('counties',),),),
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             (( 4,(130,130,130,255),1,),(('statehighways',),),),
             (( 4,(130,130,130,255),1,),(('ushighways',),),),
             (( 4,(130,130,130,255),1,),(('interstates',),),),
             (( 4,(130,130,130,255),1,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroForecastMap', d, 0)
# MAP: 77482
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18977,7940),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(100,80),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (208,89),'35W',),
                ( (409,224),'635',),
                ( (412,87),'35E',),
                ( (230,279),'35W',),
                ( (348,263),'35E',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (87,357),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (616,244),'30',),
                ( (76,148),'20',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72249002',(192,173),),
                ( 'T72249017',(321,114),),
                ( 'T72249024',(113,288),),
                ( 'T72259000',(306,226),),
                ( 'T72259014',(430,168),),
                ( 'T72259031',(428,300),),
                ( 'T72259036',(516,214),),
                ( 'T72259038',(264,342),),
                ( 'T72259052',(526,347),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72249002',(195,137),),
                ( 'T72249017',(324,78),),
                ( 'T72249024',(116,252),),
                ( 'T72259000',(309,190),),
                ( 'T72259014',(433,132),),
                ( 'T72259031',(431,264),),
                ( 'T72259036',(519,178),),
                ( 'T72259038',(267,306),),
                ( 'T72259052',(529,311),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (145,209),'Ft. Worth',),
                ( (275,150),'Arlington',),
                ( (92,324),'Boyd',),
                ( (281,262),'Irving',),
                ( (403,204),'Dallas',),
                ( (404,336),'Plano',),
                ( (480,250),'Garland',),
                ( (231,378),'Denton',),
                ( (478,383),'McKinney',),
              ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),1,),(('counties',),),),
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             (( 4,(130,130,130,255),1,),(('statehighways',),),),
             (( 4,(130,130,130,255),1,),(('ushighways',),),),
             (( 4,(130,130,130,255),1,),(('interstates',),),),
             (( 4,(130,130,130,255),1,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_MetroObservationMap', d, 0)
# MAP: 48902
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(16173,6193),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(629,503),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalForecastMap', d, 0)
#
# Local_RegionalForecastMap (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72248000',(588,152),),
                ( '72256000',(360,108),),
                ( '72259000',(407,197),),
                ( '72263000',(141,94),),
                ( '72266000',(227,174),),
                ( '72267000',(107,252),),
                ( '72351000',(288,275),),
                ( '74750046',(491,97),),
                ( '74752035',(576,253),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72248000',(585,188),),
                ( '72256000',(357,144),),
                ( '72259000',(404,233),),
                ( '72263000',(138,130),),
                ( '72266000',(224,210),),
                ( '72267000',(104,288),),
                ( '72351000',(285,311),),
                ( '74750046',(488,133),),
                ( '74752035',(573,289),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (529,224),'Shreveport',),
                ( (335,180),'Waco',),
                ( (377,269),'Dallas',),
                ( (82,166),'San Angelo',),
                ( (189,246),'Abilene',),
                ( (65,324),'Lubbock',),
                ( (219,347),'Wichita Falls',),
                ( (460,169),'Lufkin',),
                ( (522,325),'Texarkana',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 50489
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(16173,6193),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(629,503),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalObservationMap', d, 0)
#
# Local_RegionalObservationMap (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72248000',(585,188),),
                ( 'T72256000',(357,144),),
                ( 'T72259000',(404,233),),
                ( 'T72263000',(138,130),),
                ( 'T72266000',(224,210),),
                ( 'T72267000',(104,288),),
                ( 'T72351000',(285,311),),
                ( 'T74750046',(488,133),),
                ( 'T74752035',(573,289),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72248000',(588,152),),
                ( 'T72256000',(360,108),),
                ( 'T72259000',(407,197),),
                ( 'T72263000',(141,94),),
                ( 'T72266000',(227,174),),
                ( 'T72267000',(107,252),),
                ( 'T72351000',(288,275),),
                ( 'T74750046',(491,97),),
                ( 'T74752035',(576,253),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (529,224),'Shreveport',),
                ( (335,180),'Waco',),
                ( (377,269),'Dallas',),
                ( (82,166),'San Angelo',),
                ( (189,246),'Abilene',),
                ( (65,324),'Lubbock',),
                ( (219,347),'Wichita Falls',),
                ( (460,169),'Lufkin',),
                ( (522,325),'Texarkana',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 118231
# Local_RegionalRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18160,7608),
             mapcutSize=(3124,1164),
             mapFinalSize=(620,231),
             mapMilesSize=(334,149),
             datacutType='radar.us',
             datacutCoordinate=(1825,594),
             datacutSize=(383,143),
             dataFinalSize=(620,231),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.interstates.vg','mercator.us.otherroutes.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalRadarFS', d, 0)
#
# Local_RegionalRadarFS (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignGray',0,2,0,),'Tungsten-Medium',18,(235,235,235,255),1,-20,(),),
              ( ( (354,138),'30',),
                ( (50,63),'20',),
                ( (224,202),'35',),
                ( (386,75),'20',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (283,153),'75',),
                ( (116,38),'281',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (185,156),),
                ( (210,102),),
                ( (399,146),),
                ( (325,102),),
                ( (126,111),),
                ( (271,107),),
                ( (429,61),),
                ( (488,77),),
                ( (299,196),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (139,177),'Decatur',),
                ( (162,75),'Fort Worth',),
                ( (401,168),'Sulphur Springs',),
                ( (345,105),'Terrell',),
                ( (35,132),'Mineral Wells',),
                ( (250,131),'Dallas',),
                ( (410,39),'Tyler',),
                ( (487,97),'Longview',),
                ( (254,175),'Sherman',),
              ),
             ),
        ],
  vector = [
             (( 2,(101,152,191,255),2,),(('counties',),),),
             (( 3,(101,152,191,255),2,),(('states',),),),
             (( 1,(146,182,209,255),2,),(('coastlines',),),),
             (( 3,(179,180,168,255),2,),(('statehighways',),),),
             (( 4,(152,153,139,255),2,),(('ushighways',),),),
             (( 4,(152,153,139,255),2,),(('interstates',),),),
             (( 2,(179,180,168,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_RegionalRadarFS', d, 0)
# MAP: 77008
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18045,7150),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(334,267),
             datacutType='radar.us',
             datacutCoordinate=(1811,538),
             datacutSize=(383,255),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             prodActiveVocalCue=1,
)
wxdata.setMapData('Config.1.Local_RegionalDopplerRadar', d, 0)
#
# Local_RegionalDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (506,265),'30',),
                ( (84,175),'20',),
                ( (410,82),'45',),
                ( (287,337),'35',),
                ( (475,189),'20',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (355,282),'75',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (195,313),'287',),
                ( (161,146),'281',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (195,313),'287',),
                ( (355,282),'75',),
                ( (161,146),'281',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (506,265),'30',),
                ( (84,175),'20',),
                ( (410,82),'45',),
                ( (287,337),'35',),
                ( (475,189),'20',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (271,225),),
                ( (124,367),),
                ( (173,234),),
                ( (341,231),),
                ( (290,82),),
                ( (524,176),),
                ( (593,196),),
                ( (67,99),),
                ( (371,334),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (271,225),),
                ( (124,367),),
                ( (173,234),),
                ( (341,231),),
                ( (290,82),),
                ( (524,176),),
                ( (593,196),),
                ( (67,99),),
                ( (371,334),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (224,208),'Fort Worth',),
                ( (67,350),'Wichita Falls',),
                ( (114,255),'Mineral Wells',),
                ( (361,245),'Dallas',),
                ( (310,96),'Waco',),
                ( (506,159),'Tyler',),
                ( (554,217),'Longview',),
                ( (87,113),'Brownwood',),
                ( (391,348),'Sherman',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (224,208),'Fort Worth',),
                ( (67,350),'Wichita Falls',),
                ( (114,255),'Mineral Wells',),
                ( (361,245),'Dallas',),
                ( (310,96),'Waco',),
                ( (506,159),'Tyler',),
                ( (554,217),'Longview',),
                ( (87,113),'Brownwood',),
                ( (391,348),'Sherman',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,96),1,),(('statehighways',),),),
             (( 4,(20,20,20,96),1,),(('ushighways',),),),
             (( 4,(20,20,20,96),1,),(('interstates',),),),
             (( 4,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 4,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 2,(130,130,130,255),2,),(('statehighways',),),),
             (( 2,(130,130,130,255),2,),(('ushighways',),),),
             (( 2,(130,130,130,255),2,),(('interstates',),),),
             (( 2,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Local_RegionalDopplerRadar', d, 0)
#
wxdata.setInterestList('lambert.us','1',['radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.LFLocal_LocalDoppler','Config.1.Local_SummaryFS','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_MetroRadarFS','Config.1.Local_RegionalRadarFS','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['AUS','DAL','DFW',])
wxdata.setInterestList('coopId','1',['72248000','72249002','72249017','72249024','72256000','72259000','72259014','72259018','72259031','72259036','72259038','72259044','72259052','72263000','72266000','72267000','72351000','72462040','74732014','74750046','74752035',])
wxdata.setInterestList('indexId','1',['KDFW',])
wxdata.setInterestList('pollenId','1',['DFW',])
wxdata.setInterestList('obsStation','1',['KDFW','T72248000','T72249002','T72249017','T72249024','T72256000','T72259000','T72259014','T72259018','T72259031','T72259036','T72259038','T72259044','T72259052','T72263000','T72266000','T72267000','T72351000','T74745001','T74750046','T74752035',])
wxdata.setInterestList('climId','1',['412242',])
wxdata.setInterestList('metroId','1',['3',])
wxdata.setInterestList('zone','1',['TXZ119',])
wxdata.setInterestList('keyRoute','1',['23000001','23000002','23000013','23000014','23000028','23000029',])
wxdata.setInterestList('skiId','1',['505001','505007',])
wxdata.setInterestList('county','1',['TXC113','TXC121','TXC439','TXC085',])
dsm.set('Config.1.countyNameList',[('TXC113','Dallas'),('TXC121','Denton'),('TXC439','Tarrant'),('TXC085','Collin'),], 0)
#
dsm.set('dmaCode','623', 0)
dsm.set('secondaryObsStation','KDFW', 0)
dsm.set('primaryClimoStation','412242', 0)
dsm.set('primaryIndexId','KDFW', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','TX', 0)
dsm.set('primPollenSiteName','Dallas', 0)
dsm.set('expRev','7036734', 0)
dsm.set('primaryCoopId','72259000', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','DAL', 0)
dsm.set('primaryCounty','TXC113', 0)
dsm.set('primaryObsStation','T72259000', 0)
dsm.set('primaryRad',15, 0)
dsm.set('primaryLat',32.605, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','DFW', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('secondaryRad',30, 0)
dsm.set('primaryLon',-96.76167, 0)
dsm.set('primaryZone','TXZ119', 0)
dsm.set('climoRegion','4', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','The Weather Channel', 0)
dsm.set('headendId','020535', 0)
dsm.set('msoName','Unknown', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','The Weather Channel', 0)
dsm.set('msoCode','TWC', 0)
dsm.set('headendName','DOM - STAR SUPPORT 10 - DOM', 0)
dsm.set('affiliateNumber','06331', 0)
dsm.set('zipCode','99999', 0)
dsm.set('Config.1.irdAddress','0000345058627250', 0)
dsm.set('Config.1.bcNetMask','255.255.252.0', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD03040180', 0)
dsm.set('Config.1.bcExtIpAddress','10.50.41.165', 0)
dsm.set('Config.1.bcGateWay','10.50.40.1', 0)
dsm.set('Config.1.bcIpAddress','10.50.41.165', 0)
#
wxdata.setTimeZone('CST6CDT')
#
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
dsm.set('Config.1', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = ['DAL','DFW','AUS',]
d.airportLocName = ['Dallas/Love','Dallas/Ft. Worth','Austin/Bergstrom',]
d.obsStation = ['T72259014','T72259000','T74745001',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['505001','505007',]
d.coopId = ['72462040','74732014',]
d.resortName = ['Angel Fire, NM','Ski Apache, NM',]
dsm.set('Config.1.Tag.General.snowboardData', d, 0, 1)
#
#
#  Non Image Maps
#
d = [
'Config.1.Local_MetroForecastMap',
'Config.1.Local_MetroObservationMap',
'Config.1.Local_RegionalForecastMap',
'Config.1.Local_RegionalObservationMap',
]
dsm.set('Config.1.nonImageMaps', d, 0)
#

#
scmtRemove('Config.1.VocalLocalSchedule')
d = twc.Data()
d.OffTimes = ( )
dsm.set('Config.1.VocalLocalSchedule', d, 0, 1)
#
scmtRemove('Config.1.Ldl_LASCrawl')
scmtRemove('Config.1.LASCrawl')
#
d = twc.Data()
d.serialNum=1066642
d.crawls=[
(1413432000,1728964799,[(0,23)],'Theres still time on the shot clock. Order NBA LEAGUE PASS Theres still time on the shot clock. Order NBA LEAGUE PASS Theres still time on the shot clock. Order NBA LEAGUE PASS Theres still time on the shot clock. Order NBA LEAGUE'),
(1413172800,1414295999,[(0,23)],'In the biggest rematch in UFC featherweight history, Jose Aldo and number one contender Chad Mendes collide again in the Octagon. UFC 179: Aldo vs. Mendes II, Saturday, October 25, at 10PM ET/ 7PM PT, live on Time Warner Cable Pay-Per-View!'),
(1412654400,1413863999,[(0,23)],'Starring Tom Cruise, an officer finds himself caught in a time loop in a war with an alien race. Live Die Repeat: Edge of Tomorrow, now available on Time Warner Cable Movies On Demand, 28 days before Redbox and Netflix.'),
(1412654400,1413863999,[(0,23)],'A sports agent stages an unconventional recruitment strategy to get talented Indian cricket players to play Major League Baseball. Starring Jon Hamm. Million Dollar Arm, now available on Time Warner Cable Movies On Demand.'),
(1413864000,1414821599,[(0,23)],'A young couple works to survive on the streets after their car breaks down right as the annual purge commences. The Purge: Anarchy, now available on Time Warner Cable Movies On Demand, 28 days before Redbox and Netflix.'),
(1413864000,1414821599,[(0,23)],'A married couple wakes up to discover that the sex tape they made the evening before has gone missing, leading to a frantic search for its whereabouts. Sex Tape starring Cameron Diaz and Jason Segel, now available on Time Warner Cable Movies On Demand.'),
(1414476000,1416117599,[(0,23)],'The time-travelling adventures of an advanced canine and his adopted son, as they endeavor to fix a time rift they created. Mr. Peabody and Sherman, now available on Time Warner Cable Movies On Demand, 14 days before Redbox and Netflix.'),
(1414476000,1416117599,[(0,23)],'The X-Men send Wolverine to the past in a desperate effort to change history and prevent an event that results in doom for both humans and mutants. X-Men: Days of Futures Past, now available on Time Warner Cable Movies On Demand, 14 days before Redbox and Netflix.'),
(1412136000,1414821599,[(0,23)],'We still got the entire second half to play! Score big with MLS DIRECT KICK and catch up to 7 MLS games per week and watch your favorite teams and players march towards the playoffs!  Order MLS DIRECT KICK now for $49 or four installments of $12.25.'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.NationalLdl_TrafficFlow.1')
scmtRemove('Config.1.NationalLdl_TrafficFlow.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.Local_IntroFS.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.NationalLdl_Today.2')
scmtRemove('Config.1.NationalLdl_Today.1')
scmtRemove('Config.1.Local_TomorrowNightFS.0')
scmtRemove('Config.1.Local_TodayFS.0')
scmtRemove('Config.1.NationalLdl_Today.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.Local_SevereAlertFS.0')
scmtRemove('Config.1.Local_NowFS.0')
scmtRemove('Config.1.NationalLdl_TrafficIncidents.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.NationalLdl_Today.5')
scmtRemove('Config.1.NationalLdl_Today.4')
scmtRemove('Config.1.NationalLdl_TrafficFlow.0')
scmtRemove('Config.1.NationalLdl_Today.0')
#
d = twc.Data()
d.locName = ['Dallas ',]
d.coopId = ['72259000',]
dsm.set('Config.1.Local_TodayFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_7DayForecastFS.0', d, 0, 1)
dsm.set('Config.1.Local_HourlyForecastFS.0', d, 0, 1)
dsm.set('Config.1.Local_HourlyForecastTodayFS.0', d, 0, 1)
dsm.set('Config.1.Local_HourlyForecastTonightFS.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.Local_TomorrowFS.0', d, 0, 1)
dsm.set('Config.1.Local_TonightFS.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
d.zone = ['TXZ119',]
dsm.set('Config.1.Local_SevereAlertFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_SevereAlertLDL.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlert.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlertLF.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas ',]
d.coopId = ['72259000',]
dsm.set('Config.1.Local_TomorrowNightFS.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.5', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.5', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.4', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.4', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.3', d, 0, 1)
#
d = twc.Data()
d.locName = ['Mesquite',]
d.coopId = ['72259044',]
dsm.set('Config.1.NationalLdl_Today.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_TodayLDL.2', d, 0, 1)
dsm.set('Config.1.Local_TomorrowLDL.2', d, 0, 1)
dsm.set('Config.1.Local_TonightLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_ExtendedLF.2', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_HourlyForecast.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_NextWeek.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_TodayLF.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tomorrow.2', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_TomorrowLF.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tonight.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_TonightLF.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_WeekAhead.2', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_Weekend.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72259044',]
d.locName = ['Mesquite',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
d.coopId = ['72259000',]
dsm.set('Config.1.Local_SummaryFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.climId = '412242'
d.latitude  = 32.9
d.longitude = -97.03
d.locName = ['Dallas ',]
dsm.set('Config.1.Local_NowFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_WelcomeAMHQ.0', d, 0, 1)
dsm.set('Config.1.Local_WelcomeFS.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas ',]
d.keyRoutes = ['23000028','23000029',]
d.coopId = ['72259000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.2', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Addison',]
d.coopId = ['72259018',]
dsm.set('Config.1.NationalLdl_Today.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NextWeekLDL.1', d, 0, 1)
dsm.set('Config.1.Local_TodayLDL.1', d, 0, 1)
dsm.set('Config.1.Local_TomorrowLDL.1', d, 0, 1)
dsm.set('Config.1.Local_TonightLDL.1', d, 0, 1)
ds.commit()
dsm.set('Config.1.Local_WeekAheadLDL.1', d, 0, 1)
dsm.set('Config.1.Local_WeekendLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_ExtendedLF.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.1', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_NextWeek.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_TodayLF.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tomorrow.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_TomorrowLF.1', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_Tonight.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_TonightLF.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_WeekAhead.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_Weekend.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72259018',]
d.locName = ['Addison',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas ',]
d.keyRoutes = ['23000013','23000014',]
d.coopId = ['72259000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.1', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Dallas ',]
d.coopId = ['72259000',]
dsm.set('Config.1.NationalLdl_Today.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_HourlyForecastLDL.0', d, 0, 1)
dsm.set('Config.1.Local_HourlyTomorrowLDL.0', d, 0, 1)
dsm.set('Config.1.Local_HourlyTonightLDL.0', d, 0, 1)
dsm.set('Config.1.Local_NextWeekLDL.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.Local_TodayLDL.0', d, 0, 1)
dsm.set('Config.1.Local_TodayLDL.4', d, 0, 1)
dsm.set('Config.1.Local_TomorrowLDL.0', d, 0, 1)
dsm.set('Config.1.Local_TomorrowLDL.4', d, 0, 1)
ds.commit()
dsm.set('Config.1.Local_TonightLDL.0', d, 0, 1)
dsm.set('Config.1.Local_TonightLDL.4', d, 0, 1)
dsm.set('Config.1.Local_WeekAheadLDL.0', d, 0, 1)
dsm.set('Config.1.Local_WeekendLDL.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_ExtendedLF.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_NextWeek.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_TodayLF.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_Tomorrow.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_TomorrowLF.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tonight.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_TonightLF.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_WeekAhead.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_Weekend.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
dsm.set('Config.1.NationalLdl_CurrentConditions.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.0', d, 0, 1)
dsm.set('Config.1.Local_NowLDL.4', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.0', d, 0, 1)
dsm.set('Config.1.TimeTemp_Live.0', d, 0, 1)
ds.commit()
dsm.set('Config.1.TimeTemp_Promo.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas ',]
d.keyRoutes = ['23000001','23000002',]
d.coopId = ['72259000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
dsm.set('Config.1.Local_RegionalRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Dallas ',]
dsm.set('Config.1.NationalLdl_TrafficIncidents.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
dsm.set('Config.1.Local_MetroRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259000',]
d.locName = ['Dallas ',]
dsm.set('Config.1.Local_IntroFS.0', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_RadarSatelliteComposite = 1
d.activeLocal_Satellite = 0
# region keys
dsm.set('Config.1.DefaultUS.120.2', d, 0)
dsm.set('Config.1.DefaultUS.60.1', d, 0)
dsm.set('Config.1.DefaultUS.90.1', d, 0)
dsm.set('Config.1.DefaultUS.90.0', d, 0)
dsm.set('Config.1.DefaultUS.60.0', d, 0)
dsm.set('Config.1.DefaultUS.120.1', d, 0)
dsm.set('Config.1.DefaultUS.120.0', d, 0)
#
ds.commit()
d = [[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
]
dsm.set('Config.1.Playlist.NationalLdl.scheduleA', d, 0)
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimationSmall',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',0,12,12,4,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',0,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',0,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',1,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',1,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',2,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',2,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',3,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',3,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',4,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',4,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',5,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',5,20,20,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpB', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,6,8,5,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,6,7,5,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,8,4,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,20,20,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,8,8,0,0,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,15,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,23,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,7,8,6,1,12,2,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,7,8,6,1,13,2,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,8,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,7,8,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,7,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,6,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,20,20,8,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,21,21,18,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.60.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,10,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,14,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,24,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,18,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,19,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,8,1,13,4,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,27,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,15,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,20,20,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,20,20,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,14,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,8,10,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,8,10,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.2', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,6,8,5,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,6,7,5,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,8,4,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,20,20,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,8,8,0,0,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,15,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,23,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,7,8,6,1,12,2,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,7,8,6,1,13,2,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,8,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,7,8,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,7,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,6,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,21,21,18,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.60.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,7,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,11,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,10,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,14,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,23,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,10,12,9,1,7,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,10,12,9,1,19,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,26,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,27,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,15,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,20,20,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,20,20,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,14,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,9,9,9,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,9,9,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,1,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,9,9,9,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,9,9,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpSoCali', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpNConus', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('LASCrawl',0,4,120,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',3,4,44,4,1,2,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,120,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.ldl1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,20,20,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,10,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,23,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,13,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,14,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,15,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,26,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,20,20,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,20,20,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,14,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,8,11,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,10,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,17,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,14,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,26,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,20,20,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,27,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,20,20,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,15,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,23,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,11,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,12,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,10,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,20,20,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,20,20,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,25,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,26,5,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,15,16,14,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,7,11,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,7,12,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.0', d, 0)
ds.commit()
#
d = twc.Data()
d.prodPrefix='Fcst'
d.childPrefixes=[]
d.units='seconds'
d.loadHeuristic='loadPriorityOneOnly_v1'
d.overHeuristic='overPriority_v1'
d.underHeuristic='underPriority_v1'
d.playlist=[
('TextForecast.1',0,14,60,14,1,1,0,[]),
('TextForecast.2',0,14,60,14,1,1,0,[]),
('DaypartForecast',0,14,60,14,1,1,0,[]),
('ExtendedForecast',0,14,60,14,1,1,0,[]),
('Unavailable',0,1,60,1,1,2,0,[]),
]
dsm.set('Config.1.Playlist.Fcst.fcst1', d, 0)
#
ds.commit()
d = twc.Data()
d.prodPrefix='Local'
d.childPrefixes=["Cc", "Radar", "Fcst", "Logo"]
d.units='percent'
d.loadHeuristic='loadPriority_v1'
d.overHeuristic='overPriority_v1'
d.underHeuristic='underPriority_v1'
d.playlist=[
('SqueezebackFade',0,100,100,100,1,1,0,["cc1","radar1","fcst1","logo1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.57.0', d, 0)
#
ds.commit()
#
## End of SCMT Configuration
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['AdCrawl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR V FS LOT8
d.playlist=[
('WelcomeFS',              0,  3,  3,  3, 1,  3, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  5, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 8, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('TonightFS',              0, 10, 90,  8, 1, 70, 0, ['adcrawl1']),
('TomorrowFS',             0, 10, 12,  8, 1, 72, 0, ['adcrawl1']),
('TomorrowNightFS',        0, 10, 10,  8, 1, 75, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 14, 10, 1, 50, 0, ['adcrawl1']),
('OutroFS',                0,  2,  2,  2, 1, 41, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.DefaultUS.65.0', d, 0)
#
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['AdCrawl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR W FS LOT8, with LocalOCM
d.playlist=[
('LocalOCM',               0, 65, 65, 65, 0,  1, 0, ['adcrawl1']),
('WelcomeFS',              0,  3,  3,  3, 1,  3, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  5, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0,  8, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('TonightFS',              0, 10, 90,  8, 1, 70, 0, ['adcrawl1']),
('TomorrowFS',             0, 10, 12,  8, 1, 72, 0, ['adcrawl1']),
('TomorrowNightFS',        0, 10, 10,  8, 1, 75, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 14, 10, 1, 50, 0, ['adcrawl1']),
('OutroFS',                0,  2,  2,  2, 1, 41, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.DefaultUS.65.1', d, 0)
#
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['AdCrawl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR V FS LOT8
d.playlist=[
('IntroFS',                0,  2,  2,  2, 1,   1, 0, ['adcrawl1']),
('WelcomeFS',              0,  3,  3,  3, 1,   1, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,   2, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4,  20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 12, 12,  8, 4,  30, 0, ['adcrawl1']),
('MetroNowMapFS',          0,  9, 14,  7, 1,  40, 0, ['adcrawl1']),
('TodayMapFS',             0,  9, 10,  7, 1,  70, 0, ['adcrawl1']),
('TonightMapFS',           0,  9, 10,  7, 1,  80, 0, ['adcrawl1']),
('TomorrowMapFS',          0,  9, 10,  7, 1, 130, 0, ['adcrawl1']),
('TomorrowNightMapFS',     0,  9, 10,  7, 1, 131, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 12, 11, 1,  50, 0, ['adcrawl1']),
('SummaryFS',              0,  4,  9,  4, 1,  60, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.LargeAreaServed.65.0', d, 0)
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['AdCrawl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR W FS LOT8, with LocalOCM
d.playlist=[
('LocalOCM',               0, 65, 65, 65, 0,  1, 0, ['adcrawl1']),
('IntroFS',                0,  2,  2,  2, 1,   1, 0, ['adcrawl1']),
('WelcomeFS',              0,  3,  3,  3, 1,   1, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,   2, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4,  20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 12, 12,  8, 4,  30, 0, ['adcrawl1']),
('MetroNowMapFS',          0,  9, 14,  7, 1,  40, 0, ['adcrawl1']),
('TodayMapFS',             0,  9, 10,  7, 1,  70, 0, ['adcrawl1']),
('TonightMapFS',           0,  9, 10,  7, 1,  80, 0, ['adcrawl1']),
('TomorrowMapFS',          0,  9, 10,  7, 1, 130, 0, ['adcrawl1']),
('TomorrowNightMapFS',     0,  9, 10,  7, 1, 131, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 12, 11, 1,  50, 0, ['adcrawl1']),
('SummaryFS',              0,  4,  9,  4, 1,  60, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.LargeAreaServed.65.1', d, 0)
#
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['TimeTemp']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR Z, LOT8 LDL
d.playlist=[
('SevereAlertLDL',    0,  5, 15,  5, 1,  5, 0,['timeTempPromo1']),
('NowLDL',            0, 10, 65,  8, 1,  4, 0,['timeTempPromo1']),
('TodayLDL',          0,  5,  8,  4, 1,  1, 0,['timeTempPromo1']),
('HourlyTodayLDL',    0, 20, 28, 16, 1, 17, 1,['timeTempPromo1']),
('TonightLDL',        0,  5, 45,  4, 1,  2, 0,['timeTempPromo1']),
('HourlyTonightLDL',  0, 20, 28, 16, 1, 18, 1,['timeTempPromo1']),
('TomorrowLDL',       0,  5, 45,  4, 1,  3, 0,['timeTempPromo1']),
('HourlyTomorrowLDL', 0, 20, 28, 16, 1, 19, 1,['timeTempPromo1']),
('WeekAheadLDL',      0, 10, 12,  8, 1, 10, 0,['timeTempPromo1']),
('WeekendLDL',        0, 10, 12,  8, 1, 11, 0,['timeTempPromo1']),
('NextWeekLDL',       0, 10, 12,  8, 1, 12, 0,['timeTempPromo1']),
#
('NowLDL',            1, 10, 15,  8, 1,  6, 0,['timeTempPromo1']),
('TodayLDL',          1,  5,  8,  4, 1,  7, 0,['timeTempPromo1']),
('TonightLDL',        1,  5,  8,  4, 1,  8, 0,['timeTempPromo1']),
('TomorrowLDL',       1,  5,  8,  4, 1,  9, 0,['timeTempPromo1']),
#
('NowLDL',            2, 10, 15,  8, 1, 13, 1,['timeTempPromo1']),
('TodayLDL',          2,  5,  8,  4, 1, 14, 0,['timeTempPromo1']),
('TonightLDL',        2,  5,  8,  4, 1, 15, 0,['timeTempPromo1']),
('TomorrowLDL',       2,  5,  8,  4, 1, 16, 0,['timeTempPromo1']),
#
('NowLDL',            3, 10, 15,  8, 1, 20, 0,['timeTempPromo1']),
('TodayLDL',          3,  5,  8,  4, 1, 21, 0,['timeTempPromo1']),
('TonightLDL',        3,  5,  8,  4, 1, 22, 0,['timeTempPromo1']),
('TomorrowLDL',       3,  5,  8,  4, 1, 23, 0,['timeTempPromo1']),
#
('NowLDL',            4, 10, 15,  8, 1, 24, 0,['timeTempPromo1']),
('TodayLDL',          4,  5,  8,  4, 1, 25, 0,['timeTempPromo1']),
('TonightLDL',        4,  5,  8,  4, 1, 26, 0,['timeTempPromo1']),
('TomorrowLDL',       4,  5,  8,  4, 1, 27, 0,['timeTempPromo1']),
]
dsm.set('Config.1.Playlist.DefaultUS.90.3', d, 0)
dsm.set('Config.1.Playlist.LargeAreaServed.90.3', d, 0)
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['AdCrawl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
# FLAVOR U AMHQ LOT8
d.playlist=[
('Null',                   0,  3,  3,  3, 1,  3, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  5, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0,  8, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('TonightFS',              0, 10, 90,  8, 1, 70, 0, ['adcrawl1']),
('TomorrowFS',             0, 10, 12,  8, 1, 72, 0, ['adcrawl1']),
('TomorrowNightFS',        0, 10, 10,  8, 1, 75, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 14, 10, 1, 50, 0, ['adcrawl1']),
('OutroFS',                0,  2,  2,  2, 1, 41, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.DefaultUS.65.2', d, 0)
ds.commit()
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Fri Oct 17 14:49:44 GMT 2014
