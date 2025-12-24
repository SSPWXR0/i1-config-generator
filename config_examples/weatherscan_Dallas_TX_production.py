# Created on Tue Nov 18 18:31:33 EDT 2025
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
               ( ( (124,61),),
                 ( (124,35),),
                 ( (148,61),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (124,61),),
                 ( (124,35),),
                 ( (148,61),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (94,58),'Dallas',),
                 ( (110,28),'Ft Worth',),
                 ( (156,68),'Tyler',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (94,58),'Dallas',),
                 ( (110,28),'Ft Worth',),
                 ( (156,68),'Tyler',),
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
               ( ( (360,240),'35E',),
                 ( (320,180),'35W',),
                 ( (280,240),'30',),
                 ( (440,200),'20',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (360,240),'35E',),
                 ( (320,180),'35W',),
                 ( (280,240),'30',),
                 ( (440,200),'20',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (360,240),),
                 ( (320,180),),
                 ( (280,240),),
                 ( (400,280),),
                 ( (480,220),),
                 ( (240,200),),
                 ( (380,160),),
                 ( (300,300),),
                 ( (440,260),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (360,240),),
                 ( (320,180),),
                 ( (280,240),),
                 ( (400,280),),
                 ( (480,220),),
                 ( (240,200),),
                 ( (380,160),),
                 ( (300,300),),
                 ( (440,260),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (340,260),'Dallas',),
                 ( (300,160),'Fort Worth',),
                 ( (240,260),'Arlington',),
                 ( (380,300),'Mesquite',),
                 ( (500,240),'Tyler',),
                 ( (220,220),'Denton',),
                 ( (400,140),'McKinney',),
                 ( (280,320),'Waxahachie',),
                 ( (460,280),'Rockwall',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (340,260),'Dallas',),
                 ( (300,160),'Fort Worth',),
                 ( (240,260),'Arlington',),
                 ( (380,300),'Mesquite',),
                 ( (500,240),'Tyler',),
                 ( (220,220),'Denton',),
                 ( (400,140),'McKinney',),
                 ( (280,320),'Waxahachie',),
                 ( (460,280),'Rockwall',),
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
               ( ( '72259000',(360,240),),
                 ( '72243000',(450,180),),
                 ( '72249000',(280,200),),
                 ( '72265000',(520,240),),
                 ( '72240000',(220,280),),
                 ( '72293000',(380,320),),
                 ( '72251000',(280,140),),
                 ( '72208000',(540,320),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72259000',(357,276),),
                 ( '72243000',(447,216),),
                 ( '72249000',(277,236),),
                 ( '72265000',(517,276),),
                 ( '72240000',(217,316),),
                 ( '72293000',(377,356),),
                 ( '72251000',(277,176),),
                 ( '72208000',(537,356),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (320,308),'Dallas',),
                 ( (410,248),'Tyler',),
                 ( (237,268),'Fort Worth',),
                 ( (477,308),'Longview',),
                 ( (177,348),'Waco',),
                 ( (337,388),'Corsicana',),
                 ( (237,208),'Denton',),
                 ( (497,388),'Texarkana',),
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
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','IAD','IAH','LAX','LGA','MIA','ORD','PHL','PHX','SEA','SFO','SLC','STL','AUS','SAT','HOU','DAL',])
wxdata.setInterestList('coopId','1',['03772000','06240000','07149000','16242000','45007000','47671000','71182000','71624000','71627001','71852000','71879001','71892000','71892001','71913000','71936000','71966000','72205000','72219000','72240000','72243000','72249000','72251000','72259000','72265000','72293000','72208000','72235000','72266000','72245000','76255000','76393000','76405000','76595000','76679001','78073000','87576000','94767000',])
wxdata.setInterestList('pollenId','1',['DFW',])
wxdata.setInterestList('obsStation','1',['KDFW','KDAL','KFTW','KADS','KDTO','KGKY','KTKI','KTRL','KGVT','KACT','KAUS','KSAT','KIAH','KHOU','KABI','KLBB','KMAF','KSPS','KSJT','KCRP','KWRI',])
wxdata.setInterestList('metroId','1',['623',])
wxdata.setInterestList('climId','1',['412428',])
wxdata.setInterestList('zone','1',['TXZ103',])
wxdata.setInterestList('aq','1',['zz001',])
wxdata.setInterestList('skiId','1',['',])
wxdata.setInterestList('county','1',['TXC113','TXC121','TXC139','TXC231','TXC257','TXC397',])
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
dsm.set('dmaCode','623', 0)
dsm.set('secondaryObsStation','KFTW', 0)
dsm.set('primaryClimoStation','412428', 0)
dsm.set('stateCode','TX', 0)
dsm.set('expRev','617493', 0)
dsm.set('primaryCoopId','72259000', 0)
dsm.set('primarylat',32.85, 0)
dsm.set('primaryCounty','TXC113', 0)
dsm.set('primaryObsStation','KDFW', 0)
dsm.set('hasTraffic',1, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-96.85, 0)
dsm.set('primaryForecastName','Dallas', 0)
dsm.set('primaryZone','TXZ103', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','099999', 0)
dsm.set('msoName','Mist Digital Cable', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','00915', 0)
dsm.set('msoCode','99999', 0)
dsm.set('headendName','WXS - DALLAS - WXS', 0)
dsm.set('zipCode','75201', 0)
dsm.set('Config.1.irdAddress','0000315577099999', 0)
dsm.set('Config.1.bcNetMask','255.255.255.128', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD02040099', 0)
dsm.set('Config.1.bcDialInNumber','', 0)
dsm.set('Config.1.bcGateWay','10.0.0.1', 0)
dsm.set('Config.1.bcIpAddress','10.0.0.2', 0)
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
d.affiliateLogo = 'mistLogo'
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
d.shortPackageTitle = 'DALLAS RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'DALLAS'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'DALLAS'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'DALLAS'
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
d.shortPackageTitle = 'DALLAS'
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
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'international_intro_bg'
dsm.set('Config.1.International.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KFTW','KADS','KDTO','KGKY','KTKI','KTRL','KGVT','KACT',]
d.locName = ['Fort Worth','Addison','Denton','Arlington','McKinney','Terrell','Greenville','Waco',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SFO','PHL','SEA','STL',]
d.obsStation = ['KSFO','KPHL','KSEA','KSTL',]
d.locName = ['San Francisco Int`l','Philadelphia Int`l','Seattle - Tacoma Int`l','Lambert - St. Louis Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','IAH','IAD',]
d.obsStation = ['KMIA','KPHX','KIAH','KIAD',]
d.locName = ['Miami International','Phoenix / Sky Harbor','George Bush Intercontinental','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','DAL','SLC',]
d.obsStation = ['KDFW','KDEN','KDAL','KSLC',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Dallas Love Field','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Dallas'
d.coopId = '72259000'
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
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Rome','Vancouver','Hong Kong',]
d.coopId = ['16242000','71892000','45007000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Cancun','Tokyo','Sydney',]
d.coopId = ['76595000','47671000','94767000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KAUS','KSAT','KHOU','KABI','KLBB','KMAF',]
d.locName = ['Austin','San Antonio','Houston','Abilene','Lubbock','Midland',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Toronto','London','Paris',]
d.coopId = ['71624000','03772000','07149000',]
dsm.set('Config.1.International.0.Local_InternationalDestinations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'KDFW'
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Mist'
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.pollenId = 'DFW'
dsm.set('Config.1.Health.0.Local_AllergyReport.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Dallas'
d.coopId = '72259000'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Dallas'
d.coopId = '72259000'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 1
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Fort Worth','Addison','Denton','Arlington','McKinney','Terrell','Greenville','Waco',]
d.coopId = ['72249000','72259001','72251000','72240000','72259002','72259003','72259004','72240000',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KFTW','KADS','KDTO','KGKY',]
d.locName = ['Fort Worth','Addison','Denton','Arlington',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KTKI','KTRL','KGVT','KACT',]
d.locName = ['McKinney','Terrell','Greenville','Waco',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Austin','San Antonio','Houston','Abilene','Lubbock','Midland',]
d.coopId = ['72235000','72266000','72243000','72265000','72245000','72265001',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas Area'
d.zone = 'TXZ103'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
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
d.locName = ['Atlanta','Houston','Boston',]
d.coopId = ['72219000','72243000','72509000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KFTW','KADS','KDTO','KGKY',]
d.locName = ['Fort Worth','Addison','Denton','Arlington',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Mist'
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KTKI','KTRL','KGVT','KACT',]
d.locName = ['McKinney','Terrell','Greenville','Waco',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Airport','Love Field',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.bkgImage = 'neighborhood_bg'
d.affiliateName = 'Mist Digital Cable'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '412428'
d.latitude = 32.85
d.longitude = -96.85
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'garden_intro_bg'
dsm.set('Config.1.Garden.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Mist'
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Dallas'
d.coopId = '72259000'
dsm.set('Config.1.Garden.0.Local_GardeningForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'DFW'
d.obsStation = 'KDFW'
d.locName = 'Dallas / Fort Worth Int`l Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DAL',]
d.obsStation = ['KDFW','KDAL',]
d.locName = ['DFW Int`l Airport','Love Field Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'DAL'
d.obsStation = 'KDAL'
d.locName = 'Dallas Love Field Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
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