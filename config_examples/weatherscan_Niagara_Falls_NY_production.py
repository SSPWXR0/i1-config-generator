# Created on Tue Jan 11 17:16:00 GMT 2022
twc.Log.info('scmt config started')
# EXP: 24057
# VIW: 505981
# CLN: 2364
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
# MAP: 121938
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(22625,14961),
             mapcutSize=(3376,1674),
             mapFinalSize=(248,123),
             mapMilesSize=(299,178),
             datacutType='radar.us',
             datacutCoordinate=(2372,1495),
             datacutSize=(414,205),
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
               ( ( (137,93),),
                 ( (75,28),),
                 ( (120,57),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (137,93),),
                 ( (75,28),),
                 ( (120,57),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (148,88),'Marquette',),
                 ( (89,26),'Antigo',),
                 ( (74,71),'Niagara',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (148,88),'Marquette',),
                 ( (89,26),'Antigo',),
                 ( (74,71),'Niagara',),
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
# MAP: 121936
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21869,14164),
             mapcutSize=(4896,3264),
             mapFinalSize=(720,480),
             mapMilesSize=(435,348),
             datacutType='radar.us',
             datacutCoordinate=(2280,1398),
             datacutSize=(599,399),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (632,300),),
                 ( (431,240),),
                 ( (183,305),),
                 ( (388,305),),
                 ( (545,134),),
                 ( (120,307),),
                 ( (351,114),),
                 ( (352,233),),
                 ( (222,153),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (632,300),),
                 ( (431,240),),
                 ( (183,305),),
                 ( (388,305),),
                 ( (545,134),),
                 ( (120,307),),
                 ( (351,114),),
                 ( (352,233),),
                 ( (222,153),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (481,321),'Sault Ste Marie',),
                 ( (451,243),'Gladstone',),
                 ( (187,285),'Ironwood',),
                 ( (302,329),'Marquette',),
                 ( (486,155),'Traverse City',),
                 ( (93,330),'Ashland',),
                 ( (371,117),'Green Bay',),
                 ( (314,216),'Niagara',),
                 ( (138,170),'Wausau',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (481,321),'Sault Ste Marie',),
                 ( (451,243),'Gladstone',),
                 ( (187,285),'Ironwood',),
                 ( (302,329),'Marquette',),
                 ( (486,155),'Traverse City',),
                 ( (93,330),'Ashland',),
                 ( (371,117),'Green Bay',),
                 ( (314,216),'Niagara',),
                 ( (138,170),'Wausau',),
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
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
# MAP: 121937
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(22488,14768),
             mapcutSize=(3385,2257),
             mapFinalSize=(720,480),
             mapMilesSize=(300,240),
             datacutType='radar.us',
             datacutCoordinate=(2355,1471),
             datacutSize=(415,277),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (495,222),),
                 ( (136,316),),
                 ( (434,316),),
                 ( (424,123),),
                 ( (253,126),),
                 ( (353,231),),
                 ( (382,212),),
                 ( (212,192),),
                 ( (194,96),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (495,222),),
                 ( (136,316),),
                 ( (434,316),),
                 ( (424,123),),
                 ( (253,126),),
                 ( (353,231),),
                 ( (382,212),),
                 ( (212,192),),
                 ( (194,96),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (508,247),'Gladstone',),
                 ( (149,336),'Ironwood',),
                 ( (441,341),'Marquette',),
                 ( (442,114),'Menominee',),
                 ( (271,111),'Antigo',),
                 ( (279,254),'Florence',),
                 ( (370,192),'Niagara',),
                 ( (122,218),'Rhinelander',),
                 ( (110,113),'Wausau',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (508,247),'Gladstone',),
                 ( (149,336),'Ironwood',),
                 ( (441,341),'Marquette',),
                 ( (442,114),'Menominee',),
                 ( (271,111),'Antigo',),
                 ( (279,254),'Florence',),
                 ( (370,192),'Niagara',),
                 ( (122,218),'Rhinelander',),
                 ( (110,113),'Wausau',),
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
dsm.set('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
# MAP: 77149
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3563,1858),
             mapcutSize=(1656,1104),
             mapFinalSize=(720,480),
             mapMilesSize=(1593,1077),
             datacutType='radarSatellite.us',
             datacutCoordinate=(938,613),
             datacutSize=(851,571),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
# MAP: 76722
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3381,1810),
             mapcutSize=(1496,997),
             mapFinalSize=(720,480),
             mapMilesSize=(1451,979),
             datacutType='radarSatellite.us',
             datacutCoordinate=(844,588),
             datacutSize=(769,515),
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
# MAP: 210
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(17939,10087),
             mapcutSize=(14496,9664),
             mapFinalSize=(720,480),
             mapMilesSize=(1319,1055),
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
               ( ( '72528000',(561,143),),
                 ( '72530000',(311,98),),
                 ( '72537000',(436,113),),
                 ( '72546000',(157,108),),
                 ( '72639000',(432,209),),
                 ( '72645000',(295,191),),
                 ( '72658000',(166,208),),
                 ( '72743000',(314,283),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72528000',(558,183),),
                 ( '72530000',(308,138),),
                 ( '72537000',(433,153),),
                 ( '72546000',(154,148),),
                 ( '72639000',(429,249),),
                 ( '72645000',(292,231),),
                 ( '72658000',(163,248),),
                 ( '72743000',(311,323),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (529,217),'Buffalo',),
                 ( (276,172),'Chicago',),
                 ( (406,187),'Detroit',),
                 ( (105,182),'Des Moines',),
                 ( (401,283),'Alpena',),
                 ( (248,265),'Green Bay',),
                 ( (110,282),'Minneapolis',),
                 ( (266,357),'Marquette',),
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
             mapcutCoordinate=(3073,1467),
             mapcutSize=(2276,1517),
             mapFinalSize=(720,480),
             mapMilesSize=(2184,1486),
             datacutType='estimatedPrecip.us',
             datacutCoordinate=(494,397),
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
#
wxdata.setInterestList('lambert.us','1',['precipQpfForecast.us','estimatedPrecip.us','travelWeather.us','snowfallQpfForecast.us','palmerDrought.us','frostFreeze.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('precipQpfForecast.us.cuts','1',['Config.1.Garden.0.Local_PrecipitationQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.Core2.1.Local_LocalDoppler.0','Config.1.Core3.1.Local_LocalDoppler.0',])
wxdata.setInterestList('estimatedPrecip.us.cuts','1',['Config.1.Garden.0.Local_EstimatedPrecipitation.0',])
wxdata.setInterestList('frostFreeze.us.cuts','1',['Config.1.Garden.0.Local_FrostFreezeWarnings.0',])
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.1.Local_RadarSatelliteComposite.0','Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('palmerDrought.us.cuts','1',['Config.1.Garden.0.Local_PalmerDroughtSeverity.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['frostFreeze.us','palmerDrought.us','radarSatellite.us','snowfallQpfForecast.us','precipQpfForecast.us','radar.us','travelWeather.us','estimatedPrecip.us',])
#
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','GRB','IAD','LAX','LGA','MDW','MIA','MKE','MSP','ORD','PHX','SAW','SLC',])
wxdata.setInterestList('coopId','1',['72205000','72219000','72259000','72295023','72405000','72494000','72503023','72509000','72528000','72530000','72537000','72546000','72634030','72638006','72638041','72639000','72640000','72641000','72645000','72645064','72645079','72645102','72645107','72648000','72648015','72648024','72648028','72648033','72658000','72734000','72741043','72741047','72741055','72743000','72743010','72743019','72743020','72743024','72745000',])
wxdata.setInterestList('obsStation','1',['KIMT','T72202000','T72219000','T72259000','T72278000','T72295000','T72403000','T72503000','T72509000','T72530000','T72534000','T72565000','T72572000','T72638006','T72640000','T72641000','T72645000','T72645064','T72645079','T72645102','T72645107','T72648000','T72648015','T72648024','T72648028','T72648033','T72658000','T72734000','T72741043','T72741047','T72741055','T72743010','T72743019','T72743020','T72743024','T72745000',])
wxdata.setInterestList('climId','1',['204090','471139',])
wxdata.setInterestList('zone','1',['WIZ012','WIZ013',])
wxdata.setInterestList('aq','1',['mi010',])
wxdata.setInterestList('skiId','1',['108','187','191','230','25','314','321','370','43','482','496','616002','616006','77',])
wxdata.setInterestList('county','1',['WIC075','WIC037',])
#
dsm.set('Config.1.Package.36',('Ski',0), 0)
dsm.set('Config.1.Package.34',('Core2',1), 0)
dsm.set('Config.1.Package.25',('Core2',1), 0)
dsm.set('Config.1.Package.31',('Core4',0), 0)
dsm.set('Config.1.Package.23',('Core3',0), 0)
dsm.set('Config.1.Package.29',('Core3',1), 0)
dsm.set('Config.1.Package.18',('Airport',0), 0)
dsm.set('Config.1.Package.16',('Core5',0), 0)
dsm.set('Config.1.Package.13',('Core4',1), 0)
dsm.set('Config.1.Package.9',('Core2',0), 0)
dsm.set('Config.1.Package.7',('Travel',0), 0)
dsm.set('Config.1.Package.5',('Health',0), 0)
dsm.set('Config.1.Package.0',('Core3',1), 0)
dsm.set('Config.1.Package.38',('Ski',0), 0)
dsm.set('Config.1.Package.35',('Core3',1), 0)
dsm.set('Config.1.Package.26',('Core3',0), 0)
dsm.set('Config.1.Package.32',('Core4',0), 0)
dsm.set('Config.1.Package.22',('Airport',0), 0)
dsm.set('Config.1.Package.28',('Core2',1), 0)
dsm.set('Config.1.Package.20',('Core5',0), 0)
dsm.set('Config.1.Package.15',('Travel',0), 0)
dsm.set('Config.1.Package.12',('Core4',1), 0)
dsm.set('Config.1.Package.10',('Core2',0), 0)
dsm.set('Config.1.Package.6',('Core5',0), 0)
dsm.set('Config.1.Package.4',('Health',0), 0)
dsm.set('Config.1.Package.2',('Core3',1), 0)
dsm.set('Config.1.Package.37',('Core5',0), 0)
dsm.set('Config.1.Package.33',('Ski',0), 0)
dsm.set('Config.1.Package.24',('Core2',0), 0)
dsm.set('Config.1.Package.30',('Core3',0), 0)
dsm.set('Config.1.Package.21',('Health',0), 0)
dsm.set('Config.1.Package.27',('Core4',1), 0)
dsm.set('Config.1.Package.19',('Core5',0), 0)
dsm.set('Config.1.Package.17',('Core2',0), 0)
dsm.set('Config.1.Package.14',('Core3',1), 0)
dsm.set('Config.1.Package.11',('Core4',0), 0)
dsm.set('Config.1.Package.8',('Airport',0), 0)
dsm.set('Config.1.Package.3',('Travel',0), 0)
dsm.set('Config.1.Package.1',('Core2',1), 0)
dsm.set('dmaCode','658', 0)
dsm.set('secondaryObsStation','KIMT', 0)
dsm.set('primaryClimoStation','204090', 0)
dsm.set('stateCode','WI', 0)
dsm.set('primaryCoopId','72648024', 0)
dsm.set('wda','Y55', 0)
dsm.set('severeClockActive','1', 0)
dsm.set('primaryCounty','WIC075', 0)
dsm.set('primaryObsStation','T72648024', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('wdr','GRB', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryForecastName','Niagara', 0)
dsm.set('primaryZone','WIZ013', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','038015', 0)
dsm.set('msoName','Northeast Communications of Wisconsin', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','08120', 0)
dsm.set('msoCode','01803', 0)
dsm.set('headendName','WXS - NIAGARA - WXS', 0)
dsm.set('zipCode','54313', 0)
dsm.set('Config.1.irdAddress','0001140994485185', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCS03040062', 0)
dsm.set('Config.1.bcGateWay','10.10.10.1', 0)
dsm.set('Config.1.bcIpAddress','10.10.10.10', 0)
#
#  Non Image Maps
#
#

#
#
wxdata.setTimeZone('CST6CDT')
#
d = twc.Data()
d.affiliateLogo = 'nSightLogo'
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
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Core2.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Core4.1.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core2.1.Local_MenuBoard.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.Core3.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Movie.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.LocalBroadcaster.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.1.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core4.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_TextForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core4.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core4.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Almanac.0')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Local_TextForecast.0')
scmtRemove('Config.1.Core3.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core4.1.Fcst_TextForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
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
scmtRemove('Config.1.Airport.0')
d = twc.Data()
d.bkgImage = 'airport_bg'
d.packageTitle = 'Airport Conditions'
d.packageFlavor = 2
d.shortPackageTitle = 'AIRPORT'
dsm.set('Config.1.Airport.0', d, 0, 1)
scmtRemove('Config.1.Core5.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 1
d.shortPackageTitle = 'LOCAL RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'FLORENCE'
dsm.set('Config.1.Core4.1', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'NIAGARA'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'FLORENCE'
dsm.set('Config.1.Core3.1', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'NIAGARA'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'FLORENCE'
dsm.set('Config.1.Core2.1', d, 0, 1)
scmtRemove('Config.1.LocalBroadcaster.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.region = '000000'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 0
d.shortPackageTitle = 'Your Local Forecast'
dsm.set('Config.1.LocalBroadcaster.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'NIAGARA'
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
d.shortPackageTitle = 'NIAGARA'
dsm.set('Config.1.Core1.0', d, 0, 1)
scmtRemove('Config.1.Health.0')
d = twc.Data()
d.bkgImage = 'health_bg'
d.packageTitle = 'Weather & Your Health'
d.packageFlavor = 1
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Niagara'
d.coopId = '72648024'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Travel.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Airport.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Florence'
d.coopId = '72743020'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.1.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'ski_intro_bg'
dsm.set('Config.1.Ski.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743019','T72743024','T72648033','T72645102','T72648015','T72648000','T72645079','T72741047','T72741055','T72648028',]
d.locName = ['Crystal Falls',' Iron River',' Goodman',' Laona',' Stephenson',' Escanaba',' Menominee',' Rhinelander',' Eagle River',' Iron Mountain',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Airport.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Ski.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743020','KIMT',]
d.locName = ['Florence','Iron Mountain',]
dsm.set('Config.1.Core2.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1B.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Crystal Falls',' Iron River',' Goodman',' Laona',' Stephenson',' Escanaba',' Menominee',' Rhinelander',' Eagle River',' Iron Mountain',]
d.coopId = ['72743019','72743024','72648033','72645102','72648015','72648000','72645079','72741047','72741055','72648028',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Health.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Airport.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72638006','T72743010','T72745000','T72658000','T72641000','T72741043','T72645107','T72645064','T72734000','T72640000',]
d.locName = ['Houghton Lake',' Marquette',' Duluth',' Minneapolis',' Madison',' Tomahawk',' Wausau',' Sturgeon Bay',' Sault Ste. Marie',' Milwaukee',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Ski.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.coopId = '72648000'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743020','KIMT',]
d.locName = ['Florence','Iron Mountain',]
dsm.set('Config.1.Core4.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Houghton Lake',' Marquette',' Duluth',' Minneapolis',' Madison',' Tomahawk',' Wausau',' Sturgeon Bay',' Sault Ste. Marie',' Milwaukee',]
d.coopId = ['72638006','72743010','72745000','72658000','72641000','72741043','72645107','72645064','72734000','72640000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence Area'
d.zone = 'WIZ012'
dsm.set('Config.1.Core3.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Niagara'
d.coopId = '72648024'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.aq = 'mi010'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence'
d.coopId = '72743020'
dsm.set('Config.1.Core2.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Health.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Ski.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core5.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Health.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','MSP','IAD',]
d.obsStation = ['T72202000','T72278000','T72658000','T72403000',]
d.locName = ['Miami International','Phoenix / Sky Harbor','Minneapolis - St. Paul','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','BOS','SLC',]
d.obsStation = ['T72259000','T72565000','T72509000','T72572000',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Boston / Logan Int`l','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','ORD','LAX','ATL',]
d.obsStation = ['T72503000','T72530000','T72295000','T72219000',]
d.locName = ['New York / LaGuardia','Chicago O`Hare Int`l','Los Angeles Int`l','Atlanta International',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Airport.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Core5.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence'
d.coopId = '72743020'
dsm.set('Config.1.Core4.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore2.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Airport.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1A.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Vail, CO','Jackson Hole Mountain Resort, WY','Aspen Highlands, CO',]
d.skiId = ['482','191','25',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.3', d, 0, 1)
#
d = twc.Data()
d.locName = ['Big Bear Mtn. Resort, CA','Breckenridge, CO','Park City, UT',]
d.skiId = ['43','77','314',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Travel.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Ski Brule','Whitecap Mountain','Christie Mountain',]
d.skiId = ['370','496','108',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Marquette Mountain','Pine Mountain','Indianhead Mountain',]
d.skiId = ['230','321','187',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72648024'
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Orlando','Washington, DC','San Francisco',]
d.coopId = ['72205000','72405000','72494000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Ski.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'MKE'
d.obsStation = 'T72640000'
d.locName = 'Milwaukee / General Mitchell Int`l Arpt.'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743020','KIMT',]
d.locName = ['Florence','Iron Mountain',]
dsm.set('Config.1.Core3.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Dallas','Boston',]
d.coopId = ['72219000','72259000','72509000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.airportId = 'GRB'
d.obsStation = 'T72645000'
d.locName = 'Green Bay / Austin Straubel Int`l Arpt.'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Travel.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'SAW'
d.obsStation = 'T72743010'
d.locName = 'Sawyer International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Ski.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence Area'
d.zone = 'WIZ012'
dsm.set('Config.1.Core4.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.climId = '204090'
d.latitude = 45.78
d.longitude = -88.08
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence'
d.coopId = '72743020'
dsm.set('Config.1.Core4.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648015','T72648000','T72741047','T72645079',]
d.locName = ['Stephenson','Escanaba','Rhinelander','Menominee',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648015','T72648000','T72741047','T72645079',]
d.locName = ['Stephenson','Escanaba','Rhinelander','Menominee',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743019','T72648033','T72743024','T72645102',]
d.locName = ['Crystal Falls','Goodman','Iron River','Laona',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Health.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72743019','T72648033','T72743024','T72645102',]
d.locName = ['Crystal Falls','Goodman','Iron River','Laona',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Ski.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.bkgImage = 'neighborhood_bg'
d.affiliateName = 'Nsight Digital T.V.'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Core5.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence Area'
d.zone = 'WIZ012'
dsm.set('Config.1.Core2.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Travel.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core5.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Florence'
d.coopId = '72743020'
dsm.set('Config.1.Core2.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core5.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Health.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Niagara'
d.coopId = '72648024'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara Area'
d.zone = 'WIZ013'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Travel.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore2.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SAW','GRB','MKE',]
d.obsStation = ['T72743010','T72645000','T72640000',]
d.locName = ['Sawyer Int`l Arpt.','Green Bay Austin Straubel Int`l Arpt.','Milwaukee General Mitchell Arpt.',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.1', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Niagara'
d.coopId = '72648024'
dsm.set('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72648024','KIMT',]
d.locName = ['Niagara','Iron Mountain',]
d.elementDurationLong = 6
dsm.set('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0', d, 0, 1)
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
# Finished generation on Tue Jan 11 17:16:02 GMT 2022

import os; os.system("cd /twc/data/clock; tar -xvf /twc/data/clock/clocks.tar");ds.commit();wxdata.loadClock();