# Created on Fri Oct 17 14:51:51 GMT 2014
Log.info('scmt config started')
# EXP: 1237
# VIW: 13057
# CLN: 1288
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
# MAP: 121299
# Local_SummaryFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4665,15013),
             mapcutSize=(1440,554),
             mapFinalSize=(338,130),
             mapMilesSize=(129,59),
             datacutType='radar.us',
             datacutCoordinate=(173,1502),
             datacutSize=(176,67),
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
              ( ( (142,50),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (70,51),'Salem',),
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
# MAP: 73883
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4314,14874),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(129,88),
             datacutType='radar.us',
             datacutCoordinate=(130,1484),
             datacutSize=(176,101),
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
              ( ( (183,43),),
                ( (179,80),),
                ( (159,58),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (183,43),),
                ( (179,80),),
                ( (159,58),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (154,32),'Stayton',),
                ( (112,85),'Woodburn',),
                ( (117,63),'Salem',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (154,32),'Stayton',),
                ( (112,85),'Woodburn',),
                ( (117,63),'Salem',),
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
# MAP: 81065
# LFLocal_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4482,14979),
             mapcutSize=(1417,609),
             mapFinalSize=(398,171),
             mapMilesSize=(116,65),
             datacutType='radar.us',
             datacutCoordinate=(150,1497),
             datacutSize=(174,75),
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
              ( ( (265,48),),
                ( (257,110),),
                ( (222,70),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (265,48),),
                ( (257,110),),
                ( (222,70),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (236,37),'Stayton',),
                ( (190,115),'Woodburn',),
                ( (180,75),'Salem',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (236,37),'Stayton',),
                ( (190,115),'Woodburn',),
                ( (180,75),'Salem',),
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
# MAP: 116570
# Local_MetroRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4659,15052),
             mapcutSize=(1296,483),
             mapFinalSize=(620,231),
             mapMilesSize=(116,52),
             datacutType='radar.us',
             datacutCoordinate=(172,1506),
             datacutSize=(159,59),
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
              ( ( (321,42),'5',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (75,165),'101',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (236,87),),
                ( (268,175),),
                ( (426,157),),
                ( (374,113),),
                ( (370,50),),
                ( (194,138),),
                ( (354,156),),
                ( (308,101),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (214,60),'Dallas',),
                ( (144,180),'McMinnville',),
                ( (446,161),'Molalla',),
                ( (394,109),'Silverton',),
                ( (391,51),'Stayton',),
                ( (90,124),'Willamina',),
                ( (312,178),'Woodburn',),
                ( (281,119),'Salem',),
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
# MAP: 50759
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4613,14861),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(116,93),
             datacutType='radar.us',
             datacutCoordinate=(166,1483),
             datacutSize=(159,106),
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
              ( ( (371,132),'5',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (192,94),'20',),
                ( (113,295),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (192,94),'20',),
                ( (113,295),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (371,132),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (388,193),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (367,98),),
                ( (333,278),),
                ( (300,208),),
                ( (388,238),),
                ( (338,312),),
                ( (522,290),),
                ( (326,183),),
                ( (461,239),),
                ( (456,166),),
                ( (438,289),),
                ( (381,221),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (367,98),),
                ( (333,278),),
                ( (300,208),),
                ( (388,238),),
                ( (338,312),),
                ( (522,290),),
                ( (326,183),),
                ( (461,239),),
                ( (456,166),),
                ( (438,289),),
                ( (381,221),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (388,193),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (293,101),'Albany',),
                ( (267,281),'Amity',),
                ( (234,211),'Dallas',),
                ( (322,249),'Keizer',),
                ( (219,326),'McMinnville',),
                ( (542,293),'Molalla',),
                ( (219,177),'Monmouth',),
                ( (481,242),'Silverton',),
                ( (476,169),'Stayton',),
                ( (396,310),'Woodburn',),
                ( (400,220),'Salem',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (293,101),'Albany',),
                ( (267,281),'Amity',),
                ( (234,211),'Dallas',),
                ( (322,249),'Keizer',),
                ( (219,326),'McMinnville',),
                ( (542,293),'Molalla',),
                ( (219,177),'Monmouth',),
                ( (481,242),'Silverton',),
                ( (476,169),'Stayton',),
                ( (396,310),'Woodburn',),
                ( (400,220),'Salem',),
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
# MAP: 74991
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4595,14836),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(116,93),
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
              ( ( (224,102),'20',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (130,319),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (462,342),'5',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72693057',(111,114),),
                ( 'T72694000',(393,195),),
                ( 'T72694010',(519,164),),
                ( 'T72694015',(480,259),),
                ( 'T72694016',(280,263),),
                ( 'T72694023',(343,113),),
                ( 'T72694027',(342,334),),
                ( 'T72694044',(565,312),),
                ( 'T72694059',(125,230),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72693057',(114,78),),
                ( 'T72694000',(396,159),),
                ( 'T72694010',(522,128),),
                ( 'T72694015',(483,223),),
                ( 'T72694016',(283,227),),
                ( 'T72694023',(346,77),),
                ( 'T72694027',(345,298),),
                ( 'T72694044',(568,276),),
                ( 'T72694059',(128,194),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (71,150),'Newport',),
                ( (366,231),'Salem',),
                ( (481,200),'Stayton',),
                ( (435,295),'Silverton',),
                ( (253,299),'Dallas',),
                ( (311,149),'Albany',),
                ( (282,370),'McMinnville',),
                ( (533,348),'Molalla',),
                ( (64,266),'Lincoln City',),
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
# MAP: 71692
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4595,14836),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(116,93),
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
              ( ( (224,102),'20',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (130,319),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (462,342),'5',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72693057',(114,78),),
                ( '72694000',(396,159),),
                ( '72694010',(522,128),),
                ( '72694015',(483,223),),
                ( '72694016',(283,227),),
                ( '72694023',(346,77),),
                ( '72694027',(345,298),),
                ( '72694044',(568,276),),
                ( '72694059',(128,194),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72693057',(111,114),),
                ( '72694000',(393,195),),
                ( '72694010',(519,164),),
                ( '72694015',(480,259),),
                ( '72694016',(280,263),),
                ( '72694023',(343,113),),
                ( '72694027',(342,334),),
                ( '72694044',(565,312),),
                ( '72694059',(125,230),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (71,150),'Newport',),
                ( (366,231),'Salem',),
                ( (481,200),'Stayton',),
                ( (435,295),'Silverton',),
                ( (253,299),'Dallas',),
                ( (311,149),'Albany',),
                ( (282,370),'McMinnville',),
                ( (533,348),'Molalla',),
                ( (64,266),'Lincoln City',),
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
# MAP: 48097
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3750,13502),
             mapcutSize=(6192,4128),
             mapFinalSize=(720,480),
             mapMilesSize=(553,443),
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
              ( ( '72681000',(594,117),),
                ( '72683000',(433,79),),
                ( '72688000',(460,198),),
                ( '72693010',(174,87),),
                ( '72694093',(294,103),),
                ( '72698000',(244,198),),
                ( '72781000',(344,288),),
                ( '72783000',(572,279),),
                ( '72791000',(112,240),),
                ( '72793000',(210,330),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72681000',(591,153),),
                ( '72683000',(430,115),),
                ( '72688000',(457,234),),
                ( '72693010',(171,123),),
                ( '72694093',(291,139),),
                ( '72698000',(241,234),),
                ( '72781000',(341,324),),
                ( '72783000',(569,315),),
                ( '72791000',(109,276),),
                ( '72793000',(208,339),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (567,189),'Boise',),
                ( (404,151),'Burns',),
                ( (408,270),'Pendleton',),
                ( (137,159),'Eugene',),
                ( (247,175),'Redmond',),
                ( (200,270),'Portland',),
                ( (307,360),'Yakima',),
                ( (525,351),'Lewiston',),
                ( (74,312),'Astoria',),
                ( (124,375),'Seattle',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 50661
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3750,13502),
             mapcutSize=(6192,4128),
             mapFinalSize=(720,480),
             mapMilesSize=(553,443),
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
              ( ( 'T72681000',(591,153),),
                ( 'T72683000',(430,115),),
                ( 'T72688000',(457,234),),
                ( 'T72693010',(171,123),),
                ( 'T72694093',(291,139),),
                ( 'T72698000',(241,234),),
                ( 'T72781000',(341,324),),
                ( 'T72783000',(569,315),),
                ( 'T72791000',(109,276),),
                ( 'T72793010',(208,339),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72681000',(594,117),),
                ( 'T72683000',(433,79),),
                ( 'T72688000',(460,198),),
                ( 'T72693010',(174,87),),
                ( 'T72694093',(294,103),),
                ( 'T72698000',(244,198),),
                ( 'T72781000',(344,288),),
                ( 'T72783000',(572,279),),
                ( 'T72791000',(112,240),),
                ( 'T72793010',(210,330),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (567,189),'Boise',),
                ( (404,151),'Burns',),
                ( (408,270),'Pendleton',),
                ( (137,159),'Eugene',),
                ( (247,175),'Redmond',),
                ( (200,270),'Portland',),
                ( (307,360),'Yakima',),
                ( (525,351),'Lewiston',),
                ( (74,312),'Astoria',),
                ( (124,375),'Seattle',),
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
# MAP: 118740
# Local_RegionalRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3657,14649),
             mapcutSize=(3456,1288),
             mapFinalSize=(620,231),
             mapMilesSize=(311,139),
             datacutType='radar.us',
             datacutCoordinate=(49,1457),
             datacutSize=(424,158),
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
              ( ( (396,184),'84',),
                ( (299,128),'5',),
              ),
             ),
             (
               (('usHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (338,35),'20',),
                ( (196,121),'101',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (288,68),),
                ( (483,132),),
                ( (212,161),),
                ( (291,105),),
                ( (327,173),),
                ( (473,172),),
                ( (470,28),),
                ( (195,69),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (254,42),'Albany',),
                ( (455,109),'Maupin',),
                ( (110,165),'Tillamook',),
                ( (311,102),'Salem',),
                ( (289,153),'Portland',),
                ( (448,190),'The Dalles',),
                ( (448,48),'Redmond',),
                ( (106,73),'Newport',),
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
# MAP: 50130
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3533,14141),
             mapcutSize=(3456,2304),
             mapFinalSize=(720,480),
             mapMilesSize=(311,249),
             datacutType='radar.us',
             datacutCoordinate=(34,1395),
             datacutSize=(423,282),
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
              ( ( (485,316),'84',),
                ( (377,246),'5',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (418,143),'20',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (253,243),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (418,143),'20',),
                ( (253,243),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (485,316),'84',),
                ( (377,246),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (249,109),),
                ( (523,289),),
                ( (272,293),),
                ( (364,228),),
                ( (405,307),),
                ( (575,307),),
                ( (352,112),),
                ( (572,139),),
                ( (251,186),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (249,109),),
                ( (523,289),),
                ( (272,293),),
                ( (364,228),),
                ( (405,307),),
                ( (575,307),),
                ( (352,112),),
                ( (572,139),),
                ( (251,186),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (160,112),'Florence',),
                ( (470,272),'Mount Hood',),
                ( (170,296),'Tillamook',),
                ( (298,231),'Salem',),
                ( (370,290),'Portland',),
                ( (531,328),'The Dalles',),
                ( (324,133),'Eugene',),
                ( (475,142),'Redmond',),
                ( (162,189),'Newport',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (160,112),'Florence',),
                ( (470,272),'Mount Hood',),
                ( (170,296),'Tillamook',),
                ( (298,231),'Salem',),
                ( (370,290),'Portland',),
                ( (531,328),'The Dalles',),
                ( (324,133),'Eugene',),
                ( (475,142),'Redmond',),
                ( (162,189),'Newport',),
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
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Local_SummaryFS','Config.1.Radar_LocalDoppler','Config.1.LFLocal_LocalDoppler','Config.1.Local_MetroRadarFS','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalRadarFS','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['GEG','PDX','SEA',])
wxdata.setInterestList('coopId','1',['72681000','72683000','72688000','72693010','72693057','72693095','72694000','72694004','72694010','72694015','72694016','72694023','72694027','72694044','72694059','72694093','72698000','72698106','72781000','72783000','72791000','72793000',])
wxdata.setInterestList('pollenId','1',['SLE',])
wxdata.setInterestList('indexId','1',['KSLE',])
wxdata.setInterestList('obsStation','1',['KSLE','T72681000','T72683000','T72688000','T72693010','T72693057','T72694000','T72694004','T72694010','T72694015','T72694016','T72694023','T72694027','T72694044','T72694059','T72694093','T72698000','T72781000','T72783000','T72785000','T72791000','T72793000','T72793010',])
wxdata.setInterestList('climId','1',['357500',])
wxdata.setInterestList('zone','1',['ORZ007',])
wxdata.setInterestList('skiId','1',['503004','503006',])
wxdata.setInterestList('county','1',['ORC047','ORC053','ORC071',])
dsm.set('Config.1.countyNameList',[('ORC047','Marion'),('ORC053','Polk'),('ORC071','Yamhill'),], 0)
#
dsm.set('dmaCode','820', 0)
dsm.set('secondaryObsStation','KSLE', 0)
dsm.set('primaryClimoStation','357500', 0)
dsm.set('primaryIndexId','KSLE', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','OR', 0)
dsm.set('primPollenSiteName','Portland', 0)
dsm.set('expRev','7037019', 0)
dsm.set('primaryCoopId','72694000', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','SLE', 0)
dsm.set('primaryCounty','ORC047', 0)
dsm.set('primaryObsStation','T72694000', 0)
dsm.set('primaryRad',15, 0)
dsm.set('primaryLat',44.985, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','SLE', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('secondaryRad',30, 0)
dsm.set('primaryLon',-123.14139, 0)
dsm.set('primaryZone','ORZ007', 0)
dsm.set('climoRegion','7', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','022450', 0)
dsm.set('msoName','Unknown', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - SALEM - DOM', 0)
dsm.set('affiliateNumber','01135', 0)
dsm.set('zipCode','97060', 0)
dsm.set('Config.1.irdAddress','0000315596070092', 0)
dsm.set('Config.1.bcNetMask','255.255.254.0', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD03040121', 0)
dsm.set('Config.1.bcExtIpAddress','172.20.2.232', 0)
dsm.set('Config.1.bcGateWay','10.179.103.254', 0)
dsm.set('Config.1.bcIpAddress','10.179.103.112', 0)
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
d.airportId = ['PDX','SEA','GEG',]
d.airportLocName = ['Portland','Seattle-Tacoma','Spokane',]
d.obsStation = ['T72698000','T72793000','T72785000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['503004','503006',]
d.coopId = ['72693095','72698106',]
d.resortName = ['Mt Bachelor, OR','Mt Hood Mdws, OR',]
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
#
scmtRemove('Config.1.NationalLdl_TrafficFlow.2')
scmtRemove('Config.1.NationalLdl_Today.3')
scmtRemove('Config.1.Local_SevereAlertFS.0')
scmtRemove('Config.1.Local_IntroFS.0')
scmtRemove('Config.1.NationalLdl_TrafficIncidents.0')
scmtRemove('Config.1.NationalLdl_Today.4')
scmtRemove('Config.1.NationalLdl_Today.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_Today.1')
scmtRemove('Config.1.NationalLdl_TrafficFlow.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.NationalLdl_Today.5')
scmtRemove('Config.1.Local_TomorrowNightFS.0')
scmtRemove('Config.1.NationalLdl_Today.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.Local_TodayFS.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.Local_NowFS.0')
scmtRemove('Config.1.NationalLdl_TrafficFlow.1')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
#
d = twc.Data()
d.locName = ['Salem',]
d.coopId = ['72694000',]
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
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
d.zone = ['ORZ007',]
dsm.set('Config.1.Local_SevereAlertFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_SevereAlertLDL.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlert.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlertLF.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Salem',]
d.coopId = ['72694000',]
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
d.locName = ['Albany',]
d.coopId = ['72694023',]
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
d.obsStation = ['T72694023',]
d.locName = ['Albany',]
dsm.set('Config.1.NationalLdl_CurrentConditions.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.3', d, 0, 1)
#
d = twc.Data()
d.locName = ['Keizer',]
d.coopId = ['72694004',]
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
d.obsStation = ['T72694004',]
d.locName = ['Keizer',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
d.coopId = ['72694000',]
dsm.set('Config.1.Local_SummaryFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72694000',]
d.climId = '357500'
d.latitude  = 44.92
d.longitude = -123.02
d.locName = ['Salem',]
dsm.set('Config.1.Local_NowFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_WelcomeAMHQ.0', d, 0, 1)
dsm.set('Config.1.Local_WelcomeFS.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Salem',]
d.keyRoutes = ['','',]
d.coopId = ['72694000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.2', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['McMinnville',]
d.coopId = ['72694027',]
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
d.obsStation = ['T72694027',]
d.locName = ['McMinnville',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Salem',]
d.keyRoutes = ['','',]
d.coopId = ['72694000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.1', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Salem',]
d.coopId = ['72694000',]
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
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
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
d.locName = ['Salem',]
d.keyRoutes = ['','',]
d.coopId = ['72694000',]
dsm.set('Config.1.NationalLdl_TrafficFlow.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
dsm.set('Config.1.Local_RegionalRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Salem',]
dsm.set('Config.1.NationalLdl_TrafficIncidents.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
dsm.set('Config.1.Local_MetroRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72694000',]
d.locName = ['Salem',]
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
# Finished generation on Fri Oct 17 14:51:52 GMT 2014
