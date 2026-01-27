# Created on Thu Oct 02 15:42:39 GMT 2014
twc.Log.info('scmt config started')
# EXP: 26
# VIW: 7383
# CLN: 15565
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
#
dsm.set('scmt_configType', 'wxscan',0)
dsm.set('scmt.ProductTypes',['None'], 0)
#
# MAP: 74891
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32004,13077),
             mapcutSize=(2232,1107),
             mapFinalSize=(248,123),
             mapMilesSize=(210,125),
             datacutType='radar.us',
             datacutCoordinate=(3521,1264),
             datacutSize=(273,136),
             dataFinalSize=(248,123),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Radar_LocalDoppler.0', d, 0)
#
# Radar_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
               ( ( (166,59),),
                 ( (120,72),),
                 ( (139,55),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (166,59),),
                 ( (120,72),),
                 ( (139,55),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (179,62),'Boston',),
                 ( (85,87),'Fitchburg',),
                 ( (86,44),'Framingham',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (179,62),'Boston',),
                 ( (85,87),'Fitchburg',),
                 ( (86,44),'Framingham',),
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
dsm.set('Config.1.Radar_LocalDoppler.0', d, 0)
# MAP: 76349
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32624,13212),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(135,108),
             datacutType='radar.us',
             datacutCoordinate=(3597,1281),
             datacutSize=(176,117),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (318,120),'495',),
               ),
             ),
             (
               (('stateHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (115,266),'2',),
                 ( (508,125),'3',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (183,142),'90',),
                 ( (395,275),'93',),
                 ( (451,315),'95',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (183,142),'90',),
                 ( (395,275),'93',),
                 ( (451,315),'95',),
               ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (115,266),'2',),
                 ( (508,125),'3',),
               ),
             ),
             (
               (('stateHwySign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (249,132),'146',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (318,120),'495',),
               ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (249,132),'146',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (441,208),),
                 ( (447,131),),
                 ( (412,199),),
                 ( (333,188),),
                 ( (181,279),),
                 ( (546,288),),
                 ( (298,220),),
                 ( (241,260),),
                 ( (363,297),),
                 ( (461,245),),
                 ( (325,233),),
                 ( (226,183),),
                 ( (325,345),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (441,208),),
                 ( (447,131),),
                 ( (412,199),),
                 ( (333,188),),
                 ( (181,279),),
                 ( (546,288),),
                 ( (298,220),),
                 ( (241,260),),
                 ( (363,297),),
                 ( (461,245),),
                 ( (325,233),),
                 ( (226,183),),
                 ( (325,345),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (461,214),'Boston',),
                 ( (409,114),'Brockton',),
                 ( (398,182),'Brookline',),
                 ( (259,173),'Framingham',),
                 ( (147,300),'Gardner',),
                 ( (566,291),'Gloucester',),
                 ( (218,223),'Hudson',),
                 ( (124,252),'Leominster',),
                 ( (347,317),'Lowell',),
                 ( (481,248),'Lynn',),
                 ( (297,257),'Maynard',),
                 ( (118,186),'Worcester',),
                 ( (245,348),'Nashua',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (461,214),'Boston',),
                 ( (409,114),'Brockton',),
                 ( (398,182),'Brookline',),
                 ( (259,173),'Framingham',),
                 ( (147,300),'Gardner',),
                 ( (566,291),'Gloucester',),
                 ( (218,223),'Hudson',),
                 ( (124,252),'Leominster',),
                 ( (347,317),'Lowell',),
                 ( (481,248),'Lynn',),
                 ( (297,257),'Maynard',),
                 ( (118,186),'Worcester',),
                 ( (245,348),'Nashua',),
               ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 3,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 4,(130,130,130,255),2,),(('statehighways',),),),
             (( 4,(130,130,130,255),2,),(('ushighways',),),),
             (( 4,(130,130,130,255),2,),(('interstates',),),),
             (( 4,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
# MAP: 77029
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32479,13322),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(121,97),
             datacutType='radar.us',
             datacutCoordinate=(3579,1294),
             datacutSize=(159,106),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (416,105),'495',),
                 ( (329,183),'190',),
               ),
             ),
             (
               (('stateHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (137,250),'2',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (437,276),'3',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (437,276),'3',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (177,104),'90',),
                 ( (583,288),'95',),
                 ( (100,309),'91',),
                 ( (491,318),'93',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (177,104),'90',),
                 ( (583,288),'95',),
                 ( (100,309),'91',),
                 ( (491,318),'93',),
               ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (137,250),'2',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (416,105),'495',),
                 ( (329,183),'190',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (123,181),),
                 ( (569,170),),
                 ( (108,114),),
                 ( (348,245),),
                 ( (451,150),),
                 ( (283,250),),
                 ( (412,185),),
                 ( (349,229),),
                 ( (485,271),),
                 ( (443,198),),
                 ( (372,282),),
                 ( (449,250),),
                 ( (268,284),),
                 ( (333,143),),
                 ( (202,359),),
                 ( (442,323),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (123,181),),
                 ( (569,170),),
                 ( (108,114),),
                 ( (348,245),),
                 ( (451,150),),
                 ( (283,250),),
                 ( (412,185),),
                 ( (349,229),),
                 ( (485,271),),
                 ( (443,198),),
                 ( (372,282),),
                 ( (449,250),),
                 ( (268,284),),
                 ( (333,143),),
                 ( (202,359),),
                 ( (442,323),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (86,202),'Amherst',),
                 ( (589,173),'Boston',),
                 ( (87,136),'Chicopee',),
                 ( (319,265),'Fitchburg',),
                 ( (468,137),'Framingham',),
                 ( (195,253),'Gardner',),
                 ( (368,175),'Hudson',),
                 ( (232,221),'Leominster',),
                 ( (503,280),'Lowell',),
                 ( (463,201),'Maynard',),
                 ( (328,303),'Townsend',),
                 ( (469,253),'Westford',),
                 ( (138,288),'Winchendon',),
                 ( (225,146),'Worcester',),
                 ( (137,353),'Keene',),
                 ( (412,344),'Nashua',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (86,202),'Amherst',),
                 ( (589,173),'Boston',),
                 ( (87,136),'Chicopee',),
                 ( (319,265),'Fitchburg',),
                 ( (468,137),'Framingham',),
                 ( (195,253),'Gardner',),
                 ( (368,175),'Hudson',),
                 ( (232,221),'Leominster',),
                 ( (503,280),'Lowell',),
                 ( (463,201),'Maynard',),
                 ( (328,303),'Townsend',),
                 ( (469,253),'Westford',),
                 ( (138,288),'Winchendon',),
                 ( (225,146),'Worcester',),
                 ( (137,353),'Keene',),
                 ( (412,344),'Nashua',),
               ),
             ),
        ],
  vector = [
             (( 8,(20,20,20,96),1,),(('statehighways',),),),
             (( 8,(20,20,20,96),1,),(('ushighways',),),),
             (( 8,(20,20,20,96),1,),(('interstates',),),),
             (( 8,(20,20,20,96),1,),(('otherroutes',),),),
             (( 2,(20,20,20,255),2,),(('counties',),),),
             (( 3,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             (( 4,(130,130,130,255),2,),(('statehighways',),),),
             (( 4,(130,130,130,255),2,),(('ushighways',),),),
             (( 4,(130,130,130,255),2,),(('interstates',),),),
             (( 4,(130,130,130,255),2,),(('otherroutes',),),),
             ],
)
dsm.set('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
# MAP: 76350
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4195,1793),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(1500,1010),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1263,580),
             datacutSize=(785,545),
             dataFinalSize=(694,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0', d, 0)
# MAP: -402
# Local_FrostFreezeWarnings (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3463,1467),
             mapcutSize=(2384,1589),
             mapFinalSize=(720,480),
             mapMilesSize=(2263,1538),
             datacutType='frostFreeze.us',
             datacutCoordinate=(747,397),
             datacutSize=(1301,903),
             dataFinalSize=(608,420),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Garden.0.Local_FrostFreezeWarnings.0', d, 0)
#
# Local_FrostFreezeWarnings (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Garden.0.Local_FrostFreezeWarnings.0', d, 0)
# MAP: 77023
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4469,1913),
             mapcutSize=(1224,816),
             mapFinalSize=(720,480),
             mapMilesSize=(1157,778),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(1396,687),
             datacutSize=(652,529),
             dataFinalSize=(593,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Ski.0.Local_SnowfallQpfForecast.0', d, 0)
#
# Local_SnowfallQpfForecast (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Ski.0.Local_SnowfallQpfForecast.0', d, 0)
# MAP: 51
# Local_NationalTravelWeather (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1451,293),
             mapcutSize=(4792,3194),
             mapFinalSize=(720,480),
             mapMilesSize=(4360,3075),
             datacutType='travelWeather.us',
             datacutCoordinate=(0,0),
             datacutSize=(2048,1300),
             dataFinalSize=(476,301),
             dataOffset=(129,84),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Travel.0.Local_NationalTravelWeather.0', d, 0)
#
# Local_NationalTravelWeather (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_NationalTravelWeather.0', d, 0)
# MAP: 77022
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(30618,12066),
             mapcutSize=(4320,2880),
             mapFinalSize=(720,480),
             mapMilesSize=(408,326),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
#
# Local_RegionalForecastConditions (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
               ( ( '72503000',(219,92),),
                 ( '72503181',(179,158),),
                 ( '72507000',(434,133),),
                 ( '72508019',(310,122),),
                 ( '72509000',(496,232),),
                 ( '72518000',(188,271),),
                 ( '74490056',(408,286),),
                 ( '74491009',(333,207),),
                 ( '74494023',(577,92),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72503000',(219,109),),
                 ( '72503181',(176,197),),
                 ( '72507000',(431,173),),
                 ( '72508019',(307,162),),
                 ( '72509000',(494,247),),
                 ( '72518000',(186,311),),
                 ( '74490056',(405,326),),
                 ( '74491009',(330,247),),
                 ( '74494023',(574,132),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (121,135),'New York',),
                 ( (131,231),'Newburgh',),
                 ( (403,209),'Providence',),
                 ( (288,192),'Hartford',),
                 ( (428,272),'Boston',),
                 ( (158,345),'Albany',),
                 ( (376,360),'Nashua',),
                 ( (280,281),'Springfield ',),
                 ( (531,166),'Nantucket',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
# MAP: -401
# Local_EstimatedPrecipitation (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3463,1467),
             mapcutSize=(2384,1589),
             mapFinalSize=(720,480),
             mapMilesSize=(2263,1538),
             datacutType='estimatedPrecip.us',
             datacutCoordinate=(747,397),
             datacutSize=(1301,903),
             dataFinalSize=(608,420),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Garden.0.Local_EstimatedPrecipitation.0', d, 0)
#
# Local_EstimatedPrecipitation (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Garden.0.Local_EstimatedPrecipitation.0', d, 0)
# MAP: -404
# Local_PrecipitationQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3463,1467),
             mapcutSize=(2384,1589),
             mapFinalSize=(720,480),
             mapMilesSize=(2263,1538),
             datacutType='precipQpfForecast.us',
             datacutCoordinate=(747,397),
             datacutSize=(1301,903),
             dataFinalSize=(608,420),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Garden.0.Local_PrecipitationQpfForecast.0', d, 0)
#
# Local_PrecipitationQpfForecast (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Garden.0.Local_PrecipitationQpfForecast.0', d, 0)
# MAP: -403
# Local_PalmerDroughtSeverity (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3463,1467),
             mapcutSize=(2384,1589),
             mapFinalSize=(720,480),
             mapMilesSize=(2263,1538),
             datacutType='palmerDrought.us',
             datacutCoordinate=(747,397),
             datacutSize=(1301,903),
             dataFinalSize=(608,420),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Garden.0.Local_PalmerDroughtSeverity.0', d, 0)
#
# Local_PalmerDroughtSeverity (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Garden.0.Local_PalmerDroughtSeverity.0', d, 0)
#
wxdata.setInterestList('lambert.us','1',['precipQpfForecast.us','estimatedPrecip.us','travelWeather.us','snowfallQpfForecast.us','palmerDrought.us','frostFreeze.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('precipQpfForecast.us.cuts','1',['Config.1.Garden.0.Local_PrecipitationQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core3.2.Local_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.Core3.1.Local_LocalDoppler.0',])
wxdata.setInterestList('estimatedPrecip.us.cuts','1',['Config.1.Garden.0.Local_EstimatedPrecipitation.0',])
wxdata.setInterestList('frostFreeze.us.cuts','1',['Config.1.Garden.0.Local_FrostFreezeWarnings.0',])
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.2.Local_RadarSatelliteComposite.0','Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.Core4.1.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('palmerDrought.us.cuts','1',['Config.1.Garden.0.Local_PalmerDroughtSeverity.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['frostFreeze.us','palmerDrought.us','radarSatellite.us','snowfallQpfForecast.us','precipQpfForecast.us','radar.us','travelWeather.us','estimatedPrecip.us',])
#
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','IAD','JFK','LAX','LGA','MHT','MIA','MSP','ORD','PHL','PHX','SEA','SFO','SLC','STL',])
wxdata.setInterestList('coopId','1',['72205000','72219000','72259000','72295000','72405000','72494000','72503000','72503023','72503181','72507000','72508000','72508019','72509000','72518000','72530000','72537000','72605016','72605077','74490000','74490015','74490019','74490026','74490027','74490039','74490056','74490057','74490072','74490074','74490076','74491009','74492014','74494023','74494026',])
wxdata.setInterestList('obsStation','1',['KBED','KBOS','KFIT','T72202000','T72219000','T72259000','T72278000','T72295000','T72403000','T72408000','T72434000','T72494000','T72503000','T72503023','T72507000','T72508000','T72509000','T72509018','T72530000','T72565000','T72572000','T72605016','T72605077','T72658000','T72793000','T74486000','T74490000','T74490015','T74490019','T74490026','T74490027','T74490039','T74490057','T74490072','T74490074','T74490076','T74491009','T74492002','T74492011','T74492014','T74492033','T74494023','T74494026',])
wxdata.setInterestList('climId','1',['190666','190770','192975',])
wxdata.setInterestList('metroId','1',['18',])
wxdata.setInterestList('zone','1',['MAZ004','MAZ005','MAZ015',])
wxdata.setInterestList('aq','1',['ma001',])
wxdata.setInterestList('skiId','1',['198','216','287','304','356','40','407','436','443','489','54','96',])
wxdata.setInterestList('county','1',['MAC025','MAC027','MAC017','MAC021',])
#
dsm.set('Config.1.Package.36',('Health',0), 0)
dsm.set('Config.1.Package.34',('Core5',0), 0)
dsm.set('Config.1.Package.25',('Core3',2), 0)
dsm.set('Config.1.Package.31',('Travel',0), 0)
dsm.set('Config.1.Package.23',('Core4',1), 0)
dsm.set('Config.1.Package.29',('Airport',0), 0)
dsm.set('Config.1.Package.18',('Core3',0), 0)
dsm.set('Config.1.Package.16',('Garden',0), 0)
dsm.set('Config.1.Package.13',('Core5',0), 0)
dsm.set('Config.1.Package.9',('Health',0), 0)
dsm.set('Config.1.Package.7',('Core4',2), 0)
dsm.set('Config.1.Package.5',('Core3',1), 0)
dsm.set('Config.1.Package.0',('Travel',0), 0)
dsm.set('Config.1.Package.38',('Airport',0), 0)
dsm.set('Config.1.Package.35',('Garden',0), 0)
dsm.set('Config.1.Package.26',('Core4',1), 0)
dsm.set('Config.1.Package.32',('Core5',0), 0)
dsm.set('Config.1.Package.22',('Core3',0), 0)
dsm.set('Config.1.Package.28',('Core4',2), 0)
dsm.set('Config.1.Package.20',('Travel',0), 0)
dsm.set('Config.1.Package.15',('Garden',0), 0)
dsm.set('Config.1.Package.12',('Core3',2), 0)
dsm.set('Config.1.Package.10',('Core3',1), 0)
dsm.set('Config.1.Package.6',('Core4',0), 0)
dsm.set('Config.1.Package.4',('Health',0), 0)
dsm.set('Config.1.Package.2',('Core5',0), 0)
dsm.set('Config.1.Package.37',('Core5',0), 0)
dsm.set('Config.1.Package.33',('Airport',0), 0)
dsm.set('Config.1.Package.24',('Core4',1), 0)
dsm.set('Config.1.Package.30',('Health',0), 0)
dsm.set('Config.1.Package.21',('Core2',0), 0)
dsm.set('Config.1.Package.27',('Core3',2), 0)
dsm.set('Config.1.Package.19',('Travel',0), 0)
dsm.set('Config.1.Package.17',('Garden',0), 0)
dsm.set('Config.1.Package.14',('Core3',2), 0)
dsm.set('Config.1.Package.11',('Core3',1), 0)
dsm.set('Config.1.Package.8',('Core4',0), 0)
dsm.set('Config.1.Package.3',('Airport',0), 0)
dsm.set('Config.1.Package.1',('Travel',0), 0)
dsm.set('dmaCode','506', 0)
dsm.set('secondaryObsStation','KBOS', 0)
dsm.set('primaryClimoStation','190770', 0)
dsm.set('stateCode','MA', 0)
dsm.set('expRev','7009108', 0)
dsm.set('primaryCoopId','72509000', 0)
dsm.set('primarylat',42.33, 0)
dsm.set('primaryCounty','MAC025', 0)
dsm.set('primaryObsStation','T72509000', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-71.08027, 0)
dsm.set('primaryForecastName','N. Worcester Co.', 0)
dsm.set('primaryZone','MAZ015', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','020731', 0)
dsm.set('msoName','Unknown', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','21479', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','WXS - BOSTON - WXS', 0)
dsm.set('zipCode','02132', 0)
dsm.set('Config.1.irdAddress','0000315593109223', 0)
dsm.set('Config.1.starId','TWCS08030092', 0)
dsm.set('Config.1.bcDialInNumber','9788978574', 0)
dsm.set('Config.1.irdSlave','0', 0)
#
#  Non Image Maps
#
#

#
#
wxdata.setTimeZone('EST5EDT')
#
d = twc.Data()
d.affiliateLogo = 'xfinityLogo'
dsm.set('Config.1.Background_Default.0', d, 0, 1)
#
scmtRemove('Config.1.Travel.LasCrawl_Default')
scmtRemove('Config.1.Ski.LasCrawl_Default')
scmtRemove('Config.1.Golf.LasCrawl_Default')
scmtRemove('Config.1.BoatAndBeach.LasCrawl_Default')
scmtRemove('Config.1.Health.LasCrawl_Default')
scmtRemove('Config.1.Traffic.LasCrawl_Default')
scmtRemove('Config.1.SpanishCore.LasCrawl_Default')
scmtRemove('Config.1.International.LasCrawl_Default')
scmtRemove('Config.1.Core.LasCrawl_Default')
scmtRemove('Config.1.Garden.LasCrawl_Default')
scmtRemove('Config.1.Airport.LasCrawl_Default')
scmtRemove('Config.1.LasCrawl_Default')
#
scmtRemove('Config.1.Core2Spanish.LasCrawl_Default')
scmtRemove('Config.1.Core2.LasCrawl_Default')
scmtRemove('Config.1.Core5.LasCrawl_Default')
scmtRemove('Config.1.Core4Spanish.LasCrawl_Default')
scmtRemove('Config.1.Core3.LasCrawl_Default')
scmtRemove('Config.1.Core1.LasCrawl_Default')
scmtRemove('Config.1.Core4.LasCrawl_Default')
scmtRemove('Config.1.LocalBroadcaster.LasCrawl_Default')
#
#
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficFlow.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.Core3.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Local_TextForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficReport.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_CurrentConditions.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Core3.1.Local_MenuBoard.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.2.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Traffic.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Local_MenuBoard.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Core4.2.Local_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Core4.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.2.Local_TextForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.1.Local_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficOverview.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Core3.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Local_PackageIntro.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Core4.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Core3.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.SmLocal_TrafficSponsor.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.Traffic.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
#
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
scmtRemove('Config.1.SevereCore2.0')
d = twc.Data()
d.bkgImage = 'severe_core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'YOUR LOCAL FORECAST'
dsm.set('Config.1.SevereCore2.0', d, 0, 1)
scmtRemove('Config.1.Core4.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Central Middlesex Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'CENTRAL MIDDLESEX'
dsm.set('Config.1.Core4.2', d, 0, 1)
scmtRemove('Config.1.Airport.0')
d = twc.Data()
d.bkgImage = 'airport_bg'
d.packageTitle = 'Airport Conditions'
d.packageFlavor = 3
d.shortPackageTitle = 'AIRPORTS'
dsm.set('Config.1.Airport.0', d, 0, 1)
scmtRemove('Config.1.Core5.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 0
d.shortPackageTitle = 'BOSTON RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Gardner Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GARDNER'
dsm.set('Config.1.Core4.1', d, 0, 1)
scmtRemove('Config.1.Core3.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Central Middlesex Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'CENTRAL MIDDLESEX'
dsm.set('Config.1.Core3.2', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Boston Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'BOSTON'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Gardner Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GARDNER'
dsm.set('Config.1.Core3.1', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Boston Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'BOSTON'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Boston Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'BOSTON'
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
d.packageTitle = 'Boston Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'BOSTON'
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
d.packageFlavor = 2
d.shortPackageTitle = 'TRAFFIC'
dsm.set('Config.1.Traffic.0', d, 0, 1)
scmtRemove('Config.1.Health.0')
d = twc.Data()
d.bkgImage = 'health_bg'
d.packageTitle = 'Weather & Your Health'
d.packageFlavor = 1
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'boston_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Central Middlesex Co.'
d.coopId = '74490026'
dsm.set('Config.1.Core4.2.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74490026','KBED',]
d.locName = ['Framingham','Bedford',]
dsm.set('Config.1.Core4.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74490000','T74492014','T74490039','T74490057','T74490026','T74490074','T74490027','T74490019','T74490015','T74490076',]
d.locName = ['Bedford','   Brookline','   Clinton','   Fitchburg','   Framingham','   Gardner','   Hudson','   Lowell','   Maynard','   Winchendon',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'N. Worcester Co.'
d.coopId = '74490074'
dsm.set('Config.1.Core4.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['STL','SFO','SEA','IAD',]
d.obsStation = ['T72434000','T72494000','T72793000','T72403000',]
d.locName = ['St. Louis - Lambert','San Francisco Int`l','Seattle - Tacoma Int`l','Wash. - Dulles Arpt.',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','PHL','PHX','SLC',]
d.obsStation = ['T72503000','T72408000','T72278000','T72572000',]
d.locName = ['New York LaGuardia','Philadelphia Int`l','Phoenix-Sky Harbor','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LAX','MIA','MSP','JFK',]
d.obsStation = ['T72295000','T72202000','T72658000','T74486000',]
d.locName = ['Los Angeles Int`l','Miami Int`l Airport','Minn.-St. Paul Int`l','New York JFK Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Metro Boston'
d.coopId = '72509000'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['ATL','ORD','DFW','DEN',]
d.obsStation = ['T72219000','T72530000','T72259000','T72565000',]
d.locName = ['Atlanta Hartsfield-Jackson','Chicago O`Hare Int`l','Dallas-Ft. Worth Int`l','Denver Int`l Airport',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72508000','T72605016','T74494023','T72503023','T72605077','T72507000','T74494026','T74491009','T74490072',]
d.locName = ['Hartford, CT','   Manchester, NH','   Nantucket','   New York, NY','   Portsmouth, NH','   Providence, RI','   Provincetown','   Springfield','   Worcester',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72509000'
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'boston_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'N. Worcester Co.'
d.coopId = '74490074'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.1.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ XFINITY TV'
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'boston_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 1
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Metro Boston'
d.coopId = '72509000'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Metro Boston'
d.coopId = '72509000'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 1
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Bedford','   Brookline','   Clinton','   Fitchburg','   Framingham','   Gardner','   Hudson','   Lowell','   Maynard','   Winchendon',]
d.coopId = ['74490000','74492014','74490039','74490057','74490026','74490074','74490027','74490019','74490015','74490076',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'N. Worcester Co.'
d.coopId = '74490074'
dsm.set('Config.1.Core4.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74490074','KFIT',]
d.locName = ['Gardner','Fitchburg',]
dsm.set('Config.1.Core4.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Central Middlesex Co.'
d.zone = 'MAZ005'
dsm.set('Config.1.Core4.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74490026','KBED',]
d.locName = ['Framingham','Bedford',]
dsm.set('Config.1.Core3.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Central Middlesex Co.'
d.coopId = '74490026'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.2.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509018','T74490015','T74492002','T74492011',]
d.locName = ['Malden','Maynard','Milton','Quincy',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'forest_bg'
dsm.set('Config.1.Core4.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'N. Worcester Co.'
d.zone = 'MAZ004'
dsm.set('Config.1.Core4.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74492033','T74492014','T74490057','T74490019',]
d.locName = ['Brockton','Brookline','Fitchburg','Lowell',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Hartford, CT','   Manchester, NH','   Nantucket','   New York, NY','   Portsmouth, NH','   Providence, RI','   Provincetown','   Springfield','   Worcester',]
d.coopId = ['72508000','72605016','74494023','72503023','72605077','72507000','74494026','74491009','74490072',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.aq = 'ma001'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'boston_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Orlando','San Francisco','Washington, DC',]
d.coopId = ['72205000','72494000','72405000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = ['Detroit','Los Angeles','New York City',]
d.coopId = ['72537000','72295000','72503000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'boston_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509018','T74490015','T74492002','T74492011',]
d.locName = ['Malden','Maynard','Milton','Quincy',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Chicago','Dallas',]
d.coopId = ['72219000','72530000','72259000',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ XFINITY TV'
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74492033','T74492014','T74490057','T74490019',]
d.locName = ['Brockton','Brookline','Fitchburg','Lowell',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72509000','KBOS',]
d.locName = ['Boston','Logan Airport',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Boston'
d.bkgImage = 'boston_bg'
d.affiliateName = 'XFINITY TV'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Central Middlesex Co.'
d.zone = 'MAZ005'
dsm.set('Config.1.Core3.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74490074','KFIT',]
d.locName = ['Gardner','Fitchburg',]
dsm.set('Config.1.Core3.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '190770'
d.latitude = 42.37
d.longitude = -71.03
d.locName = 'Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'garden_intro_bg'
dsm.set('Config.1.Garden.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ XFINITY TV'
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'N. Worcester Co.'
d.zone = 'MAZ004'
dsm.set('Config.1.Core3.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Boston'
d.coopId = '72509000'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Boston'
d.coopId = '72509000'
dsm.set('Config.1.Garden.0.Local_GardeningForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Greater Boston Area'
d.zone = 'MAZ015'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'forest_bg'
dsm.set('Config.1.Core3.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['BOS',]
d.obsStation = ['T72509000',]
d.locName = ['Logan Int`l Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'MHT'
d.obsStation = 'T72605016'
d.locName = 'Manchester Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'BOS'
d.obsStation = 'T72509000'
d.locName = 'Logan International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Central Middlesex Co.'
d.coopId = '74490026'
dsm.set('Config.1.Core4.2.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.preRoll = 8
d.schedule = ((14,60),(29,60),(44,60),(58,120),)
dsm.set('Config.1.Local_Avail_Schedule', d, 0)
#
# End of SCMT deployment
#
ds.commit()
twc.Log.info('scmt config finished')
# Finished generation on Thu Oct 02 15:42:41 GMT 2014
