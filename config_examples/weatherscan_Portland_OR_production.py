# Created on Fri Oct 22 12:35:09 GMT 2021
twc.Log.info('scmt config started')
# EXP: 13771
# VIW: 35233
# CLN: 17935
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
# MAP: 77033
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4438,15176),
             mapcutSize=(1736,861),
             mapFinalSize=(248,123),
             mapMilesSize=(155,92),
             datacutType='radar.us',
             datacutCoordinate=(145,1521),
             datacutSize=(213,106),
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
               ( ( (113,31),),
                 ( (147,59),),
                 ( (170,63),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (113,31),),
                 ( (147,59),),
                 ( (170,63),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (88,20),'McMinnville',),
                 ( (123,48),'Portland',),
                 ( (157,79),'Troutdale',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (88,20),'McMinnville',),
                 ( (123,48),'Portland',),
                 ( (157,79),'Troutdale',),
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
# MAP: 76124
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4443,15085),
             mapcutSize=(1800,1200),
             mapFinalSize=(720,480),
             mapMilesSize=(160,128),
             datacutType='radar.us',
             datacutCoordinate=(146,1510),
             datacutSize=(220,147),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (623,241),'84',),
                 ( (402,311),'5',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (141,234),'101',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (623,241),'84',),
                 ( (402,311),'5',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (141,234),'101',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
               ( ( (434,221),),
               ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (142,308),),
                 ( (595,253),),
                 ( (496,153),),
                 ( (472,207),),
                 ( (361,214),),
                 ( (322,130),),
                 ( (437,165),),
                 ( (423,214),),
                 ( (509,181),),
                 ( (382,276),),
                 ( (173,192),),
                 ( (480,220),),
                 ( (381,117),),
                 ( (421,244),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (142,308),),
                 ( (595,253),),
                 ( (496,153),),
                 ( (472,207),),
                 ( (361,214),),
                 ( (322,130),),
                 ( (437,165),),
                 ( (423,214),),
                 ( (509,181),),
                 ( (382,276),),
                 ( (173,192),),
                 ( (480,220),),
                 ( (381,117),),
                 ( (421,244),),
               ),
             ),
             (
               ('airplane',0,1,0,),
               ( ( (434,221),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (87,329),'Cannon Bch.',),
                 ( (516,281),'Cascade Locks',),
                 ( (510,141),'Estacada',),
                 ( (491,203),'Gresham',),
                 ( (264,217),'Hillsboro',),
                 ( (202,109),'McMinnville',),
                 ( (312,164),'Oregon City',),
                 ( (380,198),'Portland',),
                 ( (529,184),'Sandy',),
                 ( (273,294),'Scappoose',),
                 ( (130,175),'Tillamook',),
                 ( (497,238),'Troutdale',),
                 ( (403,103),'Woodburn',),
                 ( (403,263),'Vancouver',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (87,329),'Cannon Bch.',),
                 ( (516,281),'Cascade Locks',),
                 ( (510,141),'Estacada',),
                 ( (491,203),'Gresham',),
                 ( (264,217),'Hillsboro',),
                 ( (202,109),'McMinnville',),
                 ( (312,164),'Oregon City',),
                 ( (380,198),'Portland',),
                 ( (529,184),'Sandy',),
                 ( (273,294),'Scappoose',),
                 ( (130,175),'Tillamook',),
                 ( (497,238),'Troutdale',),
                 ( (403,103),'Woodburn',),
                 ( (403,263),'Vancouver',),
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
dsm.set('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
# MAP: 62
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1463,1827),
             mapcutSize=(2520,1680),
             mapFinalSize=(720,480),
             mapMilesSize=(2305,1563),
             datacutType='radarSatellite.us',
             datacutCoordinate=(0,597),
             datacutSize=(1154,703),
             dataFinalSize=(641,389),
             dataOffset=(79,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
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
dsm.set('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0', d, 0)
# MAP: 77036
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1996,1960),
             mapcutSize=(1656,1104),
             mapFinalSize=(720,480),
             mapMilesSize=(1551,1045),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(0,718),
             datacutSize=(869,582),
             dataFinalSize=(585,390),
             dataOffset=(135,0),
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
# MAP: 74849
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3252,13068),
             mapcutSize=(8640,5760),
             mapFinalSize=(720,480),
             mapMilesSize=(764,611),
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
               ( ( '72681000',(487,95),),
                 ( '72683000',(324,94),),
                 ( '72688000',(378,161),),
                 ( '72693000',(152,92),),
                 ( '72698000',(193,164),),
                 ( '72773000',(569,244),),
                 ( '72781000',(274,238),),
                 ( '72785000',(390,273),),
                 ( '72793010',(185,288),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72681000',(484,135),),
                 ( '72683000',(321,134),),
                 ( '72688000',(377,207),),
                 ( '72693000',(149,132),),
                 ( '72698000',(190,204),),
                 ( '72773000',(566,284),),
                 ( '72781000',(273,266),),
                 ( '72785000',(387,313),),
                 ( '72793010',(182,328),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (465,169),'Boise',),
                 ( (301,168),'Burns',),
                 ( (346,235),'Pendleton',),
                 ( (126,166),'Salem',),
                 ( (155,238),'Portland',),
                 ( (530,318),'Missoula',),
                 ( (261,312),'Yakima',),
                 ( (351,347),'Spokane',),
                 ( (155,362),'Seattle',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
#
wxdata.setInterestList('lambert.us','1',['travelWeather.us','snowfallQpfForecast.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.1.Local_RadarSatelliteComposite.0','Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core2.1.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.Core3.1.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','snowfallQpfForecast.us','radar.us','travelWeather.us',])
#
wxdata.setInterestList('tideStation','1',['W9435328','W9439023','W9439099','W9439221',])
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','IAD','LAX','LGA','MIA','MSP','ORD','PDX','PHL','PHX','SEA','SFO','SLC','SLE','STL',])
wxdata.setInterestList('coopId','1',['72205000','72219000','72259000','72295023','72405000','72494000','72503023','72509000','72530000','72597000','72681000','72683000','72688000','72693000','72694000','72694027','72694095','72698000','72698006','72698008','72698013','72698023','72698037','72698042','72698063','72698088','72773000','72781000','72785000','72793000','72793010','74501020',])
wxdata.setInterestList('obsStation','1',['B46015','B46089','KMMV','KPDX','T72202000','T72219000','T72259000','T72278000','T72295000','T72403000','T72408000','T72434000','T72494000','T72503000','T72509000','T72530000','T72565000','T72572000','T72597000','T72658000','T72681000','T72688000','T72694000','T72694027','T72694095','T72698000','T72698006','T72698008','T72698013','T72698023','T72698037','T72698042','T72698063','T72698088','T72781000','T72785000','T72793000','T74501020',])
wxdata.setInterestList('climId','1',['355384','356751',])
wxdata.setInterestList('metroId','1',['29',])
wxdata.setInterestList('zone','1',['ORZ006','ORZ007',])
wxdata.setInterestList('aq','1',['or001',])
wxdata.setInterestList('zone.cwf','1',['PZZ250',])
wxdata.setInterestList('skiId','1',['124','1385','1672','191','25','265','266','275','470','482','494','502',])
wxdata.setInterestList('county','1',['ORC067','ORC071','ORC005','ORC009','ORC051',])
#
dsm.set('Config.1.Package.36',('Core2',0), 0)
dsm.set('Config.1.Package.34',('Core3',1), 0)
dsm.set('Config.1.Package.25',('Core4',1), 0)
dsm.set('Config.1.Package.31',('Core4',0), 0)
dsm.set('Config.1.Package.23',('Core3',0), 0)
dsm.set('Config.1.Package.29',('Core5',0), 0)
dsm.set('Config.1.Package.18',('Core5',0), 0)
dsm.set('Config.1.Package.16',('Airport',0), 0)
dsm.set('Config.1.Package.13',('Core3',1), 0)
dsm.set('Config.1.Package.9',('Core2',0), 0)
dsm.set('Config.1.Package.7',('Travel',0), 0)
dsm.set('Config.1.Package.5',('Health',0), 0)
dsm.set('Config.1.Package.0',('Core2',1), 0)
dsm.set('Config.1.Package.38',('Core2',0), 0)
dsm.set('Config.1.Package.35',('Core5',0), 0)
dsm.set('Config.1.Package.26',('Core4',0), 0)
dsm.set('Config.1.Package.32',('Core4',1), 0)
dsm.set('Config.1.Package.22',('Core2',0), 0)
dsm.set('Config.1.Package.28',('Core3',1), 0)
dsm.set('Config.1.Package.20',('Core5',0), 0)
dsm.set('Config.1.Package.15',('Core4',1), 0)
dsm.set('Config.1.Package.12',('Core3',0), 0)
dsm.set('Config.1.Package.10',('Core2',1), 0)
dsm.set('Config.1.Package.6',('Core5',0), 0)
dsm.set('Config.1.Package.4',('Core3',1), 0)
dsm.set('Config.1.Package.2',('Health',0), 0)
dsm.set('Config.1.Package.37',('Core2',0), 0)
dsm.set('Config.1.Package.33',('Core5',0), 0)
dsm.set('Config.1.Package.24',('Core2',1), 0)
dsm.set('Config.1.Package.30',('Core3',1), 0)
dsm.set('Config.1.Package.21',('Core5',0), 0)
dsm.set('Config.1.Package.27',('Core4',0), 0)
dsm.set('Config.1.Package.19',('Core2',0), 0)
dsm.set('Config.1.Package.17',('Core4',1), 0)
dsm.set('Config.1.Package.14',('Core3',0), 0)
dsm.set('Config.1.Package.11',('Airport',0), 0)
dsm.set('Config.1.Package.8',('Health',0), 0)
dsm.set('Config.1.Package.3',('Core2',1), 0)
dsm.set('Config.1.Package.1',('Travel',0), 0)
dsm.set('dmaCode','820', 0)
dsm.set('secondaryObsStation','KPDX', 0)
dsm.set('primaryClimoStation','356751', 0)
dsm.set('stateCode','OR', 0)
dsm.set('primaryCoopId','72698008', 0)
dsm.set('primarylat',45.4984, 0)
dsm.set('primaryCounty','ORC067', 0)
dsm.set('primaryObsStation','T72698008', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-122.957, 0)
dsm.set('primaryForecastName','Portland', 0)
dsm.set('primaryZone','ORZ006', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','027589', 0)
dsm.set('msoName','Northwest Fiber', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','CITIZENS TELECOM SERVICES COMPAN', 0)
dsm.set('affiliateName','09644', 0)
dsm.set('msoCode','03516', 0)
dsm.set('headendName','WXS - PORTLAND - WXS', 0)
dsm.set('zipCode','97124', 0)
dsm.set('Config.1.irdAddress','0001140995705192', 0)
dsm.set('Config.1.starId','TWCS03040056', 0)
dsm.set('Config.1.irdSlave','0', 0)
#
#  Non Image Maps
#
#

#
#
wxdata.setTimeZone('PST8PDT')
#
d = twc.Data()
d.affiliateLogo = 'ziplyLogo'
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
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Local_DaypartForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Golf.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficFlow.0')
scmtRemove('Config.1.Traffic.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.LocalBroadcaster.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core3.1.Local_TextForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_TextForecast.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Core3.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Core3.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficOverview.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Core4.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.SmLocal_TrafficSponsor.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_TextForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Almanac.0')
scmtRemove('Config.1.Traffic.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_TextForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Core2.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.1')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.0')
scmtRemove('Config.1.Golf.0.Local_TeeTimeForecast.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_Tides.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Golf.0.Local_PackageIntro.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core3.1.Local_MenuBoard.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Golf.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_CoastalWatersForecast.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficReport.0')
scmtRemove('Config.1.Core2.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_Tides.1')
scmtRemove('Config.1.Core3.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_Promo.0')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.BoatAndBeach.0.Local_SurfReport.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Movie.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Golf.0.Local_PgaEventForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core3.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Golf.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Core2.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_PackageIntro.0')
scmtRemove('Config.1.Traffic.0.Local_PackageIntro.0')
scmtRemove('Config.1.Golf.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_MenuBoard.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.2')
scmtRemove('Config.1.BoatAndBeach.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
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
scmtRemove('Config.1.Golf.0')
d = twc.Data()
d.bkgImage = 'golf_bg'
d.packageTitle = 'Golf Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GOLF'
dsm.set('Config.1.Golf.0', d, 0, 1)
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
d.packageFlavor = 1
d.shortPackageTitle = 'RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'McMINNVILLE'
dsm.set('Config.1.Core4.1', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'PORTLAND'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'McMINNVILLE'
dsm.set('Config.1.Core3.1', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'PORTLAND'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'McMINNVILLE'
dsm.set('Config.1.Core2.1', d, 0, 1)
scmtRemove('Config.1.BoatAndBeach.0')
d = twc.Data()
d.bkgImage = 'boatbeach_bg'
d.packageTitle = 'Boat & Beach'
d.packageFlavor = 1
d.shortPackageTitle = 'BEACH'
dsm.set('Config.1.BoatAndBeach.0', d, 0, 1)
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
d.shortPackageTitle = 'PORTLAND'
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
d.shortPackageTitle = 'PORTLAND'
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
d.packageFlavor = 1
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'portland_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown     Portland','Portland',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694027','KMMV',]
d.locName = ['McMinnville','McMinnville',]
dsm.set('Config.1.Core2.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown     Portland','Portland',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.coopId = '72694027'
dsm.set('Config.1.Core4.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698023','T72698088','T72698063','T72698037','T72694000','T72698042','T72698013','T72698006',]
d.locName = ['Beaverton','   Longview','   Woodland','   Hillsboro','   Salem','   Scappoose','   Troutdale','   Vancouver',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SFO','PHL','SEA','STL',]
d.obsStation = ['T72494000','T72408000','T72793000','T72434000',]
d.locName = ['San Francisco Int`l','Philadelphia Int`l','Seattle - Tacoma Int`l','Lambert - St. Louis Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','MSP','IAD',]
d.obsStation = ['T72202000','T72278000','T72658000','T72403000',]
d.locName = ['Miami International','Phoenix / Sky Harbor','Minneapolis - St. Paul','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.zone = 'ORZ007'
dsm.set('Config.1.Core2.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','BOS','SLC',]
d.obsStation = ['T72259000','T72565000','T72509000','T72572000',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Boston / Logan Int`l','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','ORD','LAX','ATL',]
d.obsStation = ['T72503000','T72530000','T72295000','T72219000',]
d.locName = ['New York / LaGuardia','Chicago O`Hare Int`l','Los Angeles Int`l','Atlanta International',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694095','T72681000','T72698088','T72597000','T72688000','T72494000','T72793000','T74501020','T72785000','T72781000',]
d.locName = ['Bend','   Boise, ID','   Longview','   Medford','   Pendleton','   San Francisco, CA','   Seattle, WA','   South Lake Tahoe, CA','   Spokane, WA','   Yakima, WA',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72698008'
d.locName = 'Metro Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'portland_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'McMinnville'
d.coopId = '72694027'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.1.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.coopId = '72694027'
dsm.set('Config.1.Core2.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'portland_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.coopId = '72694027'
dsm.set('Config.1.Core4.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694027','KMMV',]
d.locName = ['McMinnville','McMinnville',]
dsm.set('Config.1.Core4.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Beaverton','   Longview','   Woodland','   Hillsboro','   Mcnary Field','   Scappoose','   Troutdale ','   Vancouver',]
d.coopId = ['72698023','72698088','72698063','72698037','72694000','72698042','72698013','72698006',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694000','T72698042','T72698013','T72698006',]
d.locName = ['Salem','Scappoose','Troutdale','Vancouver',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.zone = 'ORZ007'
dsm.set('Config.1.Core4.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698023','T72698088','T72698063','T72698037',]
d.locName = ['Beaverton','Longview','Woodland','Hillsboro',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Bend','   Boise, ID','   Longview ','   Medford','   Pendleton','   San Francisco, CA','  Seattle, WA','  South Lake Tahoe, CA','   Spokane, WA','  Yakima, WA',]
d.coopId = ['72694095','72681000','72698088','72597000','72688000','72494000','72793000','74501020','72785000','72781000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Metro Portland'
d.aq = 'or001'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'portland_bg'
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
d.bkgImage = 'portland_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694000','T72698042','T72698013','T72698006',]
d.locName = ['Salem','Scappoose','Troutdale','Vancouver',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698023','T72698088','T72698063','T72698037',]
d.locName = ['Beaverton','Longview','Woodland','Hillsboro',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72698008','KPDX',]
d.locName = ['Downtown Portland','Portland',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.bkgImage = 'portland_bg'
d.affiliateName = 'Northwest Fiber'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.coopId = '72694027'
dsm.set('Config.1.Core2.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72694027','KMMV',]
d.locName = ['McMinnville','McMinnville',]
dsm.set('Config.1.Core3.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '356751'
d.latitude = 45.6
d.longitude = -122.6
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'McMinnville'
d.zone = 'ORZ007'
dsm.set('Config.1.Core3.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.coopId = '72698008'
d.latitude = 45.53
d.longitude = -122.67
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Portland'
d.zone = 'ORZ006'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'SLE'
d.obsStation = 'T72694000'
d.locName = 'Salem McNary Field Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['PDX','SLE',]
d.obsStation = ['T72698000','T72694000',]
d.locName = ['Portland Int`l Airport','   Salem McNary Field Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'PDX'
d.obsStation = 'T72698000'
d.locName = 'Portland International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.preRoll = 8
d.schedule = ((14,60),(44,60),)
dsm.set('Config.1.Local_Avail_Schedule', d, 0)
#
# End of SCMT deployment
#
ds.commit()
twc.Log.info('scmt config finished')
# Finished generation on Fri Oct 22 12:35:11 GMT 2021

import os; os.system("cd /twc/data/clock; tar -xvf /twc/data/clock/clocks.tar");ds.commit();wxdata.loadClock();