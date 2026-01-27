# Created on Tue Sep 29 12:00:49 EDT 2009
Log.info('scmt config started')
# EXP: 1597
# VIW: 12760
# CLN: 663
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
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.Ldl_TrafficReport')
scmtRemove('Config.1.Ldl_Almanac.0')
scmtRemove('Config.1.Ldl_DailyForecast.0')
scmtRemove('Config.1.Ldl_TravelForecast.0')
dsm.set('Scmt.PlatformType', 'IntelliStar', 0)
#Short-cast sound effect
scmtRemove('Config.1.SoundFxSchedule')
d = twc.Data()
d.OffTimes = ((0,23),)
dsm.set('Config.1.SoundFxSchedule', d, 0, 1)
#
#
# MAP: 73375
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18486,7728),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(154,105),
             datacutType='radar.us',
             datacutCoordinate=(1865,609),
             datacutSize=(177,101),
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
              ( ( (117,27),),
                ( (150,61),),
                ( (171,69),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (117,27),),
                ( (150,61),),
                ( (171,69),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (128,27),'Cleburne',),
                ( (83,53),'Grand Prairie',),
                ( (171,86),'Dallas',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (128,27),'Cleburne',),
                ( (83,53),'Grand Prairie',),
                ( (171,86),'Dallas',),
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
# MAP: 51487
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(18712,7666),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(154,123),
             datacutType='radar.us',
             datacutCoordinate=(1893,601),
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
              ( ( (608,203),'20',),
                ( (587,323),'30',),
                ( (440,162),'45',),
                ( (272,159),'35W',),
                ( (338,334),'35E',),
                ( (286,337),'35W',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (272,159),'35W',),
                ( (338,334),'35E',),
                ( (286,337),'35W',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (444,346),'75',),
                ( (213,333),'287',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (444,346),'75',),
                ( (213,333),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (608,203),'20',),
                ( (587,323),'30',),
                ( (440,162),'45',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (342,272),),
                ( (392,255),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (248,122),),
                ( (195,366),),
                ( (264,239),),
                ( (357,231),),
                ( (543,193),),
                ( (352,315),),
                ( (423,318),),
                ( (547,234),),
                ( (403,144),),
                ( (146,240),),
                ( (414,253),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (248,122),),
                ( (195,366),),
                ( (264,239),),
                ( (357,231),),
                ( (543,193),),
                ( (352,315),),
                ( (423,318),),
                ( (547,234),),
                ( (403,144),),
                ( (146,240),),
                ( (414,253),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (342,272),),
                ( (392,255),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (157,125),'Cleburne',),
                ( (112,369),'Decatur',),
                ( (217,260),'Fort Worth',),
                ( (298,214),'Grand Prairie',),
                ( (506,176),'Kaufman',),
                ( (250,318),'Lewisville',),
                ( (443,321),'Plano',),
                ( (567,237),'Terrell',),
                ( (351,127),'Waxahachie',),
                ( (92,223),'Weatherford',),
                ( (434,256),'Dallas',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (157,125),'Cleburne',),
                ( (112,369),'Decatur',),
                ( (217,260),'Fort Worth',),
                ( (298,214),'Grand Prairie',),
                ( (506,176),'Kaufman',),
                ( (250,318),'Lewisville',),
                ( (443,321),'Plano',),
                ( (567,237),'Terrell',),
                ( (351,127),'Waxahachie',),
                ( (92,223),'Weatherford',),
                ( (434,256),'Dallas',),
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
# MAP: 71648
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(2769,731),
             mapcutSize=(2032,1355),
             mapFinalSize=(720,480),
             mapMilesSize=(1949,1317),
             datacutType='radarSatellite.us',
             datacutCoordinate=(530,31),
             datacutSize=(1044,699),
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
# MAP: 476
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19077,8010),
             mapcutSize=(648,432),
             mapFinalSize=(720,480),
             mapMilesSize=(69,55),
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
              ( ( (557,284),'75',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (194,220),'35W',),
                ( (439,272),'35E',),
                ( (490,253),'635',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (138,274),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (128,112),'20',),
                ( (383,155),'30',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72249002',(171,115),),
                ( '72249013',(247,219),),
                ( '72249017',(318,92),),
                ( '72249024',(107,307),),
                ( '72259000',(385,184),),
                ( '72259013',(299,278),),
                ( '72259014',(517,153),),
                ( '72259015',(431,303),),
                ( '72259026',(470,77),),
                ( '72259031',(580,292),),
                ( '72259036',(602,192),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72249002',(168,151),),
                ( '72249013',(244,255),),
                ( '72249017',(315,128),),
                ( '72249024',(104,343),),
                ( '72259000',(382,220),),
                ( '72259013',(296,314),),
                ( '72259014',(514,189),),
                ( '72259015',(428,339),),
                ( '72259026',(467,113),),
                ( '72259031',(577,328),),
                ( '72259036',(599,228),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (121,187),'Ft. Worth',),
                ( (218,291),'Keller',),
                ( (259,164),'Arlington',),
                ( (83,379),'Boyd',),
                ( (357,256),'Irving',),
                ( (240,350),'Double Oak',),
                ( (472,225),'Dallas',),
                ( (379,375),'Lewisville',),
                ( (433,149),'DeSoto',),
                ( (553,364),'Plano',),
                ( (563,264),'Garland',),
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
# MAP: 74969
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(19077,8010),
             mapcutSize=(648,432),
             mapFinalSize=(720,480),
             mapMilesSize=(69,55),
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
              ( ( (557,284),'75',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (194,220),'35W',),
                ( (439,272),'35E',),
                ( (490,253),'635',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (138,274),'287',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (128,112),'20',),
                ( (383,155),'30',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72249002',(168,151),),
                ( 'T72249013',(244,255),),
                ( 'T72249017',(315,128),),
                ( 'T72249024',(104,343),),
                ( 'T72259000',(382,220),),
                ( 'T72259013',(296,314),),
                ( 'T72259014',(514,189),),
                ( 'T72259015',(428,339),),
                ( 'T72259026',(467,113),),
                ( 'T72259031',(577,328),),
                ( 'T72259036',(599,228),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72249002',(171,115),),
                ( 'T72249013',(247,219),),
                ( 'T72249017',(318,92),),
                ( 'T72249024',(107,307),),
                ( 'T72259000',(385,184),),
                ( 'T72259013',(299,278),),
                ( 'T72259014',(517,153),),
                ( 'T72259015',(431,303),),
                ( 'T72259026',(470,77),),
                ( 'T72259031',(580,292),),
                ( 'T72259036',(602,192),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (121,187),'Ft. Worth',),
                ( (218,291),'Keller',),
                ( (259,164),'Arlington',),
                ( (83,379),'Boyd',),
                ( (357,256),'Irving',),
                ( (240,350),'Double Oak',),
                ( (472,225),'Dallas',),
                ( (379,375),'Lewisville',),
                ( (433,149),'DeSoto',),
                ( (553,364),'Plano',),
                ( (563,264),'Garland',),
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
# MAP: 48902
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(16173,6193),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(629,503),
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
              ( ( '72248000',(588,152),),
                ( '72256000',(360,108),),
                ( '72259000',(407,197),),
                ( '72263000',(141,94),),
                ( '72266000',(227,174),),
                ( '72267000',(107,252),),
                ( '72351000',(288,275),),
                ( '74750046',(491,97),),
                ( '74752035',(576,253),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72248000',(585,188),),
                ( '72256000',(357,144),),
                ( '72259000',(404,233),),
                ( '72263000',(138,130),),
                ( '72266000',(224,210),),
                ( '72267000',(104,288),),
                ( '72351000',(285,311),),
                ( '74750046',(488,133),),
                ( '74752035',(573,289),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (529,224),'Shreveport',),
                ( (335,180),'Waco',),
                ( (377,269),'Dallas',),
                ( (82,166),'San Angelo',),
                ( (189,246),'Abilene',),
                ( (65,324),'Lubbock',),
                ( (219,347),'Wichita Falls',),
                ( (460,169),'Lufkin',),
                ( (522,325),'Texarkana',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 50489
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(16173,6193),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(629,503),
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
              ( ( 'T72248000',(585,188),),
                ( 'T72256000',(357,144),),
                ( 'T72259000',(404,233),),
                ( 'T72263000',(138,130),),
                ( 'T72266000',(224,210),),
                ( 'T72267000',(104,288),),
                ( 'T72351000',(285,311),),
                ( 'T74750046',(488,133),),
                ( 'T74752035',(573,289),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72248000',(588,152),),
                ( 'T72256000',(360,108),),
                ( 'T72259000',(407,197),),
                ( 'T72263000',(141,94),),
                ( 'T72266000',(227,174),),
                ( 'T72267000',(107,252),),
                ( 'T72351000',(288,275),),
                ( 'T74750046',(491,97),),
                ( 'T74752035',(576,253),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (529,224),'Shreveport',),
                ( (335,180),'Waco',),
                ( (377,269),'Dallas',),
                ( (82,166),'San Angelo',),
                ( (189,246),'Abilene',),
                ( (65,324),'Lubbock',),
                ( (219,347),'Wichita Falls',),
                ( (460,169),'Lufkin',),
                ( (522,325),'Texarkana',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 52193
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(17868,7103),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(334,267),
             datacutType='radar.us',
             datacutCoordinate=(1790,532),
             datacutSize=(382,256),
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
              ( ( (326,325),'35',),
                ( (452,99),'45',),
                ( (570,279),'30',),
                ( (98,182),'20',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (393,289),'75',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (239,331),'287',),
                ( (208,143),'281',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (239,331),'287',),
                ( (208,143),'281',),
                ( (393,289),'75',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (326,325),'35',),
                ( (452,99),'45',),
                ( (570,279),'30',),
                ( (98,182),'20',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (216,248),),
                ( (380,245),),
                ( (329,92),),
                ( (565,187),),
                ( (538,350),),
                ( (104,109),),
                ( (413,350),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (216,248),),
                ( (380,245),),
                ( (329,92),),
                ( (565,187),),
                ( (538,350),),
                ( (104,109),),
                ( (413,350),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (157,269),'Mineral Wells',),
                ( (400,259),'Dallas',),
                ( (349,106),'Waco',),
                ( (585,201),'Tyler',),
                ( (558,364),'Paris',),
                ( (124,123),'Brownwood',),
                ( (376,333),'Sherman',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (157,269),'Mineral Wells',),
                ( (400,259),'Dallas',),
                ( (349,106),'Waco',),
                ( (585,201),'Tyler',),
                ( (558,364),'Paris',),
                ( (124,123),'Brownwood',),
                ( (376,333),'Sherman',),
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
wxdata.setInterestList('lambert.us','1',['radarSatellite.us',])
wxdata.setInterestList('mercator.us','1',['radar.us',])
#
#
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['AUS','DAL','DFW',])
wxdata.setInterestList('coopId','1',['72248000','72249002','72249013','72249017','72249024','72251010','72253000','72256000','72259000','72259009','72259013','72259014','72259015','72259022','72259026','72259031','72259036','72259104','72263000','72266000','72267000','72340073','72351000','72462040','74732014','74750046','74752035',])
wxdata.setInterestList('indexId','1',['KGPM',])
wxdata.setInterestList('pollenId','1',['DFW',])
wxdata.setInterestList('obsStation','1',['KDFW','KGPM','T72248000','T72249002','T72249013','T72249014','T72249015','T72249017','T72249024','T72249033','T72256000','T72259000','T72259009','T72259013','T72259014','T72259015','T72259022','T72259026','T72259031','T72259036','T72259104','T72263000','T72266000','T72267000','T72351000','T74745001','T74750046','T74752035',])
wxdata.setInterestList('climId','1',['412242','412244',])
wxdata.setInterestList('metroId','1',['3',])
wxdata.setInterestList('zone','1',['TXZ119',])
wxdata.setInterestList('aq','1',['tx004',])
wxdata.setInterestList('skiId','1',['505001','505007',])
wxdata.setInterestList('county','1',['TXC113','TXC443',])
dsm.set('Config.1.countyNameList',[('TXC113','Dallas'),('TXC443','Terrell'),], 0)
#
dsm.set('dmaCode','623', 0)
dsm.set('secondaryObsStation','KGPM', 0)
dsm.set('primaryClimoStation','412244', 0)
dsm.set('primaryIndexId','KGPM', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','TX', 0)
dsm.set('primaryAqStation','tx004', 0)
dsm.set('primPollenSiteName','Dallas', 0)
dsm.set('expRev','3155584', 0)
dsm.set('primaryCoopId','72259022', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','DAL', 0)
dsm.set('primaryCounty','TXC113', 0)
dsm.set('primaryObsStation','T72259022', 0)
dsm.set('primaryLat',32.72805, 0)
dsm.set('hasTraffic',1, 0)
dsm.set('primaryPollenStation','DFW', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-97.01361, 0)
dsm.set('primaryForecastName','Grand Prairie Area', 0)
dsm.set('primaryZone','TXZ119', 0)
dsm.set('climoRegion','4', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','TIME WARNER CABLE', 0)
dsm.set('headendId','022102', 0)
dsm.set('msoName','THE WEATHER CHANNEL', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','TIME WARNER CABLE', 0)
dsm.set('msoCode','TWC', 0)
dsm.set('headendName','DOM - GRAND PRAIRIE - DOM', 0)
dsm.set('affiliateNumber','00370', 0)
dsm.set('zipCode','75051', 0)
dsm.set('Config.1.bcNetMask','255.255.255.192', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD01040063', 0)
dsm.set('Config.1.bcExtIpAddress','172.20.10.54', 0)
dsm.set('Config.1.bcGateWay','172.17.97.62', 0)
dsm.set('Config.1.bcIpAddress','172.17.97.31', 0)
#
wxdata.setTimeZone('CST6CDT')
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
d.airportId = ['DAL','DFW','AUS',]
d.airportLocName = ['Dallas/Love','Dallas/Ft. Worth','Austin/Bergstrom',]
d.obsStation = ['T72259014','T72259000','T74745001',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['505001','505007',]
d.coopId = ['72462040','74732014',]
d.resortName = ['Angel Fire, NM','Ski Apache, NM',]
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
d.serialNum=651686
d.crawls=[
(1168927200,1199685599,[(0,23)],'In 1988, Parkland was the first Level I Trauma Center in Texas. Last year, we used that certification 5,000 times. Parkland. The Right Place. The Right Time. for everyone. www.parklandhospital.com'),
(1173679200,1175407199,[(0,23)],'FREE TEXAS RANGERS TICKETS!! VISIT FREEDVDDEPOT.COM FOR OFFER DETAILS! DVD MOVIES FOR JUST SHIPPING AND HANDLING! THAT\'S FREEDVDDEPOT.COM     FREE TEXAS RANGERS TICKETS!! VISIT FREEDVDDEPOT.COM FOR DETAILS! DVD MOVIES FOR JUST SHIPPING AND HANDLING! THAT\'S FREEDVDDEPOT.COM'),
(1178510400,1179115199,[(0,23)],'ARE STATE LEGISLATORS DOING ENOUGH TO LOWER YOUR ELECTRICITY BILL? AARP URGES YOU TO TELL THEM TO ACT NOW! CALL 1-888-633-3650                 ARE STATE LEGISLATORS DOING ENOUGH TO LOWER YOUR ELECTRICITY BILL? AARP URGES YOU TO TELL THEM TO ACT NOW! CALL 1-888-633-3650'),
(1178510400,1179115199,[(0,23)],'TIRED OF HIGH ELECTRIC BILLS? AARP URGES YOU TO CALL YOUR LEGISLATORS TO TELL THEM TO LOWER YOUR ELECTRIC BILL NOW! CALL 1-888-633-3650.....TIRED OF HIGH ELECTRIC BILLS? AARP URGES YOU TO CALL YOUR LEGISLATORS TO TELL THEM .TO LOWER YOUR ELECTRIC BILL NOW! CALL 1-888-633-3650....'),
(1179720000,1182139199,[(0,23)],'Summer Sonshine Day Camp NOW enrolling k-5th graders for X-treme Summer 07\'. Come join the fun! Enjoy our fullcourt gym,gameroom,craftroom,swimming,fieldtrips and much more. For more info. Contact Laura Garrett @ (972)264-0395.'),
(1181534400,1194242399,[(0,23)],'Go green with a new Toyota Prius featuring Hybrid Synergy Drive and 50+ miles per gallon. With Extra Value Package savings, you can save yourself some green, too - up to $2,000. Your new Prius is ready and in stock. So visit your local Toyota dealer today and test drive a Prius..'),
(1189483200,1189915199,[(0,23)],'Attention Time Warner Customers! Don\'t miss the University of Oklahoma Sooners vs. the Aggies of Utah State University at 2:30pm, Saturday, September 15th on Time Warner Digital Cable Pay-Per-View channel 960. Use your remote to order!'),
(1193025600,1193637599,[(0,23)],'WRITE OFF THE CAR NOT THE KID AND DONATE YOUR CAR TODAY. CALL 866-835-5437 OR ONLINE AT WWW.CARSFORKIDS.ORG   WRITE OFF THE CAR NOT THE KID AND DONATE YOUR CAR TODAY. CALL 866-835-5437 OR ONLINE AT WWW.CARSFORKIDS.ORG'),
(1193637600,1194415199,[(0,23)],'Do you love basketball? Then get your game on with a free preview of NBA League Pass and NBA TV Oct. 30th - Nov. 6th on Time Warner Digital Cable.'),
(1197871200,1201845599,[(0,23)],'Stop making the landloard richer!call Bob Lovell at Home Marketing Services 972-392-9595.HMS will help find your home,take care of your mortgage and help with bumps and bruises on your credit.Home Marketing Services,helping the homeless one renter at a time.WWW.blessyourheart.com'),
(1197525600,1199167199,[(0,23)],'Bankston.com! For low year end prices & the largest selection of cars, trucks & SUV\'s, click Bankston.com or visit any of our 15 Bankston locations. Year End Double Rebate up to $10,000. Click Bankston.com! Over 10,000 vehicles, Bank on Bankston to save you money. Bankston.com!'),
(1217390400,1230789599,[(0,23)],'Tired of renting and making the landlord richer? Call today 972-392-9595.Home Marketing Services is truly the only one stop shop for all your real estate & mortgage needs! HMS can help locate & negotiate a new or pre-owned home for as little as zero down. www.blessyourheart.com'),
(1204524000,1205733599,[(0,23)],'If you enjoy doing silly things please join me in wishing Andy Adams Happy Birthday!Call anytime now thru March 17@214-234-1234.Andy is President of Autoflex Leasing and a truly great guy.Wish him a Happy Birthday @ 214-234-1234 now thru Mar 17 HAPPY BIRTHDAY Andy! 214-234-1234'),
(1205733600,1210564799,[(0,23)],'Start Your Spring Tan at PALM BEACH TAN! 5 Silver Level Tans just $15 for a limited time only! Or Try NEW MyMyst Sunless Tanning. See salons for details! 41 DFW Locations! NOW OPEN in Denton at University and Carroll. Visit www.palmbeachtan.com or call 1-888-palmtan'),
(1206511200,1207540799,[(0,23)],'Help your Arlington/Grand Prairie customers find you fast. Register your business at www.arlingtonbizlisting.com. Find the business listing you are looking for at arlingtonbizlisting.com your local business listing search engine arlingtonbizlisting.com'),
(1208491200,1210046399,[(0,23)],'Papal Visit 2008 coverage is available on Time Warner\'s On Demand channel 600 - North Texas folder.'),
(1212984000,1214539199,[(0,23)],'Grand Opening of Lake front Properties on June 28th and 29th. Stop by and pay no closing costs & receive $15,000 off! Call 877 watertx or go to scenicridgetexas.com for additional information.'),
(1216008000,1231048799,[(0,23)],'Hot Deals happening now at Toyota of Irving! See www.toyotaofirving.com For today\'s specials. Over 8 models with 30+ miles per gallon. Toyota of Irving, Texas Truck Capital Tundra,Tacoma,4Runner. Toyota of Irving 183 & Story Road. Call 1-800-Save-now. www.toyotaofirving.com'),
(1221105600,1221883199,[(0,23)],'Hiring Roofing Estimators for Local Established New Orleans/Baton Rouge, Louisiana Roofing Company. Leads Furnished. Commisioned Based. For Information Call 800-827-7709'),
]
dsm.set('Config.1.Ldl_LASCrawl', d, 0)
dsm.set('Config.1.LASCrawl', d, 0)
#
#
scmtRemove('Config.1.Local_TrafficOverview')
scmtRemove('Config.1.Ldl_TravelForecast')
scmtRemove('Config.1.Ldl_Almanac')
scmtRemove('Config.1.Local_7DayForecast')
scmtRemove('Config.1.Local_HeatSafetyTips')
scmtRemove('Config.1.Local_Climatology')
scmtRemove('Config.1.Ldl_CurrentObs.1')
scmtRemove('Config.1.Ldl_CurrentObs.3')
scmtRemove('Config.1.Local_Tides')
scmtRemove('Config.1.Local_RecordHighLow')
scmtRemove('Config.1.Ldl_3DayForecast')
scmtRemove('Config.1.Ldl_DailyForecast.1')
scmtRemove('Config.1.Ldl_Almanac.1')
scmtRemove('Config.1.Ldl_AirQualityForecast')
scmtRemove('Config.1.Ldl_HourlyForecast')
scmtRemove('Config.1.Ldl_AirportDelayConditions')
scmtRemove('Config.1.Ldl_CurrentObs.2')
scmtRemove('Config.1.Local_GetawayForecast')
scmtRemove('Config.1.Local_TrafficFlow')
scmtRemove('Config.1.Local_OutdoorActivityForecast')
scmtRemove('Config.1.Local_AirQualityForecast')
scmtRemove('Config.1.Ldl_DailyForecast')
scmtRemove('Config.1.Local_MarineForecast')
scmtRemove('Config.1.Ldl_HurricaneWatch')
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.Fcst_TextForecast')
scmtRemove('Config.1.Ldl_UVForecast')
scmtRemove('Config.1.Cc_CurrentConditions')
scmtRemove('Config.1.Local_TrafficReport')
scmtRemove('Config.1.Local_LocalObservations')
scmtRemove('Config.1.Ldl_CurrentObs.0')
scmtRemove('Config.1.Fcst_DaypartForecast')
scmtRemove('Config.1.Local_CurrentConditions')
scmtRemove('Config.1.Local_TextForecast')
scmtRemove('Config.1.Local_SchoolDayWeather')
scmtRemove('Config.1.Local_EventForecast')
scmtRemove('Config.1.Local_DaypartForecast')
scmtRemove('Config.1.Local_Almanac')
scmtRemove('Config.1.Local_ExtendedForecast')
scmtRemove('Config.1.Fcst_ExtendedForecast')
scmtRemove('Config.1.Local_NWSHeadlines')
scmtRemove('Config.1.Ldl_StarIDMessage')
scmtRemove('Config.1.TimeTemp_Default')
#
d = twc.Data()
d.locName = 'Grand Prairie'
d.hrsGrid = (((0, 4), 6, 12, 18), ((4, 8), 9, 12, 18), ((8, 11), 12, 15, 18), ((11, 14), 15, 18, 21), ((14, 17), 18, 21, 24), ((17, 20), 21, 24, 30), ((20, 24), 30, 36, 42),)
d.coopId = '72259022'
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Grand Prairie Area'
d.coopId = '72259022'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72249017','T72249014','T72259036','T72249002','T72259013','T72259014','T72249015','T72249033',]
d.locName = ['Arlington','Kennedale','Garland','Fort Worth','Flower Mound','Love Field','Eagle Mtn Lake','Cleburne',]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72259022','KGPM',]
d.dataTypes = ['StarId', 'SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp', 'Dewpoint', 'Pressure', 'Ceiling', 'Visibility', 'MTDPrecip']
d.prodLabel = 'Now'
d.obsLocName = ['Grand Prairie','Grand Prairie','Grand Prairie',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.3', d, 0, 1)
#
#
d = twc.Data()
d.crawlRate = 3
dsm.set('Config.1.Ldl_HurricaneWatch', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259009',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Colleyville',]
d.primaryObsProduct = 0
dsm.set('Config.1.Ldl_CurrentObs.2', d, 0, 1)
#
#
d = twc.Data()
d.climId = '412244'
d.latitude = 32.85
d.longitude = -96.85
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Waco','Wichita Falls','Abilene',]
d.coopId = ['72256000','72351000','72266000',]
d.prodLabel = 'Travel'
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259104',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Downtown Dallas',]
d.primaryObsProduct = 0
dsm.set('Config.1.Ldl_CurrentObs.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259022','KGPM',]
d.locName = ['Grand Prairie','Grand Prairie',]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Dallas/Ft Worth',]
d.actionDayPhrase = 'Air Quality Action Day'
d.aq = ['tx004',]
dsm.set('Config.1.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.trafficActive = 0
d.trafficReverseActive = [1,1,1,1,1,1,]
d.prodLabel = 'Traffic'
d.trafficFlowRoute = ['92142-3','92102-3','92096-3','91974-3','92105-3','92143-3',]
d.trafficReverseRoute = ['92141-3','92101-3','92095-3','91973-3','92106-3','92144-3',]
d.routes=[]
d.routeDisplayTime=[]
dsm.set('Config.1.Ldl_TrafficTripTimes', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72259022','KGPM',]
d.dataTypes = ['SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Grand Prairie','Grand Prairie','Grand Prairie',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.0', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Grand Prairie Area'
d.coopId = '72259022'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T72259022'
d.locName = 'GRAND PRAIRIE'
d.heatIndexThreshold = 107
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'TXZ119'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.location = 'GRAND PRAIRIE AREA'
d.coopId = '72259022'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'GRAND PRAIRIE AREA'
d.coopId = '72259022'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'DALLAS-FT. WORTH AREA'
d.maxPages = 3
d.activeVocalCue = 0
d.metroId=['3',]
d.latLongBoxes=[
             ((-97.23332730538262,32.52721692537273),(-96.89457633213222,32.87138791419514)),
             ((-96.95212543641725,32.630054764982305),(-96.51573164210453,32.93090200197062)),
             ((-97.50753572008799,32.54740442515035),(-97.19677044231985,32.85486368932523)),
             ((-97.24416733652663,32.795507696187045),(-96.91896640220624,33.11257860714942)),
]
d.severityList=[
             ('Incident',2,),
             ('Construction',1,),
             ('Unspecified',1,),
]
dsm.set('Config.1.Local_TrafficReport', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.Ldl_TrafficReport', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','T72259022','KGPM',]
d.locName = ['Grand Prairie','GRAND PRAIRIE','GRAND PRAIRIE',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'GRAND PRAIRIE AREA'
d.coopId = '72259022'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72259022','KGPM',]
d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
d.coopId = '72259022'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_StarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T72259022'
d.climId = '412244'
d.latitude = 32.85
d.longitude = -96.85
d.dataTypes = ['Sunrise', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Grand Prairie'
dsm.set('Config.1.Ldl_Almanac.1', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['DAL','DFW',]
d.obsStation = ['T72259014','T72259000',]
d.locName = ['Love Field','DFW Int\'l',]
d.displayFlag = [1,1,]
d.prodLabel = 'Airport'
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T72259022'
d.climId = '412244'
d.latitude = 32.85
d.longitude = -96.85
d.dataTypes = ['Sunrise', 'AvgHiLo', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Grand Prairie'
dsm.set('Config.1.Ldl_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['GRAND PRAIRIE AREA',]
d.coopId = ['72259022',]
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KDFW',]
d.climId = ['412242',]
d.latitude = 32.9
d.longitude = -97.03
d.locName = ['DFW Int\'l',]
d.coopId = ['72259000',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.1.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T72259022','KGPM',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Grand Prairie'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '72259022'
d.prodLabel = 'UV Index'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Dallas/Ft Worth'
d.startDate = (1,1)
d.endDate = (12,31)
d.prodLabel = 'Air Quality'
d.aq = 'tx004'
dsm.set('Config.1.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Grand Prairie'
d.coopId = '72259022'
d.prodLabel = '3 Day'
dsm.set('Config.1.Ldl_3DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.url = ['CorpusChristicvb.com','','',]
d.locNameList = ['Corpus Christi  Upper Padre Is.','Hot Springs Nat\'l Pk, AR','San Antonio, TX',]
d.coopId = ['72251010','72340073','72253000',]
dsm.set('Config.1.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Grand Prairie Area'
d.coopId = '72259022'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '72259022'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 1
d.locName = ['Grand Prairie','Downtown Dallas','Colleyville',]
d.coopId = ['72259022','72259104','72259009',]
dsm.set('Config.1.Ldl_DailyForecast.1', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Grand Prairie','Downtown Dallas','Colleyville',]
d.coopId = ['72259022','72259104','72259009',]
dsm.set('Config.1.Ldl_DailyForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KDFW'
d.climId = ['412242',]
d.latitude = 32.9
d.longitude = -97.03
d.locName = 'DFW INT\'L'
d.coopId = '72259000'
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
d.activeLocal_Satellite = 0
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 0
d.activeLocal_TrafficOverview = 0
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
d = [[             [(0,00),(0,59),'Ldl.nationalWeekdayPrimeUp',],
             [(1,00),(1,59),'Ldl.nationalWeekdayPrimeUp',],
             [(2,00),(2,59),'Ldl.nationalWeekdayPrimeUp',],
             [(3,00),(3,59),'Ldl.nationalWeekdayPrimeUp',],
             [(4,00),(4,59),'Ldl.nationalWeekdayMorningUp',],
             [(5,00),(5,59),'Ldl.nationalWeekdayMorningUp',],
             [(6,00),(6,59),'Ldl.nationalWeekdayMorningUp',],
             [(7,00),(7,59),'Ldl.nationalWeekdayMorningUp',],
             [(8,00),(8,59),'Ldl.nationalWeekdayMorningUp',],
             [(9,00),(9,59),'Ldl.nationalWeekdayMorningUp',],
             [(10,00),(10,59),'Ldl.nationalWeekdayMorningUp',],
             [(11,00),(11,59),'Ldl.nationalWeekdayUp',],
             [(12,00),(12,59),'Ldl.nationalWeekdayUp',],
             [(13,00),(13,59),'Ldl.nationalWeekdayUp',],
             [(14,00),(14,59),'Ldl.nationalWeekdayUp',],
             [(15,00),(15,59),'Ldl.nationalWeekdayUp',],
             [(16,00),(16,59),'Ldl.nationalWeekdayUp',],
             [(17,00),(17,59),'Ldl.nationalWeekdayUp',],
             [(18,00),(18,59),'Ldl.nationalWeekdayUp',],
             [(19,00),(19,59),'Ldl.nationalWeekdayPrimeUp',],
             [(20,00),(20,59),'Ldl.nationalWeekdayPrimeUp',],
             [(21,00),(21,59),'Ldl.nationalWeekdayPrimeUp',],
             [(22,00),(22,59),'Ldl.nationalWeekdayPrimeUp',],
             [(23,00),(23,59),'Ldl.nationalWeekdayPrimeUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekdayPrimeUp',],
             [(1,00),(1,59),'Ldl.nationalWeekdayPrimeUp',],
             [(2,00),(2,59),'Ldl.nationalWeekdayPrimeUp',],
             [(3,00),(3,59),'Ldl.nationalWeekdayPrimeUp',],
             [(4,00),(4,59),'Ldl.nationalWeekdayMorningUp',],
             [(5,00),(5,59),'Ldl.nationalWeekdayMorningUp',],
             [(6,00),(6,59),'Ldl.nationalWeekdayMorningUp',],
             [(7,00),(7,59),'Ldl.nationalWeekdayMorningUp',],
             [(8,00),(8,59),'Ldl.nationalWeekdayMorningUp',],
             [(9,00),(9,59),'Ldl.nationalWeekdayMorningUp',],
             [(10,00),(10,59),'Ldl.nationalWeekdayMorningUp',],
             [(11,00),(11,59),'Ldl.nationalWeekdayUp',],
             [(12,00),(12,59),'Ldl.nationalWeekdayUp',],
             [(13,00),(13,59),'Ldl.nationalWeekdayUp',],
             [(14,00),(14,59),'Ldl.nationalWeekdayUp',],
             [(15,00),(15,59),'Ldl.nationalWeekdayUp',],
             [(16,00),(16,59),'Ldl.nationalWeekdayUp',],
             [(17,00),(17,59),'Ldl.nationalWeekdayUp',],
             [(18,00),(18,59),'Ldl.nationalWeekdayUp',],
             [(19,00),(19,59),'Ldl.nationalWeekdayPrimeUp',],
             [(20,00),(20,59),'Ldl.nationalWeekdayPrimeUp',],
             [(21,00),(21,59),'Ldl.nationalWeekdayPrimeUp',],
             [(22,00),(22,59),'Ldl.nationalWeekdayPrimeUp',],
             [(23,00),(23,59),'Ldl.nationalWeekdayPrimeUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekdayPrimeUp',],
             [(1,00),(1,59),'Ldl.nationalWeekdayPrimeUp',],
             [(2,00),(2,59),'Ldl.nationalWeekdayPrimeUp',],
             [(3,00),(3,59),'Ldl.nationalWeekdayPrimeUp',],
             [(4,00),(4,59),'Ldl.nationalWeekdayMorningUp',],
             [(5,00),(5,59),'Ldl.nationalWeekdayMorningUp',],
             [(6,00),(6,59),'Ldl.nationalWeekdayMorningUp',],
             [(7,00),(7,59),'Ldl.nationalWeekdayMorningUp',],
             [(8,00),(8,59),'Ldl.nationalWeekdayMorningUp',],
             [(9,00),(9,59),'Ldl.nationalWeekdayMorningUp',],
             [(10,00),(10,59),'Ldl.nationalWeekdayMorningUp',],
             [(11,00),(11,59),'Ldl.nationalWeekdayUp',],
             [(12,00),(12,59),'Ldl.nationalWeekdayUp',],
             [(13,00),(13,59),'Ldl.nationalWeekdayUp',],
             [(14,00),(14,59),'Ldl.nationalWeekdayUp',],
             [(15,00),(15,59),'Ldl.nationalWeekdayUp',],
             [(16,00),(16,59),'Ldl.nationalWeekdayUp',],
             [(17,00),(17,59),'Ldl.nationalWeekdayUp',],
             [(18,00),(18,59),'Ldl.nationalWeekdayUp',],
             [(19,00),(19,59),'Ldl.nationalWeekdayPrimeUp',],
             [(20,00),(20,59),'Ldl.nationalWeekdayPrimeUp',],
             [(21,00),(21,59),'Ldl.nationalWeekdayPrimeUp',],
             [(22,00),(22,59),'Ldl.nationalWeekdayPrimeUp',],
             [(23,00),(23,59),'Ldl.nationalWeekdayPrimeUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekdayPrimeUp',],
             [(1,00),(1,59),'Ldl.nationalWeekdayPrimeUp',],
             [(2,00),(2,59),'Ldl.nationalWeekdayPrimeUp',],
             [(3,00),(3,59),'Ldl.nationalWeekdayPrimeUp',],
             [(4,00),(4,59),'Ldl.nationalWeekdayMorningUp',],
             [(5,00),(5,59),'Ldl.nationalWeekdayMorningUp',],
             [(6,00),(6,59),'Ldl.nationalWeekdayMorningUp',],
             [(7,00),(7,59),'Ldl.nationalWeekdayMorningUp',],
             [(8,00),(8,59),'Ldl.nationalWeekdayMorningUp',],
             [(9,00),(9,59),'Ldl.nationalWeekdayMorningUp',],
             [(10,00),(10,59),'Ldl.nationalWeekdayMorningUp',],
             [(11,00),(11,59),'Ldl.nationalWeekdayUp',],
             [(12,00),(12,59),'Ldl.nationalWeekdayUp',],
             [(13,00),(13,59),'Ldl.nationalWeekdayUp',],
             [(14,00),(14,59),'Ldl.nationalWeekdayUp',],
             [(15,00),(15,59),'Ldl.nationalWeekdayUp',],
             [(16,00),(16,59),'Ldl.nationalWeekdayUp',],
             [(17,00),(17,59),'Ldl.nationalWeekdayUp',],
             [(18,00),(18,59),'Ldl.nationalWeekdayUp',],
             [(19,00),(19,59),'Ldl.nationalWeekdayPrimeUp',],
             [(20,00),(20,59),'Ldl.nationalWeekdayPrimeUp',],
             [(21,00),(21,59),'Ldl.nationalWeekdayPrimeUp',],
             [(22,00),(22,59),'Ldl.nationalWeekdayPrimeUp',],
             [(23,00),(23,59),'Ldl.nationalWeekdayPrimeUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekdayPrimeUp',],
             [(1,00),(1,59),'Ldl.nationalWeekdayPrimeUp',],
             [(2,00),(2,59),'Ldl.nationalWeekdayPrimeUp',],
             [(3,00),(3,59),'Ldl.nationalWeekdayPrimeUp',],
             [(4,00),(4,59),'Ldl.nationalWeekdayMorningUp',],
             [(5,00),(5,59),'Ldl.nationalWeekdayMorningUp',],
             [(6,00),(6,59),'Ldl.nationalWeekdayMorningUp',],
             [(7,00),(7,59),'Ldl.nationalWeekdayMorningUp',],
             [(8,00),(8,59),'Ldl.nationalWeekdayMorningUp',],
             [(9,00),(9,59),'Ldl.nationalWeekdayMorningUp',],
             [(10,00),(10,59),'Ldl.nationalWeekdayMorningUp',],
             [(11,00),(11,59),'Ldl.nationalWeekdayUp',],
             [(12,00),(12,59),'Ldl.nationalWeekdayUp',],
             [(13,00),(13,59),'Ldl.nationalWeekdayUp',],
             [(14,00),(14,59),'Ldl.nationalWeekdayUp',],
             [(15,00),(15,59),'Ldl.nationalWeekdayUp',],
             [(16,00),(16,59),'Ldl.nationalWeekdayUp',],
             [(17,00),(17,59),'Ldl.nationalWeekdayUp',],
             [(18,00),(18,59),'Ldl.nationalWeekdayUp',],
             [(19,00),(19,59),'Ldl.nationalWeekendUp',],
             [(20,00),(20,59),'Ldl.nationalWeekendUp',],
             [(21,00),(21,59),'Ldl.nationalWeekendUp',],
             [(22,00),(22,59),'Ldl.nationalWeekendUp',],
             [(23,00),(23,59),'Ldl.nationalWeekendUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekendUp',],
             [(1,00),(1,59),'Ldl.nationalWeekendUp',],
             [(2,00),(2,59),'Ldl.nationalWeekendUp',],
             [(3,00),(3,59),'Ldl.nationalWeekendUp',],
             [(4,00),(4,59),'Ldl.nationalWeekendUp',],
             [(5,00),(5,59),'Ldl.nationalWeekendUp',],
             [(6,00),(6,59),'Ldl.nationalWeekendUp',],
             [(7,00),(7,59),'Ldl.nationalWeekendUp',],
             [(8,00),(8,59),'Ldl.nationalWeekendUp',],
             [(9,00),(9,59),'Ldl.nationalWeekendUp',],
             [(10,00),(10,59),'Ldl.nationalWeekendUp',],
             [(11,00),(11,59),'Ldl.nationalWeekendUp',],
             [(12,00),(12,59),'Ldl.nationalWeekendUp',],
             [(13,00),(13,59),'Ldl.nationalWeekendUp',],
             [(14,00),(14,59),'Ldl.nationalWeekendUp',],
             [(15,00),(15,59),'Ldl.nationalWeekendUp',],
             [(16,00),(16,59),'Ldl.nationalWeekendUp',],
             [(17,00),(17,59),'Ldl.nationalWeekendUp',],
             [(18,00),(18,59),'Ldl.nationalWeekendUp',],
             [(19,00),(19,59),'Ldl.nationalWeekendUp',],
             [(20,00),(20,59),'Ldl.nationalWeekendUp',],
             [(21,00),(21,59),'Ldl.nationalWeekendUp',],
             [(22,00),(22,59),'Ldl.nationalWeekendUp',],
             [(23,00),(23,59),'Ldl.nationalWeekendUp',],
],
[             [(0,00),(0,59),'Ldl.nationalWeekendUp',],
             [(1,00),(1,59),'Ldl.nationalWeekendUp',],
             [(2,00),(2,59),'Ldl.nationalWeekendUp',],
             [(3,00),(3,59),'Ldl.nationalWeekendUp',],
             [(4,00),(4,59),'Ldl.nationalWeekendUp',],
             [(5,00),(5,59),'Ldl.nationalWeekendUp',],
             [(6,00),(6,59),'Ldl.nationalWeekendUp',],
             [(7,00),(7,59),'Ldl.nationalWeekendUp',],
             [(8,00),(8,59),'Ldl.nationalWeekendUp',],
             [(9,00),(9,59),'Ldl.nationalWeekendUp',],
             [(10,00),(10,59),'Ldl.nationalWeekendUp',],
             [(11,00),(11,59),'Ldl.nationalWeekendUp',],
             [(12,00),(12,59),'Ldl.nationalWeekendUp',],
             [(13,00),(13,59),'Ldl.nationalWeekendUp',],
             [(14,00),(14,59),'Ldl.nationalWeekendUp',],
             [(15,00),(15,59),'Ldl.nationalWeekendUp',],
             [(16,00),(16,59),'Ldl.nationalWeekendUp',],
             [(17,00),(17,59),'Ldl.nationalWeekendUp',],
             [(18,00),(18,59),'Ldl.nationalWeekendUp',],
             [(19,00),(19,59),'Ldl.nationalWeekendUp',],
             [(20,00),(20,59),'Ldl.nationalWeekdayPrimeUp',],
             [(21,00),(21,59),'Ldl.nationalWeekdayPrimeUp',],
             [(22,00),(22,59),'Ldl.nationalWeekdayPrimeUp',],
             [(23,00),(23,59),'Ldl.nationalWeekdayPrimeUp',],
],
]
dsm.set('Config.1.Playlist.Ldl.schedule', d, 0)
d = twc.Data()
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',0,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HourlyForecast',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',1,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirQualityForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('UVForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,480,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.nationalWeekdayMorningUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',0,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',1,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',0,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HourlyForecast',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',0,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirQualityForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('UVForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,480,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.nationalWeekdayUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,8,8,6,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,8,10,6,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,4,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,24,24,16,0,1,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,9,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,9,14,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,4,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,10,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,36,36,28,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,10,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,10,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,9,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,9,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,9,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,9,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,9,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,9,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,8,10,6,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,8,10,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,8,8,6,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,1,2,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,7,1,2,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,20,20,16,0,9,2,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,9,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,9,12,8,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,1,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',0,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',1,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',0,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HourlyForecast',0,4,12,4,0,2,1,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',1,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficTripTimes',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TrafficReport',0,4,480,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirportDelayConditions',0,3,18,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',0,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirQualityForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('UVForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,480,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.nationalWeekendUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',0,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',1,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Almanac',0,3,12,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',0,4,40,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',1,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',2,4,4,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',0,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('DailyForecast',1,4,20,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('3DayForecast',0,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TravelForecast',1,3,9,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('AirQualityForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('UVForecast',0,3,3,3,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,480,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.nationalWeekdayPrimeUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,5,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,10,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,10,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,5,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,9,8,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
]
dsm.set('Config.1.Playlist.DefaultUS.120.1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Ldl'
d.childPrefixes = ['LdlMenu', 'TimeTemp', 'Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('LASCrawl',0,4,120,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('HurricaneWatch',0,4,12,4,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('TornadoWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('SevereThunderstormWatch',0,6,480,6,0,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
('CurrentObs',3,4,44,4,1,2,0,["ldlMenu1", "timeTemp1", "logo1"]),
('Void',0,1,120,1,1,1,0,["ldlMenu1", "timeTemp1", "logo1"]),
]
dsm.set('Config.1.Playlist.Ldl.ldl1', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'Local'
d.childPrefixes = ['Tag', 'BackgroundMusic', 'Ldl']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,7,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,10,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,10,16,9,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,8,11,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,6,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,7,1,1,8,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,7,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,5,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,6,1,2,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,9,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,10,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,6,6,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,8,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,10,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,10,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,5,7,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,9,8,["tag1", "bkgMusic1", "ldl1"]),
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
('TrafficOverview.1',0,7,11,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,7,12,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,9,4,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,4,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,6,5,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,11,5,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,9,6,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,30,30,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,10,1,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,10,16,9,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
# Finished generation on Tue Sep 29 12:01:02 EDT 2009
