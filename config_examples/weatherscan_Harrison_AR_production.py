# Created on Thu Sep 22 12:43:46 EDT 2005
# Updated to new format structure
twc.Log.info('scmt config started')
# EXP: 35
# VIW: 7403
# CLN: 17633
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
# MAP: 72116
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18151,8806),
             mapcutSize=(4448,2206),
             mapFinalSize=(248,123),
             mapMilesSize=(458,273),
             datacutType='radar.us',
             datacutCoordinate=(1824,741),
             datacutSize=(545,270),
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
               ( ( (148,37),),
                 ( (154,64),),
                 ( (100,64),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (148,37),),
                 ( (154,64),),
                 ( (100,64),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (156,28),'Ft Smith',),
                 ( (158,80),'Springdale',),
                 ( (77,55),'Tulsa',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (156,28),'Ft Smith',),
                 ( (158,80),'Springdale',),
                 ( (77,55),'Tulsa',),
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
# MAP: 178
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19931,9334),
             mapcutSize=(2120,1413),
             mapFinalSize=(720,480),
             mapMilesSize=(217,174),
             datacutType='radar.us',
             datacutCoordinate=(2042,806),
             datacutSize=(260,173),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (59,133),'540',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (59,133),'540',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (309,253),),
                 ( (235,275),),
                 ( (356,239),),
                 ( (188,196),),
                 ( (337,173),),
                 ( (487,146),),
                 ( (556,265),),
                 ( (337,302),),
                 ( (473,235),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (309,253),),
                 ( (235,275),),
                 ( (356,239),),
                 ( (188,196),),
                 ( (337,173),),
                 ( (487,146),),
                 ( (556,265),),
                 ( (337,302),),
                 ( (473,235),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (282,274),'Alpena',),
                 ( (134,278),'Berryville',),
                 ( (320,222),'Harrison',),
                 ( (83,199),'Huntsville',),
                 ( (310,156),'Jasper',),
                 ( (507,149),'Marshall',),
                 ( (512,286),'Mtn Home',),
                 ( (310,323),'Omaha',),
                 ( (493,238),'Yellville',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (282,274),'Alpena',),
                 ( (134,278),'Berryville',),
                 ( (320,222),'Harrison',),
                 ( (83,199),'Huntsville',),
                 ( (310,156),'Jasper',),
                 ( (507,149),'Marshall',),
                 ( (512,286),'Mtn Home',),
                 ( (310,323),'Omaha',),
                 ( (493,238),'Yellville',),
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
dsm.set('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
# MAP: 67
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3190,1873),
             mapcutSize=(1500,1000),
             mapFinalSize=(720,480),
             mapMilesSize=(1454,982),
             datacutType='radarSatellite.us',
             datacutCoordinate=(746,621),
             datacutSize=(771,516),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
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
dsm.set('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0', d, 0)
# MAP: -302
# Local_FrostFreezeWarnings (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3073,1467),
             mapcutSize=(2276,1517),
             mapFinalSize=(720,480),
             mapMilesSize=(2184,1486),
             datacutType='frostFreeze.us',
             datacutCoordinate=(494,397),
             datacutSize=(1471,903),
             dataFinalSize=(720,440),
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
# MAP: 116
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3073,1467),
             mapcutSize=(2276,1517),
             mapFinalSize=(720,480),
             mapMilesSize=(2184,1486),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(494,397),
             datacutSize=(1471,903),
             dataFinalSize=(720,440),
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
# MAP: 231
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(12019,10668),
             mapcutSize=(14304,9536),
             mapFinalSize=(720,480),
             mapMilesSize=(1283,1027),
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
               ( ( '72330002',(428,249),),
                 ( '72334001',(492,116),),
                 ( '72340004',(336,77),),
                 ( '72344000',(197,109),),
                 ( '72356000',(116,214),),
                 ( '72435000',(569,270),),
                 ( '72440000',(258,292),),
                 ( '72440066',(298,179),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72330002',(425,285),),
                 ( '72334001',(489,152),),
                 ( '72340004',(333,113),),
                 ( '72344000',(194,145),),
                 ( '72356000',(113,250),),
                 ( '72435000',(566,306),),
                 ( '72440000',(255,328),),
                 ( '72440066',(295,215),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (365,321),'Poplar Bluff',),
                 ( (447,188),'Memphis',),
                 ( (277,149),'Little Rock',),
                 ( (140,181),'Fort Smith',),
                 ( (90,286),'Tulsa',),
                 ( (526,342),'Paducah',),
                 ( (202,364),'Springfield',),
                 ( (254,251),'Harrison',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
# MAP: -301
# Local_EstimatedPrecipitation (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3426,1172),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(1398,941),
             datacutType='estimatedPrecip.us',
             datacutCoordinate=(868,259),
             datacutSize=(1471,903),
             dataFinalSize=(720,440),
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
# MAP: -304
# Local_PrecipitationQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3073,1467),
             mapcutSize=(2276,1517),
             mapFinalSize=(720,480),
             mapMilesSize=(2184,1486),
             datacutType='precipQpfForecast.us',
             datacutCoordinate=(494,397),
             datacutSize=(1471,903),
             dataFinalSize=(720,440),
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
# MAP: -303
# Local_PalmerDroughtSeverity (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3073,1467),
             mapcutSize=(2276,1517),
             mapFinalSize=(720,480),
             mapMilesSize=(2184,1486),
             datacutType='palmerDrought.us',
             datacutCoordinate=(494,397),
             datacutSize=(1471,903),
             dataFinalSize=(720,440),
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
# MAP: 246
# Local_InternationalForecast (MAP DATA)
#
d = twc.Data(mapName='mercator.mx.tif',
             mapcutCoordinate=(0,3),
             mapcutSize=(720,480),
             mapFinalSize=(720,480),
             mapMilesSize=(2979,1831),
)
wxdata.setMapData('Config.1.International.0.Local_InternationalForecast.1', d, 0)
#
# Local_InternationalForecast (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,1,0,),
               ( ( '76255000',(206,261),),
                 ( '76393000',(346,201),),
                 ( '76405000',(222,166),),
                 ( '76595000',(570,121),),
                 ( '76679001',(368,95),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),1,0,),
               ( ( '76255000',(203,301),),
                 ( '76393000',(343,241),),
                 ( '76405000',(211,206),),
                 ( '76595000',(567,161),),
                 ( '76679001',(365,135),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),1,0,1,),
               ( ( (165,335),'Guaymas',),
                 ( (298,275),'Monterrey',),
                 ( (188,240),'La Paz',),
                 ( (538,195),'Cancun',),
                 ( (315,169),'Mexico City',),
               ),
             ),
        ],
)
dsm.set('Config.1.International.0.Local_InternationalForecast.1', d, 0)
# MAP: 240
# Local_InternationalForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.ca.tif',
             mapcutCoordinate=(0,3),
             mapcutSize=(720,480),
             mapFinalSize=(720,480),
             mapMilesSize=(3635,2907),
)
wxdata.setMapData('Config.1.International.0.Local_InternationalForecast.0', d, 0)
#
# Local_InternationalForecast (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,1,0,),
               ( ( '71182000',(574,186),),
                 ( '71627001',(538,92),),
                 ( '71852000',(365,93),),
                 ( '71879001',(241,140),),
                 ( '71892001',(132,103),),
                 ( '71913000',(374,189),),
                 ( '71936000',(247,234),),
                 ( '71966000',(125,285),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),1,0,),
               ( ( '71182000',(571,226),),
                 ( '71627001',(535,132),),
                 ( '71852000',(362,133),),
                 ( '71879001',(238,180),),
                 ( '71892001',(129,143),),
                 ( '71913000',(371,229),),
                 ( '71936000',(244,274),),
                 ( '71966000',(122,325),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),1,0,1,),
               ( ( (510,260),'Churchill Falls',),
                 ( (497,166),'Montreal',),
                 ( (322,167),'Winnipeg',),
                 ( (194,214),'Edmonton',),
                 ( (84,177),'Vancouver',),
                 ( (335,263),'Churchill',),
                 ( (192,308),'Yellowknife',),
                 ( (90,359),'Dawson',),
               ),
             ),
        ],
)
dsm.set('Config.1.International.0.Local_InternationalForecast.0', d, 0)
#
wxdata.setInterestList('lambert.us','1',['precipQpfForecast.us','estimatedPrecip.us','travelWeather.us','snowfallQpfForecast.us','palmerDrought.us','frostFreeze.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('precipQpfForecast.us.cuts','1',['Config.1.Garden.0.Local_PrecipitationQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0',])
wxdata.setInterestList('estimatedPrecip.us.cuts','1',['Config.1.Garden.0.Local_EstimatedPrecipitation.0',])
wxdata.setInterestList('frostFreeze.us.cuts','1',['Config.1.Garden.0.Local_FrostFreezeWarnings.0',])
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('palmerDrought.us.cuts','1',['Config.1.Garden.0.Local_PalmerDroughtSeverity.0',])
#
wxdata.setInterestList('mapData','1',['lambert.ca','mercator.us','mercator.mx','lambert.us',])
#
wxdata.setInterestList('imageData','1',['frostFreeze.us','palmerDrought.us','radarSatellite.us','snowfallQpfForecast.us','precipQpfForecast.us','radar.us','travelWeather.us','estimatedPrecip.us',])
#
ds.commit()
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','FSM','IAD','LAX','LGA','LIT','MEM','MIA','ORD','PHL','PHX','SEA','SFO','SLC','STL','TUL','XNA',])
wxdata.setInterestList('coopId','1',['03772000','06240000','07149000','16242000','45007000','47671000','71182000','71624000','71627001','71852000','71879001','71892000','71892001','71913000','71936000','71966000','72205000','72219000','72259000','72295023','72315090','72330002','72334001','72340004','72344000','72344051','72348022','72348039','72348050','72349031','72356000','72405000','72435000','72440000','72440034','72440048','72440054','72440066','72494000','72503023','72509000','72530000','76255000','76393000','76405000','76595000','76679001','78073000','87576000','94767000',])
wxdata.setInterestList('pollenId','1',['HRO',])
wxdata.setInterestList('obsStation','1',['KASG','KBPK','KFSM','KFYV','KHRO','KJLN','KLIT','KMEM','KPAH','KPOF','KROG','KRUE','KRVS','KSGF','KSLG','KSTL','KSTP','KTUL','KUNO','KVBT','KXNA',])
wxdata.setInterestList('metroId','1',['178',])
wxdata.setInterestList('climId','1',['033165',])
wxdata.setInterestList('zone','1',['ARZ003',])
wxdata.setInterestList('aq','1',['zz001',])
wxdata.setInterestList('skiId','1',['616006','704006',])
wxdata.setInterestList('county','1',['ARC009','ARC101',])
#
dsm.set('Config.1.Package.21',('Health',0), 0)
dsm.set('Config.1.Package.10',('International',0), 0)
dsm.set('Config.1.Package.8',('Garden',0), 0)
dsm.set('Config.1.Package.4',('International',0), 0)
dsm.set('Config.1.Package.1',('Garden',0), 0)
dsm.set('Config.1.Package.19',('Core2',0), 0)
dsm.set('Config.1.Package.18',('International',0), 0)
dsm.set('Config.1.Package.15',('Garden',0), 0)
dsm.set('Config.1.Package.14',('Core5',0), 0)
dsm.set('Config.1.Package.13',('Health',0), 0)
dsm.set('Config.1.Package.9',('International',0), 0)
dsm.set('Config.1.Package.6',('Garden',0), 0)
dsm.set('Config.1.Package.3',('Core5',0), 0)
dsm.set('Config.1.Package.2',('Health',0), 0)
dsm.set('Config.1.Package.20',('Core2',0), 0)
dsm.set('Config.1.Package.17',('Garden',0), 0)
dsm.set('Config.1.Package.16',('Health',0), 0)
dsm.set('Config.1.Package.12',('International',0), 0)
dsm.set('Config.1.Package.11',('Airport',0), 0)
dsm.set('Config.1.Package.7',('Travel',0), 0)
dsm.set('Config.1.Package.5',('Garden',0), 0)
dsm.set('Config.1.Package.0',('Health',0), 0)
dsm.set('dmaCode','602', 0)
dsm.set('secondaryObsStation','KBPK', 0)
dsm.set('primaryClimoStation','033165', 0)
dsm.set('stateCode','AR', 0)
dsm.set('expRev','617493', 0)
dsm.set('primaryCoopId','72440066', 0)
dsm.set('primarylat',36.22, 0)
dsm.set('primaryCounty','ARC009', 0)
dsm.set('primaryObsStation','KHRO', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-93.13139, 0)
dsm.set('primaryForecastName','Harrison', 0)
dsm.set('primaryZone','ARZ003', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','022737', 0)
dsm.set('msoName','Cox Communications', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','00915', 0)
dsm.set('msoCode','01179', 0)
dsm.set('headendName','WXS - HARRISON - WXS', 0)
dsm.set('zipCode','72602', 0)
dsm.set('Config.1.irdAddress','0000315577006105', 0)
dsm.set('Config.1.bcNetMask','255.255.255.128', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD02040073', 0)
dsm.set('Config.1.bcDialInNumber','', 0)
dsm.set('Config.1.bcGateWay','24.248.219.129', 0)
dsm.set('Config.1.bcIpAddress','24.248.219.130', 0)
#
#  Non Image Maps
#
d = [
'Config.1.International.0.Local_InternationalForecast.0',
'Config.1.International.0.Local_InternationalForecast.1',
]
dsm.set('Config.1.nonImageMaps', d, 0)
#

#
#
wxdata.setTimeZone('CST6CDT')
#
d = twc.Data()
d.affiliateLogo = 'coxLogo'
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
d = twc.Data()
d.text=[(1127275200,1442807999,[(0,23)],'55194','Coming soon! Finding your local weather will be even easier with immediate access to your forecast, local Doppler radar and the weather affecting you right now. A new look coming soon... here on Weatherscan.'),
]
d.packageGroup = 'Global'
d.crawlFont = 'Frutiger_Bold'
d.crawlFontSize = 21
d.crawlBkgColor = (163,199,235,255)
d.crawlTextColor = (20,20,20,255)
d.maxCrawlSpeed = 2.8
dsm.set('Config.1.LasCrawl_Default', d, 0)
#
#
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.Traffic.0.Local_TrafficReport.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficFlow.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Traffic.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.Local_PackageIntro.0')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.3')
scmtRemove('Config.1.International.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Traffic.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.International.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.International.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.1')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.4')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.International.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Traffic.0.Local_TrafficOverview.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.SmLocal_TrafficSponsor.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Traffic.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.International.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.International.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.2')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.5')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
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
scmtRemove('Config.1.International.0')
d = twc.Data()
d.bkgImage = 'international_bg'
d.packageTitle = 'International Forecast'
d.packageFlavor = 3
d.shortPackageTitle = 'INTERNATIONAL'
dsm.set('Config.1.International.0', d, 0, 1)
scmtRemove('Config.1.SevereCore2.0')
d = twc.Data()
d.bkgImage = 'severe_core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'YOUR LOCAL FORECAST'
dsm.set('Config.1.SevereCore2.0', d, 0, 1)
scmtRemove('Config.1.Airport.0')
d = twc.Data()
d.bkgImage = 'airport_bg'
d.packageTitle = 'Airport Conditions'
d.packageFlavor = 3
d.shortPackageTitle = 'AIRPORT'
dsm.set('Config.1.Airport.0', d, 0, 1)
scmtRemove('Config.1.Core5.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 0
d.shortPackageTitle = 'HARRISON RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'HARRISON'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'HARRISON'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'HARRISON'
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
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'HARRISON'
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
d.packageFlavor = 3
d.shortPackageTitle = 'TRAFFIC'
dsm.set('Config.1.Traffic.0', d, 0, 1)
scmtRemove('Config.1.Health.0')
d = twc.Data()
d.bkgImage = 'health_bg'
d.packageTitle = 'Weather & Your Health'
d.packageFlavor = 2
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'international_intro_bg'
dsm.set('Config.1.International.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KASG','KFYV','KFSM','KROG','KVBT','KXNA','KSLG','KRUE','KJLN','KTUL',]
d.locName = ['Springdale','Fayetteville','Fort Smith','Rogers','Bentonville','NW AR Reg Arpt.','Siloam Springs','Russellville','Joplin','Tulsa',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SFO','PHL','SEA','STL',]
d.obsStation = ['KSFO','KPHL','KSEA','KSTL',]
d.locName = ['San Francisco Int`l','Philadelphia Int`l','Seattle - Tacoma Int`l','Lambert - St. Louis Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','LIT','IAD',]
d.obsStation = ['KMIA','KPHX','KLIT','KIAD',]
d.locName = ['Miami International','Phoenix / Sky Harbor','Adams Field / Little Rock','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','FSM','SLC',]
d.obsStation = ['KDFW','KDEN','KFSM','KSLC',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Fort Smith Regional','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Harrison'
d.coopId = '72440066'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Nassau','Amsterdam','Buenos Aires',]
d.coopId = ['78073000','06240000','87576000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','ORD','LAX','ATL',]
d.obsStation = ['KLGA','KORD','KLAX','KATL',]
d.locName = ['New York / LaGuardia','Chicago O`Hare Int`l','Los Angeles International','Atlanta International',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Rome','Vancouver','Hong Kong',]
d.coopId = ['16242000','71892000','45007000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Cancun','Tokyo','Sydney',]
d.coopId = ['76595000','47671000','94767000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KSGF','KLIT','KMEM','KSTL','KTUL','KFSM',]
d.locName = ['Springfield','Little Rock','Memphis','St. Louis','Tulsa','Fort Smith',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Toronto','London','Paris',]
d.coopId = ['71624000','03772000','07149000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'KHRO'
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Cox'
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.pollenId = 'HRO'
dsm.set('Config.1.Health.0.Local_AllergyReport.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Harrison'
d.coopId = '72440066'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Harrison'
d.coopId = '72440066'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 1
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Springdale','Fayetteville','Fort Smith','Rogers','Bentonville','NW AR Reg Arpt.','Siloam Springs','Russellville','Joplin','Tulsa',]
d.coopId = ['72344054','72344041','72344000','72440072','72344059','72344053','72440079','72349026','72440057','72356006',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KVBT','KFYV','KFSM','KROG',]
d.locName = ['Bentonville','Fayetteville','Fort Smith','Rogers',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KASG','KXNA','KSLG','KRUE',]
d.locName = ['Springdale','NW AR Reg Arpt.','Siloam Springs','Russellville',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Springfield','Little Rock','Memphis','St. Louis','Tulsa','Fort Smith',]
d.coopId = ['72440000','72340004','72334000','72435000','72356006','72344000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison Area'
d.zone = 'ARZ003'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.aq = 'zz001'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Orlando','Washington, DC','San Francisco',]
d.coopId = ['72205000','72405000','72494000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Dallas','Boston',]
d.coopId = ['72219000','72259000','72509000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KVBT','KFYV','KFSM','KROG',]
d.locName = ['Bentonville','Fayetteville','Fort Smith','Rogers',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Cox'
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KASG','KXNA','KSLG','KRUE',]
d.locName = ['Springdale','NW AR Reg Arpt.','Siloam Springs','Russellville',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KHRO','KBPK',]
d.locName = ['Harrison','Mountain Home',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.bkgImage = 'neighborhood_bg'
d.affiliateName = 'Cox Digital Cable'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '033165'
d.latitude = 36.22
d.longitude = -93.13
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'garden_intro_bg'
dsm.set('Config.1.Garden.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Cox'
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Harrison'
d.coopId = '72440066'
dsm.set('Config.1.Garden.0.Local_GardeningForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'TUL'
d.obsStation = 'KTUL'
d.locName = 'Tulsa International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['XNA','FSM',]
d.obsStation = ['KXNA','KFSM',]
d.locName = ['Northwest Regional Arpt.','Fort Smith Regional Arpt.',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'XNA'
d.obsStation = 'KXNA'
d.locName = 'Northwest Arkansas Regional Arpt.'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.preRoll = 8
d.schedule = ((14,60),(29,60),(44,60),(58,120),)
dsm.set('Config.1.Local_Avail_Schedule', d, 0)
#
# End of SCMT deployment
#
d = twc.Data()
d.text=[
(1758996325,1798996325,[(0,23)],'480282','VISIT THE NEW SIX SISTERS COFFEE AND CREPES IN DOWNTOWN HARRISON! FRESH HANDMADE CREPES AND SPECIALTY COFFEE DAILY. LOCATED IN THE HISTORIC DOWNTOWN DISTRICT. OPEN 7AM-3PM MONDAY-SATURDAY. FOLLOW US ON FACEBOOK FOR DAILY SPECIALS!'),
(1758996325,1798996325,[(0,23)],'480871','NORTHWEST ARKANSAS DISTRICT FAIR COMING UP! ENJOY GO-CART RACES, DEMOLITION DERBY, LIVESTOCK SHOWS, AND CREATIVE ARTS EXHIBITS. CHECK OUT THE KOUNTRY KITCHEN FOR HOME-STYLE FOOD. VISIT NORTHWESTARKANSASDISTRICTFAIR.COM FOR DATES AND ADMISSION INFO.'),
(1758996325,1798996325,[(0,23)],'484971','EXPLORE HARRISON ARKANSAS - WHERE BUSINESS THRIVES AMID BREATHTAKING LANDSCAPES! DISCOVER OUTDOOR ADVENTURES NEAR BUFFALO NATIONAL RIVER. HIKING, CAMPING, BIKING, HUNTING AND FISHING AWAIT. PERFECT WORK-LIFE BALANCE IN THE OZARKS!'),
(1758996325,1798996325,[(0,23)],'485066','NEW 1915 CAFE & BAKERY NOW OPEN IN DOWNTOWN HARRISON! FRESH BAKED GOODS, LUNCH SPECIALS, AND COFFEE. HOUSED IN A HISTORIC BUILDING WITH CHARMING ATMOSPHERE. PERFECT FOR BUSINESS MEETINGS OR CASUAL DINING. VISIT US TODAY!'),
(1758996325,1798996325,[(0,23)],'486203','BOBA JOES NOW SERVING HARRISON! BUBBLE TEA, SMOOTHIES, AND ASIAN-INSPIRED DRINKS IN DOWNTOWN. TRY OUR SIGNATURE FLAVORS AND FRESH FRUIT TEAS. PERFECT REFRESHMENT FOR OZARK ADVENTURES. OPEN DAILY 11AM-8PM.'),
(1758996325,1798996325,[(0,23)],'487556','TWO RAVENS RESTAURANT AT THE HISTORIC 1929 HOTEL SEVILLE! FINE DINING WITH OZARK CHARM. LOCALLY SOURCED INGREDIENTS AND CRAFT COCKTAILS. HISTORIC AMBIANCE MEETS MODERN CUISINE. RESERVATIONS RECOMMENDED. CALL FOR HOURS.'),
(1758996325,1798996325,[(0,23)],'490367','HARRISON CHAMBER OF COMMERCE WORKFORCE INITIATIVE NETWORK SUMMIT! EDUCATORS AND BUSINESS LEADERS UNITE TO DISCUSS THE FUTURE OF WORK. BUILDING CONNECTIONS FOR A STRONGER COMMUNITY. CHECK HARRISON-CHAMBER.COM FOR EVENT DETAILS.'),
(1758996325,1798996325,[(0,23)],'491782','OCTOBER EVENTS IN HARRISON! FALL FESTIVALS AND SEASONAL ACTIVITIES FROM OCTOBER 3-12. OZARK MOUNTAIN COLORS AT THEIR PEAK. PLAN YOUR VISIT TO EXPERIENCE ARKANSAS NATURAL BEAUTY. VISIT EXPLOREHARRISON.COM FOR FULL SCHEDULE.'),
(1758996325,1798996325,[(0,23)],'491787','NENOS PLACE FORMERLY THE POUR HOUSE NOW OPEN! NEW MANAGEMENT, SAME GREAT LOCATION. COMFORT FOOD AND FRIENDLY ATMOSPHERE IN HARRISON. DAILY LUNCH AND DINNER SPECIALS. COME TASTE THE DIFFERENCE!'),
(1758996325,1798996325,[(0,23)],'491792','HARRISON DAILY TIMES - IN CONTINUOUS PUBLICATION SINCE 1876! STAY INFORMED WITH LOCAL NEWS, SPORTS, AND COMMUNITY EVENTS. YOUR TRUSTED SOURCE FOR HARRISON AND BOONE COUNTY NEWS. SUBSCRIBE TODAY AT HARRISONDAILY.COM.'),
(1758996325,1798996325,[(0,23)],'491799','A GRINCH CHRISTMAS COMING DECEMBER 1ST! FAMILY-FRIENDLY HOLIDAY ENTERTAINMENT IN HARRISON. REGISTER NOW FOR THIS FESTIVE EVENT. BRING THE WHOLE FAMILY FOR HOLIDAY CHEER AND COMMUNITY FUN.'),
(1758996325,1798996325,[(0,23)],'491803','DECEMBER 10-14 HOLIDAY EVENTS IN HARRISON! MULTIPLE CHRISTMAS CELEBRATIONS AND WINTER ACTIVITIES. BUY TICKETS NOW FOR THE BEST SELECTION. CREATE LASTING HOLIDAY MEMORIES IN THE OZARKS.'),
(1758996325,1798996325,[(0,23)],'491809','TUNE IN TO KHOZ 94.9 FM & AM 900 - HARRISONS #1 ORIGINAL COUNTRY MUSIC STATION! LOCAL NEWS, WEATHER, AND THE BEST COUNTRY HITS. STAY CONNECTED TO YOUR COMMUNITY. HARRISONSORIGINALKHOZ.COM FOR MORE.'),
(1758996325,1798996325,[(0,23)],'491954','THE CAKE SHOP HARRISON - CUSTOM CAKES AND SWEET TREATS FOR EVERY OCCASION! BIRTHDAYS, WEDDINGS, AND SPECIAL EVENTS. FRESH BAKED DAILY WITH QUALITY INGREDIENTS. ORDER AHEAD FOR BEST SELECTION.'),
(1758996325,1798996325,[(0,23)],'493422','HARRISON CONVENTION & VISITORS BUREAU - DISCOVER ALL HARRISON HAS TO OFFER! OUTDOOR RECREATION, HISTORIC SITES, LOCAL DINING AND SHOPPING. PLAN YOUR OZARK ADVENTURE TODAY. VISIT EXPLOREHARRISON.COM FOR MORE INFO.'),
(1758996325,1798996325,[(0,23)],'493424','BUFFALO NATIONAL RIVER ACCESS NEAR HARRISON! WORLD-CLASS CANOEING, KAYAKING, AND FISHING. CRYSTAL CLEAR SPRING-FED WATERS AND PRISTINE WILDERNESS. YOUR OZARK OUTDOOR ADVENTURE STARTS HERE!'),
(1758996325,1798996325,[(0,23)],'493426','HARRISON HISTORIC DOWNTOWN DISTRICT REVITALIZATION! NEW RESTAURANTS, SHOPS, AND BUSINESSES OPENING. EXPLORE THE CHARM OF SMALL-TOWN ARKANSAS WITH MODERN AMENITIES. SUPPORT LOCAL BUSINESS!'),
(1758996325,1798996325,[(0,23)],'493428','FALL COLORS AND OZARK SCENIC DRIVES! HARRISON IS YOUR GATEWAY TO ARKANSAS NATURAL BEAUTY. HIKING TRAILS, SCENIC OVERLOOKS, AND PHOTO OPPORTUNITIES. PEAK FOLIAGE SEPTEMBER-OCTOBER. DONT MISS IT!'),
(1758996325,1798996325,[(0,23)],'493430','JOIN THE HARRISON COMMUNITY FOR GENUINE OZARK HOSPITALITY! BUSINESS-FRIENDLY ENVIRONMENT WITH WORK-LIFE BALANCE. NEAR PRISTINE LAKES AND RIVERS. DISCOVER WHY HARRISON IS THE PERFECT PLACE TO CALL HOME.'),
(1758996325,1798996325,[(0,23)],'493432','HARRISON AREA BUSINESS OPPORTUNITIES! STRATEGICALLY LOCATED IN THE HEART OF THE OZARKS. GROWING COMMUNITY WITH OUTDOOR RECREATION AND TOURISM. CONTACT THE HARRISON CHAMBER FOR BUSINESS DEVELOPMENT INFO.')]
d.packageGroup = 'Global'
d.crawlFont = 'Frutiger_Bold'
d.crawlFontSize = 21
d.crawlBkgColor = (163,199,235,255)
d.crawlTextColor = (20,20,20,255)
d.maxCrawlSpeed = 5
dsm.set('Config.1.LasCrawl_Default', d, 0)

ds.commit()
twc.Log.info('scmt config finished')
# Finished generation on Thu Sep 22 12:43:46 EDT 2005