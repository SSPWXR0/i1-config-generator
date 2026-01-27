# Created on Thu Dec 08 13:59:17 EST 2005
Log.info('scmt config started')
# EXP: 3633
# VIW: 31623
# CLN: 13556
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
if not (os.path.exists("/var/db/pkg/twc_domestic_release-1.6_p4")):
   Log.info("config exiting - invalid version")
   abortMsg()
#
scmtRemove('Config.0.LASCrawl')
dsm.set('primaryPollenStation', 'scmt', 0)
scmtRemove('interestlist.pollenId.0')
scmtRemove('Config.0.TextForecast')
scmtRemove('Config.0.OutdoorActivityForecast')
scmtRemove('Config.0.SchoolDayWeather')
scmtRemove('Config.0.TrafficReport')
scmtRemove('Config.0.TrafficFlow')
scmtRemove('Config.0.MetroDopplerRadar')
scmtRemove('Config.0.MetroForecastMap')
scmtRemove('Config.0.RadarSatelliteComposite')
scmtRemove('Config.0.RegionalForecastMap')
scmtRemove('Config.0.RegionalObservationMap')
scmtRemove('Config.0.AirQualityForecast')
scmtRemove('Config.0.Almanac')
scmtRemove('Config.0.Climatology')
scmtRemove('Config.0.CurrentConditions')
scmtRemove('Config.0.DaypartForecast')
scmtRemove('Config.0.EventForecast')
scmtRemove('Config.0.7DayForecast')
scmtRemove('Config.0.ExtendedForecast')
scmtRemove('Config.0.GetawayForecast')
scmtRemove('Config.0.HeatSafetyTips')
scmtRemove('Config.0.RegionalDopplerRadar')
scmtRemove('Config.0.LocalObservations')
scmtRemove('Config.0.MarineForecast')
scmtRemove('Config.0.NWSHeadlines')
scmtRemove('Config.0.Tides')
scmtRemove('Config.0.RecordHighLow')
scmtRemove('Config.0.Satellite')
scmtRemove('Config.0.LowerDisplayLine')
scmtRemove('Config.0.Ldl_LASCrawl')
scmtRemove('Config.0.DefaultUS.standard.60.0')
scmtRemove('Config.0.DefaultUS.standard.60.1')
scmtRemove('Config.0.DefaultUS.standard.90.0')
scmtRemove('Config.0.DefaultUS.standard.90.1')
scmtRemove('Config.0.DefaultUS.standard.120.2')
scmtRemove('Config.0.DefaultUS.standard.120.0')
scmtRemove('Config.0.DefaultUS.standard.120.1')
scmtRemove('Config.0.WestCoastUS.standard.60.0')
scmtRemove('Config.0.WestCoastUS.standard.60.1')
scmtRemove('Config.0.WestCoastUS.standard.90.0')
scmtRemove('Config.0.WestCoastUS.standard.90.1')
scmtRemove('Config.0.WestCoastUS.standard.120.2')
scmtRemove('Config.0.WestCoastUS.standard.120.0')
scmtRemove('Config.0.WestCoastUS.standard.120.1')
scmtRemove('Config.0.SouthernCalifornia.standard.60.0')
scmtRemove('Config.0.SouthernCalifornia.standard.60.1')
scmtRemove('Config.0.SouthernCalifornia.standard.90.0')
scmtRemove('Config.0.SouthernCalifornia.standard.90.1')
scmtRemove('Config.0.SouthernCalifornia.standard.120.2')
scmtRemove('Config.0.SouthernCalifornia.standard.120.0')
scmtRemove('Config.0.SouthernCalifornia.standard.120.1')
scmtRemove('Config.0.Ldl_CurrentApparentTemp')
scmtRemove('Config.0.Ldl_CurrentCeiling')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentDewpoint')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentGusts')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentHumidity')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentMTDPrecip')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentPressure')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentSkyTemp')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentVisibility')
ds.commit()
scmtRemove('Config.0.Ldl_CurrentWinds')
ds.commit()
scmtRemove('Config.0.Ldl_AirportDelayConditions')
ds.commit()
scmtRemove('Config.0.Ldl_AirQualityForecast')
ds.commit()
scmtRemove('Config.0.Ldl_SunriseSunset')
ds.commit()
scmtRemove('Config.0.Ldl_TravelForecast')
ds.commit()
scmtRemove('Config.0.Ldl_UVForecast')
ds.commit()
scmtRemove('Config.0.Ldl_LocalStarIDMessage')
ds.commit()
scmtRemove('Config.0.Ldl_NationalStarIDMessage')
ds.commit()
scmtRemove('Config.0.Ldl_TrafficTripTimes')
ds.commit()
scmtRemove('Config.0.Ldl_ExtendedForecast')
ds.commit()
scmtRemove('Config.0.Ldl_HourlyForecast')
ds.commit()
scmtRemove('Config.0.Ldl_Shortcast')
ds.commit()
scmtRemove('Config.0.Ldl_SummaryForecast')
ds.commit()
scmtRemove('Config.0.Ldl_Date')
ds.commit()
scmtRemove('Config.0.Ldl_TorandoWatch')
ds.commit()
scmtRemove('ldlStarIDMessage')
#
# MAP: 73678
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25650,8460),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(151,104),
             datacutType='radar.us',
             datacutCoordinate=(2743,699),
             datacutSize=(176,100),
             dataFinalSize=(240,137),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Radar_LocalDoppler', d, 0)
#
# Radar_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (96,32),),
                ( (149,81),),
                ( (157,54),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (96,32),),
                ( (149,81),),
                ( (157,54),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (78,21),'Atlanta',),
                ( (120,100),'Gainesville',),
                ( (142,43),'Winder',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (78,21),'Atlanta',),
                ( (120,100),'Gainesville',),
                ( (142,43),'Winder',),
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
dsm.set('Config.0.Radar_LocalDoppler', d, 0)
# MAP: 51156
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25880,8400),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(151,121),
             datacutType='radar.us',
             datacutCoordinate=(2771,691),
             datacutSize=(176,118),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Local_MetroDopplerRadar', d, 0)
#
# Local_MetroDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (235,242),'400',),
              ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (86,258),'75',),
                ( (556,334),'85',),
                ( (323,101),'20',),
                ( (310,251),'985',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (235,242),'400',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (310,251),'985',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (86,258),'75',),
                ( (556,334),'85',),
                ( (323,101),'20',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (177,105),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (467,196),),
                ( (193,141),),
                ( (164,277),),
                ( (443,266),),
                ( (341,290),),
                ( (432,301),),
                ( (299,196),),
                ( (373,207),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (467,196),),
                ( (193,141),),
                ( (164,277),),
                ( (443,266),),
                ( (341,290),),
                ( (432,301),),
                ( (299,196),),
                ( (373,207),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (177,105),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (484,182),'Athens',),
                ( (113,144),'Atlanta',),
                ( (136,298),'Canton',),
                ( (463,269),'Commerce',),
                ( (295,311),'Gainesville',),
                ( (449,319),'Homer',),
                ( (159,199),'Lawrenceville',),
                ( (346,190),'Winder',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (484,182),'Athens',),
                ( (113,144),'Atlanta',),
                ( (136,298),'Canton',),
                ( (463,269),'Commerce',),
                ( (295,311),'Gainesville',),
                ( (449,319),'Homer',),
                ( (159,199),'Lawrenceville',),
                ( (346,190),'Winder',),
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
dsm.set('Config.0.Local_MetroDopplerRadar', d, 0)
# MAP: 346
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3982,1115),
             mapcutSize=(1262,841),
             mapFinalSize=(720,480),
             mapMilesSize=(1213,816),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1154,229),
             datacutSize=(648,435),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.0.Local_RadarSatelliteComposite', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RadarSatelliteComposite', d, 0)
# MAP: 72566
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25990,8533),
             mapcutSize=(1152,768),
             mapFinalSize=(720,480),
             mapMilesSize=(121,97),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (311,226),'985',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (358,215),'85',),
                ( (73,203),'75',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72219000',(158,83),),
                ( '72227024',(192,193),),
                ( '72227037',(306,97),),
                ( '72227040',(147,308),),
                ( '72311000',(562,124),),
                ( '72311011',(478,220),),
                ( '72311013',(429,141),),
                ( '72311035',(337,261),),
                ( '72311050',(555,311),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72219000',(155,119),),
                ( '72227024',(189,229),),
                ( '72227037',(303,133),),
                ( '72227040',(144,344),),
                ( '72311000',(559,160),),
                ( '72311011',(475,256),),
                ( '72311013',(426,177),),
                ( '72311035',(334,297),),
                ( '72311050',(552,347),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (119,155),'Atlanta',),
                ( (135,265),'Alpharetta',),
                ( (213,169),'Lawrenceville',),
                ( (113,380),'Jasper',),
                ( (525,196),'Athens',),
                ( (424,292),'Commerce',),
                ( (395,213),'Winder',),
                ( (279,333),'Gainesville',),
                ( (520,383),'Toccoa',),
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
dsm.set('Config.0.Local_MetroForecastMap', d, 0)
# MAP: 47888
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(23875,7091),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(617,493),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.0.Local_RegionalForecastMap', d, 0)
#
# Local_RegionalForecastMap (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72217000',(345,80),),
                ( '72219000',(288,181),),
                ( '72226000',(166,79),),
                ( '72228000',(133,180),),
                ( '72310000',(504,165),),
                ( '72314000',(523,264),),
                ( '72326000',(317,285),),
                ( '72327000',(136,296),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72217000',(342,116),),
                ( '72219000',(285,217),),
                ( '72226000',(163,115),),
                ( '72228000',(130,216),),
                ( '72310000',(501,201),),
                ( '72314000',(520,300),),
                ( '72326000',(314,321),),
                ( '72327000',(133,332),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (313,152),'Macon',),
                ( (249,253),'Atlanta',),
                ( (100,151),'Montgomery',),
                ( (70,252),'Birmingham',),
                ( (457,237),'Columbia',),
                ( (474,336),'Charlotte',),
                ( (269,357),'Knoxville',),
                ( (88,368),'Nashville',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalForecastMap', d, 0)
# MAP: 49674
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(23875,7091),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(617,493),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.0.Local_RegionalObservationMap', d, 0)
#
# Local_RegionalObservationMap (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'KATL',(285,217),),
                ( 'KBHM',(130,216),),
                ( 'KBNA',(133,332),),
                ( 'KCAE',(501,201),),
                ( 'KCLT',(520,300),),
                ( 'KMCN',(342,116),),
                ( 'KMGM',(163,115),),
                ( 'KTYS',(314,321),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'KATL',(288,181),),
                ( 'KBHM',(133,180),),
                ( 'KBNA',(136,296),),
                ( 'KCAE',(504,165),),
                ( 'KCLT',(523,264),),
                ( 'KMCN',(345,80),),
                ( 'KMGM',(166,79),),
                ( 'KTYS',(317,285),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (249,253),'Atlanta',),
                ( (70,252),'Birmingham',),
                ( (88,368),'Nashville',),
                ( (457,237),'Columbia',),
                ( (474,336),'Charlotte',),
                ( (313,152),'Macon',),
                ( (100,151),'Montgomery',),
                ( (269,357),'Knoxville',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalObservationMap', d, 0)
# MAP: 48476
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(25100,7810),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(329,263),
             datacutType='radar.us',
             datacutCoordinate=(2675,619),
             datacutSize=(383,255),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Local_RegionalDopplerRadar', d, 0)
#
# Local_RegionalDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (300,117),'75',),
                ( (484,158),'20',),
                ( (91,288),'59',),
                ( (439,287),'85',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (300,117),'75',),
                ( (484,158),'20',),
                ( (91,288),'59',),
                ( (439,287),'85',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (385,225),),
                ( (559,162),),
                ( (348,87),),
                ( (160,266),),
                ( (263,195),),
                ( (514,337),),
                ( (333,265),),
                ( (344,321),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (385,225),),
                ( (559,162),),
                ( (348,87),),
                ( (160,266),),
                ( (263,195),),
                ( (514,337),),
                ( (333,265),),
                ( (344,321),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (405,228),'Athens',),
                ( (525,145),'Augusta',),
                ( (279,90),'Macon',),
                ( (139,287),'Rome',),
                ( (233,178),'Atlanta',),
                ( (534,340),'Greenville',),
                ( (287,286),'Gainesville',),
                ( (324,342),'Helen',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (405,228),'Athens',),
                ( (525,145),'Augusta',),
                ( (279,90),'Macon',),
                ( (139,287),'Rome',),
                ( (233,178),'Atlanta',),
                ( (534,340),'Greenville',),
                ( (287,286),'Gainesville',),
                ( (324,342),'Helen',),
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
dsm.set('Config.0.Local_RegionalDopplerRadar', d, 0)
#
wxdata.setInterestList('lambert.us',['radarSatellite.us',])
wxdata.setInterestList('mercator.us',['radar.us',])
#
wxdata.setInterestList('radarSatellite.us.cuts',['Config.0.Local_RadarSatelliteComposite',])
wxdata.setInterestList('radar.us.cuts',['Config.0.Radar_LocalDoppler','Config.0.Local_MetroDopplerRadar','Config.0.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData',['radarSatellite.us','radar.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId',['AHN','ATL','BHM','CLT',])
wxdata.setInterestList('coopId',['72217000','72219000','72226000','72227024','72227037','72227040','72228000','72310000','72311000','72311011','72311013','72311035','72311050','72312000','72314000','72315090','72324004','72326000','72327000','72412024',])
wxdata.setInterestList('indexId',['KGVL',])
wxdata.setInterestList('pollenId',['ATL',])
wxdata.setInterestList('obsStation',['KAHN','KAND','KATL','KBHM','KBNA','KCAE','KCLT','KDNL','KGSP','KGVL','KLZU','KMCN','KMGM','KTYS','KWDR',])
wxdata.setInterestList('climId',['093621',])
wxdata.setInterestList('zone',['GAZ023',])
wxdata.setInterestList('aq',['ga001',])
wxdata.setInterestList('skiId',['304003','704006',])
wxdata.setInterestList('county',['GAC013','GAC157','GAC139','GAC011','GAC135',])
dsm.set('countyNameList',[('GAC013','Barrow'),('GAC157','Jackson'),('GAC139','Hall'),('GAC011','Banks'),('GAC135','Gwinnett'),], 0)
#
dsm.set('dmaCode','524', 0)
dsm.set('secondaryObsStation','KWDR', 0)
dsm.set('primaryClimoStation','093621', 0)
dsm.set('primaryIndexId','KGVL', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','GA', 0)
dsm.set('primPollenSiteName','Atlanta', 0)
dsm.set('expRev','617268', 0)
dsm.set('primaryCoopId','72311035', 0)
dsm.set('PlaylistOverride','DefaultUS', 0)
dsm.set('wda','AHN', 0)
dsm.set('primaryCounty','GAC013', 0)
dsm.set('primaryObsStation','KGVL', 0)
dsm.set('primaryLat',34.03054, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','ATL', 0)
dsm.set('Clock','scmt.clock', 0)
dsm.set('primaryLon',-83.67833, 0)
dsm.set('primaryZone','GAZ023', 0)
dsm.set('climoRegion','4', 0)
dsm.set('SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','ADELPHIA COMMUNICATIONS', 0)
dsm.set('headendId','026223', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','DOM - WINDER - DOM', 0)
dsm.set('msoCode','01094', 0)
dsm.set('headendName','DOM - WINDER - DOM', 0)
dsm.set('affiliateNumber','05650', 0)
dsm.set('zipCode','30680    ', 0)
dsm.set('starId','TWCD09050042', 0)
dsm.set('irdSlave','0', 0)
#
wxdata.setTimeZone('EST5EDT')
#
# BLOCK BEGIN
d = twc.Data()
dsm.set('Config.0.Override', d, 0)
d = twc.Data()
d.activeVocal = 1
dsm.set('Config.0.Bulletin_Default', d, 0)
# BLOCK END
#
d = twc.Data()
d.sponsorLogo = ''
dsm.set('Config', d, 0, 1)
#
scmtRemove('Config.0.Tag.General.airportData')
d = twc.Data()
d.airportId = ['ATL','CLT','BHM',]
d.airportLocName = ['Atlanta/Hartsfield','Charlotte','Birmingham',]
d.obsStation = ['KATL','KCLT','KBHM',]
dsm.set('Config.0.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.0.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['704006','304003',]
d.coopId = ['72315090','72412024',]
d.resortName = ['Sugar Mountain, NC','Winterplace, WV',]
dsm.set('Config.0.Tag.General.snowboardData', d, 0, 1)
#
scmtRemove('Config.0.Ldl_LASCrawl')
scmtRemove('Config.0.LASCrawl')
#
d = twc.Data()
d.serialNum=177378
d.crawls=[
(1129086000,1129777199,[(5,23)],'Now available on Adelphia\'s High Definition (HD) Broadcast Tier - PBS (WPBA 30 Atlanta) - channel 705. Call 1-888-683-1000 today to subscribe. Some restrictions may apply.'),
]
dsm.set('Config.0.Ldl_LASCrawl', d, 0)
dsm.set('Config.0.LASCrawl', d, 0)
#
#
scmtRemove('Config.0.Ldl_TravelForecast')
scmtRemove('Config.0.TimeTemp_Default')
scmtRemove('Config.0.Ldl_NationalStarIDMessage')
scmtRemove('Config.0.Local_MarineForecast')
scmtRemove('Config.0.Local_GetawayForecast')
scmtRemove('Config.0.Ldl_ExtendedForecast')
scmtRemove('Config.0.Local_TrafficFlow')
scmtRemove('Config.0.Ldl_SunriseSunset')
scmtRemove('Config.0.Ldl_AirQualityForecast')
scmtRemove('Config.0.Local_TrafficReport')
scmtRemove('Config.0.Fcst_DaypartForecast')
scmtRemove('Config.0.Ldl_TrafficTripTimes')
scmtRemove('Config.0.Ldl_UVForecast')
scmtRemove('Config.0.Fcst_ExtendedForecast')
scmtRemove('Config.0.Local_OutdoorActivityForecast')
scmtRemove('Config.0.Local_ExtendedForecast')
scmtRemove('Config.0.Local_TextForecast')
scmtRemove('Config.0.Local_DaypartForecast')
scmtRemove('Config.0.Local_Tides')
scmtRemove('Config.0.Local_SchoolDayWeather')
scmtRemove('Config.0.Local_7DayForecast')
scmtRemove('Config.0.Ldl_CurrentApparentTemp')
scmtRemove('Config.0.Local_NWSHeadlines')
scmtRemove('Config.0.Fcst_TextForecast')
scmtRemove('Config.0.Local_Satellite')
scmtRemove('Config.0.Local_RecordHighLow')
scmtRemove('Config.0.Local_Almanac')
scmtRemove('Config.0.Local_Climatology')
scmtRemove('Config.0.Ldl_LocalStarIDMessage')
scmtRemove('Config.0.Local_CurrentConditions')
scmtRemove('Config.0.Local_HeatSafetyTips')
scmtRemove('Config.0.Local_TrafficOverview')
scmtRemove('Config.0.Local_AirQualityForecast')
scmtRemove('Config.0.Cc_CurrentConditions')
scmtRemove('Config.0.Local_LocalObservations')
scmtRemove('Config.0.Local_EventForecast')
scmtRemove('Config.0.Ldl_AirportDelayConditions')
#
d = twc.Data()
d.locName = 'Gainesville/Winder/Commerce'
d.coopId = '72311035'
dsm.set('Config.0.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KAND','KAHN','KATL','KDNL','KGVL','KGSP','KLZU','KWDR',]
d.locName = ['Anderson','Athens','Atlanta Int\'l','Augusta/Daniel','Gainesville','Greer','Lawrenceville','Winder',]
dsm.set('Config.0.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.climId = '093621'
d.latitude = 34.3
d.longitude = -83.85
dsm.set('Config.0.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Chattanooga','Macon','Greenville',]
d.coopId = ['72324004','72217000','72312000',]
dsm.set('Config.0.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KGVL','KWDR',]
d.locName = ['Gainesville','Winder',]
d.elementDuration = 6
dsm.set('Config.0.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Atlanta Metro',]
d.actionDayPhrase = 'Smog Alert'
d.aq = ['ga001',]
dsm.set('Config.0.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.activeVocalCue = 1
dsm.set('Config.0.Local_RegionalDopplerRadar', d, 0, 1)
#
#
d = twc.Data()
d.trafficActive = 0
d.trafficReverseActive = [1,1,1,1,1,1,]
d.routes=[]
d.routeDisplayTime=[]
dsm.set('Config.0.Ldl_TrafficTripTimes', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Gainesville/Winder/Commerce'
d.coopId = '72311035'
dsm.set('Config.0.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KGVL'
d.locName = 'GAINESVILLE'
d.heatIndexThreshold = 100
dsm.set('Config.0.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'GAZ023'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'GAINESVILLE/WINDER/COMMERCE'
d.coopId = '72311035'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'GAINESVILLE/WINDER/COMMERCE'
d.coopId = '72311035'
d.activeVocalCue = 1
dsm.set('Config.0.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_NationalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KGVL','KWDR',]
d.locName = ['Winder','GAINESVILLE','WINDER',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'GAINESVILLE/WINDER/COMMERCE'
d.coopId = '72311035'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KGVL','KWDR',]
d.schedule = [((11,23,16,0,0),(11,25,16,0,0)),((12,16,16,0,0),(1,6,16,0,0)),((5,19,16,0,0),(9,4,16,0,0)),]
d.coopId = '72311035'
dsm.set('Config.0.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '093621'
d.latitude = 34.3
d.longitude = -83.85
dsm.set('Config.0.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['AHN','ATL',]
d.obsStation = ['KAHN','KATL',]
d.locName = ['Ben Epps Arpt','Hartsfield Arpt.',]
d.displayFlag = [0,1,]
dsm.set('Config.0.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['GAINESVILLE/WINDER/COMMERCE',]
d.coopId = ['72311035',]
dsm.set('Config.0.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KGVL',]
d.climId = ['093621',]
d.latitude = 34.3
d.longitude = -83.85
d.locName = ['Gainesville',]
d.coopId = ['72311035',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.0.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KGVL','KWDR',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.0.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Gainesville/Winder/Commerce'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72311035'
dsm.set('Config.0.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Gainesville/Winder/Commerce'
d.coopId = '72311035'
dsm.set('Config.0.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.0.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.0.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.0.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','KGVL','KWDR',]
d.obsLocName = ['Winder','Gainesville','Winder',]
dsm.set('Config.0.Ldl_CurrentApparentTemp', d, 0, 1)
#
ds.commit()
dsm.set('Config.0.Ldl_CurrentCeiling', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentDewpoint', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentGusts', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentHumidity', d, 0, 1)
ds.commit()
dsm.set('Config.0.Ldl_CurrentMTDPrecip', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentPressure', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentSkyTemp', d, 0, 1)
dsm.set('Config.0.Ldl_CurrentVisibility', d, 0, 1)
ds.commit()
dsm.set('Config.0.Ldl_CurrentWinds', d, 0, 1)
#
d = twc.Data()
d.locName = 'Atlanta Metro'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'ga001'
dsm.set('Config.0.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Gainesville/Winder/Commerce'
d.coopId = '72311035'
dsm.set('Config.0.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72311035'
dsm.set('Config.0.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KGVL'
d.climId = ['093621',]
d.latitude = 34.3
d.longitude = -83.85
d.locName = 'GAINESVILLE'
d.coopId = '72311035'
dsm.set('Config.0.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 0
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 0
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 1
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 0
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 0
d.activeLocal_TrafficOverview = 0
d.activeLocal_TrafficReport = 0
# region keys
dsm.set('Config.0.DefaultUS.120.2', d, 0)
dsm.set('Config.0.DefaultUS.60.1', d, 0)
dsm.set('Config.0.DefaultUS.90.1', d, 0)
dsm.set('Config.0.DefaultUS.90.0', d, 0)
dsm.set('Config.0.DefaultUS.60.0', d, 0)
dsm.set('Config.0.DefaultUS.120.1', d, 0)
dsm.set('Config.0.DefaultUS.120.0', d, 0)
#
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.60.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,5,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,5,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,9,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.120.2', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,3,2,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,2,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.60.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,6,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,9,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.120.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.90.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,6,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,4,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,4,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,11,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,11,12,7,1,6,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,11,12,7,1,9,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.120.0', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Playlist.DefaultUS.90.0', d, 0)
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
dsm.set('Playlist.Fcst.fcst1', d, 0)
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
dsm.set('Playlist.DefaultUS.57.0', d, 0)
#
ds.commit()
#
# End of SCMT deployment
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Thu Dec 08 13:59:21 EST 2005
