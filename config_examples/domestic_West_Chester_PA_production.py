# Created on Tue Dec 18 12:10:47 EST 2007
Log.info('scmt config started')
# EXP: 1391
# VIW: 12640
# CLN: 17105
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
dsm.set('scmt_configType', 'domestic',0)
dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)
#
# MAP: 73592
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(30036,11814),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(140,96),
             datacutType='radar.us',
             datacutCoordinate=(3280,1110),
             datacutSize=(176,100),
             dataFinalSize=(240,137),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Radar_LocalDoppler', d, 0)
#
# Radar_LocalDoppler (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (143,60),),
                ( (135,98),),
                ( (169,38),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (143,60),),
                ( (135,98),),
                ( (169,38),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (79,73),'Coatesville',),
                ( (139,111),'Reading',),
                ( (139,25),'Wilmington',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (79,73),'Coatesville',),
                ( (139,111),'Reading',),
                ( (139,25),'Wilmington',),
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
dsm.set('Config.1.Radar_LocalDoppler', d, 0)
# MAP: 51134
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(30266,11754),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(140,112),
             datacutType='radar.us',
             datacutCoordinate=(3308,1102),
             datacutSize=(176,118),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroDopplerRadar', d, 0)
#
# Local_MetroDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (197,300),'76',),
                ( (428,333),'476',),
                ( (229,102),'95',),
                ( (84,140),'83',),
                ( (89,342),'81',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (518,101),'55',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (428,333),'476',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (518,101),'55',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (390,185),'202',),
                ( (222,227),'30',),
                ( (361,293),'422',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (390,185),'202',),
                ( (222,227),'30',),
                ( (361,293),'422',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (197,300),'76',),
                ( (229,102),'95',),
                ( (84,140),'83',),
                ( (89,342),'81',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (473,186),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (324,222),),
                ( (351,186),),
                ( (191,244),),
                ( (402,272),),
                ( (299,338),),
                ( (380,220),),
                ( (606,308),),
                ( (402,156),),
                ( (499,213),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (324,222),),
                ( (351,186),),
                ( (191,244),),
                ( (402,272),),
                ( (299,338),),
                ( (380,220),),
                ( (606,308),),
                ( (402,156),),
                ( (499,213),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (473,186),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (213,214),'Coatesville',),
                ( (201,174),'Kennett Square',),
                ( (87,247),'Lancaster',),
                ( (419,290),'Phoenixville',),
                ( (267,359),'Reading',),
                ( (397,238),'West Chester',),
                ( (575,329),'Trenton',),
                ( (419,142),'Wilmington',),
                ( (503,196),'Philadelphia',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (213,214),'Coatesville',),
                ( (201,174),'Kennett Square',),
                ( (87,247),'Lancaster',),
                ( (419,290),'Phoenixville',),
                ( (267,359),'Reading',),
                ( (397,238),'West Chester',),
                ( (575,329),'Trenton',),
                ( (419,142),'Wilmington',),
                ( (503,196),'Philadelphia',),
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
dsm.set('Config.1.Local_MetroDopplerRadar', d, 0)
# MAP: 71758
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4186,1672),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(1375,925),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1258,517),
             datacutSize=(740,496),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Local_RadarSatelliteComposite', d, 0)
#
# Local_RadarSatelliteComposite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RadarSatelliteComposite', d, 0)
# MAP: 76010
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(30216,11730),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(140,112),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (290,231),'30',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (472,299),'476',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (529,137),'55',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (390,305),'422',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (107,178),'83',),
                ( (290,125),'95',),
                ( (218,308),'76',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplane',0,1,0,),
              ( ( (498,198),),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72408000',(529,227),),
                ( 'T72408113',(372,235),),
                ( 'T72408135',(393,130),),
                ( 'T72517076',(537,333),),
                ( 'T72517100',(309,345),),
                ( 'T74002024',(218,120),),
                ( 'T74002070',(215,228),),
                ( 'T74002111',(101,324),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72408000',(532,191),),
                ( 'T72408113',(375,199),),
                ( 'T72408135',(396,94),),
                ( 'T72517076',(540,297),),
                ( 'T72517100',(312,309),),
                ( 'T74002024',(221,84),),
                ( 'T74002070',(218,192),),
                ( 'T74002111',(104,288),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (468,263),'Philadelphia',),
                ( (302,271),'West Chester',),
                ( (337,166),'Wilmington',),
                ( (478,369),'Doylestown',),
                ( (272,381),'Reading',),
                ( (186,156),'Bel Air',),
                ( (165,264),'Lancaster',),
                ( (48,360),'Harrisburg',),
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
dsm.set('Config.1.Local_MetroObservationMap', d, 0)
# MAP: 71848
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(30216,11730),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(140,112),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (290,231),'30',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (472,299),'476',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (529,137),'55',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (390,305),'422',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (107,178),'83',),
                ( (290,125),'95',),
                ( (218,308),'76',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72408000',(532,191),),
                ( '72408113',(375,199),),
                ( '72408135',(396,94),),
                ( '72517076',(540,297),),
                ( '72517100',(312,309),),
                ( '74002024',(221,84),),
                ( '74002070',(218,192),),
                ( '74002111',(104,288),),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplane',0,1,0,),
              ( ( (498,198),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72408000',(529,227),),
                ( '72408113',(372,235),),
                ( '72408135',(393,130),),
                ( '72517076',(537,333),),
                ( '72517100',(309,345),),
                ( '74002024',(218,120),),
                ( '74002070',(215,228),),
                ( '74002111',(101,324),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (468,263),'Philadelphia',),
                ( (302,271),'West Chester',),
                ( (337,166),'Wilmington',),
                ( (478,369),'Doylestown',),
                ( (272,381),'Reading',),
                ( (186,156),'Bel Air',),
                ( (165,264),'Lancaster',),
                ( (48,360),'Harrisburg',),
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
dsm.set('Config.1.Local_MetroForecastMap', d, 0)
# MAP: 48099
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27630,10314),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(572,458),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalForecastMap', d, 0)
#
# Local_RegionalForecastMap (PRODUCT DATA)
#
d = twc.Data(
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72405000',(308,111),),
                ( '72407012',(520,130),),
                ( '72408000',(402,201),),
                ( '72417000',(144,107),),
                ( '72503004',(541,256),),
                ( '72513000',(378,300),),
                ( '72520000',(136,215),),
                ( '72523075',(226,294),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72405000',(305,147),),
                ( '72407012',(517,166),),
                ( '72408000',(399,237),),
                ( '72417000',(141,143),),
                ( '72503004',(538,292),),
                ( '72513000',(375,336),),
                ( '72520000',(133,251),),
                ( '72523075',(223,330),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (246,183),'Washington, DC',),
                ( (477,200),'Atlantic City',),
                ( (338,273),'Philadelphia',),
                ( (114,179),'Elkins',),
                ( (491,328),'New York',),
                ( (331,372),'Scranton',),
                ( (87,288),'Pittsburgh',),
                ( (182,366),'Bradford',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 50663
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(27630,10314),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(572,458),
             vectors=['mercator.us.states.vg','mercator.us.coastlines.vg',],
)
wxdata.setMapData('Config.1.Local_RegionalObservationMap', d, 0)
#
# Local_RegionalObservationMap (PRODUCT DATA)
#
d = twc.Data(
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72405000',(305,147),),
                ( 'T72407012',(517,166),),
                ( 'T72408000',(399,237),),
                ( 'T72417000',(141,143),),
                ( 'T72503000',(538,292),),
                ( 'T72513000',(375,336),),
                ( 'T72520000',(133,251),),
                ( 'T72523075',(223,330),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72405000',(308,111),),
                ( 'T72407012',(520,130),),
                ( 'T72408000',(402,201),),
                ( 'T72417000',(144,107),),
                ( 'T72503000',(541,256),),
                ( 'T72513000',(378,300),),
                ( 'T72520000',(136,215),),
                ( 'T72523075',(226,294),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (246,183),'Washington, DC',),
                ( (477,200),'Atlantic City',),
                ( (338,273),'Philadelphia',),
                ( (114,179),'Elkins',),
                ( (491,328),'New York',),
                ( (331,372),'Scranton',),
                ( (87,288),'Pittsburgh',),
                ( (182,366),'Bradford',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 71822
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4477,1265),
             mapcutSize=(1905,1270),
             mapFinalSize=(720,480),
             mapMilesSize=(1766,1188),
             datacutType='satellite.us',
             datacutCoordinate=(1181,391),
             datacutSize=(512,341),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.Local_Satellite', d, 0)
#
# Local_Satellite (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDot',0,2,0,),
              ( ( (181,268),),
                ( (232,179),),
                ( (231,328),),
                ( (149,99),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (60,271),'Washington',),
                ( (83,185),'Cape Hatteras',),
                ( (127,336),'New York',),
                ( (72,125),'Charleston',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_Satellite', d, 0)
# MAP: 50938
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(29366,11203),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(304,243),
             datacutType='radar.us',
             datacutCoordinate=(3198,1035),
             datacutSize=(382,255),
             dataFinalSize=(720,480),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
             prodActiveVocalCue=1,
)
wxdata.setMapData('Config.1.Local_RegionalDopplerRadar', d, 0)
#
# Local_RegionalDopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (318,340),'81',),
                ( (237,170),'83',),
                ( (66,228),'76',),
                ( (517,283),'95',),
                ( (274,254),'76',),
                ( (395,278),'476',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (437,154),'55',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (395,278),'476',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (437,154),'55',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (318,340),'81',),
                ( (237,170),'83',),
                ( (66,228),'76',),
                ( (517,283),'95',),
                ( (274,254),'76',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (200,87),),
                ( (353,223),),
                ( (522,146),),
                ( (581,330),),
                ( (96,333),),
                ( (396,311),),
                ( (434,218),),
                ( (220,266),),
                ( (251,140),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (200,87),),
                ( (353,223),),
                ( (522,146),),
                ( (581,330),),
                ( (96,333),),
                ( (396,311),),
                ( (434,218),),
                ( (220,266),),
                ( (251,140),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (220,101),'Washington, DC',),
                ( (306,244),'Coatesville',),
                ( (466,129),'Atlantic City',),
                ( (433,333),'New York City',),
                ( (116,347),'State College',),
                ( (292,314),'Allentown',),
                ( (454,221),'Philadelphia',),
                ( (108,269),'Harrisburg',),
                ( (271,154),'Baltimore',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (220,101),'Washington, DC',),
                ( (306,244),'Coatesville',),
                ( (466,129),'Atlantic City',),
                ( (433,333),'New York City',),
                ( (116,347),'State College',),
                ( (292,314),'Allentown',),
                ( (454,221),'Philadelphia',),
                ( (108,269),'Harrisburg',),
                ( (271,154),'Baltimore',),
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
dsm.set('Config.1.Local_RegionalDopplerRadar', d, 0)
#
wxdata.setInterestList('lambert.us','1',['satellite.us','radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite',])
wxdata.setInterestList('satellite.us.cuts','1',['Config.1.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['BWI','EWR','PHL',])
wxdata.setInterestList('coopId','1',['72405000','72407000','72407012','72408000','72408113','72408135','72417000','72503004','72513000','72513039','72517000','72517076','72517078','72517100','72517102','72518089','72520000','72523075','74002024','74002070','74002111',])
wxdata.setInterestList('pollenId','1',['PHL',])
wxdata.setInterestList('indexId','1',['KILG',])
wxdata.setInterestList('obsStation','1',['KNXX','KPHL','T72405000','T72406000','T72407012','T72408000','T72408098','T72408113','T72408135','T72408162','T72408172','T72408173','T72417000','T72502000','T72503000','T72513000','T72517076','T72517083','T72517100','T72520000','T72523075','T74002024','T74002051','T74002070','T74002111',])
wxdata.setInterestList('climId','1',['361591','366889',])
wxdata.setInterestList('metroId','1',['2',])
wxdata.setInterestList('zone','1',['PAZ067',])
wxdata.setInterestList('aq','1',['pa002',])
wxdata.setInterestList('skiId','1',['717003','717008',])
wxdata.setInterestList('county','1',['PAC029','PAC045','PAC071',])
dsm.set('Config.1.countyNameList',[('PAC029','Chester'),('PAC045','Delaware'),('PAC071','Lancaster'),], 0)
#
dsm.set('dmaCode','504', 0)
dsm.set('secondaryObsStation','KPHL', 0)
dsm.set('primaryClimoStation','361591', 0)
dsm.set('primaryIndexId','KILG', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','PA', 0)
dsm.set('primaryAqStation','pa002', 0)
dsm.set('primPollenSiteName','Philadelphia', 0)
dsm.set('expRev','1966619', 0)
dsm.set('primaryCoopId','72408113', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','PHL', 0)
dsm.set('primaryCounty','PAC029', 0)
dsm.set('primaryObsStation','T72408113', 0)
dsm.set('primaryLat',40.02333, 0)
dsm.set('hasTraffic',1, 0)
dsm.set('primaryPollenStation','PHL', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-75.81278, 0)
dsm.set('primaryForecastName','West Chester-Coatesville Areas', 0)
dsm.set('primaryZone','PAZ067', 0)
dsm.set('climoRegion','1', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST CABLE COMMUNICATIONS', 0)
dsm.set('headendId','021867', 0)
dsm.set('msoName','COMCAST COMMUNICATIONS', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST CABLE COMMUNICATIONS', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - COATESVILLE - DOM', 0)
dsm.set('affiliateNumber','00493', 0)
dsm.set('zipCode','19320', 0)
dsm.set('Config.1.bcNetMask','255.255.255.224', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD09050081', 0)
dsm.set('Config.1.bcExtIpAddress','172.20.3.112', 0)
dsm.set('Config.1.bcGateWay','192.168.66.129', 0)
dsm.set('Config.1.bcIpAddress','192.168.66.150', 0)
#
wxdata.setTimeZone('EST5EDT')
#
# BLOCK BEGIN
d = twc.Data()
dsm.set('Config.1.Override', d, 0)
d = twc.Data()
d.activeVocal = 1
dsm.set('Config.1.Bulletin_Default', d, 0)
# BLOCK END
#
d = twc.Data()
d.sponsorLogo = ''
dsm.set('Config.1', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = ['PHL','EWR','BWI',]
d.airportLocName = ['Philadelphia','Newark','Balt/Wash Intl.',]
d.obsStation = ['T72408000','T72502000','T72406000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['717003','717008',]
d.coopId = ['72517078','72517102',]
d.resortName = ['Camelback, PA','Shawnee Mtn, PA',]
dsm.set('Config.1.Tag.General.snowboardData', d, 0, 1)
#
#
#  Non Image Maps
#
d = [
'Config.1.Local_MetroForecastMap',
'Config.1.Local_MetroObservationMap',
'Config.1.Local_RegionalForecastMap',
'Config.1.Local_RegionalObservationMap',
]
dsm.set('Config.1.nonImageMaps', d, 0)
#

#
scmtRemove('Config.1.VocalLocalSchedule')
d = twc.Data()
d.OffTimes = ( )
dsm.set('Config.1.VocalLocalSchedule', d, 0, 1)
#
scmtRemove('Config.1.Ldl_LASCrawl')
scmtRemove('Config.1.LASCrawl')
#
d = twc.Data()
d.serialNum=423951
d.crawls=[
(1173762000,1205211599,[(0,23)],'NEED A LARGER DRIVEWAY? CALL DREXEL PAVING FOR A FREE ESTIMATE. 610-436-8921. DREXEL PAVING INSTALLS,ENLARGES AND RESURFACES DRIVEWAYS. IF YOU\'RE A HOMEOWNER WHO CARES ABOUT QUALITY, CALL THE CO. WITH 40  YEARS EXPERIENCE.DREXEL PAVING,610-436-8921.DREXEL PAVING 610-436-8921'),
(1186542000,1513400399,[(0,23)],'SHOPPING FOR A NEW OR USED CAR? GO TO WWW.VEHIX.COM SHOP BY ZIPCODE-MAKE-MODEL-YEAR-PRICE-OR BY DEALER USE WWW.VEHIX.COM TO SEE JD POWER VIDEO BUYING GUIDES USE VEHIX-TV TO TAKE A VIRTUAL TEST DRIVE WWW.VEHIX.COM FOR ALL OF YOUR NEW AND USED CAR BUYING NEEDS WWW.VEHIX.COM'),
(1187578800,1199163599,[(0,23)],'BUSINESS OWNERS! IF YOU ARE READING THIS, SO ARE YOUR POTENTIAL CUSTOMERS! FIND OUT ABOUT THE MANY AFFORDABLE AND EFFICIENT WAYS COMCAST CABLE TV EFFECTIVELY REACHES YOUR CUSTOMERS IN CHESTER COUNTY LET US HELP YOU GROW YOUR BUSINESS! CALL BOB LATULIPPE AT 610-240-0811 TODAY!'),
(1197867600,1513400399,[(0,23)],'VALUE DRY BASEMENT WATERPROOFING 886-32-VALUE. DRY BASEMENTS - GUARANTEED! LIFETIME WARRANTY AND OVER 20 YEARS OF BASEMENT WATERPROOFING EXPERIENCE, CALL VALUE DRY 866-32-VALUE FOR A FREE EVALUATION. VISIT WWW.VALUEDRY.COM FOR $300 OFF YOUR WET BASEMENT!'),
(1196053200,1198558799,[(0,23)],'NEED FAST CASH? CAR TITLE LOANS IN 10 MINUTES-NO CREDIT CHECK! 0% APR FIRST TIME! LOWEST RATES IN DE. CALL 302-995-1400 WILMINGTON. NEED FAST CASH? CAR TITLE LOANS IN 10 MINUTES-NO CREDIT CHECK! 0% AP RATES IN DE, CALL 302-995-1400 WILMINGTON.'),
(1197867600,1513400399,[(0,23)],'HALY OIL + GREAT VALLEY PROPANE 610-251-0342 WWW.HALYOIL.COM HEATING OIL + PROPANE DELIVERY NOW OFFERING DUAL FUEL DISCOUNTS UP TO .10CENTS OFF PER GALLON!!KEEPING CHESTER CO. WARM FOR OVER 20 YEARS!!VISIT US @ WWW.HALYOIL.COM OR CALL 610-251-0341! HALY OIL + GREAT VALLEY PROPANE'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.Local_TextForecast')
scmtRemove('Config.1.Ldl_NationalStarIDMessage')
scmtRemove('Config.1.Local_GetawayForecast')
scmtRemove('Config.1.Local_7DayForecast')
scmtRemove('Config.1.Local_SchoolDayWeather')
scmtRemove('Config.1.Local_Almanac')
scmtRemove('Config.1.Ldl_UVForecast')
scmtRemove('Config.1.Local_DaypartForecast')
scmtRemove('Config.1.Ldl_ExtendedForecast')
scmtRemove('Config.1.Local_Tides')
scmtRemove('Config.1.Local_HeatSafetyTips')
scmtRemove('Config.1.Local_CurrentConditions')
scmtRemove('Config.1.Ldl_CurrentApparentTemp')
scmtRemove('Config.1.Fcst_ExtendedForecast')
scmtRemove('Config.1.Local_Climatology')
scmtRemove('Config.1.Local_LocalObservations')
scmtRemove('Config.1.Local_EventForecast')
scmtRemove('Config.1.Local_TrafficOverview')
scmtRemove('Config.1.Cc_CurrentConditions')
scmtRemove('Config.1.Local_ExtendedForecast')
scmtRemove('Config.1.Local_AirQualityForecast')
scmtRemove('Config.1.Local_TrafficReport')
scmtRemove('Config.1.Local_TrafficFlow')
scmtRemove('Config.1.Ldl_SunriseSunset')
scmtRemove('Config.1.Ldl_TravelForecast')
scmtRemove('Config.1.Fcst_TextForecast')
scmtRemove('Config.1.Local_RecordHighLow')
scmtRemove('Config.1.Ldl_AirQualityForecast')
scmtRemove('Config.1.Fcst_DaypartForecast')
scmtRemove('Config.1.Local_OutdoorActivityForecast')
scmtRemove('Config.1.Local_MarineForecast')
scmtRemove('Config.1.Ldl_CurrentMTDPrecip')
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.Ldl_LocalStarIDMessage')
scmtRemove('Config.1.TimeTemp_Default')
scmtRemove('Config.1.Ldl_HurricaneWatch')
scmtRemove('Config.1.Ldl_AirportDelayConditions')
scmtRemove('Config.1.Local_NWSHeadlines')
#
d = twc.Data()
d.trafficReverseActive = [1,1,1,1,1,1,]
d.periodBStartTime = '12:00'
d.activeVocalCue = 0
d.periodAStartTime = '00:00'
d.trafficFlowRoute = ['92257-2','92283-2','92268-2','92266-2','92295-2','92210-2',]
d.trafficReverseRoute = ['92256-2','92284-2','92269-2','92267-2','92295-2','92211-2',]
d.routes=[[
             (('2.92257','EB, Harrisburg E. to NJ Tpk Connector Brg','paTurnpikeSign','',(212,212,212,255),1),('2.92256','WB, NJ Tpk Connector Brg to Harrisburg E.','paTurnpikeSign','',(212,212,212,255),1,)),
             (('2.92283','NB, RT-30 to I-76','usHighwaySignLarge','202',(20,20,20,255),1),('2.92284','SB, I-76 to RT-30','usHighwaySignLarge','202',(20,20,20,255),1,)),
             (('2.92268','EB, PA Tpk Toll Plaza to I-476 Blue Route','interstateHighwaySignLarge','76',(212,212,212,255),1),('2.92269','WB, I-476/Blue Route to PA Tpk Toll Plaza','interstateHighwaySignLarge','76',(212,212,212,255),1,)),
],[
             (('2.92266','SB, Schuylkill Exwy to I-95','interstateHighwaySignLarge','476',(212,212,212,255),1),('2.92267','NB, I-95 to Schuylkill Exwy','interstateHighwaySignLarge','476',(212,212,212,255),1,)),
             (('2.92295','Schuylkill Exwy EB, Rt 23 to US 1','interstateHighwaySignLarge','76',(212,212,212,255),1),('2.92295','Schuylkill Exwy EB, Rt 23 to US 1','interstateHighwaySignLarge','76',(212,212,212,255),1,)),
             (('2.92210','EB, PA Turnpike to Walt Whitman Bridge','interstateHighwaySignLarge','76',(212,212,212,255),1),('2.92211','WB, Walt Whitman Bridge to PA Turnpike','interstateHighwaySignLarge','76',(212,212,212,255),1,)),
],
]
d.routeDisplayTime=[
             ((0,0),(11,59)),
             ((12,0),(23,59)),
]
dsm.set('Config.1.Local_TrafficFlow', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'West Chester-Coatesville Areas'
d.coopId = '72408113'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72408162','T72408172','T72408173','T72408098','T74002051','T72408000','T72517083','T72408135',]
d.locName = ['Coatesville','Drexel Hill','King of Prussia','Malvern','Parkesburg','Philadelphia','Pottstown','Wilmington',]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.crawlRate = 3
dsm.set('Config.1.Ldl_HurricaneWatch', d, 0, 1)
#
#
d = twc.Data()
d.climId = '361591'
d.latitude = 39.9833
d.longitude = -75.8667
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Philadelphia','Allentown','Harrisburg',]
d.coopId = ['72408000','72517000','74002111',]
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72408113','KPHL',]
d.locName = ['West Chester','Philadelphia',]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Philadelphia area',]
d.actionDayPhrase = 'Air Quality Action Day'
d.aq = ['pa002',]
dsm.set('Config.1.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.trafficActive = 1
d.trafficReverseActive = [1,1,1,1,1,1,]
d.trafficFlowRoute = ['92257-2','92283-2','92268-2','92266-2','92295-2','92210-2',]
d.trafficReverseRoute = ['92256-2','92284-2','92269-2','92267-2','92295-2','92211-2',]
d.routes=[
             (('2.92257','PA Tpk','EB','Harrisburg E.','New Jersey Tpk Connector Brg',),
             ('2.92256','PA Tpk','WB','New Jersey Tpk Connector Brg','Harrisburg E.',)),
             (('2.92283','US-202','NB','RT-30','I-76',),
             ('2.92284','US-202','SB','I-76','RT-30',)),
             (('2.92268','I-76','EB','PA Tpk Toll Plaza','I-476/Blue Route',),
             ('2.92269','I-76','WB','I-476/Blue Route','PA Tpk Toll Plaza',)),
             (('2.92266','I-476/Blue Route','SB','Schuylkill Exwy','I-95',),
             ('2.92267','I-476/Blue Route','NB','I-95','Schuylkill Exwy',)),
             (('2.92295','I-76/Schuylkill Exwy','EB','Rt  23,Conshohocken','US 1, Roosevelt Blvd',),
             ('2.92295','I-76/Schuylkill Exwy','EB','Rt  23,Conshohocken','US 1, Roosevelt Blvd',)),
             (('2.92210','I-76','EB','PA Tpk Tolls','Walt Whitman Brg ',),
             ('2.92211','I-76','WB','Walt Whitman Brg ','PA Tpk Tolls',)),
]
d.routeDisplayTime=[
(             ((0,00),(0,59),1,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,1),
             ((1,00),(1,59),0,1),
             ((2,00),(2,59),0,1),
             ((3,00),(3,59),0,1),
             ((4,00),(4,59),0,1),
             ((5,00),(5,59),0,0),
             ((6,00),(6,59),0,0),
             ((7,00),(7,59),0,0),
             ((8,00),(8,59),0,0),
             ((9,00),(9,59),0,0),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),1,1),
             ((14,00),(14,59),1,1),
             ((15,00),(15,59),1,0),
             ((16,00),(16,59),1,0),
             ((17,00),(17,59),1,0),
             ((18,00),(18,59),1,0),
             ((19,00),(19,59),1,0),
             ((20,00),(20,59),1,0),
             ((21,00),(21,59),1,1),
             ((22,00),(22,59),1,1),
             ((23,00),(23,59),1,1),
),
(             ((0,00),(0,59),0,2),
             ((1,00),(1,59),0,2),
             ((2,00),(2,59),0,2),
             ((3,00),(3,59),0,2),
             ((4,00),(4,59),0,2),
             ((5,00),(5,59),0,2),
             ((6,00),(6,59),0,2),
             ((7,00),(7,59),0,1),
             ((8,00),(8,59),0,1),
             ((9,00),(9,59),0,1),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),0,1),
             ((14,00),(14,59),0,1),
             ((15,00),(15,59),0,1),
             ((16,00),(16,59),0,1),
             ((17,00),(17,59),0,1),
             ((18,00),(18,59),0,1),
             ((19,00),(19,59),0,1),
             ((20,00),(20,59),0,1),
             ((21,00),(21,59),0,2),
             ((22,00),(22,59),0,2),
             ((23,00),(23,59),0,2),
),
(             ((0,00),(0,59),0,2),
             ((1,00),(1,59),0,2),
             ((2,00),(2,59),0,2),
             ((3,00),(3,59),0,2),
             ((4,00),(4,59),0,2),
             ((5,00),(5,59),0,2),
             ((6,00),(6,59),0,2),
             ((7,00),(7,59),0,1),
             ((8,00),(8,59),0,1),
             ((9,00),(9,59),0,1),
             ((10,00),(10,59),0,1),
             ((11,00),(11,59),0,1),
             ((12,00),(12,59),0,1),
             ((13,00),(13,59),0,1),
             ((14,00),(14,59),0,1),
             ((15,00),(15,59),0,1),
             ((16,00),(16,59),0,1),
             ((17,00),(17,59),0,1),
             ((18,00),(18,59),0,1),
             ((19,00),(19,59),0,1),
             ((20,00),(20,59),0,1),
             ((21,00),(21,59),0,2),
             ((22,00),(22,59),0,2),
             ((23,00),(23,59),0,2),
),
]
dsm.set('Config.1.Ldl_TrafficTripTimes', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'West Chester-Coatesville Areas'
d.coopId = '72408113'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.mapName = ['2.1',]
d.locName = ['PHILADELPHIA AREA',]
d.activeVocalCue = 1
dsm.set('Config.1.Local_TrafficOverview', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_LocalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T72408113'
d.locName = 'WEST CHESTER'
d.heatIndexThreshold = 100
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'PAZ067'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'WEST CHESTER-COATESVILLE AREAS'
d.coopId = '72408113'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'WEST CHESTER-COATESVILLE AREAS'
d.coopId = '72408113'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'PHILADELPHIA AREA'
d.maxPages = 3
d.activeVocalCue = 0
d.metroId=['2',]
d.latLongBoxes=[
             ((-75.7644735895195,39.70101074262176),(-75.38758803988578,40.10434440100171)),
             ((-75.74463750795982,39.99524595242353),(-75.39089405347906,40.36551947487069)),
             ((-75.42766135338539,39.86299751703118),(-75.00273213254007,40.02993399664898)),
]
d.severityList=[
             ('Incident',2,),
             ('Construction',1,),
             ('Unspecified',1,),
]
dsm.set('Config.1.Local_TrafficReport', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_NationalStarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72408113','KPHL',]
d.locName = ['West Chester','WEST CHESTER','PHILADELPHIA',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'WEST CHESTER-COATESVILLE AREAS'
d.coopId = '72408113'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72408113','KPHL',]
d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
d.coopId = '72408113'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.climId = '361591'
d.latitude = 39.9833
d.longitude = -75.8667
dsm.set('Config.1.Ldl_SunriseSunset', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['PHL',]
d.obsStation = ['T72408000',]
d.locName = ['Philadelphia Int\'l',]
d.displayFlag = [1,]
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['WEST CHESTER-COATESVILLE AREAS',]
d.coopId = ['72408113',]
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KPHL',]
d.climId = ['366889',]
d.locName = ['Philadelphia',]
d.coopId = ['72408000',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.1.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72408113','KPHL',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'West Chester'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72408113'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'West Chester'
d.coopId = '72408113'
dsm.set('Config.1.Ldl_ExtendedForecast', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
dsm.set('Config.1.Ldl_Shortcast', d, 0, 1)
dsm.set('Config.1.Ldl_SummaryForecast', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','T72408113','KPHL',]
d.obsLocName = ['West Chester','West Chester','Philadelphia',]
dsm.set('Config.1.Ldl_CurrentApparentTemp', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_CurrentCeiling', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentDewpoint', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentGusts', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentHumidity', d, 0, 1)
ds.commit()
dsm.set('Config.1.Ldl_CurrentPressure', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentSkyTemp', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentVisibility', d, 0, 1)
dsm.set('Config.1.Ldl_CurrentWinds', d, 0, 1)
#
d = twc.Data()
d.locName = 'Philadelphia area'
d.startDate = (1,1)
d.endDate = (12,31)
d.aq = 'pa002'
dsm.set('Config.1.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.url = ['','','',]
d.locNameList = ['Atlantic City, NJ','Catskill Mtns., NY','Pocono Mtns., PA',]
d.coopId = ['72407000','72518089','72513039',]
dsm.set('Config.1.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'West Chester-Coatesville Areas'
d.coopId = '72408113'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72408113'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KPHL','KNXX',]
d.obsLocName = ['Philadelphia','Willow Grove',]
dsm.set('Config.1.Ldl_CurrentMTDPrecip', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KPHL'
d.climId = ['366889',]
d.locName = 'PHILADELPHIA'
d.coopId = '72408000'
dsm.set('Config.1.Local_Climatology', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 0
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 1
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 1
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 1
d.activeLocal_TrafficOverview = 1
d.activeLocal_TrafficReport = 1
# region keys
dsm.set('Config.1.DefaultUS.120.2', d, 0)
dsm.set('Config.1.DefaultUS.60.1', d, 0)
dsm.set('Config.1.DefaultUS.90.1', d, 0)
dsm.set('Config.1.DefaultUS.90.0', d, 0)
dsm.set('Config.1.DefaultUS.60.0', d, 0)
dsm.set('Config.1.DefaultUS.120.1', d, 0)
dsm.set('Config.1.DefaultUS.120.0', d, 0)
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
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
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
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Config.1.Playlist.DefaultUS.60.1', d, 0)
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
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,5,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,8,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Config.1.Playlist.DefaultUS.120.2', d, 0)
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
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
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
('MetroForecastMap.1',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Config.1.Playlist.DefaultUS.60.0', d, 0)
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
('RegionalObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,5,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,7,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,4,6,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Config.1.Playlist.DefaultUS.120.1', d, 0)
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
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.1', d, 0)
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
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,6,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,4,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,5,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,5,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
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
dsm.set('Config.1.Playlist.DefaultUS.120.0', d, 0)
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
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,14,16,10,1,2,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.90.0', d, 0)
ds.commit()
#
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
dsm.set('Config.1.Playlist.Fcst.fcst1', d, 0)
#
ds.commit()
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
dsm.set('Config.1.Playlist.DefaultUS.57.0', d, 0)
#
ds.commit()
#
# End of SCMT deployment
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Tue Dec 18 12:10:50 EST 2007
