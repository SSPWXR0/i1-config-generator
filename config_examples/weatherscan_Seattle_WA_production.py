# Created on Tue Jan 11 16:16:23 GMT 2022
twc.Log.info('scmt config started')
# EXP: 13910
# VIW: 35396
# CLN: 15342
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
# MAP: 72125
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(2870,16052),
             mapcutSize=(4448,2206),
             mapFinalSize=(248,123),
             mapMilesSize=(380,226),
             datacutType='radar.us',
             datacutCoordinate=(0,1629),
             datacutSize=(498,270),
             dataFinalSize=(227,123),
             dataOffset=(21,0),
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
               ( ( (147,93),),
                 ( (136,27),),
                 ( (154,47),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (147,93),),
                 ( (136,27),),
                 ( (154,47),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (159,93),'Bellingham',),
                 ( (149,22),'Olympia',),
                 ( (167,49),'Seattle',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (159,93),'Bellingham',),
                 ( (149,22),'Olympia',),
                 ( (167,49),'Seattle',),
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
# MAP: 77161
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4665,16572),
             mapcutSize=(2160,1440),
             mapFinalSize=(720,480),
             mapMilesSize=(184,147),
             datacutType='radar.us',
             datacutCoordinate=(173,1692),
             datacutSize=(264,177),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core3.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.4.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (275,95),'16',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (445,183),'2',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (445,183),'2',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (459,93),'90',),
                 ( (351,262),'5',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (172,237),'101',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (459,93),'90',),
                 ( (351,262),'5',),
               ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (275,95),'16',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (172,237),'101',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
               ( ( (336,92),),
               ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (367,135),),
                 ( (358,167),),
                 ( (321,331),),
                 ( (329,185),),
                 ( (356,219),),
                 ( (357,113),),
                 ( (469,336),),
                 ( (335,134),),
                 ( (513,160),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (367,135),),
                 ( (358,167),),
                 ( (321,331),),
                 ( (329,185),),
                 ( (356,219),),
                 ( (357,113),),
                 ( (469,336),),
                 ( (335,134),),
                 ( (513,160),),
               ),
             ),
             (
               ('airplane',0,1,0,),
               ( ( (336,92),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (387,138),'Bellevue',),
                 ( (379,166),'Bothell',),
                 ( (274,314),'Burlington',),
                 ( (231,188),'Edmonds',),
                 ( (376,222),'Everett',),
                 ( (377,116),'Renton',),
                 ( (431,319),'Rockport',),
                 ( (259,138),'Seattle',),
                 ( (533,163),'Skykomish',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (387,138),'Bellevue',),
                 ( (379,166),'Bothell',),
                 ( (274,314),'Burlington',),
                 ( (231,188),'Edmonds',),
                 ( (376,222),'Everett',),
                 ( (377,116),'Renton',),
                 ( (431,319),'Rockport',),
                 ( (259,138),'Seattle',),
                 ( (533,163),'Skykomish',),
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
dsm.set('Config.1.Core2.4.Local_LocalDoppler.0', d, 0)
# MAP: 77160
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3548,15945),
             mapcutSize=(3960,2640),
             mapFinalSize=(720,480),
             mapMilesSize=(337,270),
             datacutType='radar.us',
             datacutCoordinate=(36,1616),
             datacutSize=(485,323),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core5.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.3.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.4.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (490,190),'2',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (490,190),'2',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (381,250),'5',),
                 ( (507,122),'90',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (229,238),'101',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (381,250),'5',),
                 ( (507,122),'90',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (229,238),'101',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (277,294),),
                 ( (238,112),),
                 ( (364,332),),
                 ( (342,172),),
                 ( (561,115),),
                 ( (394,227),),
                 ( (386,285),),
                 ( (332,117),),
                 ( (261,205),),
                 ( (387,187),),
                 ( (368,144),),
                 ( (594,160),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (277,294),),
                 ( (238,112),),
                 ( (364,332),),
                 ( (342,172),),
                 ( (561,115),),
                 ( (394,227),),
                 ( (386,285),),
                 ( (332,117),),
                 ( (261,205),),
                 ( (387,187),),
                 ( (368,144),),
                 ( (594,160),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (191,314),'Saanich',),
                 ( (134,115),'Aberdeen',),
                 ( (376,350),'Bellingham',),
                 ( (228,175),'Bremerton',),
                 ( (514,98),'Ellensburg',),
                 ( (414,235),'Everett',),
                 ( (406,288),'Mount Vernon',),
                 ( (338,99),'Olympia',),
                 ( (87,224),'Olympic Natl Park',),
                 ( (407,190),'Seattle',),
                 ( (388,142),'Tacoma',),
                 ( (533,181),'Wenatchee',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (191,314),'Saanich',),
                 ( (134,115),'Aberdeen',),
                 ( (376,350),'Bellingham',),
                 ( (228,175),'Bremerton',),
                 ( (514,98),'Ellensburg',),
                 ( (414,235),'Everett',),
                 ( (406,288),'Mount Vernon',),
                 ( (338,99),'Olympia',),
                 ( (87,224),'Olympic Natl Park',),
                 ( (407,190),'Seattle',),
                 ( (388,142),'Tacoma',),
                 ( (533,181),'Wenatchee',),
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
dsm.set('Config.1.Core5.1.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.3.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.4.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
# MAP: 121950
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(4845,16693),
             mapcutSize=(1800,1200),
             mapFinalSize=(720,480),
             mapMilesSize=(153,122),
             datacutType='radar.us',
             datacutCoordinate=(195,1707),
             datacutSize=(220,147),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core2.2.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.5.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2.3.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (244,98),'16',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (462,171),'2',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (462,171),'2',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (349,266),'5',),
                 ( (440,87),'90',),
               ),
             ),
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (134,236),'101',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (349,266),'5',),
                 ( (440,87),'90',),
               ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (244,98),'16',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',14,(212,212,212,255),0,0,(),),
               ( ( (134,236),'101',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (371,116),),
                 ( (315,351),),
                 ( (325,176),),
                 ( (355,213),),
                 ( (81,256),),
                 ( (382,135),),
                 ( (358,89),),
                 ( (493,356),),
                 ( (333,115),),
                 ( (545,145),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (371,116),),
                 ( (315,351),),
                 ( (325,176),),
                 ( (355,213),),
                 ( (81,256),),
                 ( (382,135),),
                 ( (358,89),),
                 ( (493,356),),
                 ( (333,115),),
                 ( (545,145),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (391,119),'Bellevue',),
                 ( (268,334),'Burlington',),
                 ( (229,189),'Edmonds',),
                 ( (368,231),'Everett',),
                 ( (88,279),'Port Angeles',),
                 ( (341,156),'Redmond',),
                 ( (281,97),'Renton',),
                 ( (455,339),'Rockport',),
                 ( (261,133),'Seattle',),
                 ( (525,124),'Skykomish',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (391,119),'Bellevue',),
                 ( (268,334),'Burlington',),
                 ( (229,189),'Edmonds',),
                 ( (368,231),'Everett',),
                 ( (88,279),'Port Angeles',),
                 ( (341,156),'Redmond',),
                 ( (281,97),'Renton',),
                 ( (455,339),'Rockport',),
                 ( (261,133),'Seattle',),
                 ( (525,124),'Skykomish',),
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
dsm.set('Config.1.Core2.1.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.5.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core2.3.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.2.Local_LocalDoppler.0', d, 0)
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
wxdata.setMapData('Config.1.Core4.3.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4.4.Local_RadarSatelliteComposite.0', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Core4.3.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.1.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.2.Local_RadarSatelliteComposite.0', d, 0)
dsm.set('Config.1.Core4.4.Local_RadarSatelliteComposite.0', d, 0)
# MAP: 77012
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(2073,2064),
             mapcutSize=(1512,1008),
             mapFinalSize=(720,480),
             mapMilesSize=(1415,953),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(0,786),
             datacutSize=(825,514),
             dataFinalSize=(608,377),
             dataOffset=(112,0),
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
# MAP: 77013
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(3335,14583),
             mapcutSize=(6840,4560),
             mapFinalSize=(720,480),
             mapMilesSize=(589,471),
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
               ( ( '72698000',(238,95),),
                 ( '72781000',(357,137),),
                 ( '72785000',(500,222),),
                 ( '72788004',(490,117),),
                 ( '72789032',(365,246),),
                 ( '72792040',(133,159),),
                 ( '72793010',(235,193),),
                 ( '74201073',(232,284),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72698000',(235,135),),
                 ( '72781000',(354,177),),
                 ( '72785000',(497,262),),
                 ( '72788004',(487,157),),
                 ( '72789032',(362,286),),
                 ( '72792040',(130,199),),
                 ( '72793010',(232,233),),
                 ( '74201073',(229,324),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (200,169),'Portland',),
                 ( (324,211),'Yakima',),
                 ( (461,296),'Spokane',),
                 ( (437,191),'Walla Walla',),
                 ( (335,320),'Chelan',),
                 ( (93,233),'Hoquiam',),
                 ( (205,267),'Seattle',),
                 ( (180,358),'Bellingham',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
# MAP: 77014
# Local_CurrentWaterTemperatures (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(1879,2031),
             mapcutSize=(1656,1104),
             mapFinalSize=(720,480),
             mapMilesSize=(1537,1035),
             datacutType='waterTemps.us',
             datacutCoordinate=(149,727),
             datacutSize=(720,481),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.BoatAndBeach.0.Local_CurrentWaterTemperatures.0', d, 0)
#
# Local_CurrentWaterTemperatures (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Frutiger_Black',24,(212,212,212,255),1,0,'waterTemp',0,(),1,0,),
               ( ( 'B46002',(131,186),),
                 ( 'B46005',(159,292),),
                 ( 'B46015',(248,150),),
                 ( 'B46022',(233,95),),
                 ( 'B46027',(249,120),),
                 ( 'B46036',(127,356),),
                 ( 'B46041',(291,279),),
                 ( 'B46087',(307,315),),
                 ( 'B46088',(336,300),),
                 ( 'B46089',(260,246),),
                 ( 'B46131',(317,358),),
                 ( 'B46132',(258,359),),
                 ( 'B46146',(335,333),),
                 ( 'B46206',(286,333),),
                 ( 'CARO3',(264,171),),
                 ( 'DESW1',(291,296),),
                 ( 'DMNO3',(300,244),),
                 ( 'NWPO3',(282,198),),
                 ( 'WPOW1',(345,277),),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.BoatAndBeach.0.Local_CurrentWaterTemperatures.0', d, 0)
#
wxdata.setInterestList('lambert.us','1',['waterTemps.us','travelWeather.us','snowfallQpfForecast.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.3.Local_RadarSatelliteComposite.0','Config.1.Core4.1.Local_RadarSatelliteComposite.0','Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.Core4.2.Local_RadarSatelliteComposite.0','Config.1.Core4.4.Local_RadarSatelliteComposite.0',])
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core3.1.Local_LocalDoppler.0','Config.1.Core2.4.Local_LocalDoppler.0','Config.1.Core5.1.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0','Config.1.Core3.3.Local_LocalDoppler.0','Config.1.Core3.4.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.Core2.2.Local_LocalDoppler.0','Config.1.Core2.1.Local_LocalDoppler.0','Config.1.Core3.5.Local_LocalDoppler.0','Config.1.Core2.3.Local_LocalDoppler.0','Config.1.Core3.2.Local_LocalDoppler.0',])
wxdata.setInterestList('waterTemps.us.cuts','1',['Config.1.BoatAndBeach.0.Local_CurrentWaterTemperatures.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['waterTemps.us','radarSatellite.us','snowfallQpfForecast.us','radar.us','travelWeather.us',])
#
wxdata.setInterestList('tideStation','1',['W9447130','W9449880',])
wxdata.setInterestList('airportId','1',['ATL','BFI','BLI','DEN','DFW','GEG','LAX','LGA','MIA','ORD','PDX','PHX','SEA',])
wxdata.setInterestList('coopId','1',['71777005','71799004','71892000','72205000','72219000','72259000','72295000','72405000','72494000','72503000','72509000','72530000','72681000','72698000','72698106','72773000','72781000','72781046','72784022','72785000','72785005','72788004','72789032','72791000','72792040','72793000','72793010','72793030','72793047','72793053','72793056','72793056','72793061','72793072','72793083','72793086','72793094','72793108','74201073','74201073',])
wxdata.setInterestList('obsStation','1',['B46002','B46005','B46015','B46022','B46027','B46036','B46041','B46087','B46088','B46089','B46131','B46132','B46146','B46206','CARO3','CYVR','DESW1','DMNO3','KPAE','KRNT','KSEA','NWPO3','T72202000','T72219000','T72259000','T72278000','T72295000','T72503000','T72530000','T72565000','T72681000','T72698000','T72773000','T72781000','T72781046','T72784022','T72785000','T72785005','T72791000','T72792000','T72793000','T72793010','T72793011','T72793015','T72793030','T72793045','T72793047','T72793056','T72793061','T72793072','T72793083','T72793086','T72793094','T72793108','T74201021','T74201060','T74201073','T74206004','WPOW1',])
wxdata.setInterestList('climId','1',['452675','457470','457473',])
wxdata.setInterestList('metroId','1',['31',])
wxdata.setInterestList('zone','1',['WAZ507','WAZ556','WAZ558',])
wxdata.setInterestList('aq','1',['wa004',])
wxdata.setInterestList('zone.cwf','1',['PZZ135',])
wxdata.setInterestList('skiId','1',['191','198','216','25','314','356','40','407','43','436','482','503006','604038','77',])
wxdata.setInterestList('county','1',['WAC033','WAC061',])
#
dsm.set('Config.1.Package.36',('Core3',0), 0)
dsm.set('Config.1.Package.34',('Ski',0), 0)
dsm.set('Config.1.Package.25',('Airport',0), 0)
dsm.set('Config.1.Package.31',('Core2',4), 0)
dsm.set('Config.1.Package.23',('Travel',0), 0)
dsm.set('Config.1.Package.29',('Core4',3), 0)
dsm.set('Config.1.Package.18',('Core3',2), 0)
dsm.set('Config.1.Package.16',('Core2',1), 0)
dsm.set('Config.1.Package.13',('Core4',0), 0)
dsm.set('Config.1.Package.9',('Core3',3), 0)
dsm.set('Config.1.Package.7',('Core5',0), 0)
dsm.set('Config.1.Package.5',('Core4',2), 0)
dsm.set('Config.1.Package.0',('Core3',4), 0)
dsm.set('Config.1.Package.38',('Core2',0), 0)
dsm.set('Config.1.Package.35',('Health',0), 0)
dsm.set('Config.1.Package.26',('Core3',3), 0)
dsm.set('Config.1.Package.32',('Core5',0), 0)
dsm.set('Config.1.Package.22',('Core2',2), 0)
dsm.set('Config.1.Package.28',('Core2',4), 0)
dsm.set('Config.1.Package.20',('Core2',1), 0)
dsm.set('Config.1.Package.15',('Ski',0), 0)
dsm.set('Config.1.Package.12',('Core3',4), 0)
dsm.set('Config.1.Package.10',('Core5',0), 0)
dsm.set('Config.1.Package.6',('Core2',3), 0)
dsm.set('Config.1.Package.4',('Core4',2), 0)
dsm.set('Config.1.Package.2',('Core3',1), 0)
dsm.set('Config.1.Package.37',('Ski',0), 0)
dsm.set('Config.1.Package.33',('Core3',3), 0)
dsm.set('Config.1.Package.24',('Health',0), 0)
dsm.set('Config.1.Package.30',('Core3',2), 0)
dsm.set('Config.1.Package.21',('Core2',0), 0)
dsm.set('Config.1.Package.27',('Core3',1), 0)
dsm.set('Config.1.Package.19',('Core4',4), 0)
dsm.set('Config.1.Package.17',('Core2',3), 0)
dsm.set('Config.1.Package.14',('Core2',0), 0)
dsm.set('Config.1.Package.11',('Travel',0), 0)
dsm.set('Config.1.Package.8',('Airport',0), 0)
dsm.set('Config.1.Package.3',('Core4',2), 0)
dsm.set('Config.1.Package.1',('Core2',1), 0)
dsm.set('dmaCode','819', 0)
dsm.set('secondaryObsStation','KSEA', 0)
dsm.set('primaryClimoStation','457473', 0)
dsm.set('stateCode','WA', 0)
dsm.set('expRev','9816925', 0)
dsm.set('primaryCoopId','72793010', 0)
dsm.set('wda','SEA', 0)
dsm.set('primarylat',47.50333, 0)
dsm.set('primaryCounty','WAC033', 0)
dsm.set('primaryObsStation','T72793010', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-122.33611, 0)
dsm.set('primaryForecastName','Seattle Metro', 0)
dsm.set('primaryZone','WAZ558', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','028081', 0)
dsm.set('msoName','Northwest Fiber', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','CITIZENS TELECOM SERVICES COMPAN', 0)
dsm.set('affiliateName','09813', 0)
dsm.set('msoCode','03516', 0)
dsm.set('headendName','WXS - SEATTLE - WXS', 0)
dsm.set('zipCode','98208', 0)
dsm.set('Config.1.irdAddress','0001140999022007', 0)
dsm.set('Config.1.starId','TWCS01040016', 0)
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
scmtRemove('Config.1.Core3.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.4.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.5.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Golf.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.5.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.4.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.2.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.2.Local_CurrentConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.3.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Core3.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Core2.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Core3.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core5.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.Core3.5.Local_TextForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_Tides.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.4.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Core3.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core3.4.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.4.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Golf.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.4.Local_DaypartForecast.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.4.Local_MenuBoard.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Core3.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.4.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Core4.4.Local_WeatherBulletin.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.4.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.Core2.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.3.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core3.1.Local_CurrentConditions.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.4.Fcst_DaypartForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.4.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.1.Local_MenuBoard.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Core2.3.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.4.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.1.Local_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.2.Local_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_Tides.1')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core4.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.3.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.2')
scmtRemove('Config.1.Golf.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.4.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.2.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.2.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_PackageIntro.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core3.5.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Core4.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.BoatAndBeach.0.Local_CoastalWatersForecast.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
scmtRemove('Config.1.Core3.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Core4.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.3.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.5.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.3.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.1.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.5.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.2.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.2.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core3.5.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.2.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core3.5.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.4.Local_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Core3.3.Local_TextForecast.0')
scmtRemove('Config.1.Core4.4.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.4.Local_TextForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_TeeTimeForecast.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.1.Local_DaypartForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.4.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.3.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Core3.5.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Core2.3.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.4.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.BoatAndBeach.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Core2.4.Local_DaypartForecast.0')
scmtRemove('Config.1.Core4.4.Local_CurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.2.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Core4.3.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.4.Local_WeatherBulletin.0')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Core4.4.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.Golf.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.Core2.2.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.2.Local_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.4.Local_MenuBoard.0')
scmtRemove('Config.1.Golf.0.Local_Promo.0')
scmtRemove('Config.1.Core3.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Core4.3.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2.4.Local_MenuBoard.0')
scmtRemove('Config.1.Core2.4.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Core4.4.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.1')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core2.3.Local_CurrentConditions.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.BoatAndBeach.0.Local_SurfReport.0')
scmtRemove('Config.1.Core2.2.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.3.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.2.Local_TextForecast.0')
scmtRemove('Config.1.Core4.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.3.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core3.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.1.Local_MenuBoard.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core2.3.Local_DaypartForecast.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Core4.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core3.4.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.4.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core3.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Golf.0.Local_PgaEventForecast.0')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
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
scmtRemove('Config.1.Core4.4')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Everett Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
dsm.set('Config.1.Core4.4', d, 0, 1)
scmtRemove('Config.1.Core3.5')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core3.5', d, 0, 1)
scmtRemove('Config.1.Core4.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Everett Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
dsm.set('Config.1.Core4.3', d, 0, 1)
scmtRemove('Config.1.Core3.4')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SEATTLE'
dsm.set('Config.1.Core3.4', d, 0, 1)
scmtRemove('Config.1.Core5.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 1
d.shortPackageTitle = 'LOCAL RADAR'
dsm.set('Config.1.Core5.1', d, 0, 1)
scmtRemove('Config.1.Core4.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core4.2', d, 0, 1)
scmtRemove('Config.1.Core3.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Seattle Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SEATTLE'
dsm.set('Config.1.Core3.3', d, 0, 1)
scmtRemove('Config.1.Core2.4')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
dsm.set('Config.1.Core2.4', d, 0, 1)
scmtRemove('Config.1.Airport.0')
d = twc.Data()
d.bkgImage = 'airport_bg'
d.packageTitle = 'Airport Conditions'
d.packageFlavor = 1
d.shortPackageTitle = 'AIRPORTS'
dsm.set('Config.1.Airport.0', d, 0, 1)
scmtRemove('Config.1.Core5.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Radar'
d.packageFlavor = 0
d.shortPackageTitle = 'LOCAL RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Everett Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
dsm.set('Config.1.Core4.1', d, 0, 1)
scmtRemove('Config.1.Core3.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core3.2', d, 0, 1)
scmtRemove('Config.1.Core2.3')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core2.3', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Seattle Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SEATTLE'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Everett Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
dsm.set('Config.1.Core3.1', d, 0, 1)
scmtRemove('Config.1.Core2.2')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core2.2', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Seattle Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SEATTLE'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Core2.1')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Redmond Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'REDMOND'
dsm.set('Config.1.Core2.1', d, 0, 1)
scmtRemove('Config.1.BoatAndBeach.0')
d = twc.Data()
d.bkgImage = 'boatbeach_bg'
d.packageTitle = 'Boat & Beach'
d.packageFlavor = 1
d.shortPackageTitle = 'BOAT & BEACH'
dsm.set('Config.1.BoatAndBeach.0', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Everett Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'EVERETT'
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
d.packageTitle = 'Seattle Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'SEATTLE'
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
d.locName = 'Seattle Metro'
d.coopId = '72793010'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'ocean_bg'
dsm.set('Config.1.Core2.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
dsm.set('Config.1.Core3.4.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core2.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Travel.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core3.5.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Airport.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.Core3.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Everett'
d.coopId = '72793083'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.1.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'ski_intro_bg'
dsm.set('Config.1.Ski.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793108','T72793056','T72793083','T72793072','T72793094','T72793072','T72793030','T72793047','T72793086','T72793061',]
d.locName = ['Arlington',' Bothell',' Mukilteo',' Lynnwood',' Marysville',' Edmonds',' Kirkland',' Shoreline',' Snohomish',' Woodinville',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.4.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Ski.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core3.5.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Airport.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core1.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core2.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Arlington',' Bothell',' Mukilteo','  Lynnwood',' Marysville',' Edmonds',' Kirkland','Shoreline','Snohomish','Woodinville',]
d.coopId = ['72793108','72793056','72793083','72793072','72793094','72793072','72793030','72793047','72793086','72793061',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Health.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.4.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core4.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.4.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core3.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core3.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.5.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Airport.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72791000','T72681000','T72784022','T72773000','T72698000','T74201021','T72785005','CYVR','T72781046','T72781000',]
d.locName = ['Astoria',' Boise',' Kennewick',' Missoula',' Portland',' Saanich',' Spokane',' Vancouver, BC',' Wenatchee',' Yakima',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'seattle_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Ski.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793000'
d.latitude = 47.44
d.longitude = -122.31
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core4.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Astoria',' Boise',' Kennewick',' Missoula',' Portland',' Saanich',' Spokane',' Vancouver, BC',' Wenatchee',' Yakima',]
d.coopId = ['72791000','72681000','72784022','72773000','72698000','71799004','72785005','71892000','72781046','72781000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core3.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Redmond'
d.coopId = '72793061'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.2.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core5.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.2.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core1.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.2.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.4.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.4.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.3.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'seattle_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.aq = 'wa004'
dsm.set('Config.1.Health.0.Local_AirQualityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.4.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793000'
d.latitude = 47.44
d.longitude = -122.31
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.4.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Ski.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Health.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core5.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core4.4.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.2.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Seattle Metro'
d.coopId = '72793010'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.3.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Health.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.4.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2.4.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core5.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core3.5.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core3.4.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core2.4.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LAX','MIA','LGA','PHX',]
d.obsStation = ['T72295000','T72202000','T72503000','T72278000',]
d.locName = ['Los Angeles Int`l','Miami Int`l Airport','New York LaGuardia','Phoenix Sky Harbor',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'seattle_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core4.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['ATL','ORD','DFW','DEN',]
d.obsStation = ['T72219000','T72530000','T72259000','T72565000',]
d.locName = ['Atlanta Hartsfield-Jackson','Chicago O`Hare Int`l','Dallas/Ft. Worth Int`l','Denver Int`l Airport',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core2.4.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.3.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core5.1.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core5.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core3.4.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.4.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Airport.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.1.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.4.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.3.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core2.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
dsm.set('Config.1.Core3.3.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core1.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Airport.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.5.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core3.4.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.4.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core4.4.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.4.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Vail, CO','Jackson Hole Mountain Resort, WY','Aspen Highlands, CO',]
d.skiId = ['482','191','25',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.3', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.3.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core4.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.2.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.2.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.2.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Big Bear Mtn. Resort, CA','Breckenridge, CO','Park City, UT',]
d.skiId = ['43','77','314',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.2', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Seattle Metro'
d.coopId = '72793010'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.4.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core1.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core2.3.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Travel.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Berkshire East Ski Resort, MA','Shawnee Mt., PA','Loon Mt., NH',]
d.skiId = ['40','356','216',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Snowshoe Mountain, WV','Sugarloaf, ME','Killington/Pico, VT',]
d.skiId = ['407','436','198',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.3.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72793010'
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.3.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.2.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Orlando','San Francisco','Washington, DC',]
d.coopId = ['72205000','72494000','72405000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Ski.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core5.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.2.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'BLI'
d.obsStation = 'T74201073'
d.locName = 'Bellingham International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.locName = ['Dallas','Los Angeles','New York City',]
d.coopId = ['72259000','72295000','72503000',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.3.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
dsm.set('Config.1.Core4.2.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'GEG'
d.obsStation = 'T72785000'
d.locName = 'Spokane International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
dsm.set('Config.1.Core3.1.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Atlanta','Boston','Chicago',]
d.coopId = ['72219000','72509000','72530000',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Travel.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core5.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KPAE',]
d.locName = ['Everett','Everett',]
d.elementDurationLong = 6
dsm.set('Config.1.Core4.4.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core4.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'BFI'
d.obsStation = 'T72793010'
d.locName = 'Boeing Field - King County International Arpt.'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core2.2.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Ski.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'SEA'
d.obsStation = 'T72793010'
d.locName = 'Seattle - Tacoma International Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core4.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core3.5.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.climId = '457473'
d.latitude = 47.45
d.longitude = -122.3
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core4.4.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.3.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.2.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72792000','T72793000','T74201060','T74206004',]
d.locName = ['Olympia','Seattle','Stanwood','Tacoma',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core3.4.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793083','KSEA',]
d.locName = ['Everett','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Ski.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Health.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793015','T72793045','T72793083','T72793011',]
d.locName = ['Auburn','Bremerton','Everett','Federal Way',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Core5.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationLong = 6
dsm.set('Config.1.Core5.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.bkgImage = 'seattle_bg'
d.affiliateName = 'Northwest Fiber'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Redmond'
d.coopId = '72793061'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.5.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core2.1.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Travel.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core5.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core2.2.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.1.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Health.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core5.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'seattle_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.3.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond Area'
d.zone = 'WAZ556'
dsm.set('Config.1.Core3.5.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793061','KRNT',]
d.locName = ['Redmond','Renton',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2.4.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Seattle Metro'
d.coopId = '72793010'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
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
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core1.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett Area'
d.zone = 'WAZ507'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core4.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.3.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Travel.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core3.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72793010','KSEA',]
d.locName = ['Seattle','Seattle-Tacoma',]
d.elementDurationShort = 6
dsm.set('Config.1.Core4.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['SEA','BFI','GEG','PDX',]
d.obsStation = ['T72793000','T72793010','T72785000','T72698000',]
d.locName = ['Seattle-Tacoma Int`l Airport',' Boeing Field Airport',' Spokane International Airport','Portland International Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Redmond'
d.coopId = '72793061'
dsm.set('Config.1.Core2.4.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Metro'
d.coopId = '72793010'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Everett'
d.coopId = '72793083'
dsm.set('Config.1.Core3.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle Area'
d.zone = 'WAZ558'
dsm.set('Config.1.Core3.4.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Seattle'
d.coopId = '72793010'
dsm.set('Config.1.Core3.5.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.4.Local_MenuBoard.0', d, 0, 1)
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
# Finished generation on Tue Jan 11 16:16:25 GMT 2022

import os; os.system("cd /twc/data/clock; tar -xvf /twc/data/clock/clocks.tar");ds.commit();wxdata.loadClock();