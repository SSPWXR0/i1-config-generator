# Created on Tue Jan 11 17:16:55 GMT 2022
twc.Log.info('scmt config started')
# EXP: 24243
# VIW: 550615
# CLN: 2935
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
# MAP: 121945
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(12790,16756),
             mapcutSize=(4168,2067),
             mapFinalSize=(248,123),
             mapMilesSize=(350,208),
             datacutType='radar.us',
             datacutCoordinate=(1168,1715),
             datacutSize=(510,253),
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
               ( ( (184,83),),
                 ( (101,73),),
                 ( (80,34),),
                 ( (119,58),),
                 ( (177,33),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (184,83),),
                 ( (101,73),),
                 ( (80,34),),
                 ( (119,58),),
                 ( (177,33),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (176,96),'Midale',),
                 ( (57,93),'Rockglen',),
                 ( (67,21),'Glasgow',),
                 ( (133,64),'Scobey',),
                 ( (163,21),'Williston',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (176,96),'Midale',),
                 ( (57,93),'Rockglen',),
                 ( (67,21),'Glasgow',),
                 ( (133,64),'Scobey',),
                 ( (163,21),'Williston',),
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
# MAP: 121944
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(13085,16614),
             mapcutSize=(3574,2383),
             mapFinalSize=(720,480),
             mapMilesSize=(300,240),
             datacutType='radar.us',
             datacutCoordinate=(1204,1698),
             datacutSize=(438,270),
             dataFinalSize=(720,445),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (564,280),),
                 ( (524,355),),
                 ( (291,285),),
                 ( (450,145),),
                 ( (220,152),),
                 ( (268,204),),
                 ( (352,233),),
                 ( (344,101),),
                 ( (501,244),),
                 ( (111,229),),
                 ( (525,134),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (564,280),),
                 ( (524,355),),
                 ( (291,285),),
                 ( (450,145),),
                 ( (220,152),),
                 ( (268,204),),
                 ( (352,233),),
                 ( (344,101),),
                 ( (501,244),),
                 ( (111,229),),
                 ( (525,134),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (560,305),'Torquay',),
                 ( (423,353),'Weyburn',),
                 ( (191,314),'Rockglen',),
                 ( (402,166),'Culbertson',),
                 ( (126,131),'Glasgow',),
                 ( (287,194),'Larslan',),
                 ( (367,252),'Scobey',),
                 ( (329,122),'Vida',),
                 ( (520,235),'Westby',),
                 ( (118,260),'Whitewater',),
                 ( (534,109),'Trenton',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (560,305),'Torquay',),
                 ( (423,353),'Weyburn',),
                 ( (191,314),'Rockglen',),
                 ( (402,166),'Culbertson',),
                 ( (126,131),'Glasgow',),
                 ( (287,194),'Larslan',),
                 ( (367,252),'Scobey',),
                 ( (329,122),'Vida',),
                 ( (520,235),'Westby',),
                 ( (118,260),'Whitewater',),
                 ( (534,109),'Trenton',),
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
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
# MAP: 121972
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(13000,16237),
             mapcutSize=(3574,2383),
             mapFinalSize=(720,480),
             mapMilesSize=(303,242),
             datacutType='radar.us',
             datacutCoordinate=(1194,1651),
             datacutSize=(437,292),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core2.3.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.3.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (351,122),),
                 ( (467,221),),
                 ( (237,228),),
                 ( (204,110),),
                 ( (285,280),),
                 ( (407,152),),
                 ( (369,309),),
                 ( (502,162),),
                 ( (518,320),),
                 ( (128,305),),
                 ( (354,214),),
                 ( (542,210),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (351,122),),
                 ( (467,221),),
                 ( (237,228),),
                 ( (204,110),),
                 ( (285,280),),
                 ( (407,152),),
                 ( (369,309),),
                 ( (502,162),),
                 ( (518,320),),
                 ( (128,305),),
                 ( (354,214),),
                 ( (542,210),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (290,134),'Circle',),
                 ( (477,244),'Culbertson',),
                 ( (142,224),'Glasgow',),
                 ( (134,123),'Jordan',),
                 ( (207,282),'Larslan',),
                 ( (339,168),'Richey',),
                 ( (384,328),'Scobey',),
                 ( (521,155),'Sidney',),
                 ( (537,311),'Westby',),
                 ( (135,336),'Whitewater',),
                 ( (334,239),'Wolf Point',),
                 ( (557,194),'Trenton',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (290,134),'Circle',),
                 ( (477,244),'Culbertson',),
                 ( (142,224),'Glasgow',),
                 ( (134,123),'Jordan',),
                 ( (207,282),'Larslan',),
                 ( (339,168),'Richey',),
                 ( (384,328),'Scobey',),
                 ( (521,155),'Sidney',),
                 ( (537,311),'Westby',),
                 ( (135,336),'Whitewater',),
                 ( (334,239),'Wolf Point',),
                 ( (557,194),'Trenton',),
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
dsm.set('Config.1.Core2.3.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.3.Local_LocalDoppler.0', d, 0)
# MAP: 121947
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(14084,16196),
             mapcutSize=(3529,2353),
             mapFinalSize=(720,480),
             mapMilesSize=(300,240),
             datacutType='radar.us',
             datacutCoordinate=(1326,1646),
             datacutSize=(432,289),
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
               ( ( (368,369),),
                 ( (93,374),),
                 ( (134,132),),
                 ( (221,92),),
                 ( (255,280),),
                 ( (153,321),),
                 ( (145,188),),
                 ( (303,332),),
                 ( (393,128),),
                 ( (446,106),),
                 ( (611,249),),
                 ( (477,208),),
                 ( (328,221),),
                 ( (351,236),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (368,369),),
                 ( (93,374),),
                 ( (134,132),),
                 ( (221,92),),
                 ( (255,280),),
                 ( (153,321),),
                 ( (145,188),),
                 ( (303,332),),
                 ( (393,128),),
                 ( (446,106),),
                 ( (611,249),),
                 ( (477,208),),
                 ( (328,221),),
                 ( (351,236),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (364,394),'Torquay',),
                 ( (117,397),'Rockglen',),
                 ( (91,155),'Circle',),
                 ( (239,103),'Glendive',),
                 ( (189,263),'Medicine Lake',),
                 ( (168,340),'Scobey',),
                 ( (130,209),'Vida',),
                 ( (322,323),'Westby',),
                 ( (335,149),'Grassy Butte',),
                 ( (466,105),'Manning',),
                 ( (552,276),'Minot',),
                 ( (497,191),'New Town',),
                 ( (257,197),'Trenton',),
                 ( (371,239),'Williston',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (364,394),'Torquay',),
                 ( (117,397),'Rockglen',),
                 ( (91,155),'Circle',),
                 ( (239,103),'Glendive',),
                 ( (189,263),'Medicine Lake',),
                 ( (168,340),'Scobey',),
                 ( (130,209),'Vida',),
                 ( (322,323),'Westby',),
                 ( (335,149),'Grassy Butte',),
                 ( (466,105),'Manning',),
                 ( (552,276),'Minot',),
                 ( (497,191),'New Town',),
                 ( (257,197),'Trenton',),
                 ( (371,239),'Williston',),
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
# MAP: 121946
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(12444,16227),
             mapcutSize=(3533,2355),
             mapFinalSize=(720,480),
             mapMilesSize=(300,240),
             datacutType='radar.us',
             datacutCoordinate=(1125,1650),
             datacutSize=(433,289),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core2.2.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (425,368),),
                 ( (282,127),),
                 ( (586,225),),
                 ( (174,260),),
                 ( (353,232),),
                 ( (130,203),),
                 ( (402,285),),
                 ( (510,104),),
                 ( (96,113),),
                 ( (487,314),),
                 ( (479,181),),
                 ( (243,310),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (425,368),),
                 ( (282,127),),
                 ( (586,225),),
                 ( (174,260),),
                 ( (353,232),),
                 ( (130,203),),
                 ( (402,285),),
                 ( (510,104),),
                 ( (96,113),),
                 ( (487,314),),
                 ( (479,181),),
                 ( (243,310),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (325,397),'Rockglen',),
                 ( (252,148),'Brusett',),
                 ( (538,246),'Culbertson',),
                 ( (108,280),'Dodson',),
                 ( (254,224),'Glasgow',),
                 ( (147,182),'Hays',),
                 ( (421,275),'Larslan',),
                 ( (479,125),'Lindsay',),
                 ( (120,108),'Roy',),
                 ( (502,333),'Scobey',),
                 ( (464,202),'Vida',),
                 ( (250,341),'Whitewater',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (325,397),'Rockglen',),
                 ( (252,148),'Brusett',),
                 ( (538,246),'Culbertson',),
                 ( (108,280),'Dodson',),
                 ( (254,224),'Glasgow',),
                 ( (147,182),'Hays',),
                 ( (421,275),'Larslan',),
                 ( (479,125),'Lindsay',),
                 ( (120,108),'Roy',),
                 ( (502,333),'Scobey',),
                 ( (464,202),'Vida',),
                 ( (250,341),'Whitewater',),
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
dsm.set('Config.1.Core2.2.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
# MAP: 121948
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(2303,1596),
             mapcutSize=(2520,1680),
             mapFinalSize=(720,480),
             mapMilesSize=(2388,1632),
             datacutType='radarSatellite.us',
             datacutCoordinate=(290,477),
             datacutSize=(1296,823),
             dataFinalSize=(720,455),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.3.Local_RadarSatelliteComposite.0', d, 0)
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
dsm.set('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.3.Local_RadarSatelliteComposite.0', d, 0)
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
# MAP: 322
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1819,1562),
             mapcutSize=(2372,1581),
             mapFinalSize=(720,480),
             mapMilesSize=(2230,1513),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(0,459),
             datacutSize=(1216,841),
             dataFinalSize=(571,393),
             dataOffset=(149,0),
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
# MAP: 206
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(2728,8907),
             mapcutSize=(14880,9920),
             mapFinalSize=(720,480),
             mapMilesSize=(1392,1113),
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
               ( ( '72488000',(223,102),),
                 ( '72565000',(582,103),),
                 ( '72572000',(411,125),),
                 ( '72666000',(545,231),),
                 ( '72681000',(299,217),),
                 ( '72698000',(132,276),),
                 ( '72772000',(411,280),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72488000',(220,142),),
                 ( '72565000',(579,143),),
                 ( '72572000',(408,165),),
                 ( '72666000',(542,271),),
                 ( '72681000',(296,257),),
                 ( '72698000',(129,316),),
                 ( '72772000',(408,320),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (202,176),'Reno',),
                 ( (551,177),'Denver',),
                 ( (348,199),'Salt Lake City',),
                 ( (505,305),'Sheridan',),
                 ( (277,291),'Boise',),
                 ( (94,350),'Portland',),
                 ( (381,354),'Helena',),
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
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.1.Local_RadarSatelliteComposite.0','Config.1.Core4.2.Local_RadarSatelliteComposite.0','Config.1.Core4.3.Local_RadarSatelliteComposite.0','Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.Core2.3.Local_LocalDoppler.0','Config.1.Core3.3.Local_LocalDoppler.0','Config.1.Core2.1.Local_LocalDoppler.0','Config.1.Core3.1.Local_LocalDoppler.0','Config.1.Core2.2.Local_LocalDoppler.0','Config.1.Core3.2.Local_LocalDoppler.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','snowfallQpfForecast.us','radar.us','travelWeather.us',])
#
wxdata.setInterestList('airportId','1',['ATL','BIL','BIS','BOS','DEN','DFW','GTF','IAD','LAX','LGA','MIA','MSP','ORD','PHX','SLC',])
wxdata.setInterestList('coopId','1',['71135000','71487000','71571000','72205000','72219000','72259000','72295023','72405000','72488000','72494000','72503023','72509000','72530000','72565000','72572000','72666000','72681000','72698000','72765046','72767000','72767019','72767020','72767024','72767027','72767032','72767034','72768000','72768005','72768006','72768010','72768017','72768020','72768022','72768024','72772000','74230000','74230020',])
wxdata.setInterestList('pollenId','1',['MSO',])
wxdata.setInterestList('obsStation','1',['KGGW','KISN','KOLF','T71135000','T71487000','T71571000','T72202000','T72219000','T72259000','T72278000','T72295000','T72403000','T72503000','T72509000','T72530000','T72565000','T72572000','T72658000','T72677000','T72764000','T72765046','T72767000','T72767019','T72767020','T72767024','T72767027','T72767032','T72767034','T72768000','T72768005','T72768006','T72768010','T72768017','T72768020','T72768022','T72768024','T72775000','T74230000','T74230020',])
wxdata.setInterestList('climId','1',['243558','247425','249103','329425',])
wxdata.setInterestList('zone','1',['MTZ017','MTZ018','MTZ020','NDZ009',])
wxdata.setInterestList('aq','1',['mt013',])
wxdata.setInterestList('skiId','1',['160','191','217','25','314','335','43','46','460','48','482','77',])
wxdata.setInterestList('county','1',['MTC019','NDC105','MTC105','MTC071','MTC091','NDC023',])
#
dsm.set('Config.1.Package.36',('Core5',0), 0)
dsm.set('Config.1.Package.34',('Core4',3), 0)
dsm.set('Config.1.Package.25',('Core3',0), 0)
dsm.set('Config.1.Package.31',('Core3',2), 0)
dsm.set('Config.1.Package.23',('Airport',0), 0)
dsm.set('Config.1.Package.29',('Core4',1), 0)
dsm.set('Config.1.Package.18',('Core3',3), 0)
dsm.set('Config.1.Package.16',('Core3',2), 0)
dsm.set('Config.1.Package.13',('Core2',1), 0)
dsm.set('Config.1.Package.9',('Ski',0), 0)
dsm.set('Config.1.Package.7',('Core2',3), 0)
dsm.set('Config.1.Package.5',('Core4',2), 0)
dsm.set('Config.1.Package.0',('Core3',1), 0)
dsm.set('Config.1.Package.38',('Health',0), 0)
dsm.set('Config.1.Package.35',('Ski',0), 0)
dsm.set('Config.1.Package.26',('Core2',0), 0)
dsm.set('Config.1.Package.32',('Core4',2), 0)
dsm.set('Config.1.Package.22',('Core5',0), 0)
dsm.set('Config.1.Package.28',('Core3',1), 0)
dsm.set('Config.1.Package.20',('Core3',3), 0)
dsm.set('Config.1.Package.15',('Core2',2), 0)
dsm.set('Config.1.Package.12',('Core2',1), 0)
dsm.set('Config.1.Package.10',('Core4',0), 0)
dsm.set('Config.1.Package.6',('Core2',3), 0)
dsm.set('Config.1.Package.4',('Core3',2), 0)
dsm.set('Config.1.Package.2',('Core3',1), 0)
dsm.set('Config.1.Package.37',('Travel',0), 0)
dsm.set('Config.1.Package.33',('Core3',3), 0)
dsm.set('Config.1.Package.24',('Core5',0), 0)
dsm.set('Config.1.Package.30',('Core3',2), 0)
dsm.set('Config.1.Package.21',('Health',0), 0)
dsm.set('Config.1.Package.27',('Core2',1), 0)
dsm.set('Config.1.Package.19',('Core4',3), 0)
dsm.set('Config.1.Package.17',('Core2',2), 0)
dsm.set('Config.1.Package.14',('Core3',1), 0)
dsm.set('Config.1.Package.11',('Ski',0), 0)
dsm.set('Config.1.Package.8',('Core2',3), 0)
dsm.set('Config.1.Package.3',('Core3',2), 0)
dsm.set('Config.1.Package.1',('Core2',1), 0)
dsm.set('dmaCode','687', 0)
dsm.set('secondaryObsStation','KOLF', 0)
dsm.set('primaryClimoStation','247425', 0)
dsm.set('stateCode','MT', 0)
dsm.set('primaryCoopId','72768022', 0)
dsm.set('primarylat',48.790955, 0)
dsm.set('severeClockActive','1', 0)
dsm.set('primaryCounty','MTC019', 0)
dsm.set('primaryObsStation','T72768022', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-105.419925, 0)
dsm.set('primaryForecastName','Wolf Point', 0)
dsm.set('primaryZone','MTZ018', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','038527', 0)
dsm.set('msoName','Nemont Communications, Inc.', 0)
dsm.set('countryCode','US', 0)
dsm.set('affiliateName','23708', 0)
dsm.set('msoCode','03060', 0)
dsm.set('headendName','WXS - SCOBEY  - WXS', 0)
dsm.set('zipCode','59263', 0)
dsm.set('Config.1.irdAddress','0001140994513212', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCS05040002', 0)
dsm.set('Config.1.bcGateWay','10.10.10.1', 0)
dsm.set('Config.1.bcIpAddress','10.10.10.10', 0)
#
#  Non Image Maps
#
#

#
#
wxdata.setTimeZone('MST7MDT')
#
d = twc.Data()
d.affiliateLogo = 'nemontLogo'
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
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core3.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core4.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core2.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_NetworkIntro.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Movie.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_CurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.3.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.3.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.2.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.2.Local_MenuBoard.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.Core2.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core4.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_Almanac.0')
scmtRemove('Config.1.Core2.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Core3.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.3.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.2.Local_DaypartForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_TextForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.3.Local_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core2.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.LocalBroadcaster.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Local_MenuBoard.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Core4.2.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.Core2.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.3.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.3.Local_TextForecast.0')
scmtRemove('Config.1.Core4.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.2.Local_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core2.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.Core3.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Local_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.Core4.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.1.Local_TextForecast.0')
scmtRemove('Config.1.Core2.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Core2.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.Core4.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.2.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.2.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Core2.3.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.LocalBroadcaster.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core4.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.3.Local_MenuBoard.0')
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
scmtRemove('Config.1.Core4.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WOLF POINT'
dsm.set('Config.1.Core4.3', d, 0, 1)
scmtRemove('Config.1.Core4.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GLASGOW'
dsm.set('Config.1.Core4.2', d, 0, 1)
scmtRemove('Config.1.Core3.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WOLF POINT'
dsm.set('Config.1.Core3.3', d, 0, 1)
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
d.shortPackageTitle = 'RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WILLISTON'
dsm.set('Config.1.Core4.1', d, 0, 1)
scmtRemove('Config.1.Core3.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GLASGOW'
dsm.set('Config.1.Core3.2', d, 0, 1)
scmtRemove('Config.1.Core2.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WOLF POINT'
dsm.set('Config.1.Core2.3', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SCOBEY'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WILLISTON'
dsm.set('Config.1.Core3.1', d, 0, 1)
scmtRemove('Config.1.Core2.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'GLASGOW'
dsm.set('Config.1.Core2.2', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SCOBEY'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'WILLISTON'
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
d.shortPackageTitle = 'SCOBEY'
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
d.shortPackageTitle = 'SCOBEY'
dsm.set('Config.1.Core1.0', d, 0, 1)
scmtRemove('Config.1.Health.0')
d = twc.Data()
d.bkgImage = 'health_bg'
d.packageTitle = 'Weather & Your Health'
d.packageFlavor = 2
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Scobey'
d.coopId = '72768022'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core2.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
dsm.set('Config.1.Core2.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core2.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Travel.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core2.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Airport.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core4.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point Area'
d.zone = 'MTZ020'
dsm.set('Config.1.Core3.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Williston'
d.coopId = '72767000'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.1.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'ski_intro_bg'
dsm.set('Config.1.Ski.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T71487000','T71571000','T72768005','T72767020','T72768006','T72767027','T72768024','T72767032','T71135000','T72768010',]
d.locName = ['Assiniboia',' Coronach',' Lustre',' Medicine Lake',' Opheim',' Plentywood','Poplar',' Raymond Border Station',' Rockglen',' Wolf Point',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core3.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core2.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Ski.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Airport.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core1.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
dsm.set('Config.1.Core2.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1B.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Assiniboia',' Coronach',' Lustre',' Medicine Lake',' Opheim',' Plentywood',' Poplar',' Raymond Border Station',' Rockglen',' Wolf Point',]
d.coopId = ['71487000','71571000','72768005','72767020','72768006','72767027','72768024','72767032','71135000','72768010',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Health.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
dsm.set('Config.1.Core4.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core4.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
dsm.set('Config.1.Core3.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core4.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core3.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow Area'
d.zone = 'MTZ017'
dsm.set('Config.1.Core3.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core2.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core3.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Airport.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767034','T72767024','T72765046','T72768000','T74230020','T72768020','T72768017','T74230000','T72767019','T72767000',]
d.locName = ['Beach',' Crosby',' Dickinson',' Glasgow',' Glendive',' Jordan',' Malta',' Miles City',' Sidney',' Williston',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Ski.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core3.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.coopId = '72768010'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
dsm.set('Config.1.Core4.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core3.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Beach',' Crosby',' Dickinson',' Glasgow',' Glendive',' Jordan',' Malta',' Miles City',' Sidney',' Williston',]
d.coopId = ['72767034','72767024','72765046','72768000','74230020','72768020','72768017','74230000','72767019','72767000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core2.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston Area'
d.zone = 'NDZ009'
dsm.set('Config.1.Core3.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Glasgow'
d.coopId = '72768000'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.2.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core4.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core2.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Scobey'
d.coopId = '72768022'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core1.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core4.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core4.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.aq = 'mt013'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core2.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.coopId = '72768010'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Ski.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Health.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core5.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.pollenId = 'MSO'
dsm.set('Config.1.Health.0.Local_AllergyReport.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core2.2.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Wolf Point'
d.coopId = '72768010'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.3.Local_TextForecast.0', d, 0, 1)
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
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Health.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core3.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MIA','PHX','MSP','IAD',]
d.obsStation = ['T72202000','T72278000','T72658000','T72403000',]
d.locName = ['Miami International','Phoenix / Sky Harbor','Minneapolis - St. Paul','Washington Dulles Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core2.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['DFW','DEN','BOS','SLC',]
d.obsStation = ['T72259000','T72565000','T72509000','T72572000',]
d.locName = ['Dallas / Ft. Worth Int`l','Denver International','Boston / Logan Int`l','Salt Lake City Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point Area'
d.zone = 'MTZ020'
dsm.set('Config.1.Core4.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','ORD','LAX','ATL',]
d.obsStation = ['T72503000','T72530000','T72295000','T72219000',]
d.locName = ['New York / LaGuardia','Chicago O`Hare Int`l','Los Angeles Int`l','Atlanta International',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core2.3.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core4.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core5.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Airport.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core2.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core4.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore2.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core4.3.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
dsm.set('Config.1.Core2.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
dsm.set('Config.1.Core3.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1A.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core1.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Airport.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core4.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core3.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Vail, CO','Jackson Hole Mountain Resort, WY','Aspen Highlands, CO',]
d.skiId = ['482','191','25',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.3', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core4.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow Area'
d.zone = 'MTZ017'
dsm.set('Config.1.Core4.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core4.2.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core3.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core2.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Big Bear Mtn. Resort, CA','Breckenridge, CO','Park City, UT',]
d.skiId = ['43','77','314',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core1.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point Area'
d.zone = 'MTZ020'
dsm.set('Config.1.Core2.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Travel.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Teton Pass Ski Area','Big Sky Resort','Lost Trail/ Powder Mtn',]
d.skiId = ['460','48','217',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Great Divide','Red Lodge Mountain','Whitefish Mountain Resort',]
d.skiId = ['160','335','46',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core2.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core2.3.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core3.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72768022'
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Orlando','Washington, DC','San Francisco',]
d.coopId = ['72205000','72405000','72494000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Ski.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core4.2.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Dallas','Boston',]
d.coopId = ['72219000','72259000','72509000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core4.3.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768000','KGGW',]
d.locName = ['Glasgow','Glasgow',]
dsm.set('Config.1.Core4.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'BIS'
d.obsStation = 'T72764000'
d.locName = 'Bismarck Municipal Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
dsm.set('Config.1.Core3.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['New York City','Chicago','Los Angeles',]
d.coopId = ['72503023','72530000','72295023',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Travel.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'GTF'
d.obsStation = 'T72775000'
d.locName = 'Great Falls International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core4.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core3.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow Area'
d.zone = 'MTZ017'
dsm.set('Config.1.Core2.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Ski.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'BIL'
d.obsStation = 'T72677000'
d.locName = 'Billings Logan International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston Area'
d.zone = 'NDZ009'
dsm.set('Config.1.Core4.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.climId = '247425'
d.latitude = 48.8333
d.longitude = -105.4833
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core4.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768024','T72767032','T71135000','T72768010',]
d.locName = ['Poplar','Raymond Border Station','Rockglen','Wolf Point',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768010','KOLF',]
d.locName = ['Wolf Point','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core2.2.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768024','T72767032','T71135000','T72768010',]
d.locName = ['Poplar','Raymond Border Station','Rockglen','Wolf Point',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Ski.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768005','T72767020','T72768006','T72767027',]
d.locName = ['Lustre','Medicine Lake','Opheim','Plentywood',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Health.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core4.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768005','T72767020','T72768006','T72767027',]
d.locName = ['Lustre','Medicine Lake','Opheim','Plentywood',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Core5.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.bkgImage = 'mountain_bg'
d.affiliateName = 'Nemont Communications'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston Area'
d.zone = 'NDZ009'
dsm.set('Config.1.Core2.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Travel.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core5.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Glasgow'
d.coopId = '72768000'
dsm.set('Config.1.Core2.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core2.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Health.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core5.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'mountain_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core3.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationLong = 6
dsm.set('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core4.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Scobey'
d.coopId = '72768022'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core1.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey Area'
d.zone = 'MTZ018'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core4.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Wolf Point'
d.coopId = '72768010'
dsm.set('Config.1.Core2.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Travel.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Williston'
d.coopId = '72767000'
dsm.set('Config.1.Core3.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore2.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72767000','KISN',]
d.locName = ['Williston','Williston',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['BIL','GTF','BIS',]
d.obsStation = ['T72677000','T72775000','T72764000',]
d.locName = ['Billings Logan Intl. Arpt.','Great Falls Intl. Arpt.','Bismarck Municipal Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Scobey'
d.coopId = '72768022'
dsm.set('Config.1.Core3.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72768022','KOLF',]
d.locName = ['Scobey','Wolf Point',]
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
# Finished generation on Tue Jan 11 17:16:56 GMT 2022

import os; os.system("cd /twc/data/clock; tar -xvf /twc/data/clock/clocks.tar");ds.commit();wxdata.loadClock();