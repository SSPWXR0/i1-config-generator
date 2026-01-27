# Created on Fri Oct 17 14:51:41 GMT 2014
Log.info('scmt config started')
# EXP: 1207
# VIW: 12917
# CLN: 17793
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
# MAP: 81045
# LFLocal_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27935,4441),
             mapcutSize=(1180,507),
             mapFinalSize=(398,171),
             mapMilesSize=(135,69),
             datacutType='radar.us',
             datacutCoordinate=(3023,206),
             datacutSize=(144,63),
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
              ( ( (203,87),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (203,87),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (135,78),'Ft. Lauderdale',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (135,78),'Ft. Lauderdale',),
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
# MAP: 73829
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27869,4388),
             mapcutSize=(1080,617),
             mapFinalSize=(240,137),
             mapMilesSize=(123,84),
             datacutType='radar.us',
             datacutCoordinate=(3014,200),
             datacutSize=(133,75),
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
              ( ( (143,29),),
                ( (159,103),),
                ( (149,67),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (143,29),),
                ( (159,103),),
                ( (149,67),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (112,21),'Miami',),
                ( (86,96),'Delray Beach',),
                ( (81,58),'Ft. Lauderdale',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (112,21),'Miami',),
                ( (86,96),'Delray Beach',),
                ( (81,58),'Ft. Lauderdale',),
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
# MAP: 121227
# Local_SummaryFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(28131,4489),
             mapcutSize=(1080,415),
             mapFinalSize=(338,130),
             mapMilesSize=(123,57),
             datacutType='radar.us',
             datacutCoordinate=(3047,212),
             datacutSize=(132,51),
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
              ( ( (127,65),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (153,54),'Ft. Lauderdale',),
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
# MAP: 51160
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(28040,4343),
             mapcutSize=(1080,720),
             mapFinalSize=(720,480),
             mapMilesSize=(123,98),
             datacutType='radar.us',
             datacutCoordinate=(3035,194),
             datacutSize=(133,89),
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
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (283,276),'869',),
                ( (256,139),'821',),
              ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (79,244),'75',),
                ( (320,157),'95',),
                ( (354,310),'95',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (283,276),'869',),
                ( (256,139),'821',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (79,244),'75',),
                ( (320,157),'95',),
                ( (354,310),'95',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (342,208),),
                ( (290,129),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (336,135),),
                ( (306,96),),
                ( (300,227),),
                ( (373,353),),
                ( (354,195),),
                ( (282,203),),
                ( (358,278),),
                ( (350,245),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (336,135),),
                ( (306,96),),
                ( (300,227),),
                ( (373,353),),
                ( (354,195),),
                ( (282,203),),
                ( (358,278),),
                ( (350,245),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (342,208),),
                ( (290,129),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (313,118),'Miami',),
                ( (251,79),'Coral Gables',),
                ( (243,245),'Davie',),
                ( (237,356),'Delray Beach',),
                ( (371,181),'Hallandale',),
                ( (121,189),'Pembroke Pines',),
                ( (375,296),'Pompano Beach',),
                ( (370,248),'Ft. Lauderdale',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (313,118),'Miami',),
                ( (251,79),'Coral Gables',),
                ( (243,245),'Davie',),
                ( (237,356),'Delray Beach',),
                ( (371,181),'Hallandale',),
                ( (121,189),'Pembroke Pines',),
                ( (375,296),'Pompano Beach',),
                ( (370,248),'Ft. Lauderdale',),
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
# MAP: 116380
# Local_MetroRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(28078,4501),
             mapcutSize=(1080,402),
             mapFinalSize=(620,231),
             mapMilesSize=(123,55),
             datacutType='radar.us',
             datacutCoordinate=(3040,214),
             datacutSize=(132,49),
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
              ( ( (68,142),'75',),
                ( (253,47),'95',),
                ( (283,179),'95',),
              ),
             ),
             (
               (('stateHighwaySignGray',0,2,0,),'Tungsten-Medium',18,(47,53,65,255),1,-20,(),),
              ( ( (221,149),'869',),
                ( (198,32),'821',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (271,27),),
                ( (248,161),),
                ( (235,104),),
                ( (281,76),),
                ( (219,83),),
                ( (285,147),),
                ( (282,120),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (297,31),'Miami',),
                ( (116,173),'Coral Springs',),
                ( (159,108),'Davie',),
                ( (301,74),'Hallandale',),
                ( (60,68),'Pembroke Pines',),
                ( (302,155),'Pompano Beach',),
                ( (304,118),'Ft. Lauderdale',),
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
# MAP: 341
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4131,710),
             mapcutSize=(1393,928),
             mapFinalSize=(720,480),
             mapMilesSize=(1311,882),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1230,20),
             datacutSize=(716,480),
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
# MAP: 76879
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(28138,4422),
             mapcutSize=(792,528),
             mapFinalSize=(720,480),
             mapMilesSize=(90,72),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (388,281),'95',),
                ( (108,264),'75',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72202000',(382,89),),
                ( 'T72202010',(279,162),),
                ( 'T72202023',(277,254),),
                ( 'T72202037',(282,332),),
                ( 'T72202064',(408,226),),
                ( 'T72203015',(428,343),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72202000',(383,76),),
                ( 'T72202010',(282,126),),
                ( 'T72202023',(280,218),),
                ( 'T72202037',(285,296),),
                ( 'T72202064',(411,190),),
                ( 'T72203015',(431,307),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (381,148),'Miami',),
                ( (266,197),'Hialeah',),
                ( (99,227),'Pembroke Pines',),
                ( (214,368),'Coral Springs',),
                ( (357,261),'Ft. Lauderdale',),
                ( (370,379),'Boca Raton',),
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
# MAP: 76878
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(28138,4422),
             mapcutSize=(792,528),
             mapFinalSize=(720,480),
             mapMilesSize=(90,72),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (388,281),'95',),
                ( (108,264),'75',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72202000',(383,76),),
                ( '72202010',(282,126),),
                ( '72202023',(280,218),),
                ( '72202037',(285,296),),
                ( '72202064',(411,190),),
                ( '72203015',(431,307),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72202000',(382,89),),
                ( '72202010',(279,162),),
                ( '72202023',(277,254),),
                ( '72202037',(282,332),),
                ( '72202064',(408,226),),
                ( '72203015',(428,343),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (381,148),'Miami',),
                ( (266,197),'Hialeah',),
                ( (99,227),'Pembroke Pines',),
                ( (214,368),'Coral Springs',),
                ( (357,261),'Ft. Lauderdale',),
                ( (370,379),'Boca Raton',),
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
# MAP: 48081
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25124,3101),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(668,534),
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
              ( ( '72201000',(277,77),),
                ( '72202000',(443,111),),
                ( '72203000',(436,211),),
                ( '72205000',(333,308),),
                ( '72211000',(199,284),),
                ( '74796045',(266,178),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72201000',(274,113),),
                ( '72202000',(440,147),),
                ( '72203000',(433,247),),
                ( '72205000',(330,344),),
                ( '72211000',(196,320),),
                ( '74796045',(263,214),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (227,149),'Key West',),
                ( (414,183),'Miami',),
                ( (360,283),'W Palm Beach',),
                ( (294,380),'Orlando',),
                ( (167,356),'Tampa',),
                ( (208,250),'Fort Myers',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 47870
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25124,3101),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(668,534),
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
              ( ( 'T72201000',(274,113),),
                ( 'T72202000',(440,147),),
                ( 'T72203000',(433,247),),
                ( 'T72205000',(330,344),),
                ( 'T72211000',(196,320),),
                ( 'T74796045',(263,214),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72201000',(277,77),),
                ( 'T72202000',(443,111),),
                ( 'T72203000',(436,211),),
                ( 'T72205000',(333,308),),
                ( 'T72211000',(199,284),),
                ( 'T74796045',(266,178),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (227,149),'Key West',),
                ( (414,183),'Miami',),
                ( (360,283),'W Palm Beach',),
                ( (294,380),'Orlando',),
                ( (167,356),'Tampa',),
                ( (208,250),'Fort Myers',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 71823
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4282,201),
             mapcutSize=(2292,1528),
             mapFinalSize=(720,480),
             mapMilesSize=(2065,1391),
             datacutType='satellite.us',
             datacutCoordinate=(1129,105),
             datacutSize=(615,411),
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
              ( ( (175,187),),
                ( (319,94),),
                ( (210,257),),
                ( (156,298),),
                ( (549,173),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (99,171),'Havana',),
                ( (225,92),'Kingston',),
                ( (148,268),'Miami',),
                ( (100,321),'Tampa',),
                ( (563,156),'San Juan',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_Satellite', d, 0)
# MAP: 52048
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27018,3675),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(357,285),
             datacutType='radar.us',
             datacutCoordinate=(2910,113),
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
              ( ( (255,230),'75',),
                ( (330,338),'95',),
                ( (79,340),'75',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (255,230),'75',),
                ( (330,338),'95',),
                ( (79,340),'75',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (139,290),),
                ( (363,301),),
                ( (348,194),),
                ( (316,113),),
                ( (147,231),),
                ( (354,233),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (139,290),),
                ( (363,301),),
                ( (348,194),),
                ( (316,113),),
                ( (147,231),),
                ( (354,233),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (92,311),'Fort Myers',),
                ( (380,319),'West Palm Beach',),
                ( (365,180),'Miami',),
                ( (273,96),'Key Largo',),
                ( (78,217),'Naples',),
                ( (374,236),'Fort Lauderdale',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (92,311),'Fort Myers',),
                ( (380,319),'West Palm Beach',),
                ( (365,180),'Miami',),
                ( (273,96),'Key Largo',),
                ( (78,217),'Naples',),
                ( (374,236),'Fort Lauderdale',),
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
# MAP: 118751
# Local_RegionalRadarFS (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27133,4137),
             mapcutSize=(3124,1164),
             mapFinalSize=(620,231),
             mapMilesSize=(357,159),
             datacutType='radar.us',
             datacutCoordinate=(2924,169),
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
              ( ( (94,131),'75',),
                ( (204,104),'75',),
                ( (268,190),'95',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotNew',0,2,0,),
              ( ( (96,157),),
                ( (290,166),),
                ( (276,74),),
                ( (145,139),),
                ( (103,106),),
                ( (281,108),),
              ),
             ),
        ],
  textString = [
             (
               ('AkkoPro-Regular',22,(47,53,65,255),1,-20,0,(),2,0,0,),
              ( ( (67,179),'Fort Myers',),
                ( (309,172),'West Palm Beach',),
                ( (284,50),'Miami',),
                ( (161,137),'Immokalee',),
                ( (65,84),'Naples',),
                ( (301,106),'Fort Lauderdale',),
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
#
wxdata.setInterestList('lambert.us','1',['satellite.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite',])
wxdata.setInterestList('satellite.us.cuts','1',['Config.1.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.LFLocal_LocalDoppler','Config.1.Radar_LocalDoppler','Config.1.Local_SummaryFS','Config.1.Local_MetroDopplerRadar','Config.1.Local_MetroRadarFS','Config.1.Local_RegionalDopplerRadar','Config.1.Local_RegionalRadarFS',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['FLL','MIA','PBI',])
wxdata.setInterestList('coopId','1',['72201000','72202000','72202001','72202010','72202023','72202032','72202037','72202064','72203000','72203015','72205000','72211000','72315090','72412024','74796045',])
wxdata.setInterestList('indexId','1',['KFLL',])
wxdata.setInterestList('pollenId','1',['FLL',])
wxdata.setInterestList('obsStation','1',['KFLL','T72201000','T72202000','T72202001','T72202010','T72202023','T72202032','T72202037','T72202064','T72203000','T72203015','T72205000','T72211000','T74796045',])
wxdata.setInterestList('metroId','1',['20',])
wxdata.setInterestList('climId','1',['083163',])
wxdata.setInterestList('zone','1',['FLZ172',])
wxdata.setInterestList('keyRoute','1',['59000054','59000055','59000060','59000061','59000088','59000089',])
wxdata.setInterestList('skiId','1',['304003','704006',])
wxdata.setInterestList('county','1',['FLC011',])
dsm.set('Config.1.countyNameList',[('FLC011','Broward'),], 0)
#
dsm.set('dmaCode','528', 0)
dsm.set('secondaryObsStation','KFLL', 0)
dsm.set('primaryClimoStation','083163', 0)
dsm.set('primaryIndexId','KFLL', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','FL', 0)
dsm.set('primPollenSiteName','Boca Raton', 0)
dsm.set('expRev','7037003', 0)
dsm.set('primaryCoopId','72202032', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','MIA', 0)
dsm.set('primaryCounty','FLC011', 0)
dsm.set('primaryObsStation','T72202032', 0)
dsm.set('primaryRad',15, 0)
dsm.set('primaryLat',26.12194, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','FLL', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('secondaryRad',30, 0)
dsm.set('primaryLon',-80.14361, 0)
dsm.set('primaryZone','FLZ172', 0)
dsm.set('climoRegion','5', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','022356', 0)
dsm.set('msoName','Unknown', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - FT. LAUDERDALE - DOM', 0)
dsm.set('affiliateNumber','20802', 0)
dsm.set('zipCode','33060', 0)
dsm.set('Config.1.irdAddress','0000315596324203', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD07040021', 0)
dsm.set('Config.1.bcExtIpAddress','172.20.3.106', 0)
dsm.set('Config.1.bcGateWay','10.190.25.254', 0)
dsm.set('Config.1.bcIpAddress','10.190.25.244', 0)
#
wxdata.setTimeZone('EST5EDT')
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
d.airportId = ['MIA','FLL','PBI',]
d.airportLocName = ['Miami','Fort Lauderdale','West Palm Beach',]
d.obsStation = ['T72202000','T72202032','T72203000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['704006','304003',]
d.coopId = ['72315090','72412024',]
d.resortName = ['Sugar Mountain, NC','Winterplace, WV',]
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
d.serialNum=1067332
d.crawls=[
(1324789200,1330145999,[(0,23)],'NBA FANS! WATCH YOUR FAVORITE TEAM ANYTIME, ANYWHERE AND GET REAL TIME STATS WITH THE NBA LEAGUE PASS REGULAR SEASON PKG ON CH\'S 750-760 NOW THROUGH FEBRUARY 24TH. GET UP TO 40 OUT OF MARKET GAMES PER WEEK IN REGULAR SEASON WITH SELECT GAMES IN HD!  CALL 954-COMCAST TODAY!'),
(1327294800,1329109199,[(0,23)],'FLORIDA GRAND OPERA PRESENTS VERDI\'S MASTERPIECE RIGOLETTO ABOUT A DEFORMED COURT JESTER AND THE TWIST OF FATE WITH HIS OWN DAUGHTER.  RIGOLETTO RUNS JANUARY 28 - FEBRUARY 18 AT THE ARSHT AND BROWARD CENTERS.  FOR MORE INFO ON RIGOLETTO GO TO WWW.FGO.ORG OR CALL 800-741-1010.'),
(1326690000,1332046799,[(0,23)],'CITY OF MIAMI GARDENS\' 7TH ANNUAL JAZZ IN THE GARDENS  MARCH 17 AND 18 @ SUNLIFE STADIUM - MARY J. BLIGE, JILL SCOTT, PATTI LABELLE, KEM, KENNY G., DOUG E. FRESH, LEDISI, KEVIN EUBANKS AND MORE HOSTED BY M.C. LYTE ON SALE NOW JAZZINTHEGARDENS.COM BROUGHT TO YOU LOCALLY BY COMCAST'),
(1327035600,1327899599,[(0,23)],'WWE FANS: DON\'T MISS JOHN CENA, RANDY ORTON, CM PUNK, ALBERTO DEL RIO AND MORE AT WWE\'S MOST UNPREDICTABLE EVENT, ROYAL RUMBLE LIVE SUNDAY 1/29 AT 7:30 PM! TO ORDER USING YOUR ON SCREEN GUIDE, GO TO CH. 501 OR HD CH. 509 (HDTV AND HD RECEIVER REQUIRED), PRESS OK THEN PRESS BUY'),
(1328072400,1329109199,[(0,23)],'ON 2/6 GERMAN-LANGUAGE NETWORK DEUTSCHE WELLE ON CH 688 WILL BECOME DW (AMERIKA), FEATURING 20 HRS OF GERMAN LANGUAGE AND 4 HRS OF ENGLISH LANGUAGE PROGRAMMING DAILY. FOR MORE INFO CHECK YOUR ON SCREEN GUIDE, VISIT COMCAST.COM/INTERNATIONALTV OR CALL 954-COMCAST.'),
(1327554000,1328417999,[(0,23)],'DON\'T MISS UFC 143 IN 3D ON SATURDAY 2/4 STARTING AT 7 PM ON CH. 793! TO SEE DIAZ TAKE ON CONDIT IN 3D, GO TO CHANNEL 793, PRESS OK THEN BUY (3D TV, 3D CODE, COMPATIBLE 3D GLASSES, HD SERVICE, HDMI CABLE AND EQUIPMENT REQUIRED). FOR MORE INFO ON UFC 143 in 3D, CALL 954-COMCAST.'),
(1328072400,1330491599,[(0,23)],'ESPN FULL COURT GIVES YOU THE MOST COLLEGE BASKETBALL FROM ACROSS THE COUNTRY ALL SEASON LONG. FEATURING THE NATION\'S TOP CONFERENCES, KEY RIVALRIES AND THE FIRST 2 ROUNDS OF THE NCAA WOMEN\'S TOURNAMENT! CALL 954-266-2278 TO ORDER ESPN FULL COURT HALF SEASON PKG TODAY.'),
(1329109200,1329713999,[(0,23)],'ATTENTION HOCKEY FANS! GET A SNEAK PEAK OF THE NHL CENTER ICE RACE TO THE STANLEY CUP FREE PREVIEW NOW THROUGH 2/19 ON CHANNELS 771 -786!  CALL 954-COMCAST TODAY!'),
(1329109200,1337137199,[(0,23)],'LOVE HOCKEY? FOLLOW YOUR FAVORITE TEAMS ON THE PATH TO VICTORY WITH THE NHL CENTER ICE RACE TO THE STANLEY CUP PACKAGE FEATURING SELECT GAMES IN HD NOW THROUGH 5/15. CALL 954-COMCAST TODAY!'),
(1328072400,1329109199,[(0,23)],'FOLLOW YOUR FAVORITE NHL PLAYERS AND TEAMS WITH THE NHL CENTER ICE HALF SEASON PACKAGE! CHOOSE UP TO 40 OUT OF MARKET GAMES TO WATCH WEEKLY PLUS SELECT STANLEY CUP PLAYOFF GAMES THROUGH 5/15/12. DON\'T WAIT- CALL 954-COMCAST TODAY!'),
(1328850000,1329281999,[(0,23)],'ENJOY A FREE PREVIEW OF PORTUGUESE-LANGUAGE NETWORK BAND INTERNACIONAL ON CH. 696 THROUGH 2/14. BAND INTERNACIONAL FEATURES BRAZILIAN NEWS, TALK SHOWS, DOCUMENTARIES, MUSICALS, SPORTS AND MORE. CHECK YOUR ON-SCREEN GUIDE FOR DETAILS OR CALL 954-COMCAST TO SUBSCRIBE.'),
(1328936400,1329627599,[(0,23)],'ENJOY A FREE PREVIEW OF PORTUGUESE-LANGUAGE NETWORK TV GLOBO ON CH. 693 THROUGH 2/18. TV GLOBO FEATURES NOVELLAS, MINI-SERIES, LIVE SOCCER, SPORTS PROGRAMMING AND MORE. CHECK YOUR ON-SCREEN GUIDE FOR DETAILS OR CALL 954-COMCAST TO SUBSCRIBE.'),
(1329627600,1330318799,[(0,23)],'GREAT NEWS! GENTV HD IS NOW AVAILABLE IN YOUR AREA ON HD LIMITED BASIC CH 445.  WITH THE SUPPORT OF COLOMBIAN NETWORK CANAL CARACOL, WGEN HD OFFERS HIGH QUALITY LOCAL NEWS, NOVELAS, AND ENTERTAINMENT PROGRAMMING. FOR MORE INFO CHECK YOUR ON SCREEN GUIDE.'),
(1329714000,1330232399,[(0,23)],'UFC LIGHTWEIGHT CHAMP FRANKIE EDGAR TAKES ON FORMER WEC CHAMP BEN HENDERSON PLUS RAMPAGE JACKSON BATTLES RYAN BADER AT UFC 144 SAT 2/25 AT 9 P.M.!  TO ORDER USING YOUR ON SCREEN GUIDE, GO TO CH. 501 OR HD CH. 509 (HDTV AND HD RECEIVER REQUIRED), PRESS OK THEN PRESS BUY.'),
(1330146000,1333594799,[(0,23)],'NBA FANS! WATCH YOUR FAVORITE TEAM ANYTIME, ANYWHERE AND GET REAL TIME STATS WITH THE NBA LEAGUE PASS HALF SEASON PACKAGE ON CHS 750-760 NOW THROUGH APRIL 4TH. GET UP TO 40 OUT OF MARKET GAMES PER WEEK IN REGULAR SEASON WITH SELECT GAMES IN HD!  CALL 954-COMCAST TODAY!'),
(1333508400,1335495599,[(0,23)],'IT\'S THE RACE TO THE PLAYOFFS! CATCH THE LAST OF THE NBA SEASON WITH THE NBA RACE TO THE PLAYOFFS PACKAGE NOW THROUGH APRIL 26TH ON CHANNELS 750- 760 FEATURING SELECT GAMES IN HD. CALL 954-COMCAST TO ORDER TODAY!'),
(1330232400,1333256399,[(0,23)],'XFINITY ON DEMAND OFFERS OVER 75,000 ENTERTAINMENT CHOICES INCLUDING MOVIES, TV SHOWS AND MORE!  WATCH YOUR FAVORITE TITLES WHENEVER YOU WANT FROM THE COMFORT OF YOUR OWN HOME! GO TO CHANNEL 1 OR PRESS THE ON DEMAND BUTTON ON YOUR REMOTE.'),
(1329282000,1332305999,[(0,23)],'NAT MOORE FLORIDA GOLF CLASSIC CELEBRITY WEEKEND FUND RAISING EVENT, MARCH 17-19, 2012, SATURDAY CELEBRITY PARTY SEMINOLE HARD ROCK HOTEL AND CASINO, MONDAY GOLF TOURNAMENT DORAL GOLF RESORT AND SPA. CALL 305.770.0995 OR E-MAIL GILLIANM@NATMOOREFOUNDATION.NET FOR MORE INFO.'),
(1331442000,1334285999,[(0,23)],'FOR REASONS BEYOND OUR CONTROL, ON APRIL 12, 2012, ALMAVISION ON DIGITAL LIMITED BASIC CHANNEL 83 AND TELEAMERICA ON DIGITAL LIMITED BASIC CHANNEL 88 WILL NO LONGER BE AVAILABLE.'),
(1334026800,1334372399,[(0,23)],'WATCH THE MARLINS VS. ASTROS EXCLUSIVELY ON MLB NETWORK! FRIDAY, APRIL 13 AT 7:10 PM ET ON COMCAST. DONT HAVE MLB NETWORK? CALL 1-800-COMCAST TODAY!'),
(1334631600,1335841199,[(0,23)],'ON APRIL 24, WPLG-LATV WILL BE REPLACED WITH WPLG-METV (MEMORABLE ENTERTAINMENT TELEVSION). WPLG-METV WILL CONTINUE TO AIR ON CHANNEL 209, BUT WILL BE REMOVED FROM CHANNEL 602. FOR QUESTIONS PLEASE CALL 1-800-COMCAST.'),
(1334890800,1336273199,[(0,23)],'DON\'T MISS THE BIGGEST BOXING EVENT OF THE YEAR AS FLOYD MAYWEATHER TAKES ON MIGUEL COTTO. LIVE SATURDAY, MAY 5TH. TO ORDER CALL 1-800-XFINITY OR USE YOUR REMOTE CONTROL ON CHANNEL 501/509 HD (HDTV & EQUIPMENT REQ.)'),
(1334545200,1336359599,[(0,23)],'FLORIDA GRAND OPERA PRESENTS THE GREATEST LOVE STORY OF ALL TIME - ROMEO AND JULIETTE. INSPIRED BY SHAKESPEARE\'S PLAY ABOUT TWO STAR CROSSED LOVERS, ROMEO AND JULIETTE RUNS APRIL 21 - MAY 12 AT THE ARSHT AND BROWARD CENTERS. FOR MORE INFO GO TO FGO.ORG OR CALL 800-741-1010.'),
(1335754800,1338173999,[(0,23)],'ACTORS\' PLAYHOUSE AT THE MIRACLE THEATRE PRESENTS THE HILARIOUS NEW COMEDY BECKY\'S NEW CAR, PLAYING MAY 9 - JUNE 3. TICKETS ARE ON SALE NOW AND CAN BE PURCHASED THROUGH THE BOX OFFICE AT 305-444-9293 OR ONLINE WWW.ACTORSPLAYHOUSE.ORG. BROUGHT TO YOU LOCALLY BY COMCAST.'),
(1336359600,1336877999,[(0,23)],'ON MAY 12TH FROM 12PM-3PM COME MEET DIEGO FROM NICKELODEON\'S GO, DIEGO, GO! AND INTERACT WITH HIS ANIMAL FRIENDS. DIEGO WILL BE AT FLOOR AND DECOR\'S GRAND OPENING IN BOYNTON BEACH! FREE EVENT AND FUN FOR THE WHOLE FAMILY! MAY 12TH FROM 12PM-3PM AT FLOOR AND DECOR, BOYNTON BEACH.'),
(1337914800,1339297199,[(0,23)],'DON\'T MISS THE BIGGEST BOXING EVENT OF THE YEAR AS MANNY PACQUIAO TAKES ON TIMOTHY BRADLEY. LIVE SATURDAY, JUNE 9TH. TO ORDER CALL 1-800-XFINITY OR USE YOUR REMOTE CONTROL ON CHANNEL 501/509 HD (HDTV AND EQUIPMENT REQ.)'),
(1339988400,1340938799,[(0,23)],'ATTENTION COMCAST CUSTOMERS: ON, OR AROUND, JUNE 26, GMC WILL BECOME A DIGITAL STARTER SERVICE, AND GMC HD WILL BECOME AN HD DIGITAL STARTER SERVICE (WHERE CARRIED). FOR QUESTIONS PLEASE CALL 1-800-COMCAST.'),
(1339729200,1340765999,[(0,23)],'COMCAST SPOTLIGHT OPEN HOUSE. JOIN OUR AD SALES TEAM, WEDNESDAY, JUNE 27TH 9:00 AM - 3:00 PM, WEST PALM BEACH AIRPORT MARIOTT.'),
(1339988400,1340938799,[(0,23)],'GREAT NEWS! ON, OR AROUND, JUNE 26, \'ASPIRE\' WILL BE ADDED ON CHANNEL 267 AS A DIGITAL PREFERRED SERVICE. FOR QUESTIONS PLEASE CALL 1-800-COMCAST.'),
(1344999600,1345777199,[(0,23)],'GREAT NEWS! ON, OR AROUND, AUGUST 15, 2012, PAC 12 WILL BE ADDED ON THE SPORTS ENTERTAINMENT PACK, CHANNEL 764. FOR QUESTIONS, PLEASE CALL 1-800-COMCAST. (CHANNELS MAY VARY BY LOCATION)'),
(1345604400,1346468399,[(0,23)],'GREAT NEWS! ON, OR AROUND, AUGUST 29, 2012, ESPN GOAL LINE WILL BE ADDED TO THE SPORTS ENTERTAINMENT PACK, CHANNEL 766, AND CSS HD WILL BE ADDED TO HD STARTER  HD MULTILATINO MAX, CHANNEL 486. FOR QUESTIONS, PLEASE CALL 1-800-COMCAST. (*NOT AVAILABLE IN ALL AREAS)'),
(1346036400,1347332399,[(0,23)],'NEW FROM XFINITY! WITH ANYPLAY AND THE XFINITY TV(R) APP YOU CAN VIEW TV ON SELECT TABLET DEVICES FROM ANYWHERE IN YOUR HOME. WATCH A PROGRAM ON YOUR TABLET WHILE OTHERS WATCH ANOTHER PROGRAM ON TV. CALL 1-800-XFINITY FOR MORE INFORMATION.'),
(1346900400,1348196399,[(0,23)],'ON 9/6 WATCH EXCLUSIVE COVERAGE OF THE SOUTH AMERICAN WORLD CUP QUALIFIERS ON BEIN SPORT CH 621. CALL 1-800-XFINITY FOR MORE INFO. EL 6 DE SEPT. VEA COBERTURA EXCLUSIVA DE LAS ELIMINATORIAS SUDAMERICANAS EN EL CANAL 621. LLAME AL 1-800-XFINITY PARA MAS INFORMACION.'),
(1350529200,1350874799,[(0,23)],'NO BETTER TIME THAN RIGHT NOW FOR A GREAT DEAL ON A BOAT. GET YOUR DISCOUNT TICKETS TODAY: WWW.SHOWMANAGEMENT.COM'),
(1350529200,1351486799,[(0,23)],'NO BETTER TIME THAN RIGHT NOW FOR A GREAT DEAL ON A BOAT. GET YOUR DISCOUNT TICKETS TODAY: WWW.SHOWMANAGEMENT.COM'),
(1353646800,1355029199,[(0,23)],'DON\'T MISS THE BIGGEST BOXING EVENT OF THE YEAR AS MANNY PACQUIAO TAKES ON JUAN MANUEL MARQUEZ. LIVE SATURDAY, DECEMBER 8TH. TO ORDER CALL 1-800-XFINITY OR USE YOUR REMOTE CONTROL ON CHANNEL 501/509 HD (HDTV & EQUIPMENT REQ.)'),
(1351746000,1353301199,[(0,23)],'MIAMI BOOK FAIR INTERNATIONAL, NOV. 11-18! MORE THAN 350 AUTHORS, 200 EXHIBITORS, HUNDREDS OF THOUSANDS OF BOOKS ON SALE! VISIT CHILDREN\'S ALLEY, KID\'S COMICON AND THE PARAGUAY PAVILION! FOR MORE INFO CALL 305-237-3258 OR VISIT WWW.MIAMIBOOKFAIR.COM BROUGHT TO YOU BY COMCAST.'),
(1351746000,1352437199,[(0,23)],'COMCAST SALES CAREERS JOB FAIR - RESIDENTIAL/BUSINESS SALES OPENING! INTERVIEWS ON THE SPOT - NOVEMBER 8, 11AM-7PM - DOUBLETREE HOTEL 13100 W SUNRISE BLVD SUNRISE'),
(1352696400,1355547599,[(0,23)],'ATTN SFL COMCAST CUSTOMERS: EFF 12/12/12, LAS (675), TELEFUTURA-W (676), UNIVISION-W (677), XFINITY LATINO* (600), BABYFIRSTTV-ESPANOL (645), BANDAMAX (647) AND RITMOSON LATINO(651) WILL BE ADDED TO MULTILATINO.(*NOT AVAILABLE IN HOMESTEAD/REDLANDS)'),
(1352696400,1355547599,[(0,23)],'ATTN:  MIAMI-DADE, KEYS AND FT. LAUDERDALE CUSTOMERS: EFF 12/12/12, GALAVISION-W (CH 620), TELEHIT-W (CH 671), MUN2-W (CH 672), DE PELCULA-W (CH 673), DE PELCULA CLSICO-W (674), CINE MEXICANO-W (675), CINELATINO-W (676), AND VIENDOMOVIES-W (677) WILL NO LONGER BE AVAILABLE.'),
(1352350800,1355029199,[(0,23)],'GREAT NEWS SOCCER FANS!  BEIN SPORT-ENGLISH IS NOW AVAILABLE ON SPORTS ENTERTAINMENT PACK CHANNEL 638! CALL 1-800-XFINITY FOR MORE INFO.'),
(1353301200,1358139599,[(0,23)],'GET A FREE SET OF 16OZ TERVIS TUMBLERS AND SUPPORT FISHING, DIVING, DOLPHINS, SEA TURTLES AND OUR OCEANS WHEN YOU SWITCH TO A NEW PROTECT OUR REEFS LICENSE PLATE FOR YOUR VEHICLE. HELP RESTORE AND PROTECT FLORIDA\'S CORAL REEFS! PLEASE VISIT WWWW.REEFPLATE.COM FOR DETAILS'),
(1354942800,1357880399,[(0,23)],'ATTN COMCAST BROWARD CNTY CUSTOMERS: EFF 1/8/13, WFUN AMERICA TEVE (CH 12OR15) WILL MOVE TO CH 82; WJAN MUNDOFOX, CH 82, WILL MOVE TO CH 12 (SOUTH BROWARD) OR CH 15 (ALL OTHER BROWARD AREAS). A DIGITAL-READY TV SET AND/OR DIGITAL EQUIP MAY BE REQUIRED. 1-800-COMCAST.'),
(1355202000,1356238799,[(0,23)],'ATTN BROWARD COUNTY COMCAST CUSTOMERS: EFFEC 12/20/2012, GALAVISION (601) WILL ONLY BE AVAILABLE WITH DIGITAL PREFERRED OR MULTILATINO. GALAVISION HD (378) WILL ONLY BE AVAILABLE WITH HD DIGITAL PREFERRED OR MULTILATINO.'),
(1355202000,1356238799,[(0,23)],'ATTN BROWARD COUNTY COMCAST CUSTOMERS: EFFEC 12/20/2012, MTV2 (140), TCM (169), MILITARY CHANNEL (112), CENTRIC (174), & FLIX (170) WILL ONLY BE AVAILABLE WITH DIGITAL PREFERRED. FOX DEPORTES (622) WILL ONLY BE AVAILABLE WITH MULTILATINO.'),
(1361768400,1363150799,[(0,23)],'ATTENTION SOCCER FANS! SCORE BIG LEAGUE ACTION WITH THE MLS DIRECT KICK PACKAGE. GET UP TO 221 REGULAR SEASON GAMES FOR ONLY 4 LOW PAYMENTS OF $19.75. CALL 1-800-XFINITY TO ORDER.'),
(1362114000,1363755599,[(0,23)],'WATCH UP TO 40 OUT-OF-MARKET GAMES A WEEK. CALL 1-800-XFINITY OR VISIT XFINITY.COM/MOSTLIVESPORTS TO ORDER NBA LEAGUE PASS FOR ONLY 4 LOW PAYMENTS OF $24.75.'),
(1364792400,1365994799,[(0,23)],'JOIN XFINITY & NFL NETWORK AT THE VERIZON WIRELESS POMPANO STORE ON SATURDAY, APRIL 13TH FOR FUN PRIZES, AND A CHANCE TO WIN A NFLSHOP.COM GIFT CARD!'),
(1364792400,1367377199,[(0,23)],'GREAT NEWS FOR SOUTH FLORIDA COMCAST CUSTOMERS! ON, OR AROUND, 4/1/13, WPLG-LIVE WELL NETWORK WILL BE ADDED ON DIGITAL LIMITED BASIC CHANNEL 210.'),
(1366167600,1366772399,[(0,23)],'CATCH THE BATTLE ROUNDS OF THE VOICE ON NBC MONDAYS AND TUESDAYS AT 8PM. WATCH ON XFINITY HD CHANNEL 432. NOT AN HD SUBSCRIBER? CALL 1-800-XFINITY TO UPGRADE TODAY!'),
(1366772400,1367377199,[(0,23)],'THE COMPETITION HEATS UP WITH THE KNOCKOUT ROUNDS OF THE VOICE ON NBC MONDAYS AND TUESDAYS AT 8PM. WATCH ON XFINITY HD CHANNEL 432. NOT AN HD SUBSCRIBER? CALL 1-800-XFINITY TO UPGRADE TODAY!'),
(1367377200,1371610799,[(0,23)],'DONT MISS THE EXCITING LIVE EPISODES OF THE VOICE ON NBC MONDAYS AND TUESDAYS AT 8PM. WATCH ON XFINITY HD CHANNEL 432. NOT AN HD SUBSCRIBER? CALL 1-800-XFINITY TO UPGRADE TODAY!'),
(1366513200,1367722799,[(0,23)],'DON\'T MISS THE BOXING EVENT OF THE YEAR AS MAYWEATHER BATTLES GUERRERO! LIVE ON PPV SATURDAY, MAY 4 AT 9PM. TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1366599600,1369364399,[(0,23)],'ON OR AROUND 5/21/13, FOX BUSINESS (106) AND FOX BUSINESS HD*(469) WILL BECOME AVAILABLE W DIGITAL STARTER, BUT WILL NO LONGER BE INCLUDED W MULTILATINO ULTRA*. FOR BUSINESS CLASS TV CUSTOMERS: THESE CHANNELS WILL BECOME AVAILABLE W STANDARD AND DIGITAL STANDARD. *WHERE AVAILABLE'),
(1366599600,1369364399,[(0,23)],'GREAT NEWS SOUTH FLORIDA COMCAST CUSTOMERS! ON, OR AROUND, 4/23/13, WLRN-HD WILL BE AVAILABLE ON HD LIMITED BASIC CHANNEL 487.'),
(1369191600,1371956399,[(0,23)],'ON, OR AROUND, 6/18/13, BBC WORLD NEWS WILL BE ADDED ON DIGITAL PREFERRED CHANNEL 171. FOR BUSINESS CLASS TV CUSTOMERS: THIS CHANNEL WILL BE ADDED ON PREFERRED OR DIGITAL DELUXE CHANNEL 171.'),
(1372820400,1373338799,[(0,23)],'ATTN COMCAST CUSTOMERS: AS OF 7/1/2013, WLRN-LEARN ON 79 HAS CEASED OPERATIONS.'),
(1372993200,1375930799,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND 8/6/2013, TELEMIAMI ON 18 WILL NO LONGER BE AVAILABLE WITH LIMITED BASIC.'),
(1374202800,1374893999,[(0,23)],'\'42\' NOW AVAILABLE ON DEMAND. IN 1946, BRANCH RICKEY SIGNED JACKIE ROBINSON TO THE BROOKLYN DODGERS, BREAKING MLB\'S INFAMOUS COLOR LINE AND FOREVER CHANGING HISTORY.'),
(1376535600,1379213999,[(0,23)],'DON\'T MISS THE BOXING EVENT OF THE YEAR AS MAYWEATHER BATTLES ALVAREZ. LIVE ON PPV SATURDAY, SEPTEMBER 14 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1381287600,1381633199,[(0,23)],'DON\'T MISS THE BOXING EVENT OF THE YEAR AS BRADLEY BATTLES MARQUEZ. LIVE ON PPV SATURDAY, OCTOBER 12 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1383195600,1383627599,[(0,23)],'GREATEST BOAT SHOW IN THE WORLD  FORT LAUDERDALE  - FLORIDA  OCT 31ST THRU NOV 4TH.OVER 1000 BOATS ON DISPLAY.  ALL YOUR FAVORITE BRANDS IN ONE PLACE.  TICKETS, GREAT HOTEL DEALS AND ALL THE INFO ONLY AT  SHOWMANAGEMENT.COM. DOWNLOAD FREE APP: MYBOATSHOW'),
(1383368400,1385269199,[(0,23)],'DON\'T MISS THE BOXING EVENT OF THE YEAR AS PACQUIAO BATTLES RIOS. LIVE ON PPV SATURDAY, NOVEMBER 23 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1386651600,1387342799,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND JANUARY 1, 2014, SHOPNBC WILL CHANGE ITS NAME TO SHOPHQ.'),
(1387947600,1388638799,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND JANUARY 1, 2014, SHOPNBC WILL CHANGE ITS NAME TO SHOPHQ.'),
(1389243600,1390712399,[(0,23)],'ON JANUARY 25TH, 2014 THE SOUTH FLORIDA COMMUNITY WILL COME TOGETHER TO CELEBRATE THE 4TH ANNUAL DAN MARINO FOUNDATION WALKABOUT AUTISM AND EXPO, BROUGHT TO YOU BY COMCAST AND WALGREENS. TO REGISTER A TEAM OR FOR MORE INFORMATION, PLEASE VISIT WWW.DMFWALKABOUTAUTISM.ORG.'),
(1389848400,1390107599,[(0,10)],'COME TO AN ITT TECH OPEN HOUSE ON SATURDAY, JANUARY 18TH FROM 10A-1P. VISIT WWW.ITT-TECH.EDU FOR MORE INFORMATION.'),
(1389848400,1393131599,[(0,10)],'COME TO AN ITT TECH OPEN HOUSE ON SATURDAY, FEBRUARY 22ND FROM 10:00 AM TO 1:00 PM. VISIT WWW.ITT-TECH.EDU FOR MORE INFORMATION.'),
(1389934800,1394341199,[(0,23)],'JOIN US ON SATURDAY, MARCH 8 AT SUN LIFE STADIUM IN MIAMI OR TRADITION SQUARE IN PORT ST LUCIE FOR THE DIABETES RESEARCH INSTITUTE WALK FOR DIABETES AND FAMILY FUN DAY, PRESENTED BY WALGREENS. FOR MORE INFORMATION OR TO REGISTER YOUR TEAM, PLEASE VISIT WWW.WALGREENSWALKDRI.ORG!'),
(1390539600,1391921999,[(0,23)],'RUNWILD 5K RUN WALK BENEFITING CHAPMAN PARTNERSHIP @ ZOO MIAMI SAT. FEB 8 - FUN FOR THE WHOLE FAMILY - WWW.RUNWILD5KMIAMI.COM'),
(1392094800,1392785999,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND MARCH 3, 2014, MILITARY CHANNEL, ON CHANNEL 112 WITH DIGITAL PREFERRED, WILL CHANGE ITS NAME TO AMERICAN HEROES CHANNEL.'),
(1393218000,1393909199,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND MARCH 3, 2014, MILITARY CHANNEL, ON CHANNEL 112 WITH DIGITAL PREFERRED, WILL CHANGE ITS NAME TO AMERICAN HEROES CHANNEL.'),
(1392872400,1395205199,[(0,23)],'BOXING SUPERSTAR CANELO ALVAREZ GOES TOE TO TOE WITH POWER PUNCHER ALFREDO ANGULO. LIVE ON PPV SATURDAY, MARCH 8 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1393304400,1393995599,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND MARCH 25, 2014, EL REY WILL NO LONGER BE AVAILABLE ON CHANNEL 664. EL REY WILL CONTINUE TO BE AVAILABLE ON CHANNEL 120 WITH DIGITAL PREFERRED.'),
(1395118800,1395809999,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND MARCH 25, 2014, EL REY WILL NO LONGER BE AVAILABLE ON CHANNEL 664. EL REY WILL CONTINUE TO BE AVAILABLE ON CHANNEL 120 WITH DIGITAL PREFERRED.'),
(1393736400,1394427599,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND APRIL 2, 2014, TV COLOMBIA, ON CHANNEL 653 WITH MULTILATINO, WILL CHANGE ITS NAME TO NUESTRA TELE.'),
(1395810000,1396501199,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND APRIL 2, 2014, TV COLOMBIA, ON CHANNEL 653 WITH MULTILATINO, WILL CHANGE ITS NAME TO NUESTRA TELE.'),
(1393736400,1394427599,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND APRIL 2, 2014, TV COLOMBIA, ON CHANNEL 630 WITH MULTILATINO, WILL CHANGE ITS NAME TO NUESTRA TELE.'),
(1395810000,1396501199,[(0,23)],'ATTN COMCAST CUSTOMERS: ON OR AROUND APRIL 2, 2014, TV COLOMBIA, ON CHANNEL 630 WITH MULTILATINO, WILL CHANGE ITS NAME TO NUESTRA TELE.'),
(1393563600,1394427599,[(0,23)],'TNA WRESTLING PRESENTS LOCKDOWN LIVE AT MIAMIS BANKUNITED CENTER, 8PM SUNDAY 3/9. GO TO TICKETMASTER.COM FOR TICKETS, OR ORDER ON XFINITY PAY PER VIEW WITH YOUR REMOTE CONTROL. PRESS MENU TWICE OR CALL 1-800-XFINITY. GO TO WWW.COMCAST.COM/CHANNELLINEUP FOR CHANNEL LISTINGS'),
(1396242000,1397357999,[(0,23)],'COME TO AN ITT TECH OPEN HOUSE ON SATURDAY, APRIL 12TH FROM 10:00 AM TO 1:00 PM. VISIT WWW.ITT-TECH.EDU FOR MORE INFORMATION.'),
(1399258800,1400295599,[(0,23)],'COME TO AN ITT TECH OPEN HOUSE ON SATURDAY, MAY 17TH FROM 10:00 AM TO 1:00 PM. VISIT WWW.ITT-TECH.EDU FOR MORE INFORMATION.'),
(1395982800,1397357999,[(0,23)],'PACQUIAO IS TAKING ON UNDEFEATED CHAMPION TIMOTHY BRADLEY JR. LIVE ON PPV SATURDAY, APRIL 12 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1396926000,1398567599,[(0,23)],'FORD ECOBOOST CHALLENGE IS COMING TO CALDER CASINO IN MIAMI, FL ON APRIL 26TH. YOULL HAVE THE CHANCE TO GET BEHIND THE WHEEL OF A 2014 FORD ESCAPE, FUSION, C-MAX AND F-150 AND FACE OFF AGAINST THE COMPETITION. FOR COMPLETE DETAILS, INCLUDING HOW TO ENTER, VISIT ECOBOOSTDRIVE.COM'),
(1397790000,1399172399,[(0,23)],'DON\'T MISS THE BOXING EVENT OF THE YEAR AS MAYWEATHER BATTLES MAIDANA. LIVE ON PPV SATURDAY, MAY 3 AT 9PM! TO ORDER WITH YOUR REMOTE, PRESS \'MENU\' TWICE OR CALL 1-800-XFINITY.'),
(1398740400,1401591599,[(0,23)],'LOOKING FOR A REWARDING CAREER?  LOOK NO FURTHER!  COMCAST IS HIRING SUPERVISORS FOR OUR FT MYERS, WEST PALM BEACH & MIRAMAR CALL CENTERS. TO LEARN MORE ABOUT THESE EXCITING OPPORTUNITIES, VISIT  WWW.JOBS.COMCAST.COM AND SELECT POSITIONS #46874, #53550 & #53195.'),
(1398740400,1401591599,[(0,23)],'LOOKING FOR A REWARDING CAREER? LOOK NO FURTHER! COMCAST IS HIRING SUPERVISORS FOR OUR FT MYERS, WEST PALM BEACH AND MIRAMAR CALL CENTERS. TO LEARN MORE ABOUT THESE EXCITING OPPORTUNITIES, VISIT WWW.JOBS.COMCAST.COM AND SELECT POSITIONS #46874, #53550 AND #53195.'),
(1398913200,1399258799,[(5,0)],'HOW DID YOU SLEEP LAST NIGHT? NOT SO GR8? CHECK YOUR MATTRESS TAG AND IF YOUR MATTRESS IS OVER 8 ITS TIME TO TERMIN8. SO COME INTO MATTRESS FIRM TO REJUVEN8. MATTRESS FIRM OFFERS ALL THE BEST BRANDS AT ALL THE BEST PRICES TO GUARANTEE YOUR HAPPINESS AND A GREAT NIGHTS SLEEP.'),
(1392354000,1423803599,[(0,23)],'HOME NEEDS RE-ROOFING OR JUST REPAIRS? CALL UNIVERSAL ROOFING INC. AT 954-923-5100 FOR A FREE ESTIMATE. WE HAVE BEEN REPAIRING ROOFS CORRECTLY IN SFL SINCE 1961. LEARN MORE ABOUT OUR RESIDENTIAL AND COMMERCIAL WORK AT UNIVERSALROOFINGINC.COM CALL UNIVERSAL ROOFING AT 954-923-5100'),
(1405911600,1406516399,[(0,23)],'ABC SAFE BOATING CLASS STARTS JULY 29TH WWW.ABCBOATINGCLASS.COM  LEARN ALL ABOUT BOATING FOR THE ENTIRE FAMILY AND POSSIBLY RECEIVE DISCOUNTED BOATING INSURANCE. 954-782-7277 REGISTER TODAY!  ABC SAFE BOATING CLASS REGISTRATION - STARTS JULY 29TH WWW.ABCBOATINGCLASS.COM'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.NationalLdl_TrafficFlow.2')
scmtRemove('Config.1.NationalLdl_TrafficFlow.0')
scmtRemove('Config.1.NationalLdl_Today.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.Local_TodayFS.0')
scmtRemove('Config.1.Local_IntroFS.0')
scmtRemove('Config.1.NationalLdl_Today.3')
scmtRemove('Config.1.NationalLdl_Today.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.Local_SevereAlertFS.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.NationalLdl_TrafficIncidents.0')
scmtRemove('Config.1.NationalLdl_Today.5')
scmtRemove('Config.1.NationalLdl_Today.4')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.Local_NowFS.0')
scmtRemove('Config.1.Local_TomorrowNightFS.0')
scmtRemove('Config.1.NationalLdl_TrafficFlow.1')
scmtRemove('Config.1.NationalLdl_Today.1')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
d.coopId = ['72202032',]
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
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
d.zone = ['FLZ172',]
dsm.set('Config.1.Local_SevereAlertFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_SevereAlertLDL.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlert.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_SevereAlertLF.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
d.coopId = ['72202032',]
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
d.locName = ['Oakland Park',]
d.coopId = ['72202037',]
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
d.obsStation = ['T72202037',]
d.locName = ['Oakland Park',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
d.coopId = ['72202032',]
dsm.set('Config.1.Local_SummaryFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72202032',]
d.climId = '083163'
d.latitude  = 26.1
d.longitude = -80.2
d.locName = ['Fort Lauderdale',]
dsm.set('Config.1.Local_NowFS.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_WelcomeAMHQ.0', d, 0, 1)
dsm.set('Config.1.Local_WelcomeFS.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
d.keyRoutes = ['59000088','59000089',]
d.coopId = ['72202032',]
dsm.set('Config.1.NationalLdl_TrafficFlow.2', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Hialeah',]
d.coopId = ['72202001',]
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
d.obsStation = ['T72202001',]
d.locName = ['Hialeah',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Local_NowLDL.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_CurrentConditionsLF.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
d.keyRoutes = ['59000060','59000061',]
d.coopId = ['72202032',]
dsm.set('Config.1.NationalLdl_TrafficFlow.1', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
d.coopId = ['72202032',]
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
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
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
d.locName = ['Fort Lauderdale',]
d.keyRoutes = ['59000054','59000055',]
d.coopId = ['72202032',]
dsm.set('Config.1.NationalLdl_TrafficFlow.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
dsm.set('Config.1.Local_RegionalRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Fort Lauderdale',]
dsm.set('Config.1.NationalLdl_TrafficIncidents.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
dsm.set('Config.1.Local_MetroRadarFS', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72202032',]
d.locName = ['Fort Lauderdale',]
dsm.set('Config.1.Local_IntroFS.0', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_RadarSatelliteComposite = 1
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
# Finished generation on Fri Oct 17 14:51:55 GMT 2014
