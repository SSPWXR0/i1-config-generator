# Created on Mon Apr 10 17:12:45 EDT 2006
twc.Log.info('scmt config started')
# EXP: 86
# VIW: 7392
# CLN: 2365
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
#
# MAP: 72052
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(26190,5277),
             mapcutSize=(2704,1341),
             mapFinalSize=(248,123),
             mapMilesSize=(302,180),
             datacutType='radar.us',
             datacutCoordinate=(2809,309),
             datacutSize=(331,164),
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
               ( ( (130,70),),
                 ( (190,36),),
                 ( (153,57),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (130,70),),
                 ( (190,36),),
                 ( (153,57),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (94,87),'Leesburg',),
                 ( (162,27),'Melbourne',),
                 ( (167,62),'Orlando',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (94,87),'Leesburg',),
                 ( (162,27),'Melbourne',),
                 ( (167,62),'Orlando',),
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
# MAP: 103
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(26421,5024),
             mapcutSize=(2551,1701),
             mapFinalSize=(720,480),
             mapMilesSize=(285,228),
             datacutType='radar.us',
             datacutCoordinate=(2837,278),
             datacutSize=(313,208),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (532,130),'95',),
                 ( (278,336),'75',),
                 ( (329,188),'4',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (532,130),'95',),
                 ( (278,336),'75',),
                 ( (329,188),'4',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (163,346),),
                 ( (468,350),),
                 ( (340,296),),
                 ( (532,193),),
                 ( (417,259),),
                 ( (225,145),),
                 ( (411,104),),
                 ( (237,248),),
                 ( (252,173),),
                 ( (506,253),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (163,346),),
                 ( (468,350),),
                 ( (340,296),),
                 ( (532,193),),
                 ( (417,259),),
                 ( (225,145),),
                 ( (411,104),),
                 ( (237,248),),
                 ( (252,173),),
                 ( (506,253),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (119,329),'Cedar Key',),
                 ( (399,333),'Daytona Beach',),
                 ( (301,279),'Leesburg',),
                 ( (484,176),'Melbourne',),
                 ( (383,242),'Orlando',),
                 ( (160,128),'St. Petersburg',),
                 ( (431,107),'Sebring',),
                 ( (126,251),'Spring Hill',),
                 ( (226,194),'Tampa',),
                 ( (526,256),'Titusville',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (119,329),'Cedar Key',),
                 ( (399,333),'Daytona Beach',),
                 ( (301,279),'Leesburg',),
                 ( (484,176),'Melbourne',),
                 ( (383,242),'Orlando',),
                 ( (160,128),'St. Petersburg',),
                 ( (431,107),'Sebring',),
                 ( (126,251),'Spring Hill',),
                 ( (226,194),'Tampa',),
                 ( (526,256),'Titusville',),
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
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
# MAP: 72522
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(22220,2613),
             mapcutSize=(8592,5728),
             mapFinalSize=(720,480),
             mapMilesSize=(969,775),
             datacutType='radar.us',
             datacutCoordinate=(2323,0),
             datacutSize=(1052,684),
             dataFinalSize=(720,468),
             dataOffset=(0,12),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Core5.5.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (355,346),'10',),
                 ( (508,212),'95',),
                 ( (423,300),'75',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (355,346),'10',),
                 ( (508,212),'95',),
                 ( (423,300),'75',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (303,323),),
                 ( (454,350),),
                 ( (451,103),),
                 ( (523,153),),
                 ( (450,169),),
                 ( (420,246),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (303,323),),
                 ( (454,350),),
                 ( (451,103),),
                 ( (523,153),),
                 ( (450,169),),
                 ( (420,246),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (245,306),'Apalachicola',),
                 ( (471,353),'Jacksonville',),
                 ( (411,124),'Key West',),
                 ( (541,156),'Miami',),
                 ( (379,172),'Naples',),
                 ( (347,251),'Tampa',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (245,306),'Apalachicola',),
                 ( (471,353),'Jacksonville',),
                 ( (411,124),'Key West',),
                 ( (541,156),'Miami',),
                 ( (379,172),'Naples',),
                 ( (347,251),'Tampa',),
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
dsm.set('Config.1.Core5.5.Local_LocalDoppler.0', d, 0)
# MAP: 72532
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21762,1800),
             mapcutSize=(10288,6859),
             mapFinalSize=(720,480),
             mapMilesSize=(1166,931),
             datacutType='radar.us',
             datacutCoordinate=(2267,0),
             datacutSize=(1260,723),
             dataFinalSize=(720,413),
             dataOffset=(0,67),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Core5.4.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (329,346),'10',),
                 ( (456,234),'95',),
                 ( (385,307),'75',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (329,346),'10',),
                 ( (456,234),'95',),
                 ( (385,307),'75',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (284,325),),
                 ( (410,348),),
                 ( (407,141),),
                 ( (467,184),),
                 ( (406,196),),
                 ( (381,261),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (284,325),),
                 ( (410,348),),
                 ( (407,141),),
                 ( (467,184),),
                 ( (406,196),),
                 ( (381,261),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (226,308),'Apalachicola',),
                 ( (427,351),'Jacksonville',),
                 ( (367,162),'Key West',),
                 ( (485,187),'Miami',),
                 ( (335,199),'Naples',),
                 ( (308,266),'Tampa',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (226,308),'Apalachicola',),
                 ( (427,351),'Jacksonville',),
                 ( (367,162),'Key West',),
                 ( (485,187),'Miami',),
                 ( (335,199),'Naples',),
                 ( (308,266),'Tampa',),
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
dsm.set('Config.1.Core5.4.Local_LocalDoppler.0', d, 0)
# MAP: 74
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3617,704),
             mapcutSize=(1816,1211),
             mapFinalSize=(720,480),
             mapMilesSize=(1729,1166),
             datacutType='radarSatellite.us',
             datacutCoordinate=(966,17),
             datacutSize=(933,625),
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
# MAP: 225
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19916,3490),
             mapcutSize=(11168,7445),
             mapFinalSize=(720,480),
             mapMilesSize=(1219,974),
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
               ( ( '72205000',(514,103),),
                 ( '72207000',(524,227),),
                 ( '72214000',(393,169),),
                 ( '72219000',(399,281),),
                 ( '72231000',(200,150),),
                 ( '72235000',(207,252),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72205000',(511,143),),
                 ( '72207000',(521,267),),
                 ( '72214000',(390,209),),
                 ( '72219000',(396,321),),
                 ( '72231000',(197,190),),
                 ( '72235000',(204,292),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (479,177),'Orlando',),
                 ( (479,301),'Savannah',),
                 ( (341,243),'Tallahassee',),
                 ( (367,355),'Atlanta',),
                 ( (142,224),'New Orleans',),
                 ( (174,326),'Jackson',),
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
wxdata.setInterestList('lambert.us','1',['travelWeather.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.Core5.5.Local_LocalDoppler.0','Config.1.Core5.4.Local_LocalDoppler.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us','travelWeather.us',])
#
wxdata.setInterestList('airportId','1',['ATL','BOS','DAB','DEN','DFW','GNV','IAD','LAX','LGA','MCO','MIA','MSP','ORD','PHL','PHX','SEA','SFO','SLC','STL','TPA',])
wxdata.setInterestList('coopId','1',['72203000','72204000','72205000','72205027','72205049','72205057','72205069','72205076','72206000','72207000','72211000','72211034','72212027','72214000','72219000','72231000','72235000','72259000','72295023','72405000','72494000','72503023','72509000','72530000','74794004','74796048',])
wxdata.setInterestList('obsStation','1',['KLEE','T72202000','T72203000','T72204000','T72205000','T72205004','T72205027','T72205049','T72205057','T72205069','T72205076','T72206000','T72211000','T72211034','T72212027','T72212040','T72214000','T72219000','T72259000','T72278000','T72295000','T72403000','T72408000','T72434000','T72494000','T72503000','T72509000','T72530000','T72565000','T72572000','T72658000','T72793000','T74794004','T74796045',])
wxdata.setInterestList('metroId','1',['23',])
wxdata.setInterestList('climId','1',['086628',])
wxdata.setInterestList('zone','1',['FLZ044',])
wxdata.setInterestList('county','1',['FLC069','FLC083','FLC119',])
#
dsm.set('Config.1.Package.19',('Core2',0), 0)
dsm.set('Config.1.Package.5',('Core4',0), 0)
dsm.set('Config.1.Package.1',('Core4',0), 0)
dsm.set('Config.1.Package.20',('Core2',0), 0)
dsm.set('Config.1.Package.17',('Travel',0), 0)
dsm.set('Config.1.Package.15',('Airport',0), 0)
dsm.set('Config.1.Package.13',('Travel',0), 0)
dsm.set('Config.1.Package.11',('Airport',0), 0)
dsm.set('Config.1.Package.9',('Travel',0), 0)
dsm.set('Config.1.Package.7',('Airport',0), 0)
dsm.set('Config.1.Package.4',('Travel',0), 0)
dsm.set('Config.1.Package.2',('Airport',0), 0)
dsm.set('Config.1.Package.18',('Core2',0), 0)
dsm.set('Config.1.Package.16',('Airport',0), 0)
dsm.set('Config.1.Package.14',('Core2',0), 0)
dsm.set('Config.1.Package.12',('Travel',0), 0)
dsm.set('Config.1.Package.10',('Core4',0), 0)
dsm.set('Config.1.Package.8',('Airport',0), 0)
dsm.set('Config.1.Package.6',('Core2',0), 0)
dsm.set('Config.1.Package.3',('Travel',0), 0)
dsm.set('Config.1.Package.0',('Core4',0), 0)
dsm.set('secondaryObsStation','KLEE', 0)
dsm.set('primaryClimoStation','086628', 0)
dsm.set('expRev','860965', 0)
dsm.set('primaryCoopId','72205057', 0)
dsm.set('primaryCounty','FLC069', 0)
dsm.set('primaryObsStation','T72205057', 0)
dsm.set('hasTraffic',1, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryForecastName','Leesburg', 0)
dsm.set('primaryZone','FLZ044', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','020737', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','00939', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','WXS - LAKE COUNTY/LEESBURG - WXS', 0)
dsm.set('zipCode','34748    ', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCS05040001', 0)
dsm.set('Config.1.bcGateWay','10.15.19.50', 0)
dsm.set('Config.1.bcIpAddress','10.15.19.253', 0)
#
wxdata.setTimeZone('EST5EDT')
#
d = twc.Data()
d.affiliateLogo = 'comcastLogo'
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
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core5.5.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficOverview.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficFlow.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficReport.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Traffic.0.SmLocal_TrafficSponsor.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core5.4.Local_MenuBoard.0')
#
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
scmtRemove('Config.1.Core5.5')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Hurricane Wilma'
d.packageFlavor = 1
d.shortPackageTitle = 'HURRICANE WILMA'
dsm.set('Config.1.Core5.5', d, 0, 1)
scmtRemove('Config.1.Core5.4')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Hurricane Wilma'
d.packageFlavor = 1
d.shortPackageTitle = 'HURRICANE WILMA'
dsm.set('Config.1.Core5.4', d, 0, 1)
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
d.shortPackageTitle = 'LEESBURG RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'LEESBURG'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'LEESBURG'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'LEESBURG'
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
d.shortPackageTitle = 'LEESBURG'
dsm.set('Config.1.Core1.0', d, 0, 1)
scmtRemove('Config.1.Traffic.0')
d = twc.Data()
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
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Orlando Area'
d.trafficReverseActive = [1,1,1,1,1,1,]
d.periodBStartTime = '12:00'
d.activeVocalCue = 0
d.periodAStartTime = '00:00'
d.trafficFlowRoute = ['92736-23','92740-23','92709-23','92688-23','92699-23','92715-23',]
d.trafficReverseRoute = ['92735-23','92739-23','92710-23','92687-23','92700-23','92716-23',]
d.routes=[[
             (('23.92736','SB, US-27 to SR-436','usHighwaySignLarge','441',(20,20,20,255),0),('23.92735','NB, SR-436 to US-27','usHighwaySignLarge','441',(20,20,20,255),0,)),
             (('23.92740','SB, Beachline Exwy to US-192','usHighwaySignLarge','17/92',(20,20,20,255),0),('23.92739','NB, US-192 to Beachline Exwy','usHighwaySignLarge','17/92',(20,20,20,255),0,)),
             (('23.92709','SB, Orange Blossom Trl N to Florida\'s Tpk','stateHighwaySignLarge','429',(20,20,20,255),0),('23.92710','NB, Florida\'s Tpk to Orange Blossom Trl N','stateHighwaySignLarge','429',(20,20,20,255),0,)),
],[
             (('23.92688','WB, US-17/92 to East-West Exwy','interstateHighwaySignLarge','4',(212,212,212,255),1),('23.92687','EB, East-West Exwy to US-17/92','interstateHighwaySignLarge','4',(212,212,212,255),1,)),
             (('23.92699','SB, I-4 (Seminole Co) to SR-434','stateHighwaySignLarge','417',(20,20,20,255),0),('23.92700','NB, SR-434 to I-4 (Seminole Co)','stateHighwaySignLarge','417',(20,20,20,255),0,)),
             (('23.92715','EB, Florida\'s Tpk to I-4','stateHighwaySignLarge','50',(20,20,20,255),0),('23.92716','WB, I-4 to Florida\'s Tpk','stateHighwaySignLarge','50',(20,20,20,255),0,)),
],
]
d.routeDisplayTime=[
             ((0,0),(11,59)),
             ((12,0),(23,59)),
]
dsm.set('Config.1.Traffic.0.Local_TrafficFlow.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205069','T72205000','T72212027','T72211034','T72205076','T72205027','T72205049','T72211000',]
d.locName = ['The Villages','Orlando','Gainesville','Brooksville','Daytona Beach','Sanford','Winter Haven','Tampa',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SFO','PHL','SEA','STL',]
d.obsStation = ['T72494000','T72408000','T72793000','T72434000',]
d.locName = ['San Francisco Int`l','Philadelphia Int`l','Seattle - Tacoma Int`l','Lambert - St. Louis Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.locName = 'Orlando Area'
d.maxPages = 3
d.activeVocalCue = 0
d.metroId=['23',]
d.latLongBoxes=[
             ((-81.9898339133759,28.236395203061004),(-81.56625092173714,28.9905795540276)),
             ((-81.66439820028758,28.52050574623335),(-81.21498697745132,28.97508261530911)),
             ((-81.72122030892206,28.200235679384523),(-81.13233663761936,28.67030948717877)),
]
d.severityList=[
             ('Incident',3,),
             ('Construction',3,),
             ('Unspecified',1,),
]
dsm.set('Config.1.Traffic.0.Local_TrafficReport.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','MSP','IAD',]
d.obsStation = ['T72202000','T72278000','T72658000','T72403000',]
d.locName = ['Miami International','Phoenix / Sky Harbor','Minneapolis - St. Paul','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','BOS','SLC',]
d.obsStation = ['T72259000','T72565000','T72509000','T72572000',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Boston / Logan Int`l','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Leesburg'
d.coopId = '72205057'
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
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.mapName = ['23.1',]
d.locName = ['Orlando Area',]
d.activeVocalCue = 1
dsm.set('Config.1.Traffic.0.Local_TrafficOverview.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72206000','T74794004','T72204000','T74796045','T72203000','T72214000',]
d.locName = ['Jacksonville','Cape Canaveral','Melbourne','Fort Myers','West Palm Beach','Tallahassee',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Comcast'
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Leesburg'
d.coopId = '72205057'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Leesburg'
d.coopId = '72205057'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['The Villages','Orlando','Gainesville','Brooksville','Daytona Beach','Sanford','Winter Haven','Tampa',]
d.coopId = ['72205069','72205000','72212027','72211034','72205076','72205027','72205049','72211000',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205000','T72205004','T72205027','T72205049',]
d.locName = ['Orlando Arpt.','Orlando Ex. Arpt.','Sanford','Winter Haven',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205076','T72205057','T72204000','T72212040',]
d.locName = ['Daytona Beach','Leesburg','Melbourne','Ocala',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Jacksonville','Cape Canaveral','Melbourne','Fort Myers','West Palm Beach','Tallahassee',]
d.coopId = ['72206000','74794004','72204000','74796048','72203000','72214000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
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
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205000','T72205004','T72205027','T72205049',]
d.locName = ['Orlando Arpt.','Orlando Ex. Arpt.','Sanford','Winter Haven',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Comcast'
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205076','T72205057','T72204000','T72212040',]
d.locName = ['Daytona Beach','Leesburg','Melbourne','Ocala',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72205057','KLEE',]
d.locName = ['Leesburg','Leesburg',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.bkgImage = 'orlando_bg'
d.affiliateName = 'Comcast Digital Cable '
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '086628'
d.latitude = 28.43
d.longitude = -81.33
d.locName = 'Orlando'
d.coopId = '72205057'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core5.5.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = '/ Comcast'
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg'
d.coopId = '72205057'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Leesburg Area'
d.zone = 'FLZ044'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'orlando_bg'
dsm.set('Config.1.Core5.4.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'TPA'
d.obsStation = 'T72211000'
d.locName = 'Tampa International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MCO','DAB','GNV','TPA',]
d.obsStation = ['T72205000','T72205076','T72212027','T72211000',]
d.locName = ['Orlando International Airport','Daytona Beach Int`l Airport','Gainesville Regional Airport','Tampa International Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'traffic_intro_bg'
dsm.set('Config.1.Traffic.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.maxCosponsors = 4
dsm.set('Config.1.Traffic.0.SmLocal_TrafficSponsor.0', d, 0, 1)
dsm.set('Config.1.Traffic.0.Local_TrafficSponsor.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'MCO'
d.obsStation = 'T72205000'
d.locName = 'Orlando International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.preRoll = 8
d.schedule = ((14,60),(29,60),(44,60),(58,120),)
dsm.set('Config.1.Local-Avail-Schedule', d, 0)
#
# End of SCMT deployment
#
ds.commit()
twc.Log.info('scmt config finished')
# Finished generation on Mon Apr 10 17:13:21 EDT 2006
