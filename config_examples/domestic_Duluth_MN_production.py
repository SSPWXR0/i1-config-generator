# Created on Thu Dec 08 14:01:54 EST 2005
Log.info('scmt config started')
# EXP: 2193
# VIW: 29820
# CLN: 6615
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
# MAP: 74218
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21138,16026),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(125,86),
             datacutType='radar.us',
             datacutCoordinate=(2190,1626),
             datacutSize=(177,100),
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
              ( ( (113,98),),
                ( (152,66),),
                ( (179,18),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (113,98),),
                ( (152,66),),
                ( (179,18),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (123,107),'Independence',),
                ( (107,71),'Duluth',),
                ( (86,23),'Solon Springs',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (123,107),'Independence',),
                ( (107,71),'Duluth',),
                ( (86,23),'Solon Springs',),
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
# MAP: 52165
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21366,15966),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(125,100),
             datacutType='radar.us',
             datacutCoordinate=(2218,1618),
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
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (153,91),'35',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (417,139),'53',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (417,139),'53',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (153,91),'35',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (328,251),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (355,269),),
                ( (197,147),),
                ( (221,266),),
                ( (270,198),),
                ( (250,220),),
                ( (240,299),),
                ( (472,320),),
                ( (359,246),),
                ( (442,171),),
                ( (432,95),),
                ( (367,212),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (355,269),),
                ( (197,147),),
                ( (221,266),),
                ( (270,198),),
                ( (250,220),),
                ( (240,299),),
                ( (472,320),),
                ( (359,246),),
                ( (442,171),),
                ( (432,95),),
                ( (367,212),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (328,251),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (329,290),'Arnold',),
                ( (165,130),'Barnum',),
                ( (113,269),'Brookston',),
                ( (195,184),'Carlton',),
                ( (170,223),'Cloquet',),
                ( (181,320),'Independence',),
                ( (492,323),'Two Harbors',),
                ( (379,249),'Duluth',),
                ( (462,174),'Poplar',),
                ( (371,116),'Solon Springs',),
                ( (332,195),'Superior',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (329,290),'Arnold',),
                ( (165,130),'Barnum',),
                ( (113,269),'Brookston',),
                ( (195,184),'Carlton',),
                ( (170,223),'Cloquet',),
                ( (181,320),'Independence',),
                ( (492,323),'Two Harbors',),
                ( (379,249),'Duluth',),
                ( (462,174),'Poplar',),
                ( (371,116),'Solon Springs',),
                ( (332,195),'Superior',),
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
# MAP: 72403
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21362,15855),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(138,110),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (390,76),'53',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (131,81),'35',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72741038',(560,119),),
                ( '72745000',(299,265),),
                ( '72745008',(357,172),),
                ( '72745013',(197,206),),
                ( '72745019',(155,303),),
                ( '72745021',(409,312),),
                ( '72745025',(420,79),),
                ( '72745027',(133,112),),
                ( '72745028',(514,215),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72741038',(557,155),),
                ( '72745000',(296,301),),
                ( '72745008',(354,208),),
                ( '72745013',(194,242),),
                ( '72745019',(152,339),),
                ( '72745021',(406,348),),
                ( '72745025',(417,115),),
                ( '72745027',(130,148),),
                ( '72745028',(511,251),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (504,191),'Drummond',),
                ( (265,337),'Duluth',),
                ( (314,244),'Superior',),
                ( (158,278),'Cloquet',),
                ( (85,375),'Meadowlands',),
                ( (342,384),'Two Harbors',),
                ( (347,151),'Solon Springs',),
                ( (71,184),'Moose Lake',),
                ( (463,287),'Port Wing',),
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
# MAP: 48903
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19322,14190),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(516,413),
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
              ( ( '72643059',(421,79),),
                ( '72658000',(271,85),),
                ( '72741047',(493,149),),
                ( '72744000',(578,258),),
                ( '72744030',(449,305),),
                ( '72745000',(328,220),),
                ( '72745050',(262,310),),
                ( '72750008',(185,196),),
                ( '74341013',(116,88),),
                ( '74341057',(115,293),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72643059',(418,115),),
                ( '72658000',(268,121),),
                ( '72741047',(490,185),),
                ( '72744000',(575,294),),
                ( '72744030',(446,341),),
                ( '72745000',(325,256),),
                ( '72745050',(259,346),),
                ( '72750008',(182,232),),
                ( '74341013',(113,124),),
                ( '74341057',(112,329),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (368,151),'Eau Claire',),
                ( (209,157),'Minneapolis',),
                ( (430,221),'Rhinelander',),
                ( (534,330),'Hancock',),
                ( (379,377),'Grand Marais',),
                ( (294,292),'Duluth',),
                ( (224,382),'Hibbing',),
                ( (141,268),'Brainerd',),
                ( (71,161),'Montevideo',),
                ( (74,365),'Fosston',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalForecastMap', d, 0)
# MAP: 50490
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19322,14190),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(516,413),
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
              ( ( 'KBRD',(182,232),),
                ( 'KCKC',(446,341),),
                ( 'KCMX',(575,294),),
                ( 'KDLH',(325,256),),
                ( 'KEAU',(418,115),),
                ( 'KFSE',(112,329),),
                ( 'KHIB',(259,346),),
                ( 'KMSP',(268,121),),
                ( 'KMVE',(113,124),),
                ( 'KRHI',(490,185),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'KBRD',(185,196),),
                ( 'KCKC',(449,305),),
                ( 'KCMX',(578,258),),
                ( 'KDLH',(328,220),),
                ( 'KEAU',(421,79),),
                ( 'KFSE',(115,293),),
                ( 'KHIB',(262,310),),
                ( 'KMSP',(271,85),),
                ( 'KMVE',(116,88),),
                ( 'KRHI',(493,149),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (141,268),'Brainerd',),
                ( (379,377),'Grand Marais',),
                ( (534,330),'Hancock',),
                ( (294,292),'Duluth',),
                ( (368,151),'Eau Claire',),
                ( (74,365),'Fosston',),
                ( (224,382),'Hibbing',),
                ( (209,157),'Minneapolis',),
                ( (71,161),'Montevideo',),
                ( (430,221),'Rhinelander',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalObservationMap', d, 0)
# MAP: 51201
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(20523,15403),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(272,218),
             datacutType='radar.us',
             datacutCoordinate=(2115,1549),
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
              ( ( (263,173),'35',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (377,98),'53',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (377,98),'53',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (263,173),'35',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (173,308),),
                ( (248,92),),
                ( (408,273),),
                ( (249,330),),
                ( (353,239),),
                ( (432,119),),
                ( (360,222),),
                ( (574,383),),
                ( (90,175),),
                ( (599,189),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (173,308),),
                ( (248,92),),
                ( (408,273),),
                ( (249,330),),
                ( (353,239),),
                ( (432,119),),
                ( (360,222),),
                ( (574,383),),
                ( (90,175),),
                ( (599,189),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (114,291),'Grand Rapids',),
                ( (211,113),'Pine City',),
                ( (425,291),'Two Harbors',),
                ( (219,351),'Hibbing',),
                ( (328,260),'Duluth',),
                ( (395,140),'Hayward',),
                ( (376,212),'Superior',),
                ( (515,366),'Grand Marais',),
                ( (110,178),'Brainerd',),
                ( (503,192),'Ironwood',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (114,291),'Grand Rapids',),
                ( (211,113),'Pine City',),
                ( (425,291),'Two Harbors',),
                ( (219,351),'Hibbing',),
                ( (328,260),'Duluth',),
                ( (395,140),'Hayward',),
                ( (376,212),'Superior',),
                ( (515,366),'Grand Marais',),
                ( (110,178),'Brainerd',),
                ( (503,192),'Ironwood',),
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
wxdata.setInterestList('airportId',['DLH','FAR','FSD','MSP',])
wxdata.setInterestList('coopId',['72634030','72638041','72643059','72658000','72741038','72741047','72744000','72744030','72745000','72745008','72745013','72745019','72745021','72745025','72745027','72745028','72745050','72747000','72750008','74341013','74341057',])
wxdata.setInterestList('indexId',['KDLH',])
wxdata.setInterestList('pollenId',['DLH',])
wxdata.setInterestList('obsStation',['KBRD','KCKC','KCMX','KCOQ','KDLH','KDYT','KEAU','KEVM','KFAR','KFSD','KFSE','KHIB','KHYR','KMSP','KMVE','KMZH','KRHI','KSUW','KTWM',])
wxdata.setInterestList('climId',['212246','212248',])
wxdata.setInterestList('zone',['MNZ037',])
wxdata.setInterestList('aq',['zz001',])
wxdata.setInterestList('skiId',['616002','616006',])
wxdata.setInterestList('county',['MNC137','WIC031',])
dsm.set('countyNameList',[('MNC137','Saint Louis'),('WIC031','Douglas'),], 0)
#
dsm.set('dmaCode','676', 0)
dsm.set('secondaryObsStation','KSUW', 0)
dsm.set('primaryClimoStation','212246', 0)
dsm.set('primaryIndexId','KDLH', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','MN', 0)
dsm.set('primPollenSiteName','Duluth', 0)
dsm.set('expRev','617375', 0)
dsm.set('primaryCoopId','72745000', 0)
dsm.set('PlaylistOverride','DefaultUS', 0)
dsm.set('wda','DLH', 0)
dsm.set('primaryCounty','MNC137', 0)
dsm.set('primaryObsStation','KDLH', 0)
dsm.set('primaryLat',46.76583, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','DLH', 0)
dsm.set('Clock','scmt.clock', 0)
dsm.set('primaryLon',-92.11889, 0)
dsm.set('primaryZone','MNZ037', 0)
dsm.set('climoRegion','2', 0)
dsm.set('SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','CHARTER COMMUNICATIONS', 0)
dsm.set('headendId','023812', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','DOM - DULUTH - DOM', 0)
dsm.set('msoCode','01148', 0)
dsm.set('headendName','DOM - DULUTH - DOM', 0)
dsm.set('affiliateNumber','01010', 0)
dsm.set('zipCode','55811    ', 0)
dsm.set('bcNetMask','255.255.255.248', 0)
dsm.set('bcConnectMethod','E', 0)
dsm.set('irdSlave','0', 0)
dsm.set('starId','TWCD04040027', 0)
dsm.set('bcDialInNumber','218-727-3730', 0)
dsm.set('bcGateWay','24.158.21.97', 0)
dsm.set('bcIpAddress','24.158.21.98', 0)
#
wxdata.setTimeZone('CST6CDT')
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
d.airportId = ['MSP','FAR','FSD',]
d.airportLocName = ['Minneapolis','Fargo','Sioux Falls',]
d.obsStation = ['KMSP','KFAR','KFSD',]
dsm.set('Config.0.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.0.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['616006','616002',]
d.coopId = ['72638041','72634030',]
d.resortName = ['Crystal Mtn, MI','Boyne Highlands, MI',]
dsm.set('Config.0.Tag.General.snowboardData', d, 0, 1)
#
scmtRemove('Config.0.Ldl_LASCrawl')
scmtRemove('Config.0.LASCrawl')
#
d = twc.Data()
d.serialNum=177499
d.crawls=[
(1089172800,1089518399,[(0,23)],'Be there live July 8th through the 11th for the ESPN Great Outdoor Games at the Alliant Energy Center in Madison WI. It\'s FREE and FUN for the whole family.'),
(1089259200,1089518399,[(0,23)],'Join us at the Iron River Community Center Sunday July 11th, 8am - 1pm for a Pancake Breakfast Fundraiser to send the Wisconsin Super-Hoops U12 Basketball team to the Nationals in Lexington, Kentucky. Tickets are $5, only $3 for children 10 and under'),
(1091505600,1094875199,[(0,23)],'Come see STIHL TIMBERSPORTS September 11th at the Chippewa Falls Fair Grounds in Chippewa Falls Wisconsin. Tickets and information available at www.chippewavalley.net or call 715 831 2345'),
(1091764800,1093924799,[(0,23)],'There\'s a whole lot of breakfast going on now at Taco John\'s. The new breakfast menu offers great West Mex favorites like Egg Burrito, Bravo Scrambler or Breakfast Quesadilla...now being served every morning. Visit us today in Duluth, Cloquet, Superior, Grand Rapids and Hibbing.'),
(1095048000,1095739199,[(0,23)],'FREE PREVIEW of The SPORTS TIER, 9.09 through 9.20. Check out the NFL NETWORK on channel 412. FUEL on channel 410 and ESPNews on channel 408. Call 1 888 GET CHARTER.'),
(1095652800,1095825599,[(0,23)],'Attend the important School Board meeting regarding closure of Piedmont, Grant and Chester Park schools. Meeting is Tuesday 9.21.2004, 6:30pm in Board Room at Central Administration Building. Meeting will also be televised on Channel 22 on Charter Communications in Duluth.'),
(1095393600,1099195199,[(0,23)],'Oktoberfest at Buena Vista Restaurant and Lounge-featuring authentic German cuisine, apple cider, pork tenderloin, chicken schnitzel, German beer and more, served just the way you like it. Full service bar, banquet facilities and catering. Buena Vista Restaurant and Lounge.'),
(1096516800,1096862399,[(0,23)],'Security Jewelers\' 80th Anniversary Celebration now through Saturday. Special purchase of round and princess cut diamonds-limited numbers. Special values on watches and gifts throughout the store. SECURITY JEWELERS - ROCK SOLID for 80 years. Downtown Duluth'),
(1096603200,1097294399,[(0,23)],'Attention Charter customers...effective October 8th, the Charter Channel (channel 19) will no longer be shown.'),
(1097553600,1099288799,[(0,23)],'Hooked on great movies? New in October on Charter Pay Per View...Oct. 14 \'Man On Fire\' and \'Scooby Doo 2,\' Oct. 22 \'Soul Plane\' and \'The Ladykillers,\' Oct. 30 \'The Passion Of The Christ.\' Only $3.99 each. Order Today'),
(1097553600,1104559199,[(0,23)],'Attention Charter customers? Do you feel the need for speed? Add our blazing fast 3 Megabyte Internet service for only $29.99 per month for the next three months. Call 1 888 GET CHARTER today.'),
(1097553600,1104559199,[(0,23)],'Charter Digital\'s BIG, BIGGER and BIGGEST packages mean more movies at the best value for our customers. Get ready to fulfill the cravings of millions of kids, movie buffs, sports fans, and TV fanatics as Charter grows bigger and better than ever. Call 1 888 GET CHARTER today'),
(1097553600,1104559199,[(0,23)],'Did you know satellite companies can raise their rates at any time, even when you\'ve signed a long term contract. Charter doesn\'t have any long term obligations to trap you in. We know you\'ll stay...because our service is worth keeping! Call 1 888 GET CHARTER today'),
(1097553600,1104559199,[(0,23)],'With Charter, rain won\'t stop you from watching your favorite programs, sports and special events. With satellite TV, weather may interrupt the signal to your dish, leaving you with no or bad reception for hours at a time. For GOOD RECEPTION always, call 1 888 GET CHARTER today.'),
(1099288800,1103176799,[(0,23)],'The perfect holiday gift - a gift certificate from the Buena Vista Restaurant, in any denomination to fit anyone\'s budget, Reserve your holiday party or banquet at the Buena Vista. Banquet facilities and a full service bar. LUTEFISK served for the holidays. Call 7 2 2  9 0 4 7'),
(1099980000,1103954399,[(0,23)],'NEW NFL licensed, HIGH TECH titanium team jewelry from Security Jewelers. With purchase of Viking or Packer ring or bracelet, Security donates $5.00  to organizations in Minnesota and Wisconsin that provide Christmas toys to kids. Order at vikingsrings.com or packersrings.com'),
(1100584800,1101103199,[(0,23)],'Soak up the savings during Beachcomers Hot Tubs end-of-season clearance sale!  Enjoy discounts on all in-stock hot tubs, plus save up to $500 off floor models.  Prices good while supplies last at Beachcomers Hot Tubs, 4881 Miller Trunk Highway, Hermantown.'),
(1100844000,1103608799,[(0,23)],'On December 20, 2004, Charter viewers will see some changes to the channel line-up. Please watch for more information in your Charter billing and in the newspaper. If you have questions, please call Charter Customer Service - 800 581 0081.'),
(1102485600,1103608799,[(0,23)],'Free Financing up to 36 months at Robert\'s Home Furnishings and Sleepcenters during the Giant Holiday Sale on NOW. Save 30-50% on all name brands - Flexsteel, Lane, King Koil and Sealy. Sofas, recliners, gliders, curios, oak dining and bedroom sets. Nobody beats Robert\'s, NOBODY'),
(1103004000,1104559199,[(0,23)],'Could you use some cash today? It\'s easy. If you have a clear vehicle title and you live in the Duluth Superior area, call us at 398 4448. Caught short between paychecks? Lowest interest payday loans in the area. Cash today and NEVER a credit check. Title Loan Co.  3 9 8  4 4 4 8'),
(1103349600,1103781599,[(0,23)],'The Union Gospel Mission is in need of toys for children 1-16 years of age. Please drop off a new, unwrapped toy at The Union Gospel Mission, 219 E. First St., or at Charter Communications, 302 E Superior St. Your gift will help make a child\'s Christmas brighter. Thank you.'),
(1104386400,1104991199,[(0,23)],'Great deals from Abby Travel. Cancun from $299, Air/hotel from $499. Cozumel from $309, air/hotel from $569. Ixtapa $220, a/h from $638. Las Vegas $149, a/h from $189. Jamaica from $140, a/h from $400. Orlando $129, a/h from $218. Book today. Abby Travel, 727 3851'),
(1105682400,1107669599,[(0,23)],'GOLF 2005 - Call Turtleback in Rice Lake, 715 234 7641. Pre-book your golf group of 12 or more between now and SuperBowl Sunday and receive a dozen FREE GOLF BALLS. Call now - play later. Turtleback in Rice Lake, 715 234 7641.'),
(1106805600,1108274399,[(0,23)],'Join in the FUN at the 4th Annual Grand Casino \'Hook And Slice On Ice\' Rotary Golf Classic, Saturday February 12th at Chub Lake in Carlton. Tee times are 9am and 1pm. For tickets and more information, please call 800 625 4661. Sponsored by The Cloquet Rotary. See you there.'),
(1107842400,1110779999,[(0,23)],'Hey Cookie Lovers...the Girl Scouts are back! The annual Girl Scout Cookie Sale begins Saturday, Feb 19. Eight varieties - only $3.50 per box. THIN MINTs, SAMOAs, TAGALONGs, TREFOILs, DO-SI-DOs, ALL ABOUTs, DOUBLE DUTCH, and LEMON COOLERs. Cookie Hot Line - 218 726 4710'),
(1108101600,1108965599,[(0,23)],'It\'s the 39th Annual Duluth Boat, Sports and Travel Show, Wednesday - Sunday, Feb 16th - 20th at the DECC. Entertainment provided by T G Sheppard, musical comedy from Johnny Matson. It\'s the best entertainment value in town, and it\'s all at the DECC - Feb. 16 through 20'),
(1107928800,1108274399,[(0,23)],'Join the American National Ballet February 11 + 12 at St. Scholastica\'s Mitchell Auditorium for A Renaissance In Dance. Tickets for the American National Ballet\'s Feb 11 + 12 performances available @ www.css.edu/mitchell or call 723 7000. American National Ballet, Feb 11 + 12.'),
(1108015200,1108706399,[(0,23)],'It\'s Chocolate and Flowers Weekend at Indianhead Mountain in Wakefield Michigan. The Lodge Restaurant has the Friday Seafood Buffet and the Saturday Grande Buffet. LIVE MUSIC in Dudley\'s - 9pm Friday and Saturday. Call 1 800 3INDIAN'),
(1108447200,1108879199,[(0,23)],'It\'s President\'s Pajama Party Weekend at Indianhead Mountain Resort. Dress as your favorite president - in their pajamas. Kids\' contest Saturday at 1 pm in the Summit Center, adults\' contest at 10 pm at Dudley\'s. Call 1 800 3Indian for more nformation.'),
(1108533600,1108965599,[(0,23)],'Save 25% to 50% on all Presidential quality furniture at Robert\'s Home Furnishings\' Presidents\' Day Sale ON NOW. Plus, Robert\'s pays all sales tax. Sofa-Loveseat combos only $799 for both pieces. Flexsteel sofas, sleepers + recliners all on sale. Nobody beats Robert\'s - NOBODY'),
(1109138400,1109483999,[(0,23)],'This Saturday is the BIG AIR Contest at Indianhead Mountain Resort...begins at 1 pm in the Terrain Park. Skier and snowboarder divisions. Call 1 800 3INDIAN for more information or visit www.indianheadmtn.com. The fun never ends at Indianhead Mountain Resort.'),
(1109224800,1112759999,[(0,23)],'On April 5, 2005, Charter customers will see a change to their Basic Line-up. C Span 2 will move to Channel 19 and Charter Main Street will move to Channel 15. If you have any questions, please contact Customer service at 800 581 0081. Thank you'),
(1109570400,1115006399,[(0,23)],'Taco John\'s new grilled Fajitas are sizzling with chicken or steak, onions, peppers, and all the fixings. Visit us in Duluth at Miller Hill Mall, on London Road and Grand Avenue. Tower Ave. in Superior, and in Cloquet, Hibbing and Grand Rapids. Taco John\'s new grilled Fajitas.'),
(1109829600,1110088799,[(0,23)],'Catch the Wisconsin State Championships in Boys\' and Girls\' hockey - Saturday at Noon and 2pm on Charter channel 25. Great hockey action. Catch the Wisconsin State Championships in Boys\' and Girls\' hockey - Saturday at Noon and 2pm on Charter channel 25'),
(1110434400,1110520799,[(10,19)],'TONIGHT on WDSE, your local PBS affiliate. Harbor History III - Modern Harbor, World Port(1954-1980) 7pm. At 8:30 pm, watch the Chmielewski Funtime Reunion. WDSE is on Charter channel 12 in Duluth and Superior.'),
(1110520800,1110693599,[(0,23)],'The Holocaust Survivors program scheduled for Saturday March 12 at the Richard I. Bong Heritage Center has been postponed. Call 715 392 7151 if you have questions.'),
(1110780000,1111298399,[(0,23)],'WIAA Boys basketball tournament this weekend on Charter channel 25. Coverage begins Thursday morning at 9:00. Check channel 25 for a schedule of telecasts.'),
(1110780000,1111384799,[(0,23)],'Come to Iron River Sports\' Anniversary Sale going on now at Mariner Mall in Superior and the Iron River location. All fishing, recreational and pontoon boats, PWC, ATVs, and motorcycles on sale with HUGE DISCOUNTS. Call 715 372 5252 or 715 392 5252. Sale ends March 20.'),
(1110952800,1112421599,[(0,23)],'Register for the MS 150 Bike Tour presented by GMAC-RFC at www.ms150.com or register for the MS TRAM Bike Tour at www.msTRAM.com. The MS 150 and MS TRAM Bike Tours both start in Duluth. Call 1 800 FIGHT MS for details.'),
(1111384800,1112421599,[(0,23)],'MARCH MADNESS AT TURTLEBACK! Final Foursome Special. 18 holes with cart - only $99. Call 715 234 7641. BUY NOW BEFORE APRIL 15th, play later. MARCH MADNESS FINAL FOURSOME $99. Only at Turtleback in Rice Lake. CAll 7 1 5  2 3 4  7 6 4 1'),
(1113537600,1114919999,[(0,23)],'Turtleback Golf in Rice Lake is now open. FORE a great day of golfing...play Turtleback Golf in Rice Lake Call 715 234 7641 for information and tee times. Turtleback Golf in Rice Lake is NOW OPEN. Call 715 234 7641 for tee times'),
(1111557600,1112162399,[(0,23)],'Kindergarten Round-up, Wednesday, March 30, 2005, 10 am at St. John\'s School in Woodland. St. John\'s School offere full day Kindergarten in a disciplined, faith based environment. Call 218 724 9392 for more details or go to our website - www.stjohnsduluth.org'),
(1111557600,1111730399,[(0,23)],'Are you a young professional in the Duluth area? Join us for a special event in the lobby of the Technology Village, Thursday, March 24, at 4:45 pm. This Young Professionals Introductory Event is sponsored by Duluth Area Chamber Of Commerce. RSVP to 218 722 5501'),
(1112162400,1113191999,[(0,23)],'Catch the MLB Extra Innings Free Preview on channels 865 - 874, April 4th through April 10th. Watch the games nobody else can see unless they have Charter iNDEMAND. Get Hooked on Major League Baseball with MLB Extra Innings. Call for more information - 800 581 0081'),
(1112076000,1114401599,[(0,23)],'A family tradition since 1954, Sammy\'s Pizza And Restaurant has been voted the Northland\'s Best Pizza year after year. What\'s the secret? The secret is in the sauce. Visit us in Duluth, Cloquet, Grand Rapids and Hibbing. Sammy\'s Pizza And Restaurant. COME ON OVER.'),
(1112335200,1113191999,[(0,23)],'It\'s the 39th Anuual Home And Builders Show at the DECC, April 6th - 10th. Best Entertainment value in town. Over 80 vendors, daily stage shows by The Fifth Dimension. Register for prize giveaways and exhibitor discounts. Fun and excitement at the DECC, April 6th - 10th'),
(1116993600,1120190399,[(0,23)],'Whitewater Lake lakeshore lots near Giant\'s Ridge Golf and Ski Resort offer city water, sewer and paved street, exclusively offered by Minnesota Power\'s ShoreLand Traditions, premier managed lakeshore leasing program. Find more information about the lots at www.mpland.com.'),
(1113364800,1113710399,[(0,23)],'Eleven hours to save 20 to 50% at Slumberland Furniture this Saturday only. Ask about financing till 2007 from 10am until 9pm. Only at Slumberland, furniture that lives the way you do. Maple Grove Road, across from Sam\'s Club.'),
(1113537600,1114315199,[(0,23)],'Pure Golf at amazing rates has arrived. Big Fish Golf Club of Hayward is open and is in great shape. DESIGNED BY THE LEGENDARY PETE DYE. Very reasonable $35 spring special includes a cart. Call 715 934 4770 or www.bigfishgolf for details. Pure Golf - Amazing Rates.'),
(1113883200,1114401599,[(0,23)],'Tune in to the NFL Draft on ESPN, channel 34, Saturday, April 23, 11am - 4:30pm and Sunday. April 24, 10am - 5pm. ESPN2, channel 35 will provide coverage Saturday 4:30pm - 9pm'),
(1114142400,1115092799,[(0,23)],'Mark your calendars for the 27th Annual Bids For Kids Auction to benefit the Boys and Girls Club, to be held May 3rd at Grandma\'s Sports Garden. Bid on a 4 Day Miami NASCAR trip, a one carat diamond ring and more while enjoying free appetizers. Bids For Kids Auction, May 3rd'),
(1114401600,1114919999,[(0,23)],'April is Child Abuse Prevention Month in Minnesota. Wear a blue ribbon to show that you care, and help us make sure that it doesn\'t hurt to be a child.'),
(1115006400,1115524799,[(0,23)],'Don\'t miss Mobile Housing and RV\'s Spring Open House, May 2-7. Save BIG $$$ on manufactured homes, travel trailers and 5th wheels. Financing available. Open Mon-Thurs 8-8, Fri and Sat 8-5. Mobile Housing and RV Open House, May 2-7, next to Menards on Hwy 53, Duluth.'),
(1115006400,1116215999,[(0,23)],'Stop by your local Super One grocery store from Wed. May 11th through Sat. May 14th and support the Knights Of Columbus as they will be raising funds for the Shriners Hospital in Minneapolis. Enjoy a hot dog, chips and a soda for only $1.25. Please support this community event.'),
(1116216000,1119239999,[(0,23)],'Support Arts, Culture and History in Duluth. Send a gift to the 506 Fund. This fund drive supports the 9 organizations at the St Louis County Heritage and Arts Center/The Depot. Please send your gift to: 506 Fund, 506 West Michigan Street, Duluth MN 55802. Thank you.'),
(1116302400,1116734399,[(0,23)],'Park and save during Beachcomber Hot Tubs\' Parking Lot Sale. Save up to $1,900 on the Beachcomber Limited Edition package. Sale prices are good this Friday, Saturday and Sunday at Beachcomber Hot Tubs, 4881 Miller Trunk Highway.'),
(1116302400,1118894399,[(0,23)],'17th Annual Bayfront Blues Festival, August 11-14. Tickets on sale now at Bayfrontblues.com ... 17th Annual Bayfront Blues Festival, August 11-14. Tickets on sale now at Bayfrontblues.com ...'),
(1116302400,1116734399,[(0,23)],'Please join us for Mayflower Fest, Saturday, May 21st at Chester Bowl, 10am - 4pm. Rock-A-Billy  Revue LIVE, 2-4. Gifts, crafts and food vendors. Family Fun all day. Shuttles from parking at UMD all day.'),
(1117598400,1118030399,[(0,23)],'Please join your neighbors for a silent auction and spaghetti dinner at Mr D\'s - June 5th @ 3pm for Lisa Winklesky Greene, who is battling Lupus. June 5th @ 3 pm  - Mr D\'s - Benefit for Lisa Winklesky Greene. Thank you.'),
(1117598400,1119758399,[(0,23)],'Attention Military Families! Please join Younkers for Military Appreciation Day - Saturday June 25. Free Lunch - 12-1:30, 20% off most merchandise with military ID. Special discounts in the Salon and Cosmetic departments. Details in Sunday, June 19th Duluth News Tribune.'),
(1117771200,1118289599,[(0,23)],'The Medical Assistant program at DBU is sponsoring a dunk tank and car wash in their parking lot - Wednesday June 8, 10:30am-2:30pm. Dunk Mayor Herb Bergson and other local personalities for a good cause - all proceeds going to Lifehouse - Mark it down - Wednesday, June 8th.'),
(1117771200,1119153599,[(0,23)],'The Medical Assistant program at DBU is sponsoring a Block Party and Spaghetti Dinner at JT\'s Bar And Grill in Superior, June 18th. Tickets available at DBU and at JT\'s Bar And Grill. All proceeds going to LifeHouse.'),
(1118980800,1119931199,[(0,23)],'It\'s time for the 35th Annual Park Point Art Fair, June 25-26 From 10AM to 5PM at the end of Park Point.  Come shop the works of 110 artists working in clay, wood, 2D, fiber and metal.  Food court, free parking & admission. Info: www.parkpointcommunityclub.org or 715-398-5970'),
(1119326400,1119931199,[(0,23)],'The Lake Superior Garden Center, GRAND OPENING SALE! Friday, June 24 through Sunday, June 26 in Duluth at 5137 Jean Duluth Road and in Superior at 2704 North 21st Street.'),
(1119326400,1120190399,[(0,23)],'It is Morgan Park Class reunion time! Classes 1974, 1975, 1976, 1977 are set for Saturday, July 23rd at Buffalo Junction. Are you registered? Deadline is Friday, July 1st. Call Brad at 218-626-2004...Let\'s get clicking, classes!'),
(1119326400,1119844799,[(0,23)],'Haugfest, Sunday, June 26th, featuring the Doobie Brothers, Big Head Todd and the Monsters, and Martin Zellar. Ole Haugsrud Field, on the UWS campus, Superior, Wisconsin. Gates open at 2:00 PM. For ticket information call: 218-727-2121'),
(1119412800,1120535999,[(0,23)],'SUPER BUYS @ WHERLEY MOTORS in International Falls-New 04 Dodge Stratus SXT-14,900*(save $6750)! New 04 Chrysler Concorde LX-$17,457*(save $8378)! New 04 Chrysler 300 M Special includes Navigation,Sirius Satellite Radio-Loaded-$25,590*(save $9045)!(*all rebates to dealer).'),
(1125288000,1131515999,[(0,23)],'DULUTH,STOP WASTING MILLIONS OF $ BEFORE INCREASING TAXES 11.5%.HANSEN CAN RUN THE CITY CHECKBOOK LIKE YOU RUN YOUR OWN,PRIORTIZE ESSENTIAL SPENDING;POLICE,FIRE,NEW HIGH PAYING JOBS,STREETS and SEWERS. Paid for by the HANSEN for Council Volunteer Committee. WWW.HANSENATLARGE.COM.'),
(1120708800,1121486399,[(0,23)],'Join UWS in the Yellowjacket Hall Of Fame Golf Outing, July 22nd. Shotgun starts at noon and 12:30 at Nemadji Golf Course. Includes up to two carts per team, green fees, steak dinner, shirt, team awards and proximity prizes. Call for info. 394 8452 or 888 893 8593'),
(1120795200,1121745599,[(0,23)],'Set the date! Monday, July 18th. Spaghetti Benefit Dinner for Cindy Parker at Mr. D\'s Bar and Grill. Dinner starts at 5pm. Adults $10, children 10 and under $5. Silent Auction and prizes will be awarded.'),
(1121400000,1122263999,[(0,23)],'Now at the Omnimax! Charlie And The Chocolate Factory. Get your \'Golden Ticket\' today for this extraordinary event on the huge domed screen. Johnny Depp as Willy Wonka, and the most magnificent Chocolate Factory. Showtimes-11am, 2:10pm, 5:20pm and 8:30pm. Omnimax at the DECC.'),
(1121659200,1123473599,[(0,23)],'Slumberland Furniture\'s Anniversary Sale is going on NOW. Register to win a 2005 Ford Escape Hybrid. Get 0% interest for 38 months. Inquire at store for details. Slumberland Furniture on Maple Grove Road across from Sam\'s Club.'),
(1121745600,1122350399,[(0,23)],'It\'s the funniest show in Minnesota. COMEDY KINGS Louie Anderson, Scott Hansen and Jeff Cesario LIVE at Grandma\'s Sports Garden, Monday, July 25th - 7:00 and 9:30pm. Save $10 on advance tickets at Grandma\'s, Miller Hill and Canal Park. Grandma\'s Sports Garden in Canal Park.'),
(1121918400,1122782399,[(0,23)],'Motocross Racing at State Line Motocross, Saturday, July 30th in Ironwood, Michigan. Many kids\' classes and trophies, perfect race for beginnings and intermediate riders. 100% payback on \'A\' classes. Call 906 663 4070 or visit www.gogebiccountyfair.com'),
(1122436800,1124078399,[(0,23)],'Legendary StormChaser and Photojournalist Alex Sahlberg, creater of Real WX Extreme Northland, thanks you for celebrating his life w/prayers gift cards and emails. Especially MN StormChasers, News 6 and Harbor City HS. In memory of Vortex Alex Stormchasing Spirit of The Northland'),
(1123473600,1123819199,[(16,11)],'The State of Hockey is coming to Duluth! Meet Minnesota Wild personalities and put your signature on the official \'State of Hockey\' Flag, Thursday, August 11th from 11am to 12:30pm at the Wells Fargo Bank Downtown Duluth. Minnesota Wild, Thursday at Wells Fargo Bank Downtown.'),
(1123819200,1124510399,[(0,23)],'Reward: $1000 for catching the Largest Walleye at the 4th Annual HAWG Walleye Contest Aug. 20-21 at Island Lake to benefit the Boy Scouts. Get tickets at area bait shops. Lots of fun and prizes at the HAWG Walleye Contest Aug 20-21 at Island Lake, benefiting the Boy Scouts.'),
(1124337600,1124596799,[(0,23)],'Come celebrate Proctor\'s heritage at the Hoghead Festival this weekend! Saturday\'s activities include parade at noon, merchandise, food and craft vendors all day, Kids Korner Activities 1-4, Fireworks at 9:45 and a Street Dance till midnight! Please join in on the FUN!'),
(1124424000,1125201599,[(0,23)],'Join us Sat. Aug 27, 10am-6pm for the Public Safety Expo at the Hermantown Police Department! Police Rescue Canines, Police Motorcycling, Taser Demo, Rappeling...the MSP and Lukes One Helicopter and more! Exciting demos every half hour! Public Safety Expo, Saturday, Aug 27 10-6!'),
(1124510400,1126929599,[(0,23)],'Re-elect Neill Atkins 4th District City Council. Re-elect Neill Atkins 4th District City Council. Re-elect Neill Atkins 4th District City Council. Re-elect Neill Atkins 4th District City Council. Re-elect Neill Atkins 4th District City Council. Paid by Atkins Volunteer Committee'),
(1124942400,1126065599,[(0,23)],'Charter Media wants you to be a part of \'Miss Saigon.\' Tell us, in fifty words or less, why you DO NOT want to miss \'Miss Saigon.\' You could win two tickets. Send your essay to Charter Media, Suite 200, 230 East Superior Street, Duluth MN 55802 by September 6th.'),
(1126497600,1132639199,[(0,23)],'M&I Bank. Experience banking the way it was meant to be. Visit your neighborhood M&I Bank or mibank.com today. M&I Bank. Experience banking the way it was meant to be. Visit your neighborhood M&I Bank or mibank.com today. M&I Bank. Experience banking the way it was meant to be.'),
(1127188800,1130039999,[(0,23)],'Charter presents \'Women Rock\'-a breast cancer fundraiser. Featuring national headliner-Jo Dee Messina, Sun Oct 23 @ the DECC! VIP tickets available: include pre-party & meet and greet. Tickets on sale NOW! Jo Dee Messina, Oct 23 @ the DECC. www.charterwomenrock.com'),
(1127275200,1130558399,[(0,23)],'Charter presents \'Women Rock\'-a breast cancer fundraiser. Enjoy a relaxing women\'s retreat-Sat Oct 29 @ the Holiday Inn. Free admission, pampering, hourly prizes, Maurices fashion show, Madill dancers, plus displays w/area products & services! www.charterwomenrock.com'),
(1127275200,1138859999,[(0,23)],'\'Dear Auntie, Why Me?\' an informative, thoughtful book about a Duluth woman\'s journey from breast cancer diagnosis to remission. Causes, detection and treatment. Get it at J.W.Beecroft, Twin Ports Bible and Book, Northern Lights. breastcancer-book.com or call 525 1905.'),
(1127966400,1133243999,[(0,23)],'PACKER FANS: This and every Wednesday at 7:30 pm, join us for the \'Green & Gold Show!\' A behind-the-scenes look at players, coaches and tailgaters too! Sponsored by Rockdale Garden Center and Les Bird\'s Bar. Every Wednesday at 7:30 pm on Charter Main Street, channel 15.'),
(1127966400,1128052799,[(10,21)],'PACKERS FANS: Tonight at 8:30 pm, a special showing of the \'Green & Gold Show!\' A behind-the-scenes look at players, coaches and tailgaters.  Sponsored by Rockdale Garden Center and Les Bird\'s Bar. The Green & Gold Show tonight at 8:30 on Charter Main Street, channel 15.'),
(1128398400,1449467999,[(0,23)],'Charter Communications\' new office at Miller Hill Mall is NOW OPEN across from Great American Grill. Hours are normal mall hours - 10am-9pm Monday through Friday, 10am-7pm on Saturday and 11am-6pm on Sundays.'),
(1128398400,1130644799,[(0,23)],'Join us: Race, Culture And The Achievement Gap Summit - Your voice is needed to help identify issues and solutions. Lincoln Park School, 2424 West Fifth Street, Friday October 28, 4pm to 9pm and Saturday, October 29, 8:30am to 5pm. Call for more info - Alanna Oswald 628 4881'),
(1129262400,1130644799,[(0,23)],'Historic Halloween Howl Costume Party Saturday, October 29th. Old Berger Hardware sets the stage for this event - with dinner, live band, contests and PRIZES. Saturday, October 29th. Call 715 392 8449.'),
(1129608000,1130644799,[(0,23)],'Relax, pamper yourself and have some fun at \'A Taste Of Italy,\' a Women\'s Retreat presented by Charter Communications, Duluth Clinic Breast Program and B-105...Saturday October 29 at the Great Lakes Ballroom at Holiday Center, 9am - 5pm. Free Admission. Help fight Breast Cancer.'),
(1133848800,1133935199,[(15,21)],'Charter College Hockey-TONIGHT! Mankato St. vs Notre Dame...7:30pm Cable Channel 15, Charter Main Street...Charter College Hockey-TONIGHT! Mankato St. vs Notre Dame...7:30pm Cable Channel 15.'),
(1130824800,1131429599,[(0,23)],'BOB HANSEN, YOUR VOTE FOR CHANGE, PRIORITIZE SPENDING, SAFE NEIGHBORHOODS, POLICE, FIRE, STREETS, NEW HIGH PAYING JOBS. BUILD HOCKEY CENTER IN WEST DULUTH, HELP UMD NEIGHBORS, NO TO SPECIAL INTERESTS, NO NEW TAXES. Paid by Hansen for Council Volunteer Committee. hansenatlarge.com'),
(1132120800,1132725599,[(0,23)],'Soak up all the savings during Beachcomber Hot Tub\'s end of season Close Out Sale. Enjoy discounts on all in-stock hot tubs, plus save up to $500 on floor models. Prices good while supplies last at Beachcomber Hot Tubs, 4881 Miller Trunk Highway.'),
(1132034400,1133675999,[(0,18)],'UMD HOCKEY...LIVE...THIS FRIDAY AND SATURDAY NIGHT... UMD AT MANKATO STATE, LIVE ON CHARTER  CABLE CHANNEL 15...UMD HOCKEY THIS WEEKEND LIVE, CHANNEL 15 FROM MANKATO ON CHARTER MAIN STREET, CABLE CHANNEL 15...'),
(1132207200,1136095199,[(10,18)],'Nations Trust Open House Show. Tune in to cable channel 15 every Friday, Saturday and Sunday morning at 9:30 to plan your open house \'hunting.\' Not one realtor, but many realtors involved!! Presented by Nations Trust, 312 West Superior Street, Duluth.'),
(1132293600,1132811999,[(0,23)],'Many Twin Ports families are in need of turkey, stuffing, veggies and butter for their Thanksgiving meal. Please make a family\'s Thanksgiving complete by donating one of these items to the Union Gospel Mission, 219 1/2 East First Street. Thanks for supporting this worthy cause.'),
(1133416800,1138341599,[(15,23)],'Join the Powerhouse Bar for Texas Hold \'Em every Thursday night for your chance to win your share of prizes and Powerhouse Bucks! Call the Powerhouse for details 624-0626. Powerhouse Bar, 423 3rd Ave in Proctor.'),
]
dsm.set('Config.0.Ldl_LASCrawl', d, 0)
dsm.set('Config.0.LASCrawl', d, 0)
#
#
scmtRemove('Config.0.Local_MarineForecast')
scmtRemove('Config.0.Local_Satellite')
scmtRemove('Config.0.Local_OutdoorActivityForecast')
scmtRemove('Config.0.Ldl_UVForecast')
scmtRemove('Config.0.Fcst_TextForecast')
scmtRemove('Config.0.Local_TrafficFlow')
scmtRemove('Config.0.Local_SchoolDayWeather')
scmtRemove('Config.0.Ldl_ExtendedForecast')
scmtRemove('Config.0.Local_CurrentConditions')
scmtRemove('Config.0.Ldl_TravelForecast')
scmtRemove('Config.0.Local_EventForecast')
scmtRemove('Config.0.Local_LocalObservations')
scmtRemove('Config.0.Local_TrafficReport')
scmtRemove('Config.0.Local_RecordHighLow')
scmtRemove('Config.0.Ldl_SunriseSunset')
scmtRemove('Config.0.Local_Climatology')
scmtRemove('Config.0.Local_Almanac')
scmtRemove('Config.0.Ldl_NationalStarIDMessage')
scmtRemove('Config.0.Local_7DayForecast')
scmtRemove('Config.0.Local_HeatSafetyTips')
scmtRemove('Config.0.Ldl_CurrentApparentTemp')
scmtRemove('Config.0.Ldl_AirQualityForecast')
scmtRemove('Config.0.Local_NWSHeadlines')
scmtRemove('Config.0.TimeTemp_Default')
scmtRemove('Config.0.Ldl_TrafficTripTimes')
scmtRemove('Config.0.Local_TrafficOverview')
scmtRemove('Config.0.Local_Tides')
scmtRemove('Config.0.Ldl_AirportDelayConditions')
scmtRemove('Config.0.Local_TextForecast')
scmtRemove('Config.0.Local_GetawayForecast')
scmtRemove('Config.0.Local_DaypartForecast')
scmtRemove('Config.0.Fcst_ExtendedForecast')
scmtRemove('Config.0.Cc_CurrentConditions')
scmtRemove('Config.0.Ldl_LocalStarIDMessage')
scmtRemove('Config.0.Fcst_DaypartForecast')
scmtRemove('Config.0.Local_AirQualityForecast')
scmtRemove('Config.0.Local_ExtendedForecast')
#
d = twc.Data()
d.locName = 'Duluth-Superior Metro'
d.coopId = '72745000'
dsm.set('Config.0.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KDYT','KSUW','KCOQ','KMZH','KHIB','KEVM','KTWM','KHYR',]
d.locName = ['Duluth-Harbor','Superior','Cloquet','Moose Lake','Hibbing','Eveleth','Two Harbors','Hayward',]
dsm.set('Config.0.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.climId = '212246'
d.latitude = 46.77
d.longitude = -92.08
dsm.set('Config.0.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['International Falls','Minneapolis','Hancock',]
d.coopId = ['72747000','72658000','72744000',]
dsm.set('Config.0.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KDLH','KSUW',]
d.locName = ['Duluth','Superior',]
d.elementDuration = 6
dsm.set('Config.0.Cc_CurrentConditions', d, 0, 1)
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
d.locName = 'Duluth-Superior Metro'
d.coopId = '72745000'
dsm.set('Config.0.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KDLH'
d.locName = 'DULUTH'
d.heatIndexThreshold = 95
dsm.set('Config.0.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'MNZ037'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'DULUTH-SUPERIOR METRO'
d.coopId = '72745000'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'DULUTH-SUPERIOR METRO'
d.coopId = '72745000'
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
d.obsStation = ['SENSOR','KDLH','KSUW',]
d.locName = ['Duluth','DULUTH','SUPERIOR',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'DULUTH-SUPERIOR METRO'
d.coopId = '72745000'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KDLH','KSUW',]
d.schedule = [((11,23,16,0,0),(11,25,16,0,0)),((12,16,16,0,0),(1,6,16,0,0)),((5,19,16,0,0),(9,4,16,0,0)),]
d.coopId = '72745000'
dsm.set('Config.0.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '212246'
d.latitude = 46.77
d.longitude = -92.08
dsm.set('Config.0.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['DLH',]
d.obsStation = ['KDLH',]
d.locName = ['Duluth Int\'l',]
d.displayFlag = [0,]
dsm.set('Config.0.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['DULUTH-SUPERIOR METRO',]
d.coopId = ['72745000',]
dsm.set('Config.0.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KDLH',]
d.climId = ['212248',]
d.locName = ['Duluth',]
d.coopId = ['72745000',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.0.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KDLH','KSUW',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.0.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Duluth'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72745000'
dsm.set('Config.0.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Duluth'
d.coopId = '72745000'
dsm.set('Config.0.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.0.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.0.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.0.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','KDLH','KSUW',]
d.obsLocName = ['Duluth','Duluth','Superior',]
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
d.locName = 'Not Active'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'zz001'
dsm.set('Config.0.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Duluth-Superior Metro'
d.coopId = '72745000'
dsm.set('Config.0.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72745000'
dsm.set('Config.0.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KDLH'
d.climId = ['212248',]
d.locName = 'DULUTH'
d.coopId = '72745000'
dsm.set('Config.0.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 0
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
# Finished generation on Thu Dec 08 14:03:03 EST 2005
