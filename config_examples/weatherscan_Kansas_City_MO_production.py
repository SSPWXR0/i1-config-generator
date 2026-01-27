# Created on Tue Jan 11 15:57:28 GMT 2022
twc.Log.info('scmt config started')
# EXP: 12518
# VIW: 30977
# CLN: 12247
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
# MAP: 72120
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19140,11130),
             mapcutSize=(2480,1230),
             mapFinalSize=(248,123),
             mapMilesSize=(244,145),
             datacutType='radar.us',
             datacutCoordinate=(1945,1026),
             datacutSize=(304,151),
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
               ( ( (138,36),),
                 ( (154,52),),
                 ( (140,91),),
               ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
               ( ( (138,36),),
                 ( (154,52),),
                 ( (140,91),),
               ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(255,255,255,192),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (93,29),'Olathe',),
                 ( (121,65),'Kansas City',),
                 ( (154,96),'St. Joseph',),
               ),
             ),
             (
               ('Interstate-Bold',14,(255,255,255,255),1,0,0,(20,20,20,64),1,0,0,),
               ( ( (93,29),'Olathe',),
                 ( (121,65),'Kansas City',),
                 ( (154,96),'St. Joseph',),
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
# MAP: 96
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19618,11040),
             mapcutSize=(2100,1400),
             mapFinalSize=(720,480),
             mapMilesSize=(207,165),
             datacutType='radar.us',
             datacutCoordinate=(2004,1015),
             datacutSize=(257,171),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.Core1.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core2Spanish.0.Local_LocalDopplerSpanish.0', d, 0)
wxdata.setMapData('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (169,149),'75',),
                 ( (413,100),'71',),
                 ( (159,314),'75',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (169,149),'75',),
                 ( (413,100),'71',),
                 ( (159,314),'75',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (334,306),'29',),
                 ( (436,329),'35',),
                 ( (511,197),'70',),
                 ( (101,204),'70',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (334,306),'29',),
                 ( (436,329),'35',),
                 ( (511,197),'70',),
                 ( (101,204),'70',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (318,274),),
                 ( (328,172),),
                 ( (249,121),),
                 ( (178,213),),
                 ( (338,190),),
                 ( (582,357),),
                 ( (444,269),),
                 ( (434,224),),
                 ( (382,222),),
                 ( (420,183),),
                 ( (336,353),),
                 ( (639,141),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (318,274),),
                 ( (328,172),),
                 ( (249,121),),
                 ( (178,213),),
                 ( (338,190),),
                 ( (582,357),),
                 ( (444,269),),
                 ( (434,224),),
                 ( (382,222),),
                 ( (420,183),),
                 ( (336,353),),
                 ( (639,141),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (182,292),'Leavenworth',),
                 ( (301,155),'Olathe',),
                 ( (218,104),'Ottawa',),
                 ( (146,236),'Topeka',),
                 ( (262,193),'Lenexa',),
                 ( (564,338),'Chillicothe',),
                 ( (410,289),'Excelsior Springs',),
                 ( (454,227),'Independence',),
                 ( (306,244),'Kansas City',),
                 ( (437,170),'Lee\'s Summit',),
                 ( (229,356),'St. Joseph',),
                 ( (596,119),'Sedalia',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (182,292),'Leavenworth',),
                 ( (301,155),'Olathe',),
                 ( (218,104),'Ottawa',),
                 ( (146,236),'Topeka',),
                 ( (262,193),'Lenexa',),
                 ( (564,338),'Chillicothe',),
                 ( (410,289),'Excelsior Springs',),
                 ( (454,227),'Independence',),
                 ( (306,244),'Kansas City',),
                 ( (437,170),'Lee\'s Summit',),
                 ( (229,356),'St. Joseph',),
                 ( (596,119),'Sedalia',),
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
dsm.set('Config.1.Core2Spanish.0.Local_LocalDopplerSpanish.0', d, 0)
dsm.set('Config.1.Core2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core3.0.Local_LocalDoppler.0', d, 0)
# MAP: 76275
# Local_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19976,11252),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(142,113),
             datacutType='radar.us',
             datacutCoordinate=(2048,1041),
             datacutSize=(176,117),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             activeVocalCue=1,
)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
wxdata.setMapData('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
#
# Local_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (345,113),'69',),
               ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (345,113),'69',),
               ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (312,340),'29',),
                 ( (450,334),'35',),
                 ( (582,185),'70',),
                 ( (249,107),'35',),
               ),
             ),
             (
               (('interstateSign',0,1,0,),'Frutiger_Black',16,(212,212,212,255),0,0,(),),
               ( ( (312,340),'29',),
                 ( (450,334),'35',),
                 ( (582,185),'70',),
                 ( (249,107),'35',),
               ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
               ( ( (342,272),),
               ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
               ( ( (336,182),),
                 ( (199,183),),
                 ( (287,298),),
                 ( (314,155),),
                 ( (362,189),),
                 ( (244,222),),
                 ( (393,138),),
                 ( (427,216),),
                 ( (379,222),),
                 ( (437,164),),
                 ( (423,260),),
                 ( (545,272),),
                 ( (382,301),),
               ),
             ),
             (
               ('locatorDot',0,1,0,),
               ( ( (336,182),),
                 ( (199,183),),
                 ( (287,298),),
                 ( (314,155),),
                 ( (362,189),),
                 ( (244,222),),
                 ( (393,138),),
                 ( (427,216),),
                 ( (379,222),),
                 ( (437,164),),
                 ( (423,260),),
                 ( (545,272),),
                 ( (382,301),),
               ),
             ),
             (
               ('airplane',0,1,0,),
               ( ( (342,272),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',20,(230,230,230,205),1,0,0,(20,20,20,128),2,0,0,),
               ( ( (260,185),'Lenexa',),
                 ( (97,186),'Lawrence',),
                 ( (148,301),'Leavenworth',),
                 ( (241,158),'Olathe',),
                 ( (382,192),'Overland Park',),
                 ( (124,240),'Tonganoxie',),
                 ( (410,125),'Belton',),
                 ( (446,228),'Independence',),
                 ( (300,244),'Kansas City',),
                 ( (454,151),'Lee\'s Summit',),
                 ( (440,278),'Liberty',),
                 ( (565,275),'Richmond',),
                 ( (337,322),'Smithville',),
               ),
             ),
             (
               ('Frutiger_Black',20,(230,230,230,255),1,0,0,(20,20,20,128),1,0,0,),
               ( ( (260,185),'Lenexa',),
                 ( (97,186),'Lawrence',),
                 ( (148,301),'Leavenworth',),
                 ( (241,158),'Olathe',),
                 ( (382,192),'Overland Park',),
                 ( (124,240),'Tonganoxie',),
                 ( (410,125),'Belton',),
                 ( (446,228),'Independence',),
                 ( (300,244),'Kansas City',),
                 ( (454,151),'Lee\'s Summit',),
                 ( (440,278),'Liberty',),
                 ( (565,275),'Richmond',),
                 ( (337,322),'Smithville',),
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
dsm.set('Config.1.SevereCore1A.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore2.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.SevereCore1B.0.Local_LocalDoppler.0', d, 0)
dsm.set('Config.1.Core5.0.Local_LocalDoppler.0', d, 0)
# MAP: 76144
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3092,1284),
             mapcutSize=(1816,1211),
             mapFinalSize=(720,480),
             mapMilesSize=(1762,1191),
             datacutType='radarSatellite.us',
             datacutCoordinate=(696,316),
             datacutSize=(933,626),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Core4.0.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0', d, 0)
wxdata.setMapData('Config.1.Core4Spanish.0.Local_RadarSatelliteCompositeSpanish.0', d, 0)
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
dsm.set('Config.1.Core4Spanish.0.Local_RadarSatelliteCompositeSpanish.0', d, 0)
# MAP: 77009
# Local_SnowfallQpfForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3247,1393),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(1541,1040),
             datacutType='snowfallQpfForecast.us',
             datacutCoordinate=(607,349),
             datacutSize=(1023,686),
             dataFinalSize=(720,480),
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
wxdata.setMapData('Config.1.Travel.1.Local_NationalTravelWeather.0', d, 0)
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
dsm.set('Config.1.Travel.1.Local_NationalTravelWeather.0', d, 0)
# MAP: 76333
# Local_RegionalForecastConditions (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(13200,6700),
             mapcutSize=(14400,9600),
             mapFinalSize=(720,480),
             mapMilesSize=(1430,1143),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
wxdata.setMapData('Config.1.Travel.1.Local_RegionalForecastConditions.0', d, 0)
#
# Local_RegionalForecastConditions (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
               ( ( '72327000',(587,107),),
                 ( '72340004',(423,94),),
                 ( '72353004',(284,98),),
                 ( '72434000',(472,191),),
                 ( '72446000',(346,192),),
                 ( '72534000',(558,278),),
                 ( '72546000',(395,283),),
                 ( '72562000',(216,275),),
                 ( '72565000',(131,212),),
               ),
             ),
        ],
  fcstValue = [
             (
               ('Frutiger_Bold',26,(212,212,0,255),1,0,'highTemp',1,(),2,0,),
               ( ( '72327000',(584,147),),
                 ( '72340004',(420,134),),
                 ( '72353004',(281,138),),
                 ( '72434000',(469,231),),
                 ( '72446000',(343,232),),
                 ( '72534000',(555,318),),
                 ( '72546000',(392,323),),
                 ( '72562000',(213,315),),
                 ( '72565000',(128,252),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (546,181),'Nashville',),
                 ( (376,168),'Little Rock',),
                 ( (215,172),'Oklahoma City',),
                 ( (435,265),'St. Louis',),
                 ( (294,266),'Kansas City',),
                 ( (523,352),'Chicago',),
                 ( (343,357),'Des Moines',),
                 ( (160,349),'North Platte',),
                 ( (100,286),'Denver',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Travel.0.Local_RegionalForecastConditions.0', d, 0)
dsm.set('Config.1.Travel.1.Local_RegionalForecastConditions.0', d, 0)
# MAP: 77010
# Local_RegionalGolfIndexForecast (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3654,1568),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(915,615),
             datacutType='golfIndexForecast.us',
             datacutCoordinate=(870,463),
             datacutSize=(605,405),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Golf.0.Local_RegionalGolfIndexForecast.0', d, 0)
#
# Local_RegionalGolfIndexForecast (PRODUCT DATA)
#
d = twc.Data(
  fcstValue = [
             (
               ('Frutiger_Black',32,(212,212,212,255),1,0,'golfIndex',0,(),2,0,),
               ( ( '72432000',(577,220),),
                 ( '72434035',(446,246),),
                 ( '72439000',(465,317),),
                 ( '72440000',(317,165),),
                 ( '72445000',(364,258),),
                 ( '72445054',(385,190),),
                 ( '72446000',(253,273),),
                 ( '72450000',(145,177),),
                 ( '72455004',(153,262),),
                 ( '72540046',(343,323),),
                 ( '72551000',(163,340),),
                 ( '74662019',(486,162),),
               ),
             ),
        ],
  textString = [
             (
               ('Frutiger_Black',19,(212,212,212,255),1,0,0,(),2,0,1,),
               ( ( (548,197),'Evansville',),
                 ( (442,224),'St. Louis',),
                 ( (432,296),'Springfield',),
                 ( (270,142),'Springfield',),
                 ( (334,235),'Columbia',),
                 ( (384,168),'Rolla',),
                 ( (212,248),'Kansas City',),
                 ( (128,160),'Wichita',),
                 ( (93,243),'Manhattan',),
                 ( (316,303),'Kirksville',),
                 ( (147,323),'Lincoln',),
                 ( (455,141),'Cape Girardeau',),
               ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Golf.0.Local_RegionalGolfIndexForecast.0', d, 0)
#
wxdata.setInterestList('lambert.us','1',['travelWeather.us','snowfallQpfForecast.us','golfIndexForecast.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('golfIndexForecast.us.cuts','1',['Config.1.Golf.0.Local_RegionalGolfIndexForecast.0',])
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Core4.0.Local_RadarSatelliteComposite.0','Config.1.SevereCore1A.0.Local_RadarSatelliteComposite.0','Config.1.Core4Spanish.0.Local_RadarSatelliteCompositeSpanish.0',])
wxdata.setInterestList('travelWeather.us.cuts','1',['Config.1.Travel.0.Local_NationalTravelWeather.0','Config.1.Travel.1.Local_NationalTravelWeather.0',])
wxdata.setInterestList('snowfallQpfForecast.us.cuts','1',['Config.1.Ski.0.Local_SnowfallQpfForecast.0',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler.0','Config.1.Core1.0.Local_LocalDoppler.0','Config.1.Core2Spanish.0.Local_LocalDopplerSpanish.0','Config.1.Core2.0.Local_LocalDoppler.0','Config.1.Core3.0.Local_LocalDoppler.0','Config.1.SevereCore1A.0.Local_LocalDoppler.0','Config.1.SevereCore2.0.Local_LocalDoppler.0','Config.1.SevereCore1B.0.Local_LocalDoppler.0','Config.1.Core5.0.Local_LocalDoppler.0',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['golfIndexForecast.us','radarSatellite.us','snowfallQpfForecast.us','radar.us','travelWeather.us',])
#
wxdata.setInterestList('airportId','1',['ATL','BOS','DEN','DFW','IAD','ICT','LAX','LGA','MCI','MEM','MIA','MKC','MSP','ORD','PHL','PHX','SEA','SFO','STL',])
wxdata.setInterestList('coopId','1',['03772000','07149000','16242000','72205000','72327000','72340004','72353004','72356006','72357000','72386000','72405000','72432000','72434000','72434035','72439000','72440000','72440034','72445000','72445054','72446000','72446003','72446011','72446015','72446018','72446020','72446020','72446022','72446027','72446032','72446032','72446038','72446045','72446056','72446064','72449000','72449017','72450000','72455004','72455009','72456005','72456014','72456037','72534000','72540046','72545015','72546000','72550000','72551000','72562000','72565000','74542046','74542057','74550021','74550031','74662019','76405007','76556003','76595000','78073000','78543000','78982001',])
wxdata.setInterestList('obsStation','1',['KMKC','T72202000','T72219000','T72259000','T72278000','T72295000','T72334000','T72340004','T72356006','T72403000','T72408000','T72434000','T72446000','T72446003','T72446011','T72446018','T72446020','T72446022','T72446027','T72446032','T72446038','T72446045','T72446064','T72449000','T72450000','T72455009','T72456000','T72456014','T72456037','T72494000','T72503000','T72509000','T72530000','T72546000','T72550000','T72572000','T72658000','T72793000','T74542057',])
wxdata.setInterestList('metroId','1',['59',])
wxdata.setInterestList('climId','1',['234359',])
wxdata.setInterestList('zone','1',['KSZ105',])
wxdata.setInterestList('skiId','1',['113','120','191','197','25','314','425','454','456','482','507','77',])
wxdata.setInterestList('county','1',['KSC091','MOC095','KSC209',])
#
dsm.set('Config.1.Package.36',('Ski',0), 0)
dsm.set('Config.1.Package.34',('Core3',0), 0)
dsm.set('Config.1.Package.25',('Core2',0), 0)
dsm.set('Config.1.Package.31',('Airport',0), 0)
dsm.set('Config.1.Package.23',('Core2Spanish',0), 0)
dsm.set('Config.1.Package.29',('Core4',0), 0)
dsm.set('Config.1.Package.18',('Core5',0), 0)
dsm.set('Config.1.Package.16',('Core3',0), 0)
dsm.set('Config.1.Package.13',('Core4',0), 0)
dsm.set('Config.1.Package.9',('Core3',0), 0)
dsm.set('Config.1.Package.7',('Core2',0), 0)
dsm.set('Config.1.Package.5',('Travel',0), 0)
dsm.set('Config.1.Package.0',('Health',0), 0)
dsm.set('Config.1.Package.38',('Core2Spanish',0), 0)
dsm.set('Config.1.Package.35',('Core5',0), 0)
dsm.set('Config.1.Package.26',('Core4',0), 0)
dsm.set('Config.1.Package.32',('Core3',0), 0)
dsm.set('Config.1.Package.22',('Core2',0), 0)
dsm.set('Config.1.Package.28',('Airport',0), 0)
dsm.set('Config.1.Package.20',('Ski',0), 0)
dsm.set('Config.1.Package.15',('Travel',0), 0)
dsm.set('Config.1.Package.12',('Core3',0), 0)
dsm.set('Config.1.Package.10',('Core5',0), 0)
dsm.set('Config.1.Package.6',('Core4Spanish',0), 0)
dsm.set('Config.1.Package.4',('Core2',0), 0)
dsm.set('Config.1.Package.2',('Health',0), 0)
dsm.set('Config.1.Package.37',('Core2',0), 0)
dsm.set('Config.1.Package.33',('Core3',0), 0)
dsm.set('Config.1.Package.24',('Core4',0), 0)
dsm.set('Config.1.Package.30',('Core5',0), 0)
dsm.set('Config.1.Package.21',('Ski',0), 0)
dsm.set('Config.1.Package.27',('Core4Spanish',0), 0)
dsm.set('Config.1.Package.19',('Health',0), 0)
dsm.set('Config.1.Package.17',('Core3',0), 0)
dsm.set('Config.1.Package.14',('Core5',0), 0)
dsm.set('Config.1.Package.11',('Core2Spanish',0), 0)
dsm.set('Config.1.Package.8',('Airport',0), 0)
dsm.set('Config.1.Package.3',('Core2',0), 0)
dsm.set('Config.1.Package.1',('Travel',0), 0)
dsm.set('dmaCode','616', 0)
dsm.set('secondaryObsStation','KMKC', 0)
dsm.set('primaryClimoStation','234359', 0)
dsm.set('stateCode','KS', 0)
dsm.set('primaryCoopId','72446011', 0)
dsm.set('primarylat',38.95361, 0)
dsm.set('primaryCounty','KSC091', 0)
dsm.set('primaryObsStation','T72446011', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-94.75945, 0)
dsm.set('primaryForecastName','Kansas City Area', 0)
dsm.set('primaryZone','KSZ105', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('headendId','025341', 0)
dsm.set('msoName','Consolidated Communications', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','CONSOLIDATED COMMUNICATIONS NETW', 0)
dsm.set('affiliateName','17335', 0)
dsm.set('msoCode','02655', 0)
dsm.set('headendName','WXS - KANSAS CITY METRO - WXS', 0)
dsm.set('zipCode','66219', 0)
dsm.set('Config.1.irdAddress','0001140994782000', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.bcNetMask','255.255.255.0', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCS01030027', 0)
dsm.set('Config.1.bcGateWay','10.224.2.23', 0)
dsm.set('Config.1.bcIpAddress','10.224.2.60', 0)
#
#  Non Image Maps
#
#

#
#
wxdata.setTimeZone('CST6CDT')
#
d = twc.Data()
d.affiliateLogo = 'consolidatedLogo'
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
scmtRemove('Config.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Traffic.0.Fcst_TextForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.5')
scmtRemove('Config.1.Health.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core4Spanish.0.Local_ExtendedForecastSpanish.0')
scmtRemove('Config.1.Travel.1.Local_Destinations.1')
scmtRemove('Config.1.Traffic.0.Local_TrafficReport.0')
scmtRemove('Config.1.SevereCore1B.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Local_PackageIntro.0')
scmtRemove('Config.1.Ski.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.3')
scmtRemove('Config.1.Golf.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core2.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Local_PackageIntro.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficOverview.0')
scmtRemove('Config.1.CityTicker_TravelCitiesCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.International.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_AirportDelays.0')
scmtRemove('Config.1.Garden.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2Spanish.0.Local_DaypartForecastSpanish.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.1')
scmtRemove('Config.1.Garden.0.Local_Promo.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.2')
scmtRemove('Config.1.Health.0.Local_AllergyReport.0')
scmtRemove('Config.1.Core4Spanish.0.Local_CurrentConditionsSpanish.0')
scmtRemove('Config.1.Travel.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core4Spanish.0.Local_MenuBoardSpanish.0')
scmtRemove('Config.1.Golf.0.Local_PgaEventForecast.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.1')
scmtRemove('Config.1.Core2Spanish.0.Local_ExtendedForecastSpanish.0')
scmtRemove('Config.1.Travel.0.Local_PackageIntro.0')
scmtRemove('Config.1.Travel.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.2')
scmtRemove('Config.1.Travel.1.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.2')
scmtRemove('Config.1.Health.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.3')
scmtRemove('Config.1.Airport.0.Local_PackageIntro.0')
scmtRemove('Config.1.Golf.0.Local_TeeTimeForecast.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.1')
scmtRemove('Config.1.Travel.1.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core2Spanish.0.Local_CurrentConditionsSpanish.0')
scmtRemove('Config.1.Garden.0.Local_PackageIntro.0')
scmtRemove('Config.1.Core1.0.Local_NetworkIntro.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.0')
scmtRemove('Config.1.Golf.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.1')
scmtRemove('Config.1.Core2Spanish.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.3')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.1')
scmtRemove('Config.1.Core1.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core5.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Health.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Health.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_TextForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Core1.0.Local_Almanac.0')
scmtRemove('Config.1.Core4Spanish.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_TextForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1B.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_HealthForecast.0')
scmtRemove('Config.1.Core4.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Travel.1.Local_Destinations.2')
scmtRemove('Config.1.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core4Spanish.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.2')
scmtRemove('Config.1.Health.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Golf.0.Local_GolfCourseForecast.0')
scmtRemove('Config.1.Traffic.0.Local_TrafficFlow.0')
scmtRemove('Config.1.CityTicker_LocalCitiesForecast.0')
scmtRemove('Config.1.Airport.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core3.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Local_MenuBoard.0')
scmtRemove('Config.1.Ski.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.SevereCore2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2Spanish.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore2.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.SevereCore1A.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.1')
scmtRemove('Config.1.Core1.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.International.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.2')
scmtRemove('Config.1.Traffic.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core4.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2Spanish.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Travel.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core5.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core1.0.Local_TextForecast.0')
scmtRemove('Config.1.Core1.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2.0.Local_DaypartForecast.0')
scmtRemove('Config.1.Core3.0.Local_TextForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Golf.0.Local_Promo.0')
scmtRemove('Config.1.Core2.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core2Spanish.0.Local_MenuBoardSpanish.0')
scmtRemove('Config.1.Travel.1.Local_Destinations.0')
scmtRemove('Config.1.Traffic.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.International.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Core2.0.Local_CurrentConditions.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.0')
scmtRemove('Config.1.Core4Spanish.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_UltravioletIndex.0')
scmtRemove('Config.1.Core3.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Core2.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Health.0.Local_OutdoorActivityForecast.0')
scmtRemove('Config.1.Core4Spanish.0.Local_DaypartForecastSpanish.0')
scmtRemove('Config.1.Core5.0.Local_MenuBoard.0')
scmtRemove('Config.1.Core1.0.Local_ExtendedForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.2')
scmtRemove('Config.1.Golf.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.1')
scmtRemove('Config.1.Airport.0.Local_LocalAirportConditions.0')
scmtRemove('Config.1.Core3.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.CityTicker_LocalCitiesCurrentConditions.0')
scmtRemove('Config.1.Garden.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Travel.0.Local_Destinations.0')
scmtRemove('Config.1.Travel.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.SevereCore1B.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.CityTicker_TravelCitiesForecast.0')
scmtRemove('Config.1.Health.0.Local_Promo.0')
scmtRemove('Config.1.Golf.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Airport.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.SevereCore1A.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core1.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Health.0.Local_AirQualityForecast.0')
scmtRemove('Config.1.SevereCore2.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.International.0.Local_InternationalDestinations.4')
scmtRemove('Config.1.Core2.0.Cc_LongCurrentConditions.0')
scmtRemove('Config.1.Core2.0.Local_MenuBoard.0')
scmtRemove('Config.1.Traffic.0.SmLocal_TrafficSponsor.0')
scmtRemove('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0')
scmtRemove('Config.1.Golf.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Travel.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Ski.0.Local_PackageIntro.0')
scmtRemove('Config.1.SevereCore1B.0.Local_CurrentConditions.0')
scmtRemove('Config.1.SevereCore1A.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core4.0.Local_WeatherBulletin.0')
scmtRemove('Config.1.Core4.0.Local_CurrentConditions.0')
scmtRemove('Config.1.Health.0.Local_PackageIntro.0')
scmtRemove('Config.1.Travel.1.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.International.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core2Spanish.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Core1.0.Local_LocalObservations.0')
scmtRemove('Config.1.Core4Spanish.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Garden.0.Local_GardeningForecast.0')
scmtRemove('Config.1.Core3.0.Local_MenuBoard.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.3')
scmtRemove('Config.1.Traffic.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Fcst_TextForecast.0')
scmtRemove('Config.1.Core5.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Airport.0.Local_NationalAirportConditions.1')
scmtRemove('Config.1.Ski.0.Local_SunSafetyFacts.0')
scmtRemove('Config.1.Core4Spanish.0.Fcst_DaypartForecast.0')
scmtRemove('Config.1.Core2Spanish.0.Fcst_TextForecast.0')
scmtRemove('Config.1.Core3.0.Cc_ShortCurrentConditions.0')
scmtRemove('Config.1.Traffic.0.Fcst_ExtendedForecast.0')
scmtRemove('Config.1.Ski.0.Local_SkiConditions.1')
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
scmtRemove('Config.1.Core2Spanish.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Forecast en Espanol'
d.packageFlavor = 1
d.shortPackageTitle = 'ESPANOL'
dsm.set('Config.1.Core2Spanish.0', d, 0, 1)
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
d.packageFlavor = 4
d.shortPackageTitle = 'INTERNATIONAL'
dsm.set('Config.1.International.0', d, 0, 1)
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
scmtRemove('Config.1.Core4Spanish.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Forecast en Espanol'
d.packageFlavor = 1
d.shortPackageTitle = 'ESPANOL'
dsm.set('Config.1.Core4Spanish.0', d, 0, 1)
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
d.shortPackageTitle = 'LOCAL RADAR'
dsm.set('Config.1.Core5.0', d, 0, 1)
scmtRemove('Config.1.Core4.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'KANSAS CITY'
dsm.set('Config.1.Core4.0', d, 0, 1)
scmtRemove('Config.1.Core3.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'KANSAS CITY'
dsm.set('Config.1.Core3.0', d, 0, 1)
scmtRemove('Config.1.Travel.1')
d = twc.Data()
d.bkgImage = 'travel_bg'
d.packageTitle = 'Travel Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'TRAVEL'
dsm.set('Config.1.Travel.1', d, 0, 1)
scmtRemove('Config.1.Core2.0')
d = twc.Data()
d.bkgImage = 'core_bg'
d.packageTitle = 'Your Local Forecast'
d.packageFlavor = 1
d.shortPackageTitle = 'KANSAS CITY'
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
d.shortPackageTitle = 'KANSAS CITY'
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
d.activeLocal_TrafficOverview = 0
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
d.packageFlavor = 4
d.shortPackageTitle = 'HEALTH'
dsm.set('Config.1.Health.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core3.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.1.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Health.0.Local_HealthForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
d.elementDurationShort = 6
dsm.set('Config.1.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.SevereCore2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.SevereCore1A.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City'
d.coopId = '72446011'
dsm.set('Config.1.Core2Spanish.0.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core3.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Ski.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.SevereCore1B.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.SevereCore1B.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
d.elementDurationLong = 6
dsm.set('Config.1.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446018','T72446027','T72456014','T72446003','T72446032','T72446064','T72446038','T72446022','T72446020','T72446045',]
d.locName = ['Gladstone',' Independence',' Lawrence',' Leavenworth',' Leawood',' Lee`s Summit',' Olathe',' Overland Park',' Shawnee',' Spring Hill',]
dsm.set('Config.1.CityTicker_LocalCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['STL','SFO','SEA','IAD',]
d.obsStation = ['T72434000','T72494000','T72793000','T72403000',]
d.locName = ['St. Louis - Lambert','San Francisco Int`l','Seattle - Tacoma Int`l','Wash. - Dulles Arpt.',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.3', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LGA','PHL','PHX','DEN',]
d.obsStation = ['T72503000','T72408000','T72278000','T72572000',]
d.locName = ['New York LaGuardia','Philadelphia Int`l','Phoenix - Sky Harbor','Denver Int`l Arpt',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.2', d, 0, 1)
#
d = twc.Data()
d.airportId = ['LAX','MEM','MIA','MSP',]
d.obsStation = ['T72295000','T72334000','T72202000','T72658000',]
d.locName = ['Los Angeles Int`l','Memphis Int`l Arpt','Miami Int`l Airport','Minn. - St. Paul Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Kansas City Area'
d.coopId = '72446011'
d.maxPageDuration = 14
dsm.set('Config.1.Core3.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City'
d.coopId = '72446011'
dsm.set('Config.1.Core2Spanish.0.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['ATL','BOS','ORD','DFW',]
d.obsStation = ['T72219000','T72509000','T72530000','T72259000',]
d.locName = ['Atlanta Hartsfield-Jackson','Boston Logan Airport','Chicago O`Hare Arpt.','Dallas - Ft. Worth Int`l',]
dsm.set('Config.1.Airport.0.Local_NationalAirportConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
d.elementDurationLong = 6
dsm.set('Config.1.Core2Spanish.0.Cc_LongCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.SevereCore1B.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core4.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.Core2.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City'
d.coopId = '72446011'
dsm.set('Config.1.Core2Spanish.0.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72546000','T72456037','T74542057','T72340004','T72550000','T72455009','T72434000','T72449000','T72356006','T72450000',]
d.locName = ['Des Moines',' Emporia',' Fort Scott',' Little Rock',' Omaha',' Manhattan',' St. Louis',' St. Joseph',' Tulsa',' Wichita',]
dsm.set('Config.1.CityTicker_TravelCitiesCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = 'T72446011'
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Health.0.Local_UltravioletIndex.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core5.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Fcst_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1A.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core2.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Kansas City Area'
d.coopId = '72446011'
d.maxPageDuration = 14
dsm.set('Config.1.SevereCore1A.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'Kansas City Area'
d.coopId = '72446011'
d.maxPageDuration = 14
dsm.set('Config.1.Core1.0.Local_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.summerFlag = 0
dsm.set('Config.1.Health.0.Local_SunSafetyFacts.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Gladstone',' Independence',' Lawrence',' Leavenworth',' Leawood',' Lee`s Summit',' Olathe',' Overland Park',' Shawnee',' Spring Hill',]
d.coopId = ['72446018','72446027','72456014','72446003','72446032','72446064','72446038','72446022','72446020','72446045',]
dsm.set('Config.1.CityTicker_LocalCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.SevereCore1A.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'ski_intro_bg'
dsm.set('Config.1.Ski.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core2Spanish.0.Local_ExtendedForecastSpanish.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core2Spanish.0.Local_CurrentConditionsSpanish.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.SevereCore1A.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Park City Mountain Resort, UT','Jackson Hole, WY','Taos Ski Valley, NM',]
d.skiId = ['314','191','454',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.3', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446038','T72446022','T72449000','T72456000',]
d.locName = ['Olathe','Overland Park','St. Joseph','Topeka',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Health.0.Local_OutdoorActivityForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.Core1.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Copper Mountain Resort, CO','Keystone, CO','Telluride, CO',]
d.skiId = ['113','197','456',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446027','T72456014','T72446032','T72446020',]
d.locName = ['Independence','Lawrence','Leawood','Shawnee',]
dsm.set('Config.1.SevereCore1A.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core2Spanish.0.Local_MenuBoardSpanish.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Winter Park Resort, CO','Crested Butte Mountain, CO','Steamboat, CO',]
d.skiId = ['507','120','425',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.1', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Fcst_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core4Spanish.0.Local_ExtendedForecastSpanish.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Des Moines',' Emporia',' Fort Scott',' Little Rock',' Omaha',' Manhattan',' St. Louis',' St. Joseph',' Tulsa',' Wichita',]
d.coopId = ['72546000','72456037','74542057','72340004','72550000','72455009','72434000','72449000','72356006','72450000',]
dsm.set('Config.1.CityTicker_TravelCitiesForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Fcst_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.Core4.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Breckenridge, CO','Vail, CO','Aspen / Snowmass, CO',]
d.skiId = ['77','482','25',]
dsm.set('Config.1.Ski.0.Local_SkiConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4Spanish.0.Local_MenuBoardSpanish.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core4.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Univ. of Nebraska','University of Iowa','Univ. of Oklahoma',]
d.coopId = ['72551000','72545015','72357000',]
dsm.set('Config.1.Travel.0.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.locName = ['Missouri State U.','U. of MO-Columbia ','NW MO State U.',]
d.coopId = ['72440000','72445000','72449017',]
dsm.set('Config.1.Travel.0.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
d.elementDurationShort = 6
dsm.set('Config.1.Core2Spanish.0.Cc_ShortCurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'neighborhood_bg'
dsm.set('Config.1.Core1.0.Local_MenuBoard.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446038','T72446022','T72449000','T72456000',]
d.locName = ['Olathe','Overland Park','St. Joseph','Topeka',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['Univ. of Kansas','Kansas State Univ.','Pittsburg State U.',]
d.coopId = ['72456014','72455004','74542046',]
dsm.set('Config.1.Travel.0.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore1B.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.SevereCore1B.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core1.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446027','T72456014','T72446032','T72446020',]
d.locName = ['Independence','Lawrence','Leawood','Shawnee',]
dsm.set('Config.1.Core1.0.Local_LocalObservations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core2Spanish.0.Local_DaypartForecastSpanish.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core4.0.Local_CurrentConditions.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City'
d.bkgImage = 'neighborhood_bg'
d.affiliateName = 'Consolidated Communications'
dsm.set('Config.1.Core1.0.Local_NetworkIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Disney World, FL','Las Vegas, NV','Washington, DC',]
d.coopId = ['72205000','72386000','72405000',]
dsm.set('Config.1.Travel.1.Local_Destinations.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T72446011','KMKC',]
d.locName = ['Kansas City','Kansas City',]
dsm.set('Config.1.Core4Spanish.0.Local_CurrentConditionsSpanish.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Lawrence, KS','Perry Lake, KS','Paola, KS',]
d.coopId = ['72456014','72456005','72446056',]
dsm.set('Config.1.Travel.1.Local_Destinations.1', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'airport_intro_bg'
dsm.set('Config.1.Airport.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.climId = '234359'
d.latitude = 39.1167
d.longitude = -94.6
d.locName = 'Kansas City'
d.coopId = '72446011'
dsm.set('Config.1.Core1.0.Local_Almanac.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core1.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = ['Osage Beach, MO','Branson, MO','Warsaw, MO',]
d.coopId = ['74550021','72440034','74550031',]
dsm.set('Config.1.Travel.1.Local_Destinations.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core4.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core2.0.Local_ExtendedForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core4Spanish.0.Local_DaypartForecastSpanish.0', d, 0, 1)
#
d = twc.Data()
d.locName = ' '
dsm.set('Config.1.SevereCore2.0.Local_SevereWeatherMessage.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Kansas City Area'
d.coopId = '72446011'
dsm.set('Config.1.Core2.0.Local_DaypartForecast.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'travel_intro_bg'
dsm.set('Config.1.Travel.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Johnson County Area'
d.zone = 'KSZ105'
dsm.set('Config.1.Core3.0.Local_WeatherBulletin.0', d, 0, 1)
#
d = twc.Data()
d.activeVocalCue = 1
dsm.set('Config.1.Core2Spanish.0.Local_LocalDopplerSpanish.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'ICT'
d.obsStation = 'T72450000'
d.locName = 'Wichita Mid-Continent Airport'
dsm.set('Config.1.Airport.0.Local_LocalAirportConditions.1', d, 0, 1)
#
d = twc.Data()
d.promoText = ['For more on weather and your health','tune to The Weather Channel or','go to weather.com/health',]
d.promoImage = 'health_promo'
d.promoLogo = 'blankLogo'
dsm.set('Config.1.Health.0.Local_Promo.0', d, 0, 1)
#
d = twc.Data()
d.airportId = ['MKC','MCI',]
d.obsStation = ['T72446011','T72446000',]
d.locName = ['Wheeler Downtown Airport','   Kansas City Int`l Airport',]
dsm.set('Config.1.CityTicker_AirportDelays.0', d, 0, 1)
#
d = twc.Data()
d.bkgImage = 'health_intro_bg'
dsm.set('Config.1.Health.0.Local_PackageIntro.0', d, 0, 1)
#
d = twc.Data()
d.airportId = 'MCI'
d.obsStation = 'T72446000'
d.locName = 'Kansas City International Airport'
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
# Finished generation on Tue Jan 11 15:57:30 GMT 2022

import os; os.system("cd /twc/data/clock; tar -xvf /twc/data/clock/clocks.tar");ds.commit();wxdata.loadClock();