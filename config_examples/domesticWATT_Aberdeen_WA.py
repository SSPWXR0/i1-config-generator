# Created on Fri Oct 17 14:50:26 GMT 2014
Log.info('scmt config started')
# EXP: 1072
# VIW: 12884
# CLN: 15893
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
# MAP: 73310
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3942,16164),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(125,85),
             datacutType='radar.us',
             datacutCoordinate=(84,1643),
             datacutSize=(177,100),
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
              ( ( (152,64),),
                ( (156,31),),
                ( (158,98),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (152,64),),
                ( (156,31),),
                ( (158,98),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (86,69),'Aberdeen',),
                ( (78,36),'South Bend',),
                ( (81,103),'Humptulips',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (86,69),'Aberdeen',),
                ( (78,36),'South Bend',),
                ( (81,103),'Humptulips',),
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
# MAP: 120831
# Local_SummaryFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4290,16296),
             mapcutSize=(1440,554),
             mapFinalSize=(338,130),
             mapMilesSize=(125,57),
             datacutType='radar.us',
             datacutCoordinate=(127,1659),
             datacutSize=(176,68),
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
              ( ( (135,62),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (90,83),'Aberdeen',),
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
# MAP: 80951
# LFLocal_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4030,16235),
             mapcutSize=(1576,677),
             mapFinalSize=(398,171),
             mapMilesSize=(125,70),
             datacutType='radar.us',
             datacutCoordinate=(95,1651),
             datacutSize=(193,83),
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
              ( ( (211,84),),
                ( (219,34),),
                ( (248,138),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (211,84),),
                ( (219,34),),
                ( (248,138),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (145,89),'Aberdeen',),
                ( (141,39),'South Bend',),
                ( (171,143),'Humptulips',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (145,89),'Aberdeen',),
                ( (141,39),'South Bend',),
                ( (171,143),'Humptulips',),
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
# MAP: 50442
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4172,16104),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(125,100),
             datacutType='radar.us',
             datacutCoordinate=(112,1635),
             datacutSize=(177,118),
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
              ( ( (574,190),'5',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (513,177),'12',),
                ( (325,276),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (513,177),'12',),
                ( (325,276),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (574,190),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (348,234),),
                ( (585,149),),
                ( (246,315),),
                ( (417,246),),
                ( (331,83),),
                ( (512,259),),
                ( (358,135),),
                ( (546,312),),
                ( (310,329),),
                ( (274,205),),
                ( (605,259),),
                ( (334,233),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (348,234),),
                ( (585,149),),
                ( (246,315),),
                ( (417,246),),
                ( (331,83),),
                ( (512,259),),
                ( (358,135),),
                ( (546,312),),
                ( (310,329),),
                ( (274,205),),
                ( (605,259),),
                ( (334,233),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (365,220),'Aberdeen',),
                ( (547,132),'Centralia',),
                ( (107,318),'Pacific Beach',),
                ( (370,267),'Montesano',),
                ( (351,86),'Nemah',),
                ( (473,242),'McCleary',),
                ( (378,138),'South Bend',),
                ( (516,333),'Shelton',),
                ( (330,332),'Humptulips',),
                ( (178,208),'Westport',),
                ( (572,280),'Olympia',),
                ( (244,251),'Hoquiam',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (365,220),'Aberdeen',),
                ( (547,132),'Centralia',),
                ( (107,318),'Pacific Beach',),
                ( (370,267),'Montesano',),
                ( (351,86),'Nemah',),
                ( (473,242),'McCleary',),
                ( (378,138),'South Bend',),
                ( (516,333),'Shelton',),
                ( (330,332),'Humptulips',),
                ( (178,208),'Westport',),
                ( (572,280),'Olympia',),
                ( (244,251),'Hoquiam',),
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
# MAP: 116180
# Local_MetroRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4225,16316),
             mapcutSize=(1440,537),
             mapFinalSize=(620,231),
             mapMilesSize=(125,55),
             datacutType='radar.us',
             datacutCoordinate=(119,1661),
             datacutSize=(176,66),
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
              ( ( (479,100),'5',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (408,75),'12',),
                ( (257,149),'101',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (275,110),),
                ( (480,36),),
                ( (205,110),),
                ( (302,28),),
                ( (447,177),),
                ( (212,188),),
                ( (212,84),),
                ( (497,131),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (290,94),'Aberdeen',),
                ( (446,53),'Centralia',),
                ( (73,124),'Ocean Shores',),
                ( (321,35),'Raymond',),
                ( (472,175),'Shelton',),
                ( (231,187),'Humptulips',),
                ( (126,64),'Westport',),
                ( (407,127),'Olympia',),
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
# MAP: 75218
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4364,16107),
             mapcutSize=(1512,1008),
             mapFinalSize=(720,480),
             mapMilesSize=(131,105),
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
              ( ( (382,172),'12',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (545,372),'16',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (213,278),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (454,176),'5',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72791028',(276,113),),
                ( 'T72791037',(139,156),),
                ( 'T72791049',(121,252),),
                ( 'T72792000',(516,210),),
                ( 'T72792008',(464,117),),
                ( 'T72792012',(375,253),),
                ( 'T72792014',(416,346),),
                ( 'T72792040',(255,211),),
                ( 'T72797013',(113,343),),
                ( 'T72797014',(252,338),),
                ( 'T74206006',(566,315),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72791028',(279,77),),
                ( 'T72791037',(142,120),),
                ( 'T72791049',(124,216),),
                ( 'T72792000',(519,174),),
                ( 'T72792008',(467,81),),
                ( 'T72792012',(378,217),),
                ( 'T72792014',(419,310),),
                ( 'T72792040',(258,175),),
                ( 'T72797013',(116,307),),
                ( 'T72797014',(255,302),),
                ( 'T74206006',(569,279),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (218,149),'South Bend',),
                ( (94,192),'Westport',),
                ( (51,288),'Ocean Shores',),
                ( (478,246),'Olympia',),
                ( (420,153),'Centralia',),
                ( (331,289),'McCleary',),
                ( (380,382),'Shelton',),
                ( (209,247),'Aberdeen',),
                ( (76,379),'Taholah',),
                ( (211,374),'Quinault',),
                ( (530,351),'Tacoma',),
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
# MAP: 71490
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4364,16107),
             mapcutSize=(1512,1008),
             mapFinalSize=(720,480),
             mapMilesSize=(131,105),
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
              ( ( (382,172),'12',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (545,372),'16',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (213,278),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (454,176),'5',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72791028',(279,77),),
                ( '72791037',(142,120),),
                ( '72791049',(124,216),),
                ( '72792000',(519,174),),
                ( '72792008',(467,81),),
                ( '72792012',(378,217),),
                ( '72792014',(419,310),),
                ( '72792040',(258,175),),
                ( '72797013',(116,307),),
                ( '72797014',(255,302),),
                ( '74206006',(569,279),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72791028',(276,113),),
                ( '72791037',(139,156),),
                ( '72791049',(121,252),),
                ( '72792000',(516,210),),
                ( '72792008',(464,117),),
                ( '72792012',(375,253),),
                ( '72792014',(416,346),),
                ( '72792040',(255,211),),
                ( '72797013',(113,343),),
                ( '72797014',(252,338),),
                ( '74206006',(566,315),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (218,149),'South Bend',),
                ( (94,192),'Westport',),
                ( (51,288),'Ocean Shores',),
                ( (478,246),'Olympia',),
                ( (420,153),'Centralia',),
                ( (331,289),'McCleary',),
                ( (380,382),'Shelton',),
                ( (209,247),'Aberdeen',),
                ( (76,379),'Taholah',),
                ( (211,374),'Quinault',),
                ( (530,351),'Tacoma',),
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
# MAP: 48598
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3053,14740),
             mapcutSize=(6192,4128),
             mapFinalSize=(720,480),
             mapMilesSize=(534,428),
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
              ( ( '72698000',(296,77),),
                ( '72781000',(418,120),),
                ( '72784036',(468,195),),
                ( '72785000',(578,236),),
                ( '72789001',(440,300),),
                ( '72791000',(162,111),),
                ( '72793000',(295,197),),
                ( '72797000',(153,245),),
                ( '74201073',(290,305),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72698000',(293,113),),
                ( '72781000',(415,156),),
                ( '72784036',(465,231),),
                ( '72785000',(575,272),),
                ( '72789001',(437,336),),
                ( '72791000',(159,147),),
                ( '72793000',(292,233),),
                ( '72797000',(150,281),),
                ( '74201073',(287,341),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (252,149),'Portland',),
                ( (381,192),'Yakima',),
                ( (428,267),'Ephrata',),
                ( (535,308),'Spokane',),
                ( (413,372),'Omak',),
                ( (124,183),'Astoria',),
                ( (258,269),'Seattle',),
                ( (99,317),'Quillayute',),
                ( (232,377),'Bellingham',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 47878
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3053,14740),
             mapcutSize=(6192,4128),
             mapFinalSize=(720,480),
             mapMilesSize=(534,428),
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
              ( ( 'T72698000',(293,113),),
                ( 'T72781000',(415,156),),
                ( 'T72784036',(465,231),),
                ( 'T72785000',(575,272),),
                ( 'T72789001',(437,336),),
                ( 'T72791000',(159,147),),
                ( 'T72793000',(292,233),),
                ( 'T72797000',(150,281),),
                ( 'T74201073',(287,341),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72698000',(296,77),),
                ( 'T72781000',(418,120),),
                ( 'T72784036',(468,195),),
                ( 'T72785000',(578,236),),
                ( 'T72789001',(440,300),),
                ( 'T72791000',(162,111),),
                ( 'T72793000',(295,197),),
                ( 'T72797000',(153,245),),
                ( 'T74201073',(290,305),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (252,149),'Portland',),
                ( (381,192),'Yakima',),
                ( (428,267),'Ephrata',),
                ( (535,308),'Spokane',),
                ( (413,372),'Omak',),
                ( (124,183),'Astoria',),
                ( (258,269),'Seattle',),
                ( (99,317),'Quillayute',),
                ( (232,377),'Bellingham',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 366
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(861,1634),
             mapcutSize=(2979,1986),
             mapFinalSize=(720,480),
             mapMilesSize=(2663,1796),
             datacutType='satellite.us',
             datacutCoordinate=(210,491),
             datacutSize=(800,534),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Local_Satellite', d, 0)
#
# Local_Satellite (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDot',0,2,0,),
              ( ( (438,273),),
                ( (425,212),),
                ( (439,245),),
                ( (439,245),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (455,291),'Vancouver',),
                ( (442,198),'Portland',),
                ( (459,248),'Seattle',),
                ( (459,248),'Seattle',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_Satellite', d, 0)
# MAP: 118355
# Local_RegionalRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3532,15891),
             mapcutSize=(3960,1475),
             mapFinalSize=(620,231),
             mapMilesSize=(343,153),
             datacutType='radar.us',
             datacutCoordinate=(34,1609),
             datacutSize=(485,181),
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
              ( ( (301,26),'5',),
                ( (384,151),'90',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (243,94),'12',),
                ( (455,181),'2',),
                ( (263,152),'101',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (206,101),),
                ( (278,74),),
                ( (486,106),),
                ( (188,40),),
                ( (321,130),),
                ( (488,64),),
                ( (284,108),),
                ( (330,168),),
                ( (142,194),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (101,103),'Aberdeen',),
                ( (245,50),'Centralia',),
                ( (452,131),'Ellensburg',),
                ( (74,35),'Long Beach',),
                ( (243,136),'Tacoma',),
                ( (460,47),'Yakima',),
                ( (300,94),'Olympia',),
                ( (350,176),'Seattle',),
                ( (162,188),'Quillayute',),
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
# MAP: 50441
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3388,15307),
             mapcutSize=(3960,2640),
             mapFinalSize=(720,480),
             mapMilesSize=(343,275),
             datacutType='radar.us',
             datacutCoordinate=(16,1537),
             datacutSize=(485,324),
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
              ( ( (473,279),'90',),
                ( (354,155),'5',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (308,212),'12',),
                ( (555,313),'2',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (332,279),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (308,212),'12',),
                ( (555,313),'2',),
                ( (332,279),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (473,279),'90',),
                ( (354,155),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (267,225),),
                ( (350,194),),
                ( (351,126),),
                ( (400,258),),
                ( (265,130),),
                ( (357,233),),
                ( (411,303),),
                ( (193,334),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (267,225),),
                ( (350,194),),
                ( (351,126),),
                ( (400,258),),
                ( (265,130),),
                ( (357,233),),
                ( (411,303),),
                ( (193,334),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (228,246),'Aberdeen',),
                ( (370,197),'Centralia',),
                ( (371,129),'Longview',),
                ( (420,261),'Tacoma',),
                ( (235,113),'Astoria',),
                ( (377,236),'Olympia',),
                ( (428,321),'Seattle',),
                ( (213,337),'Quillayute',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (228,246),'Aberdeen',),
                ( (370,197),'Centralia',),
                ( (371,129),'Longview',),
                ( (420,261),'Tacoma',),
                ( (235,113),'Astoria',),
                ( (377,236),'Olympia',),
                ( (428,321),'Seattle',),
                ( (213,337),'Quillayute',),
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
wxdata.setInterestList('lambert.us','1',['satellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('satellite.us.cuts','1',['Config.1.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler','Config.1.Local_SummaryFS','Config.1.LFLocal_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_MetroRadarFS','Config.1.Local_RegionalRadarFS','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['GEG','PDX','SEA',])
wxdata.setInterestList('coopId','1',['71777005','72698000','72698106','72781000','72784036','72785000','72789001','72791000','72791028','72791037','72791049','72792000','72792008','72792012','72792014','72792022','72792034','72792040','72793000','72797000','72797013','72797014','74201073','74206006',])
wxdata.setInterestList('indexId','1',['KHQM',])
wxdata.setInterestList('obsStation','1',['KHQM','T72698000','T72781000','T72784036','T72785000','T72789001','T72791000','T72791028','T72791037','T72791049','T72792000','T72792008','T72792012','T72792014','T72792022','T72792034','T72792040','T72793000','T72797000','T72797013','T72797014','T74201073','T74206006',])
wxdata.setInterestList('climId','1',['450008',])
wxdata.setInterestList('zone','1',['WAZ517',])
wxdata.setInterestList('skiId','1',['503006','604038',])
wxdata.setInterestList('county','1',['WAC027','WAC031','WAC049','WAC045',])
dsm.set('Config.1.countyNameList',[('WAC027','Grays Harbor'),('WAC031','Jefferson'),('WAC049','Pacific'),('WAC045','Mason'),], 0)
#
dsm.set('dmaCode','819', 0)
dsm.set('secondaryObsStation','KHQM', 0)
dsm.set('primaryClimoStation','450008', 0)
dsm.set('primaryIndexId','KHQM', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','WA', 0)
dsm.set('expRev','7036808', 0)
dsm.set('primaryCoopId','72792034', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','HQM', 0)
dsm.set('primaryCounty','WAC027', 0)
dsm.set('primaryObsStation','T72792034', 0)
dsm.set('primaryRad',15, 0)
dsm.set('primaryLat',46.97167, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('secondaryRad',30, 0)
dsm.set('primaryLon',-123.82278, 0)
dsm.set('primaryZone','WAZ517', 0)
dsm.set('climoRegion','7', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','022286', 0)
dsm.set('msoName','Unknown', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - ABERDEEN/WESTPORT - DOM', 0)
dsm.set('affiliateNumber','32654', 0)
dsm.set('zipCode','98520', 0)
dsm.set('Config.1.irdAddress','0000315595270090', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD09050142', 0)
dsm.set('Config.1.bcDialInNumber','3606123064', 0)
dsm.set('Config.1.bcExtIpAddress','50.132.21.141', 0)
dsm.set('Config.1.bcGateWay','192.168.1.1', 0)
dsm.set('Config.1.bcIpAddress','192.168.1.101', 0)
#
wxdata.setTimeZone('PST8PDT')
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
d.airportId = ['SEA','PDX','GEG',]
d.airportLocName = ['Seattle-Tacoma','Portland','Spokane',]
d.obsStation = ['T72793000','T72698000','T72785000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['604038','503006',]
d.coopId = ['71777005','72698106',]
d.resortName = ['Whistler, ','Mt Hood Mdws, OR',]
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
d.serialNum=1066964
d.crawls=[
(1237276800,1259654399,[(0,23)],'ATTN BASIC CABLE CUSTOMERS: We at Comcast are enhancing our network. You will need new digital equipment to keep channels above 29. To avoid any service interruptions call 1-800-COMCAST and ask about how to receive digital equipment at no additional charge. Restrictions apply.'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.NationalLdl_Today.2')
scmtRemove('Config.1.NationalLdl_Today.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_Today.1')
scmtRemove('Config.1.Local_SevereAlertFS.0')
scmtRemove('Config.1.NationalLdl_Today.4')
scmtRemove('Config.1.NationalLdl_TrafficFlow.1')
scmtRemove('Config.1.Local_TodayFS.0')
scmtRemove('Config.1.NationalLdl_Today.3')
scmtRemove('Config.1.Local_NowFS.0')
scmtRemove('Config.1.NationalLdl_TrafficFlow.0')
scmtRemove('Config.1.NationalLdl_Today.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.Local_TomorrowNightFS.0')
scmtRemove('Config.1.NationalLdl_TrafficIncidents.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.Local_IntroFS.0')
scmtRemove('Config.1.NationalLdl_TrafficFlow.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.coopId = ['72792034',]
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
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
d.zone = ['WAZ517',]
dsm.set('Config.1.Local_SevereAlertFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_SevereAlertLDL.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlert.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlertLF.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.coopId = ['72792034',]
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
d.locName = ['McCleary',]
d.coopId = ['72792012',]
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
d.obsStation = ['T72792012',]
d.locName = ['McCleary',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
d.coopId = ['72792034',]
dsm.set('Config.1.Local_SummaryFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72792034',]
d.climId = '450008'
d.latitude  = 46.97
d.longitude = -123.82
d.locName = ['Aberdeen',]
dsm.set('Config.1.Local_NowFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_WelcomeAMHQ.0', d, 0, 1)
dsm.set('Config.1.Local_WelcomeFS.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.keyRoutes = ['','',]
d.coopId = ['72792034',]
dsm.set('Config.1.NationalLdl_TrafficFlow.2', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Montesano',]
d.coopId = ['72792022',]
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
d.obsStation = ['T72792022',]
d.locName = ['Montesano',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.keyRoutes = ['','',]
d.coopId = ['72792034',]
dsm.set('Config.1.NationalLdl_TrafficFlow.1', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.coopId = ['72792034',]
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
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
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
d.locName = ['Aberdeen',]
d.keyRoutes = ['','',]
d.coopId = ['72792034',]
dsm.set('Config.1.NationalLdl_TrafficFlow.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
dsm.set('Config.1.Local_RegionalRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Aberdeen',]
dsm.set('Config.1.NationalLdl_TrafficIncidents.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
dsm.set('Config.1.Local_MetroRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72792034',]
d.locName = ['Aberdeen',]
dsm.set('Config.1.Local_IntroFS.0', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_RadarSatelliteComposite = 0
d.activeLocal_Satellite = 1
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
# Finished generation on Fri Oct 17 14:50:27 GMT 2014
