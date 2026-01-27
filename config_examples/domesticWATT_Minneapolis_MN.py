# Created on Thu Jul 24 15:47:10 GMT 2014
Log.info('scmt config started')
# EXP: 1099
# VIW: 12894
# CLN: 3148
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
# MAP: 73527
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20677,14936),
             mapcutSize=(1296,740),
             mapFinalSize=(240,137),
             mapMilesSize=(116,79),
             datacutType='radar.us',
             datacutCoordinate=(2134,1492),
             datacutSize=(158,91),
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
              ( ( (133,91),),
                ( (151,62),),
                ( (132,55),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (133,91),),
                ( (151,62),),
                ( (132,55),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (98,105),'Andover',),
                ( (162,69),'Roseville',),
                ( (79,45),'Minneapolis',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (98,105),'Andover',),
                ( (162,69),'Roseville',),
                ( (79,45),'Minneapolis',),
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
# MAP: 80965
# LFLocal_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20756,15000),
             mapcutSize=(1417,609),
             mapFinalSize=(398,171),
             mapMilesSize=(116,65),
             datacutType='radar.us',
             datacutCoordinate=(2143,1500),
             datacutSize=(174,74),
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
              ( ( (183,124),),
                ( (210,80),),
                ( (180,69),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (183,124),),
                ( (210,80),),
                ( (180,69),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (148,138),'Andover',),
                ( (221,87),'Roseville',),
                ( (127,59),'Minneapolis',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (148,138),'Andover',),
                ( (221,87),'Roseville',),
                ( (127,59),'Minneapolis',),
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
# MAP: 120639
# Local_SummaryFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20993,15054),
             mapcutSize=(1296,498),
             mapFinalSize=(338,130),
             mapMilesSize=(116,53),
             datacutType='radar.us',
             datacutCoordinate=(2172,1506),
             datacutSize=(159,62),
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
              ( ( (141,51),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (166,39),'St. Paul',),
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
# MAP: 52834
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20884,14882),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(116,93),
             datacutType='radar.us',
             datacutCoordinate=(2159,1486),
             datacutSize=(159,105),
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
              ( ( (386,339),'35',),
                ( (136,325),'94',),
                ( (241,228),'494',),
                ( (599,195),'94',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (241,228),'494',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (299,267),'10',),
                ( (166,136),'212',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (299,267),'10',),
                ( (166,136),'212',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (386,339),'35',),
                ( (136,325),'94',),
                ( (599,195),'94',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (322,171),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (335,130),),
                ( (332,283),),
                ( (277,283),),
                ( (406,281),),
                ( (256,262),),
                ( (349,230),),
                ( (373,206),),
                ( (448,244),),
                ( (295,210),),
                ( (472,213),),
                ( (458,136),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (335,130),),
                ( (332,283),),
                ( (277,283),),
                ( (406,281),),
                ( (256,262),),
                ( (349,230),),
                ( (373,206),),
                ( (448,244),),
                ( (295,210),),
                ( (472,213),),
                ( (458,136),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (322,171),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (280,113),'Apple Valley',),
                ( (309,304),'Blaine',),
                ( (183,301),'Champlin',),
                ( (426,284),'Hugo',),
                ( (128,265),'Maple Grove',),
                ( (321,250),'Roseville',),
                ( (353,191),'St. Paul',),
                ( (465,262),'Stillwater',),
                ( (173,213),'Minneapolis',),
                ( (492,216),'Hudson',),
                ( (478,139),'Prescott',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (280,113),'Apple Valley',),
                ( (309,304),'Blaine',),
                ( (183,301),'Champlin',),
                ( (426,284),'Hugo',),
                ( (128,265),'Maple Grove',),
                ( (321,250),'Roseville',),
                ( (353,191),'St. Paul',),
                ( (465,262),'Stillwater',),
                ( (173,213),'Minneapolis',),
                ( (492,216),'Hudson',),
                ( (478,139),'Prescott',),
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
# MAP: 116263
# Local_MetroRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20930,15073),
             mapcutSize=(1296,483),
             mapFinalSize=(620,231),
             mapMilesSize=(116,52),
             datacutType='radar.us',
             datacutCoordinate=(2165,1509),
             datacutSize=(158,59),
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
              ( ( (324,187),'35',),
                ( (107,184),'94',),
                ( (185,108),'494',),
                ( (493,80),'94',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (235,142),'10',),
                ( (90,33),'212',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (265,20),),
                ( (262,152),),
                ( (197,133),),
                ( (277,105),),
                ( (295,91),),
                ( (362,118),),
                ( (232,90),),
                ( (383,91),),
                ( (371,25),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (134,32),'Apple Valley',),
                ( (241,176),'Blaine',),
                ( (69,133),'Maple Grove',),
                ( (234,120),'Roseville',),
                ( (303,67),'St. Paul',),
                ( (372,129),'Stillwater',),
                ( (106,76),'Minneapolis',),
                ( (405,88),'Hudson',),
                ( (394,31),'Prescott',),
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
# MAP: 72401
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3312,1972),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(1393,940),
             datacutType='radarSatellite.us',
             datacutCoordinate=(809,672),
             datacutSize=(740,496),
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
# MAP: 409
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21135,15053),
             mapcutSize=(720,480),
             mapFinalSize=(720,480),
             mapMilesSize=(64,51),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (276,360),'10',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (392,274),'694',),
                ( (208,181),'494',),
                ( (356,111),'35E',),
                ( (413,359),'35W',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (89,92),'212',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (510,199),'94',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72649007',(208,84),),
                ( '72649014',(130,183),),
                ( '72658000',(269,184),),
                ( '72658010',(426,185),),
                ( '72658024',(485,79),),
                ( '72658030',(560,195),),
                ( '72658034',(345,294),),
                ( '72658043',(490,298),),
                ( '72658047',(212,308),),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplane',0,1,0,),
              ( ( (344,157),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72649007',(205,120),),
                ( '72649014',(127,219),),
                ( '72658000',(266,220),),
                ( '72658010',(423,221),),
                ( '72658024',(482,115),),
                ( '72658030',(557,231),),
                ( '72658034',(342,330),),
                ( '72658043',(487,334),),
                ( '72658047',(209,344),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (143,156),'Eden Prairie',),
                ( (80,255),'Plymouth',),
                ( (207,256),'Minneapolis',),
                ( (385,257),'St. Paul',),
                ( (408,151),'Cottage Grove',),
                ( (508,267),'Stillwater',),
                ( (314,366),'Blaine',),
                ( (466,370),'Hugo',),
                ( (165,380),'Champlin',),
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
# MAP: 74937
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21135,15053),
             mapcutSize=(720,480),
             mapFinalSize=(720,480),
             mapMilesSize=(64,51),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (276,360),'10',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (392,274),'694',),
                ( (208,181),'494',),
                ( (356,111),'35E',),
                ( (413,359),'35W',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (89,92),'212',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (510,199),'94',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplane',0,1,0,),
              ( ( (344,157),),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72649007',(205,120),),
                ( 'T72649014',(127,219),),
                ( 'T72658000',(266,220),),
                ( 'T72658010',(423,221),),
                ( 'T72658024',(482,115),),
                ( 'T72658030',(557,231),),
                ( 'T72658034',(342,330),),
                ( 'T72658043',(487,334),),
                ( 'T72658047',(209,344),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72649007',(208,84),),
                ( 'T72649014',(130,183),),
                ( 'T72658000',(269,184),),
                ( 'T72658010',(426,185),),
                ( 'T72658024',(485,79),),
                ( 'T72658030',(560,195),),
                ( 'T72658034',(345,294),),
                ( 'T72658043',(490,298),),
                ( 'T72658047',(212,308),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (143,156),'Eden Prairie',),
                ( (80,255),'Plymouth',),
                ( (207,256),'Minneapolis',),
                ( (385,257),'St. Paul',),
                ( (408,151),'Cottage Grove',),
                ( (508,267),'Stillwater',),
                ( (314,366),'Blaine',),
                ( (466,370),'Hugo',),
                ( (165,380),'Champlin',),
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
# MAP: 74674
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18432,13293),
             mapcutSize=(6480,4320),
             mapFinalSize=(720,480),
             mapMilesSize=(581,465),
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
              ( ( '72643000',(452,130),),
                ( '72644000',(349,85),),
                ( '72645107',(582,138),),
                ( '72651000',(116,92),),
                ( '72658000',(319,184),),
                ( '72741047',(551,232),),
                ( '72745000',(409,309),),
                ( '72750008',(269,287),),
                ( '72753000',(108,305),),
                ( '74341068',(164,207),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72643000',(449,166),),
                ( '72644000',(346,121),),
                ( '72645107',(579,174),),
                ( '72651000',(113,128),),
                ( '72658000',(316,220),),
                ( '72741047',(548,268),),
                ( '72745000',(406,345),),
                ( '72750008',(266,323),),
                ( '72753000',(105,341),),
                ( '74341068',(161,243),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (400,202),'La Crosse',),
                ( (275,158),'Rochester',),
                ( (543,210),'Wausau',),
                ( (75,164),'Sioux Falls',),
                ( (257,256),'Minneapolis',),
                ( (488,304),'Rhinelander',),
                ( (375,381),'Duluth',),
                ( (246,359),'Brainerd',),
                ( (81,377),'Fargo',),
                ( (132,279),'Morris',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 74673
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18432,13293),
             mapcutSize=(6480,4320),
             mapFinalSize=(720,480),
             mapMilesSize=(581,465),
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
              ( ( 'KAUW',(579,174),),
                ( 'KFAR',(105,341),),
                ( 'KFSD',(113,128),),
                ( 'KRHI',(548,268),),
                ( 'KRST',(346,121),),
                ( 'T72643000',(449,166),),
                ( 'T72658000',(316,220),),
                ( 'T72745000',(406,345),),
                ( 'T72750008',(266,323),),
                ( 'T74341068',(161,243),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'KAUW',(582,138),),
                ( 'KFAR',(108,305),),
                ( 'KFSD',(116,92),),
                ( 'KRHI',(551,232),),
                ( 'KRST',(349,85),),
                ( 'T72643000',(452,130),),
                ( 'T72658000',(319,184),),
                ( 'T72745000',(409,309),),
                ( 'T72750008',(269,287),),
                ( 'T74341068',(164,207),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (543,210),'Wausau',),
                ( (81,377),'Fargo',),
                ( (75,164),'Sioux Falls',),
                ( (488,304),'Rhinelander',),
                ( (275,158),'Rochester',),
                ( (400,202),'La Crosse',),
                ( (257,256),'Minneapolis',),
                ( (375,381),'Duluth',),
                ( (246,359),'Brainerd',),
                ( (132,279),'Morris',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 118438
# Local_RegionalRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19928,14666),
             mapcutSize=(3456,1288),
             mapFinalSize=(620,231),
             mapMilesSize=(311,139),
             datacutType='radar.us',
             datacutCoordinate=(2042,1459),
             datacutSize=(423,158),
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
              ( ( (292,187),'35',),
                ( (193,149),'94',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (431,127),'53',),
                ( (149,79),'212',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (273,72),),
                ( (154,31),),
                ( (283,100),),
                ( (178,176),),
                ( (266,107),),
                ( (93,125),),
                ( (439,91),),
                ( (415,168),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (238,45),'Lakeville',),
                ( (62,30),'New Ulm',),
                ( (304,104),'St. Paul',),
                ( (189,185),'St. Cloud',),
                ( (145,110),'Minneapolis',),
                ( (68,146),'Willmar',),
                ( (468,80),'Eau Claire',),
                ( (435,176),'Rice Lake',),
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
# MAP: 49658
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19800,14160),
             mapcutSize=(3456,2304),
             mapFinalSize=(720,480),
             mapMilesSize=(311,249),
             datacutType='radar.us',
             datacutCoordinate=(2026,1397),
             datacutSize=(424,282),
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
              ( ( (366,320),'35',),
                ( (251,274),'94',),
                ( (502,82),'90',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (527,249),'53',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (200,184),'212',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (527,249),'53',),
                ( (200,184),'212',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (366,320),'35',),
                ( (251,274),'94',),
                ( (502,82),'90',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (254,124),),
                ( (357,223),),
                ( (100,347),),
                ( (233,310),),
                ( (336,229),),
                ( (426,105),),
                ( (135,251),),
                ( (536,211),),
                ( (508,301),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (254,124),),
                ( (357,223),),
                ( (100,347),),
                ( (233,310),),
                ( (336,229),),
                ( (426,105),),
                ( (135,251),),
                ( (536,211),),
                ( (508,301),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (163,127),'Mankato',),
                ( (377,226),'St. Paul',),
                ( (69,329),'Alexandria',),
                ( (209,332),'St. Cloud',),
                ( (214,232),'Minneapolis',),
                ( (383,126),'Rochester',),
                ( (104,234),'Willmar',),
                ( (493,194),'Eau Claire',),
                ( (467,322),'Rice Lake',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (163,127),'Mankato',),
                ( (377,226),'St. Paul',),
                ( (69,329),'Alexandria',),
                ( (209,332),'St. Cloud',),
                ( (214,232),'Minneapolis',),
                ( (383,126),'Rochester',),
                ( (104,234),'Willmar',),
                ( (493,194),'Eau Claire',),
                ( (467,322),'Rice Lake',),
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
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler','Config.1.LFLocal_LocalDoppler','Config.1.Local_SummaryFS','Config.1.Local_MetroDopplerRadar','Config.1.Local_MetroRadarFS','Config.1.Local_RegionalRadarFS','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['FAR','FSD','MSP',])
wxdata.setInterestList('coopId','1',['72634030','72638041','72643000','72644000','72645107','72649007','72649014','72651000','72658000','72658010','72658020','72658024','72658030','72658034','72658043','72658047','72741047','72745000','72750008','72753000','74341068',])
wxdata.setInterestList('pollenId','1',['MSP',])
wxdata.setInterestList('indexId','1',['KSTP',])
wxdata.setInterestList('obsStation','1',['KAUW','KFAR','KFSD','KRHI','KRST','KSTP','T72643000','T72649007','T72649014','T72651000','T72658000','T72658010','T72658020','T72658024','T72658030','T72658034','T72658043','T72658047','T72745000','T72750008','T72753000','T74341068',])
wxdata.setInterestList('metroId','1',['25',])
wxdata.setInterestList('climId','1',['217377',])
wxdata.setInterestList('zone','1',['MNZ062',])
wxdata.setInterestList('keyRoute','1',['62000003','62000004','62000005','62000006','62000014','62000015',])
wxdata.setInterestList('skiId','1',['616002','616006',])
wxdata.setInterestList('county','1',['MNC123','MNC163','MNC003','MNC053','MNC037','WIC093','WIC109',])
dsm.set('Config.1.countyNameList',[('MNC123','Ramsey'),('MNC163','Washington'),('MNC003','Anoka'),('MNC053','Hennepin'),('MNC037','Dakota'),('WIC093','Pierce'),('WIC109','Saint Croix'),], 0)
#
dsm.set('dmaCode','613', 0)
dsm.set('secondaryObsStation','KSTP', 0)
dsm.set('primaryClimoStation','217377', 0)
dsm.set('primaryIndexId','KSTP', 0)
dsm.set('stateCode','MN', 0)
dsm.set('primPollenSiteName','Minneapolis', 0)
dsm.set('expRev','6880732', 0)
dsm.set('primaryCoopId','72658000', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','MSP', 0)
dsm.set('primaryCounty','MNC123', 0)
dsm.set('primaryObsStation','T72658010', 0)
dsm.set('primaryRad',15, 0)
dsm.set('primaryLat',45.02166, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','MSP', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('secondaryRad',30, 0)
dsm.set('primaryLon',-93.14027, 0)
dsm.set('primaryZone','MNZ062', 0)
dsm.set('climoRegion','2', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','022317', 0)
dsm.set('msoName','COMCAST COMMUNICATIONS', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - ROSEVILLE - DOM', 0)
dsm.set('affiliateNumber','01471', 0)
dsm.set('zipCode','55113', 0)
dsm.set('Config.1.irdAddress','0000315578079052', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD06040049', 0)
dsm.set('Config.1.bcDialInNumber','6516394243', 0)
dsm.set('Config.1.bcExtIpAddress','172.20.3.221', 0)
dsm.set('Config.1.bcGateWay','10.3.169.1', 0)
dsm.set('Config.1.bcIpAddress','10.3.169.60', 0)
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
d.airportId = ['MSP','FSD','FAR',]
d.airportLocName = ['Minneapolis','Sioux Falls','Fargo',]
d.obsStation = ['T72658000','T72651000','T72753000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['616006','616002',]
d.coopId = ['72638041','72634030',]
d.resortName = ['Crystal Mtn, MI','Boyne Highlands, MI',]
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
d.serialNum=1052829
d.crawls=[
(1389592800,1420091999,[(0,23)],'NEED IT REPAIRED QUICKLY AND CORRECTLY? WITH BONFE YOU KNOW IT WILL BE. BONFE OFFERS A LIFETIME WARRANTY ON ALL RECOMMENDED PLUMBING, HEATING, COOLING, ELECTRICAL AND APPLIANCE REPAIRS. CALL BONFE TODAY (651)332-6633 OR WWW.BONFE.COM'),
(1401940800,1407124799,[(0,23)],'TIRED OF HOUSECLEANING AND OTHER CHORES? LET DARTS DO IT. IF YOU\'RE 50+ AND LIVE IN DAKOTA COUNTY, CALL 651-234-2233. CHOOSE DARTS AND SUPPORT OUR 40-YEAR TRADITION OF HELPING OUR SENIOR COMMUNITY. CALL DARTS AT 651-234-2233.'),
(1404705600,1421647199,[(0,23)],'THE HEAT IS ON AT SIMONET FURNITURE. SAVE 25% ON STIFFEL LAMPS! $200 ON NORWALK SOFAS AND $200 OFF AMISH DINING AND BEDROOM SETS. SIMONET\'S FURNITURE NOW ON MAIN STREET AND THE MAIN SHOWROOM ON CURVE CREST BLVD STILLWATER. SIMONETS FURNITURE, WWW.SIMONETFURNITURE.COM'),
(1404792000,1419832799,[(0,23)],'GIVE UNEXPECTED APPLIANCE REPAIR COSTS THE BOOT! WITH CENTERPOINT ENERGY\'S HOME SERVICE PLUS REPAIR PLAN, YOU MAY NEVER SEE ANOTHER APPLIANCE REPAIR BILL. ENROLL TODAY AND GET THE FIRST MONTH FREE! GO TO HSPTODAY.COM TO LEARN MORE.'),
(1404964800,1406260799,[(0,23)],'DR. SEUSS THE CAT IN THE HAT NOW PLAYING AT THE CHILDREN\'S THEATRE CO. AND EXTENDED THROUGH JULY 27TH.TICKETS AVAILABLE AT WWW.CHILDRENSTHEATRE.ORG DR. SEUSS THE CAT IN THE HAT EXTENDED THROUGH JULY 27TH AT THE CHILDRENS THEATRE CO.'),
(1405483200,1419832799,[(0,23)],'PRESERVE THE FRESH TASTE OF FRUITS AND GARDEN VEGETABLES WITH CANNING SUPPLIES FROM MILLS FLEET FARM. FIND THE BEST SELECTION OF CANNING JARS, SEASONINGS AND MORE! STOP BY OR VISIT FLEETFARM.COM. MILLS FLEET FARM, YOUR CANNING HEADQUARTERS!'),
(1405310400,1405915199,[(0,23)],'DROP IT LIKE IT\'S HOT THIS JULY AT GRAND CASINO MILLE LACS! WIN YOUR SHARE OF $50,000 WITH PRIZES RANGING FROM $100 TO $1,000! DRAWINGS ON JULY 13 AND 27 FROM 2-6 PM. SEE GRAND REWARDS OR GRANDCASINOMN.COM FOR DETAILS. GRAND CASINO: THE BEST STORIES START HERE. WHAT\'S YOURS?'),
(1405915200,1419832799,[(0,23)],'IT\'S TIME TO WIN SMOKIN\' HOT CASH AT GRAND CASINO HINCKLEY! WE\'RE GIVING AWAY $1,000 EVERY 15 MINUTES! DRAWINGS TAKE PLACE ON SATURDAY, AUGUST 2 FROM 4-9 PM. SEE GRAND REWARDS OR GRANDCASINOMN.COM FOR DETAILS. GRAND CASINO: THE BEST STORIES START HERE. WHAT\'S YOURS?'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.NationalLdl_TrafficFlow.0')
scmtRemove('Config.1.NationalLdl_Today.1')
scmtRemove('Config.1.Local_NowFS.0')
scmtRemove('Config.1.NationalLdl_TrafficIncidents.0')
scmtRemove('Config.1.NationalLdl_Today.5')
scmtRemove('Config.1.NationalLdl_Today.4')
scmtRemove('Config.1.NationalLdl_TrafficFlow.1')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.Local_IntroFS.0')
scmtRemove('Config.1.NationalLdl_TrafficFlow.2')
scmtRemove('Config.1.Local_TodayFS.0')
scmtRemove('Config.1.Local_SevereAlertFS.0')
scmtRemove('Config.1.NationalLdl_Today.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.NationalLdl_Today.2')
scmtRemove('Config.1.NationalLdl_Today.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
#
d = twc.Data()
d.locName = ['St. Paul',]
d.coopId = ['72658010',]
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
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
d.zone = ['MNZ062',]
dsm.set('Config.1.Local_SevereAlertFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_SevereAlertLDL.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlert.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlertLF.0', d, 0, 1)
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
d.locName = ['Anoka',]
d.coopId = ['72658047',]
dsm.set('Config.1.NationalLdl_Today.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_TodayLDL.3', d, 0, 1)
dsm.set('Config.1.Local_TomorrowLDL.3', d, 0, 1)
dsm.set('Config.1.Local_TonightLDL.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_ExtendedLF.3', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_HourlyForecast.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_NextWeek.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_TodayLF.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tomorrow.3', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_TomorrowLF.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_Tonight.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_TonightLF.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_WeekAhead.3', d, 0, 1)
ds.commit()
dsm.set('Config.1.NationalLdl_Weekend.3', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72658047',]
d.locName = ['Anoka',]
dsm.set('Config.1.NationalLdl_CurrentConditions.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.3', d, 0, 1)
#
d = twc.Data()
d.locName = ['Crystal',]
d.coopId = ['72658020',]
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
d.obsStation = ['T72658020',]
d.locName = ['Crystal',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
d.coopId = ['72658000',]
dsm.set('Config.1.Local_SummaryFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72658010',]
d.climId = '217377'
d.latitude  = 44.97
d.longitude = -93.08
d.locName = ['St. Paul',]
dsm.set('Config.1.Local_NowFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_WelcomeAMHQ.0', d, 0, 1)
dsm.set('Config.1.Local_WelcomeFS.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['St. Paul',]
d.keyRoutes = ['62000014','62000015',]
d.coopId = ['72658000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.2', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Minneapolis',]
d.coopId = ['72658000',]
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
d.obsStation = ['T72658000',]
d.locName = ['Minneapolis',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['St. Paul',]
d.keyRoutes = ['62000005','62000006',]
d.coopId = ['72658000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.1', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['St. Paul',]
d.coopId = ['72658010',]
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
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
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
d.locName = ['St. Paul',]
d.keyRoutes = ['62000003','62000004',]
d.coopId = ['72658000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
dsm.set('Config.1.Local_RegionalRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['St. Paul',]
dsm.set('Config.1.NationalLdl_TrafficIncidents.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
dsm.set('Config.1.Local_MetroRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72658010',]
d.locName = ['St. Paul',]
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
('IntroFS',                0,  2,  2,  2, 1,  1, 0, ['adcrawl1']),
('WelcomeFS',              0,  3,  3,  3, 1,  2, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  3, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 12, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('HourlyForecastTodayFS',  0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TonightFS',              0, 10, 10,  9, 1, 70, 0, ['adcrawl1']),
('HourlyForecastTonightFS',0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TomorrowFS',             0, 10, 90,  8, 1, 72, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 12, 10, 1, 50, 0, ['adcrawl1']),
('SummaryFS',              0,  4,  6,  4, 1, 60, 0, ['adcrawl1']),
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
('IntroFS',                0,  2,  2,  2, 1,  1, 0, ['adcrawl1']),
('WelcomeFS',              0,  3,  3,  3, 1,  2, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  3, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 12, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('HourlyForecastTodayFS',  0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TonightFS',              0, 10, 10,  9, 1, 70, 0, ['adcrawl1']),
('HourlyForecastTonightFS',0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TomorrowFS',             0, 10, 90,  8, 1, 72, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 12, 10, 1, 50, 0, ['adcrawl1']),
('SummaryFS',              0,  4,  6,  4, 1, 60, 0, ['adcrawl1']),
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
('Null',                   0,  2,  2,  2, 1,  1, 0, ['adcrawl1']),
('WelcomeAMHQ',            0,  3,  3,  3, 1,  2, 0, ['adcrawl1']),
('SevereAlertFS',          0,  8,  8,  6, 1,  3, 0, ['adcrawl1']),
('NowFS',                  0,  8, 90,  6, 1, 10, 0, ['adcrawl1']),
('RegionalRadarFS',        0,  8,  8,  8, 4, 20, 0, ['adcrawl1']),
('MetroRadarFS',           0, 12, 12,  8, 4, 30, 0, ['adcrawl1']),
('TodayFS',                0, 10, 90,  8, 1, 40, 0, ['adcrawl1']),
('HourlyForecastTodayFS',  0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TonightFS',              0, 10, 10,  9, 1, 70, 0, ['adcrawl1']),
('HourlyForecastTonightFS',0, 10, 12, 10, 1, 80, 1, ['adcrawl1']),
('TomorrowFS',             0, 10, 90,  8, 1, 72, 0, ['adcrawl1']),
('7DayForecastFS',         0, 12, 12, 10, 1, 50, 0, ['adcrawl1']),
('SummaryFS',              0,  4,  6,  4, 1, 60, 0, ['adcrawl1']),
]
dsm.set('Config.1.Playlist.DefaultUS.65.2', d, 0)
ds.commit()
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Thu Jul 24 15:47:12 GMT 2014
