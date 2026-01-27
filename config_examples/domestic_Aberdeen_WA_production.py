# Created on Thu Dec 08 14:12:36 EST 2005
Log.info('scmt config started')
# EXP: 1072
# VIW: 12884
# CLN: 6599
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
wxdata.setMapData('Config.0.Radar_LocalDoppler', d, 0)
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
dsm.set('Config.0.Radar_LocalDoppler', d, 0)
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
wxdata.setMapData('Config.0.Local_MetroDopplerRadar', d, 0)
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
                ( (331,83),),
                ( (512,259),),
                ( (358,135),),
                ( (546,312),),
                ( (310,329),),
                ( (274,205),),
                ( (605,259),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (348,234),),
                ( (585,149),),
                ( (246,315),),
                ( (331,83),),
                ( (512,259),),
                ( (358,135),),
                ( (546,312),),
                ( (310,329),),
                ( (274,205),),
                ( (605,259),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (309,255),'Aberdeen',),
                ( (547,132),'Centralia',),
                ( (107,318),'Pacific Beach',),
                ( (351,86),'Nemah',),
                ( (473,242),'McCleary',),
                ( (378,138),'South Bend',),
                ( (516,333),'Shelton',),
                ( (330,332),'Humptulips',),
                ( (178,208),'Westport',),
                ( (572,280),'Olympia',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (309,255),'Aberdeen',),
                ( (547,132),'Centralia',),
                ( (107,318),'Pacific Beach',),
                ( (351,86),'Nemah',),
                ( (473,242),'McCleary',),
                ( (378,138),'South Bend',),
                ( (516,333),'Shelton',),
                ( (330,332),'Humptulips',),
                ( (178,208),'Westport',),
                ( (572,280),'Olympia',),
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
# MAP: 71490
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4327,16084),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(137,110),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.0.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72791028',(304,73),),
                ( '72791037',(166,102),),
                ( '72791049',(135,193),),
                ( '72792000',(507,162),),
                ( '72792008',(464,76),),
                ( '72792012',(390,195),),
                ( '72792014',(396,286),),
                ( '72792040',(264,175),),
                ( '72797013',(140,283),),
                ( '72797014',(261,295),),
                ( '74206006',(558,265),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72791028',(301,109),),
                ( '72791037',(163,138),),
                ( '72791049',(132,229),),
                ( '72792000',(504,198),),
                ( '72792008',(461,112),),
                ( '72792012',(387,231),),
                ( '72792014',(393,322),),
                ( '72792040',(261,211),),
                ( '72797013',(137,319),),
                ( '72797014',(258,331),),
                ( '74206006',(555,301),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (243,145),'South Bend',),
                ( (120,174),'Grayland',),
                ( (62,265),'Ocean Shores',),
                ( (466,234),'Olympia',),
                ( (417,148),'Centralia',),
                ( (343,267),'Mccleary',),
                ( (357,358),'Shelton',),
                ( (215,247),'Aberdeen',),
                ( (100,355),'Taholah',),
                ( (217,367),'Quinault',),
                ( (519,337),'Tacoma',),
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
wxdata.setMapData('Config.0.Local_RegionalForecastMap', d, 0)
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
dsm.set('Config.0.Local_RegionalForecastMap', d, 0)
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
wxdata.setMapData('Config.0.Local_RegionalObservationMap', d, 0)
#
# Local_RegionalObservationMap (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'KAST',(159,147),),
                ( 'KBLI',(287,341),),
                ( 'KEPH',(465,231),),
                ( 'KGEG',(575,272),),
                ( 'KOMK',(437,336),),
                ( 'KPDX',(293,113),),
                ( 'KSEA',(292,233),),
                ( 'KUIL',(150,281),),
                ( 'KYKM',(415,156),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'KAST',(162,111),),
                ( 'KBLI',(290,305),),
                ( 'KEPH',(468,195),),
                ( 'KGEG',(578,236),),
                ( 'KOMK',(440,300),),
                ( 'KPDX',(296,77),),
                ( 'KSEA',(295,197),),
                ( 'KUIL',(153,245),),
                ( 'KYKM',(418,120),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (124,183),'Astoria',),
                ( (232,377),'Bellingham',),
                ( (428,267),'Ephrata',),
                ( (535,308),'Spokane',),
                ( (413,372),'Omak',),
                ( (252,149),'Portland',),
                ( (258,269),'Seattle',),
                ( (99,317),'Quillayute',),
                ( (381,192),'Yakima',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_RegionalObservationMap', d, 0)
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
wxdata.setMapData('Config.0.Local_Satellite', d, 0)
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
                ( (388,86),),
                ( (406,162),),
                ( (424,212),),
                ( (439,245),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (455,291),'Vancouver',),
                ( (445,215),'Portland',),
                ( (459,248),'Seattle',),
                ( (408,89),'San Francisco',),
                ( (426,165),'Medford',),
                ( (444,215),'Portland',),
                ( (459,248),'Seattle',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.0.Local_Satellite', d, 0)
# MAP: 50441
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3328,15542),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(271,217),
             datacutType='radar.us',
             datacutCoordinate=(9,1566),
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
              ( ( (613,299),'90',),
                ( (462,142),'5',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (495,296),'16',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (495,296),'16',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (613,299),'90',),
                ( (462,142),'5',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (354,233),),
                ( (460,194),),
                ( (461,107),),
                ( (523,275),),
                ( (352,113),),
                ( (469,243),),
                ( (537,332),),
                ( (260,373),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (354,233),),
                ( (460,194),),
                ( (461,107),),
                ( (523,275),),
                ( (352,113),),
                ( (469,243),),
                ( (537,332),),
                ( (260,373),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (315,254),'Aberdeen',),
                ( (422,177),'Centralia',),
                ( (422,90),'Longview',),
                ( (543,278),'Tacoma',),
                ( (273,116),'Astoria',),
                ( (436,226),'Olympia',),
                ( (509,353),'Seattle',),
                ( (217,356),'Quillayute',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (315,254),'Aberdeen',),
                ( (422,177),'Centralia',),
                ( (422,90),'Longview',),
                ( (543,278),'Tacoma',),
                ( (273,116),'Astoria',),
                ( (436,226),'Olympia',),
                ( (509,353),'Seattle',),
                ( (217,356),'Quillayute',),
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
wxdata.setInterestList('tideStation',['W9440573','W9440910',])
wxdata.setInterestList('airportId',['GEG','PDX','SEA',])
wxdata.setInterestList('coopId',['71777005','71892000','72698000','72698106','72781000','72781046','72784036','72785000','72789001','72791000','72791028','72791037','72791049','72792000','72792008','72792012','72792014','72792034','72792040','72793000','72797000','72797013','72797014','74201073','74206006','74206023',])
wxdata.setInterestList('indexId',['KHQM',])
wxdata.setInterestList('obsStation',['KAST','KBLI','KEPH','KGEG','KHQM','KKLS','KOLM','KOMK','KPDX','KSEA','KSHN','KUIL','KYKM',])
wxdata.setInterestList('climId',['450008','453807',])
wxdata.setInterestList('zone',['WAZ016',])
wxdata.setInterestList('aq',['wa008',])
wxdata.setInterestList('zone.cwf',['PZZ156',])
wxdata.setInterestList('skiId',['503006','604038',])
wxdata.setInterestList('county',['WAC027',])
dsm.set('countyNameList',[('WAC027','Grays Harbor'),], 0)
#
dsm.set('dmaCode','819', 0)
dsm.set('secondaryObsStation','KAST', 0)
dsm.set('primaryClimoStation','450008', 0)
dsm.set('primaryIndexId','KHQM', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','WA', 0)
dsm.set('expRev','616433', 0)
dsm.set('primaryCoopId','72792034', 0)
dsm.set('PlaylistOverride','WestCoastUS', 0)
dsm.set('wda','HQM', 0)
dsm.set('primaryCounty','WAC027', 0)
dsm.set('primaryObsStation','KHQM', 0)
dsm.set('primaryLat',46.97167, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Clock','scmt.clock', 0)
dsm.set('primaryLon',-123.82278, 0)
dsm.set('primaryZone','WAZ016', 0)
dsm.set('climoRegion','7', 0)
dsm.set('SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','022286', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','DOM - ABERDEEN/WESTPORT - DOM', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - ABERDEEN/WESTPORT - DOM', 0)
dsm.set('affiliateNumber','30574', 0)
dsm.set('zipCode','98520    ', 0)
dsm.set('bcConnectMethod','D', 0)
dsm.set('bcIspDialupPassword','k493hasd', 0)
dsm.set('bcIspDialupNumber','5370980', 0)
dsm.set('irdSlave','0', 0)
dsm.set('starId','TWCD06040080', 0)
dsm.set('bcDialInNumber','360-533-7534', 0)
dsm.set('bcIspDialupLogin','headend-022286@weather.com', 0)
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
d.airportId = ['SEA','PDX','GEG',]
d.airportLocName = ['Seattle-Tacoma','Portland','Spokane',]
d.obsStation = ['KSEA','KPDX','KGEG',]
dsm.set('Config.0.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.0.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['604038','503006',]
d.coopId = ['71777005','72698106',]
d.resortName = ['Whistler/Blackcomb, ','Mt Hood Mdws, OR',]
dsm.set('Config.0.Tag.General.snowboardData', d, 0, 1)
#
scmtRemove('Config.0.Ldl_LASCrawl')
scmtRemove('Config.0.LASCrawl')
#
#
scmtRemove('Config.0.Local_SchoolDayWeather')
scmtRemove('Config.0.Local_CurrentConditions')
scmtRemove('Config.0.Ldl_LocalStarIDMessage')
scmtRemove('Config.0.TimeTemp_Default')
scmtRemove('Config.0.Local_AirQualityForecast')
scmtRemove('Config.0.Ldl_AirportDelayConditions')
scmtRemove('Config.0.Local_MarineForecast')
scmtRemove('Config.0.Local_Climatology')
scmtRemove('Config.0.Local_HeatSafetyTips')
scmtRemove('Config.0.Cc_CurrentConditions')
scmtRemove('Config.0.Local_7DayForecast')
scmtRemove('Config.0.Local_RadarSatelliteComposite')
scmtRemove('Config.0.Fcst_TextForecast')
scmtRemove('Config.0.Local_Tides')
scmtRemove('Config.0.Local_LocalObservations')
scmtRemove('Config.0.Local_ExtendedForecast')
scmtRemove('Config.0.Local_Almanac')
scmtRemove('Config.0.Local_GetawayForecast')
scmtRemove('Config.0.Ldl_NationalStarIDMessage')
scmtRemove('Config.0.Local_RecordHighLow')
scmtRemove('Config.0.Local_TrafficFlow')
scmtRemove('Config.0.Local_NWSHeadlines')
scmtRemove('Config.0.Local_DaypartForecast')
scmtRemove('Config.0.Ldl_TravelForecast')
scmtRemove('Config.0.Ldl_SunriseSunset')
scmtRemove('Config.0.Ldl_CurrentApparentTemp')
scmtRemove('Config.0.Local_TrafficReport')
scmtRemove('Config.0.Local_TrafficOverview')
scmtRemove('Config.0.Local_OutdoorActivityForecast')
scmtRemove('Config.0.Ldl_ExtendedForecast')
scmtRemove('Config.0.Ldl_AirQualityForecast')
scmtRemove('Config.0.Fcst_ExtendedForecast')
scmtRemove('Config.0.Local_EventForecast')
scmtRemove('Config.0.Local_TextForecast')
scmtRemove('Config.0.Ldl_TrafficTripTimes')
scmtRemove('Config.0.Fcst_DaypartForecast')
scmtRemove('Config.0.Ldl_UVForecast')
#
d = twc.Data()
d.locName = 'Aberdeen Area'
d.coopId = '72792034'
dsm.set('Config.0.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KAST','KHQM','KKLS','KOLM','KPDX','KUIL','KSEA','KSHN',]
d.locName = ['Astoria','Hoquiam','Kelso/Longview','Olympia','Portland','Quillayute','Seattle-Tacoma','Shelton',]
dsm.set('Config.0.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'CAPE SHOALWATER TO PT. GRENVILLE'
d.zone = 'PZZ156'
dsm.set('Config.0.Local_MarineForecast', d, 0, 1)
#
#
d = twc.Data()
d.climId = '450008'
d.latitude = 46.97
d.longitude = -123.82
dsm.set('Config.0.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Astoria','Quillayute','Seattle',]
d.coopId = ['72791000','72797000','72793000',]
dsm.set('Config.0.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KHQM','KAST',]
d.locName = ['Hoquiam','Astoria',]
d.elementDuration = 6
dsm.set('Config.0.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Aberdeen',]
d.actionDayPhrase = 'Air Quality Action Day'
d.aq = ['wa008',]
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
d.locName = 'Aberdeen Area'
d.coopId = '72792034'
dsm.set('Config.0.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.0.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KHQM'
d.locName = 'HOQUIAM'
d.heatIndexThreshold = 95
dsm.set('Config.0.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'WAZ016'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'ABERDEEN AREA'
d.coopId = '72792034'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'ABERDEEN AREA'
d.coopId = '72792034'
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
d.obsStation = ['SENSOR','KHQM','KAST',]
d.locName = ['Aberdeen','HOQUIAM','ASTORIA',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'ABERDEEN AREA'
d.coopId = '72792034'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.0.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KHQM','KAST',]
d.schedule = [((11,23,16,0,0),(11,25,16,0,0)),((12,16,16,0,0),(1,6,16,0,0)),((5,19,16,0,0),(9,4,16,0,0)),]
d.coopId = '72792034'
dsm.set('Config.0.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '450008'
d.latitude = 46.97
d.longitude = -123.82
dsm.set('Config.0.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['SEA',]
d.obsStation = ['KSEA',]
d.locName = ['Sea-Tac Int\'l',]
d.displayFlag = [1,]
dsm.set('Config.0.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['ABERDEEN AREA',]
d.coopId = ['72792034',]
dsm.set('Config.0.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KHQM',]
d.climId = ['453807',]
d.locName = ['Hoquiam',]
d.coopId = ['72792040',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.0.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','KHQM','KAST',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.0.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Aberdeen Area'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72792034'
dsm.set('Config.0.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Aberdeen Area'
d.coopId = '72792034'
dsm.set('Config.0.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.0.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.0.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.0.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','KHQM','KAST',]
d.obsLocName = ['Aberdeen','Hoquiam','Astoria',]
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
d.locName = 'Aberdeen'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'wa008'
dsm.set('Config.0.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locNameList = ['Leavenworth, WA','Mt. Rainier N.P., WA','Vancouver, Canada',]
d.coopId = ['72781046','74206023','71892000',]
dsm.set('Config.0.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Aberdeen Area'
d.coopId = '72792034'
dsm.set('Config.0.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72792034'
dsm.set('Config.0.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.tideStation = ['W9440910','W9440573',]
d.locName = ['Toke Point','Chinook, Baker Bay, WA.',]
dsm.set('Config.0.Local_Tides', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KHQM'
d.climId = ['453807',]
d.locName = 'HOQUIAM'
d.coopId = '72792040'
dsm.set('Config.0.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 1
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 0
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 1
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 1
d.activeLocal_TrafficFlow = 0
d.activeLocal_TrafficOverview = 0
d.activeLocal_TrafficReport = 0
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
# Finished generation on Thu Dec 08 14:12:43 EST 2005
