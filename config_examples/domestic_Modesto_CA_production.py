# Created on Thu Dec 08 14:18:12 EST 2005
Log.info('scmt config started')
# EXP: 1178
# VIW: 12966
# CLN: 12368
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
# MAP: 74130
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(5466,10452),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(145,99),
             datacutType='radar.us',
             datacutCoordinate=(271,943),
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
              ( ( (125,93),),
                ( (201,29),),
                ( (152,64),),
                ( (167,49),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (125,93),),
                ( (201,29),),
                ( (152,64),),
                ( (167,49),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (138,95),'Stockton',),
                ( (148,32),'Merced',),
                ( (92,68),'Modesto',),
                ( (179,50),'Turlock',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (138,95),'Stockton',),
                ( (148,32),'Merced',),
                ( (92,68),'Modesto',),
                ( (179,50),'Turlock',),
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
# MAP: 51241
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(5692,10394),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(145,116),
             datacutType='radar.us',
             datacutCoordinate=(299,936),
             datacutSize=(176,117),
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
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (335,84),'5',),
                ( (156,242),'580',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (445,146),'99',),
                ( (125,326),'4',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (156,242),'580',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (445,146),'99',),
                ( (125,326),'4',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (149,101),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (149,101),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (335,84),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (282,320),),
                ( (121,146),),
                ( (509,134),),
                ( (297,273),),
                ( (360,239),),
                ( (398,264),),
                ( (323,180),),
                ( (122,238),),
                ( (525,325),),
                ( (240,255),),
                ( (398,189),),
                ( (421,229),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (282,320),),
                ( (121,146),),
                ( (509,134),),
                ( (297,273),),
                ( (360,239),),
                ( (398,264),),
                ( (323,180),),
                ( (122,238),),
                ( (525,325),),
                ( (240,255),),
                ( (398,189),),
                ( (421,229),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (244,341),'Stockton',),
                ( (141,149),'San Jose',),
                ( (529,137),'Merced',),
                ( (262,294),'Manteca',),
                ( (325,222),'Modesto',),
                ( (418,267),'Oakdale',),
                ( (281,163),'Patterson',),
                ( (74,221),'Pleasanton',),
                ( (545,328),'Sonora',),
                ( (219,238),'Tracy',),
                ( (418,192),'Turlock',),
                ( (441,232),'Waterford',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (244,341),'Stockton',),
                ( (141,149),'San Jose',),
                ( (529,137),'Merced',),
                ( (262,294),'Manteca',),
                ( (325,222),'Modesto',),
                ( (418,267),'Oakdale',),
                ( (281,163),'Patterson',),
                ( (74,221),'Pleasanton',),
                ( (545,328),'Sonora',),
                ( (219,238),'Tracy',),
                ( (418,192),'Turlock',),
                ( (441,232),'Waterford',),
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
# MAP: 71633
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(5859,10491),
             mapcutSize=(1080,720),
             mapFinalSize=(720,480),
             mapMilesSize=(108,87),
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
              ( ( (88,258),'580',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (423,167),'99',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (328,84),'5',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72481004',(486,81),),
                ( '72481015',(506,194),),
                ( '72492000',(290,300),),
                ( '72492015',(187,227),),
                ( '72492018',(432,286),),
                ( '72492025',(371,194),),
                ( '72492028',(306,114),),
                ( '74509035',(156,91),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72481004',(483,117),),
                ( '72481015',(503,230),),
                ( '72492000',(287,336),),
                ( '72492015',(184,263),),
                ( '72492018',(429,322),),
                ( '72492025',(368,230),),
                ( '72492028',(303,150),),
                ( '74509035',(153,127),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (450,153),'Merced',),
                ( (454,266),'Waterford',),
                ( (243,372),'Stockton',),
                ( (159,299),'Tracy',),
                ( (392,358),'Oakdale',),
                ( (328,266),'Modesto',),
                ( (254,186),'Patterson',),
                ( (83,163),'Mnt Hamilton',),
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
# MAP: 48376
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4512,9114),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(589,471),
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
              ( ( '72386000',(578,120),),
                ( '72389000',(328,76),),
                ( '72480035',(453,217),),
                ( '72483000',(186,280),),
                ( '72486000',(578,288),),
                ( '72488000',(332,304),),
                ( '72491001',(178,85),),
                ( '72492025',(272,171),),
                ( '72494000',(139,185),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72386000',(575,156),),
                ( '72389000',(325,112),),
                ( '72480035',(450,253),),
                ( '72483000',(183,316),),
                ( '72486000',(575,324),),
                ( '72488000',(329,340),),
                ( '72491001',(175,121),),
                ( '72492025',(269,207),),
                ( '72494000',(136,221),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (524,192),'Las Vegas',),
                ( (294,148),'Fresno',),
                ( (410,289),'Tonopah',),
                ( (123,352),'Sacramento',),
                ( (564,360),'Ely',),
                ( (308,376),'Reno',),
                ( (129,157),'Monterey',),
                ( (229,243),'Modesto',),
                ( (63,257),'San Francisco',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalForecastMap', d, 0)
# MAP: 48885
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4512,9114),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(589,471),
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
              ( ( 'KELY',(575,324),),
                ( 'KFAT',(325,112),),
                ( 'KLAS',(575,156),),
                ( 'KMOD',(269,207),),
                ( 'KMRY',(175,121),),
                ( 'KRNO',(329,340),),
                ( 'KSAC',(183,316),),
                ( 'KSFO',(136,221),),
                ( 'KTPH',(450,253),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'KELY',(578,288),),
                ( 'KFAT',(328,76),),
                ( 'KLAS',(578,120),),
                ( 'KMOD',(272,171),),
                ( 'KMRY',(178,85),),
                ( 'KRNO',(332,304),),
                ( 'KSAC',(186,280),),
                ( 'KSFO',(139,185),),
                ( 'KTPH',(453,217),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (564,360),'Ely',),
                ( (294,148),'Fresno',),
                ( (524,192),'Las Vegas',),
                ( (229,243),'Modesto',),
                ( (129,157),'Monterey',),
                ( (308,376),'Reno',),
                ( (123,352),'Sacramento',),
                ( (63,257),'San Francisco',),
                ( (410,289),'Tonopah',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalObservationMap', d, 0)
# MAP: 71608
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1497,1257),
             mapcutSize=(2160,1440),
             mapFinalSize=(720,480),
             mapMilesSize=(2011,1355),
             datacutType='satellite.us',
             datacutCoordinate=(381,389),
             datacutSize=(580,388),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.0.Local_Satellite', d, 0)
#
# Local_Satellite (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDot',0,2,0,),
              ( ( (317,322),),
                ( (378,142),),
                ( (348,260),),
                ( (391,106),),
                ( (326,247),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (243,325),'Eureka',),
                ( (253,145),'Los Angeles',),
                ( (368,263),'Sacramento',),
                ( (287,109),'San Diego',),
                ( (181,250),'San Francisco',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_Satellite', d, 0)
# MAP: 49722
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4851,9832),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(315,252),
             datacutType='radar.us',
             datacutCoordinate=(196,867),
             datacutSize=(382,255),
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
              ( ( (232,325),'80',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (441,152),'99',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (441,152),'99',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (269,153),'101',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (269,153),'101',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (232,325),'80',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (293,357),),
                ( (322,276),),
                ( (172,250),),
                ( (510,119),),
                ( (351,236),),
                ( (242,94),),
                ( (138,341),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (293,357),),
                ( (322,276),),
                ( (172,250),),
                ( (510,119),),
                ( (351,236),),
                ( (242,94),),
                ( (138,341),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (313,360),'Sacramento',),
                ( (342,279),'Stockton',),
                ( (109,233),'San Francisco',),
                ( (438,122),'Fresno',),
                ( (316,219),'Modesto',),
                ( (203,115),'Monterey',),
                ( (88,324),'Santa Rosa',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (313,360),'Sacramento',),
                ( (342,279),'Stockton',),
                ( (109,233),'San Francisco',),
                ( (438,122),'Fresno',),
                ( (316,219),'Modesto',),
                ( (203,115),'Monterey',),
                ( (88,324),'Santa Rosa',),
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
wxdata.setInterestList('lambert.us',['satellite.us',])
wxdata.setInterestList('mercator.us',['radar.us',])
#
wxdata.setInterestList('satellite.us.cuts',['Config.0.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts',['Config.0.Radar_LocalDoppler','Config.0.Local_MetroDopplerRadar','Config.0.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData',['radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId',['MOD','OAK','SJC','SMF',])
wxdata.setInterestList('coopId',['72386000','72389000','72480035','72481004','72481015','72481041','72483000','72486000','72488000','72488012','72491001','72492000','72492015','72492018','72492025','72492028','72494000','74501008','74501026','74509014','74509035',])
wxdata.setInterestList('indexId',['KMOD',])
wxdata.setInterestList('obsStation',['KCCR','KELY','KFAT','KLAS','KLVK','KMCE','KMOD','KMRY','KOAK','KRNO','KSAC','KSCK','KSFO','KSJC','KSMF','KSUU','KTPH',])
wxdata.setInterestList('metroId',['30',])
wxdata.setInterestList('climId',['045738',])
wxdata.setInterestList('zone',['CAZ019',])
wxdata.setInterestList('aq',['ca056','ca061','ca106',])
wxdata.setInterestList('skiId',['916004','916008',])
wxdata.setInterestList('county',['CAC099',])
dsm.set('countyNameList',[('CAC099','Stanislaus'),], 0)
#
dsm.set('dmaCode','862', 0)
dsm.set('secondaryObsStation','KSCK', 0)
dsm.set('primaryClimoStation','045738', 0)
dsm.set('primaryIndexId','KMOD', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','CA', 0)
dsm.set('expRev','616635', 0)
dsm.set('primaryCoopId','72492025', 0)
dsm.set('PlaylistOverride','WestCoastUS', 0)
dsm.set('wda','MOD', 0)
dsm.set('primaryCounty','CAC099', 0)
dsm.set('primaryObsStation','KMOD', 0)
dsm.set('primaryLat',37.6575, 0)
dsm.set('hasTraffic',1, 0)
dsm.set('Clock','scmt.clock', 0)
dsm.set('primaryLon',-121.01945, 0)
dsm.set('primaryZone','CAZ019', 0)
dsm.set('climoRegion','6', 0)
dsm.set('SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','022404', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','DOM - MODESTO - DOM', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - MODESTO - DOM', 0)
dsm.set('affiliateNumber','00658', 0)
dsm.set('zipCode','95350    ', 0)
dsm.set('bcConnectMethod','D', 0)
dsm.set('bcIspDialupPassword','t23w23ci', 0)
dsm.set('bcIspDialupNumber','9,5311416', 0)
dsm.set('irdSlave','0', 0)
dsm.set('starId','TWCD02040064', 0)
dsm.set('bcDialInNumber','2099556531', 0)
dsm.set('bcIspDialupLogin','headend-022404@weather.com', 0)
#
wxdata.setTimeZone('PST8PDT')
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
d.airportId = ['SJC','SMF','OAK',]
d.airportLocName = ['San Jose','Sacramento','Oakland',]
d.obsStation = ['KSJC','KSMF','KOAK',]
dsm.set('Config.0.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.0.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['916008','916004',]
d.coopId = ['74501008','74501026',]
d.resortName = ['Sierra at Tahoe, CA','Heavenly, CA',]
dsm.set('Config.0.Tag.General.snowboardData', d, 0, 1)
#
scmtRemove('Config.0.Ldl_LASCrawl')
scmtRemove('Config.0.LASCrawl')
#
d = twc.Data()
d.serialNum=178163
d.crawls=[
(1123221600,1124171999,[(0,23)],'Bridal Showcase, Sunday August 21st at the Hyatt Regency Hotel 11am to 4 pm. Event sponsored by Bridal Mart, Selix Formalwear, Rayna’s Gourmet Catering, Snow Cleaners and the Sterling Hotel/Vizcaya. Discount tickets available at www.bridalshowcase-ca.com.'),
(1125640800,1125899999,[(0,23)],'Jewelry Television will be donating 5% of net sales from 9/01 – 9/04 for victims of Hurricane Katrina thru  America’s Second Harvest, the nations largest food relief organization.'),
(1126159200,1128923999,[(0,23)],'If you know or suspect you have high blood pressure, a dangerous disease, local physicians are conducting a clinical research. Qualified participants will receive all study related care and meds at no cost. To learn more call 916-781-6718'),
(1126159200,1128923999,[(0,23)],'Having trouble with your type 2 diabetes? You may be eligible to participate in a clinical trial,if you are b/w 18 and 70 and have limited or no exposure to anti-diabetic medication or insulin. Eligible patients may receive free related medication. To learn more call 916-781-6718'),
(1128319200,1129010399,[(0,23)],'The 19th annual Sacramento SPCA Gala “Reigning Cats and Dogs” on Oct 15th saves animals. Reigning Cats and Dogs will have award winning wineries, microbrewers, music and prizes. Go to www.spca.org for your tickets or call 383-7387 ex 9102.'),
(1128319200,1131955199,[(0,23)],'Now Enrolling THE GAIN HUMIRA Research Trial for Active Crohn’s Patients who have stopped Remicade due to loss of response or intolerance. Call Kindra at Capitol GI (916) 773-3523 or visit www.cfs.org/trials to learn more about this study.'),
(1129269600,1130831999,[(0,23)],'Watch the Ellis Eye Laser & Surgery Show Monday-Friday @ 9:30pm on Channel 2 (in Sacramento/Roseville), Channel 69 (in Stockton) and Channel 48 (in Modesto)'),
(1129788000,1131091199,[(0,23)],'Financial aid for college is still available, so go to college. We’ll help you pay for it. Log on to icanaffordcollege.com or call 8---987-ICAN. You will receive one-on-one help to get you going. icanaffordcollege.com or 800-987-ICAN.'),
]
dsm.set('Config.0.Ldl_LASCrawl', d, 0)
dsm.set('Config.0.LASCrawl', d, 0)
#
#
scmtRemove('Config.0.Local_TextForecast')
scmtRemove('Config.0.Cc_CurrentConditions')
scmtRemove('Config.0.Local_SchoolDayWeather')
scmtRemove('Config.0.Fcst_ExtendedForecast')
scmtRemove('Config.0.Ldl_AirportDelayConditions')
scmtRemove('Config.0.Local_AirQualityForecast')
scmtRemove('Config.0.Local_MarineForecast')
scmtRemove('Config.0.Local_EventForecast')
scmtRemove('Config.0.Local_HeatSafetyTips')
scmtRemove('Config.0.Local_7DayForecast')
scmtRemove('Config.0.Local_TrafficFlow')
scmtRemove('Config.0.Local_RecordHighLow')
scmtRemove('Config.0.Ldl_AirQualityForecast')
scmtRemove('Config.0.Ldl_SunriseSunset')
scmtRemove('Config.0.Local_TrafficReport')
scmtRemove('Config.0.Fcst_TextForecast')
scmtRemove('Config.0.Local_CurrentConditions')
scmtRemove('Config.0.Local_Almanac')
scmtRemove('Config.0.Ldl_CurrentApparentTemp')
scmtRemove('Config.0.Local_GetawayForecast')
scmtRemove('Config.0.Local_DaypartForecast')
scmtRemove('Config.0.Local_TrafficOverview')
scmtRemove('Config.0.TimeTemp_Default')
scmtRemove('Config.0.Ldl_LocalStarIDMessage')
scmtRemove('Config.0.Local_OutdoorActivityForecast')
scmtRemove('Config.0.Local_ExtendedForecast')
scmtRemove('Config.0.Ldl_ExtendedForecast')
scmtRemove('Config.0.Local_NWSHeadlines')
scmtRemove('Config.0.Local_Tides')
scmtRemove('Config.0.Ldl_TrafficTripTimes')
scmtRemove('Config.0.Fcst_DaypartForecast')
scmtRemove('Config.0.Local_RadarSatelliteComposite')
scmtRemove('Config.0.Local_Climatology')
scmtRemove('Config.0.Ldl_NationalStarIDMessage')
scmtRemove('Config.0.Local_LocalObservations')
scmtRemove('Config.0.Ldl_UVForecast')
scmtRemove('Config.0.Ldl_TravelForecast')
#
d = twc.Data()
d.locName = 'Modesto Area'
d.coopId = '72492025'
dsm.set('Config.0.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KCCR','KFAT','KLVK','KMCE','KMOD','KSAC','KSCK','KSUU',]
d.locName = ['Concord','Fresno','Livermore','Merced Arpt.','Modesto','Sacramento','Stockton','Travis AFB',]
dsm.set('Config.0.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.climId = '045738'
d.latitude = 37.65
d.longitude = -121
dsm.set('Config.0.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['San Jose','Sacramento','San Francisco',]
d.coopId = ['74509014','72483000','72494000',]
dsm.set('Config.0.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KMOD','KSCK',]
d.locName = ['Modesto','Stockton',]
d.elementDuration = 6
dsm.set('Config.0.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Modesto','Stockton','Merced',]
d.actionDayPhrase = 'Check Before You Burn'
d.aq = ['ca061','ca106','ca056',]
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
d.locName = 'Modesto Area'
d.coopId = '72492025'
dsm.set('Config.0.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KMOD'
d.locName = 'MODESTO'
d.heatIndexThreshold = 100
dsm.set('Config.0.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'CAZ019'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'MODESTO AREA'
d.coopId = '72492025'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'MODESTO AREA'
d.coopId = '72492025'
d.activeVocalCue = 1
dsm.set('Config.0.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'MODESTO AREA'
d.maxPages = 3
d.activeVocalCue = 1
d.metroId=['30',]
d.latLongBoxes=[
             ((-121.673755098051,37.4649374250332),(-120.72840365547,38.2346702201785)),
]
d.severityList=[
             ('Construction',1,),
             ('Incident',1,),
             ('Unspecified',1,),
]
dsm.set('Config.0.Local_TrafficReport', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_NationalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KMOD','KSCK',]
d.locName = ['Modesto','MODESTO','STOCKTON',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'MODESTO AREA'
d.coopId = '72492025'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KMOD','KSCK',]
d.schedule = [((11,23,16,0,0),(11,25,16,0,0)),((12,16,16,0,0),(1,6,16,0,0)),((5,19,16,0,0),(9,4,16,0,0)),]
d.coopId = '72492025'
dsm.set('Config.0.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '045738'
d.latitude = 37.65
d.longitude = -121
dsm.set('Config.0.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['MOD',]
d.obsStation = ['KMOD',]
d.locName = ['Modesto Arpt',]
d.displayFlag = [0,]
dsm.set('Config.0.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['MODESTO AREA',]
d.coopId = ['72492025',]
dsm.set('Config.0.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KMOD',]
d.climId = ['045738',]
d.latitude = 37.65
d.longitude = -121
d.locName = ['Modesto',]
d.coopId = ['72492025',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.0.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KMOD','KSCK',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.0.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Modesto'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72492025'
dsm.set('Config.0.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Modesto'
d.coopId = '72492025'
dsm.set('Config.0.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.0.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.0.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.0.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','KMOD','KSCK',]
d.obsLocName = ['Modesto','Modesto','Stockton',]
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
d.locName = 'Modesto'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'ca061'
dsm.set('Config.0.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locNameList = ['Lake Tahoe, CA','San Francisco, CA','Yosemite N.P., CA',]
d.coopId = ['72488012','72494000','72481041',]
dsm.set('Config.0.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Modesto Area'
d.coopId = '72492025'
dsm.set('Config.0.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72492025'
dsm.set('Config.0.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KMOD'
d.climId = ['045738',]
d.latitude = 37.65
d.longitude = -121
d.locName = 'MODESTO'
d.coopId = '72492025'
dsm.set('Config.0.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 0
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 0
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 1
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 0
d.activeLocal_TrafficOverview = 0
d.activeLocal_TrafficReport = 1
# region keys
dsm.set('Config.0.WestCoastUS.120.2', d, 0)
dsm.set('Config.0.WestCoastUS.120.0', d, 0)
dsm.set('Config.0.WestCoastUS.60.1', d, 0)
dsm.set('Config.0.WestCoastUS.60.0', d, 0)
dsm.set('Config.0.WestCoastUS.90.0', d, 0)
dsm.set('Config.0.WestCoastUS.120.1', d, 0)
dsm.set('Config.0.WestCoastUS.90.1', d, 0)
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
dsm.set('Playlist.WestCoastUS.60.1', d, 0)
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
dsm.set('Playlist.WestCoastUS.60.0', d, 0)
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
dsm.set('Playlist.WestCoastUS.90.1', d, 0)
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
('RadarSatelliteComposite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Playlist.WestCoastUS.120.2', d, 0)
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
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Playlist.WestCoastUS.120.1', d, 0)
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
dsm.set('Playlist.WestCoastUS.90.0', d, 0)
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
('RadarSatelliteComposite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Playlist.WestCoastUS.120.0', d, 0)
ds.commit()
#
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
dsm.set('Playlist.WestCoastUS.57.0', d, 0)
#
ds.commit()
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
#
# End of SCMT deployment
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Thu Dec 08 14:18:20 EST 2005
