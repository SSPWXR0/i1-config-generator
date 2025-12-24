# Created on Mon May 03 14:37:14 GMT 2010
Log.info('scmt config started')
# EXP: 1672
# VIW: 13090
# CLN: 1133
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
scmtRemove('Config.1.NationalLdl_HourlyForecast.0')
scmtRemove('Config.1.NationalLdl_HourlyForecast.1')
scmtRemove('Config.1.NationalLdl_HourlyForecast.2')
scmtRemove('Config.1.NationalLdl_HourlyForecast.3')
scmtRemove('Config.1.NationalLdl_HourlyForecast.4')
scmtRemove('Config.1.NationalLdl_HourlyForecast.5')
scmtRemove('Config.1.NationalLdl_TextForecast.0')
scmtRemove('Config.1.NationalLdl_36HourForecast.0')
scmtRemove('Config.1.NationalLdl_36HourForecast.1')
scmtRemove('Config.1.NationalLdl_36HourForecast.2')
scmtRemove('Config.1.NationalLdl_36HourForecast.3')
scmtRemove('Config.1.NationalLdl_36HourForecast.4')
scmtRemove('Config.1.NationalLdl_36HourForecast.5')
scmtRemove('Config.1.NationalLdl_RadarSatellite')
scmtRemove('Config.1.NationalLdl_DopplerRadar')
scmtRemove('Config.1.NationalLdl_DaypartForecast')
#
#
# MAP: 78257
# NationalLdl_DopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(24711,11438),
             mapcutSize=(1440,821),
             mapFinalSize=(193,110),
             mapMilesSize=(141,97),
             datacutType='radar.us',
             datacutCoordinate=(2628,1064),
             datacutSize=(176,100),
             dataFinalSize=(193,110),
             dataOffset=(0,0),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.NationalLdl_DopplerRadar', d, 0)
#
# NationalLdl_DopplerRadar (PRODUCT DATA)
#
d = twc.Data(
  tiffImage = [
             (
               ('locatorDotSmallOutline',0,2,1,),
              ( ( (97,50),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (97,50),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (81,41),'Flat Rock',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (81,41),'Flat Rock',),
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
dsm.set('Config.1.NationalLdl_DopplerRadar', d, 0)
# MAP: 74056
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(24552,11436),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(141,97),
             datacutType='radar.us',
             datacutCoordinate=(2608,1063),
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
              ( ( (125,97),),
                ( (147,63),),
                ( (153,20),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (125,97),),
                ( (147,63),),
                ( (153,20),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (89,113),'Indianapolis',),
                ( (131,54),'Flat Rock',),
                ( (165,15),'Seymour',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (89,113),'Indianapolis',),
                ( (131,54),'Flat Rock',),
                ( (165,15),'Seymour',),
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
# MAP: 50398
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(24853,11426),
             mapcutSize=(1296,864),
             mapFinalSize=(720,480),
             mapMilesSize=(127,102),
             datacutType='radar.us',
             datacutCoordinate=(2645,1062),
             datacutSize=(159,106),
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
              ( ( (95,290),'70',),
                ( (322,312),'74',),
                ( (321,120),'65',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (95,290),'70',),
                ( (322,312),'74',),
                ( (321,120),'65',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (205,336),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (252,364),),
                ( (142,169),),
                ( (325,183),),
                ( (311,227),),
                ( (282,274),),
                ( (455,225),),
                ( (264,306),),
                ( (465,314),),
                ( (366,285),),
                ( (338,237),),
                ( (416,110),),
                ( (427,172),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (252,364),),
                ( (142,169),),
                ( (325,183),),
                ( (311,227),),
                ( (282,274),),
                ( (455,225),),
                ( (264,306),),
                ( (465,314),),
                ( (366,285),),
                ( (338,237),),
                ( (416,110),),
                ( (427,172),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (205,336),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (272,367),'Indianapolis',),
                ( (86,190),'Bloomington',),
                ( (284,166),'Columbus',),
                ( (206,230),'Edinburgh',),
                ( (196,277),'Franklin',),
                ( (475,228),'Greensburg',),
                ( (150,309),'Greenwood',),
                ( (485,317),'Rushville',),
                ( (386,288),'Shelbyville',),
                ( (314,256),'Flat Rock',),
                ( (436,113),'Vernon',),
                ( (447,175),'Westport',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (272,367),'Indianapolis',),
                ( (86,190),'Bloomington',),
                ( (284,166),'Columbus',),
                ( (206,230),'Edinburgh',),
                ( (196,277),'Franklin',),
                ( (475,228),'Greensburg',),
                ( (150,309),'Greenwood',),
                ( (485,317),'Rushville',),
                ( (386,288),'Shelbyville',),
                ( (314,256),'Flat Rock',),
                ( (436,113),'Vernon',),
                ( (447,175),'Westport',),
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
# MAP: 79831
# NationalLdl_RadarSatellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3823,1587),
             mapcutSize=(1392,793),
             mapFinalSize=(193,110),
             mapMilesSize=(1348,776),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1071,473),
             datacutSize=(716,410),
             dataFinalSize=(193,110),
             dataOffset=(0,0),
             vectors=['lambert.us.coastlines.vg','lambert.us.states.vg',],
)
wxdata.setMapData('Config.1.NationalLdl_RadarSatellite', d, 0)
#
# NationalLdl_RadarSatellite (PRODUCT DATA)
#
d = twc.Data(
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.NationalLdl_RadarSatellite', d, 0)
# MAP: 71585
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(3870,1645),
             mapcutSize=(1152,768),
             mapFinalSize=(720,480),
             mapMilesSize=(1120,753),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1096,503),
             datacutSize=(592,397),
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
# MAP: 72556
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(24790,11382),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(141,113),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (280,272),'65',),
                ( (594,197),'74',),
                ( (480,371),'70',),
                ( (174,306),'70',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72421059',(522,276),),
                ( '72438000',(219,312),),
                ( '72438026',(177,214),),
                ( '72438029',(356,271),),
                ( '72438068',(145,116),),
                ( '74468006',(447,80),),
                ( '74468026',(308,82),),
                ( '74468028',(512,161),),
                ( '74468031',(360,178),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72421059',(519,312),),
                ( '72438000',(216,348),),
                ( '72438026',(174,250),),
                ( '72438029',(353,307),),
                ( '72438068',(142,152),),
                ( '74468006',(444,116),),
                ( '74468026',(305,118),),
                ( '74468028',(509,197),),
                ( '74468031',(357,214),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (456,348),'Connersville',),
                ( (156,384),'Indianapolis',),
                ( (114,286),'Martinsville',),
                ( (298,343),'Shelbyville',),
                ( (79,188),'Bloomington',),
                ( (395,152),'N. Vernon',),
                ( (263,154),'Seymour',),
                ( (459,233),'Batesville',),
                ( (310,250),'Flat Rock',),
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
# MAP: 75314
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(24790,11382),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(141,113),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (280,272),'65',),
                ( (594,197),'74',),
                ( (480,371),'70',),
                ( (174,306),'70',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72421059',(519,312),),
                ( 'T72438000',(216,348),),
                ( 'T72438026',(174,250),),
                ( 'T72438029',(353,307),),
                ( 'T72438068',(142,152),),
                ( 'T74468006',(444,116),),
                ( 'T74468026',(305,118),),
                ( 'T74468028',(509,197),),
                ( 'T74468031',(357,214),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72421059',(522,276),),
                ( 'T72438000',(219,312),),
                ( 'T72438026',(177,214),),
                ( 'T72438029',(356,271),),
                ( 'T72438068',(145,116),),
                ( 'T74468006',(447,80),),
                ( 'T74468026',(308,82),),
                ( 'T74468028',(512,161),),
                ( 'T74468031',(360,178),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (456,348),'Connersville',),
                ( (156,384),'Indianapolis',),
                ( (114,286),'Martinsville',),
                ( (298,343),'Shelbyville',),
                ( (79,188),'Bloomington',),
                ( (395,152),'N. Vernon',),
                ( (263,154),'Seymour',),
                ( (459,233),'Batesville',),
                ( (310,250),'Flat Rock',),
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
# MAP: 49707
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21868,10159),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(575,459),
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
              ( ( '72421000',(525,149),),
                ( '72423000',(446,72),),
                ( '72428000',(590,230),),
                ( '72432000',(309,91),),
                ( '72434000',(125,94),),
                ( '72438000',(387,201),),
                ( '72439000',(187,185),),
                ( '72530000',(292,314),),
                ( '72532000',(159,289),),
                ( '72533000',(461,300),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72421000',(522,185),),
                ( '72423000',(443,108),),
                ( '72428000',(587,266),),
                ( '72432000',(306,127),),
                ( '72434000',(122,130),),
                ( '72438000',(384,237),),
                ( '72439000',(184,221),),
                ( '72530000',(289,350),),
                ( '72532000',(156,325),),
                ( '72533000',(458,336),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (472,221),'Cincinnati',),
                ( (396,144),'Louisville',),
                ( (540,302),'Columbus',),
                ( (255,163),'Evansville',),
                ( (78,166),'St. Louis',),
                ( (324,273),'Indianapolis',),
                ( (131,257),'Springfield',),
                ( (252,386),'Chicago',),
                ( (128,361),'Peoria',),
                ( (400,372),'Fort Wayne',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 47696
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(21868,10159),
             mapcutSize=(5875,3917),
             mapFinalSize=(720,480),
             mapMilesSize=(575,459),
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
              ( ( 'T72421000',(522,185),),
                ( 'T72423003',(447,114),),
                ( 'T72428000',(587,266),),
                ( 'T72432000',(306,127),),
                ( 'T72434000',(122,130),),
                ( 'T72438000',(384,237),),
                ( 'T72439000',(184,221),),
                ( 'T72530000',(289,350),),
                ( 'T72532000',(156,325),),
                ( 'T72533000',(458,336),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72421000',(525,149),),
                ( 'T72423003',(450,78),),
                ( 'T72428000',(590,230),),
                ( 'T72432000',(309,91),),
                ( 'T72434000',(125,94),),
                ( 'T72438000',(387,201),),
                ( 'T72439000',(187,185),),
                ( 'T72530000',(292,314),),
                ( 'T72532000',(159,289),),
                ( 'T72533000',(461,300),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (472,221),'Cincinnati',),
                ( (403,150),'Louisvlle',),
                ( (540,302),'Columbus',),
                ( (255,163),'Evansville',),
                ( (78,166),'St. Louis',),
                ( (324,273),'Indianapolis',),
                ( (131,257),'Springfield',),
                ( (252,386),'Chicago',),
                ( (128,361),'Peoria',),
                ( (400,372),'Fort Wayne',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 50241
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(23774,10709),
             mapcutSize=(3456,2304),
             mapFinalSize=(720,480),
             mapMilesSize=(340,272),
             datacutType='radar.us',
             datacutCoordinate=(2513,974),
             datacutSize=(423,282),
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
              ( ( (370,352),'69',),
                ( (435,214),'74',),
                ( (348,141),'65',),
                ( (534,343),'75',),
                ( (239,252),'70',),
                ( (94,316),'74',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (370,352),'69',),
                ( (435,214),'74',),
                ( (348,141),'65',),
                ( (534,343),'75',),
                ( (239,252),'70',),
                ( (94,316),'74',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (400,334),),
                ( (273,208),),
                ( (540,272),),
                ( (501,203),),
                ( (149,328),),
                ( (374,240),),
                ( (314,282),),
                ( (177,245),),
                ( (199,146),),
                ( (357,93),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (400,334),),
                ( (273,208),),
                ( (540,272),),
                ( (501,203),),
                ( (149,328),),
                ( (374,240),),
                ( (314,282),),
                ( (177,245),),
                ( (199,146),),
                ( (357,93),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (420,337),'Muncie',),
                ( (142,211),'Bloomington',),
                ( (512,293),'Dayton',),
                ( (521,206),'Cincinnati',),
                ( (117,349),'Danville',),
                ( (334,223),'Flat Rock',),
                ( (262,303),'Indianapolis',),
                ( (54,248),'Terre Haute',),
                ( (148,129),'Washington',),
                ( (377,96),'Louisville',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (420,337),'Muncie',),
                ( (142,211),'Bloomington',),
                ( (512,293),'Dayton',),
                ( (521,206),'Cincinnati',),
                ( (117,349),'Danville',),
                ( (334,223),'Flat Rock',),
                ( (262,303),'Indianapolis',),
                ( (54,248),'Terre Haute',),
                ( (148,129),'Washington',),
                ( (377,96),'Louisville',),
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
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.NationalLdl_RadarSatellite','Config.1.Local_RadarSatelliteComposite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.NationalLdl_DopplerRadar','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('airportId','1',['CVG','IND','SDF',])
wxdata.setInterestList('coopId','1',['72412024','72421000','72421059','72423000','72428000','72429000','72432000','72434000','72438000','72438026','72438029','72438048','72438068','72439000','72530000','72532000','72533000','72638041','74465033','74466005','74466030','74468006','74468026','74468028','74468031','74468032',])
wxdata.setInterestList('indexId','1',['KGEZ',])
wxdata.setInterestList('pollenId','1',['IND',])
wxdata.setInterestList('obsStation','1',['KGEZ','T72421000','T72421059','T72423000','T72423003','T72428000','T72432000','T72434000','T72438000','T72438012','T72438026','T72438029','T72438038','T72438048','T72438068','T72438070','T72439000','T72530000','T72532000','T72533000','T74468006','T74468023','T74468026','T74468028','T74468029','T74468031','T74468032',])
wxdata.setInterestList('climId','1',['127999',])
wxdata.setInterestList('zone','1',['INZ056',])
wxdata.setInterestList('aq','1',['in004',])
wxdata.setInterestList('skiId','1',['304003','616006',])
wxdata.setInterestList('county','1',['INC145',])
dsm.set('Config.1.countyNameList',[('INC145','Shelby'),], 0)
#
dsm.set('dmaCode','527', 0)
dsm.set('secondaryObsStation','KGEZ', 0)
dsm.set('primaryClimoStation','127999', 0)
dsm.set('primaryIndexId','KGEZ', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','IN', 0)
dsm.set('primaryAqStation','in004', 0)
dsm.set('primPollenSiteName','Indianapolis', 0)
dsm.set('expRev','3778825', 0)
dsm.set('primaryCoopId','74468031', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','IND', 0)
dsm.set('primaryCounty','INC145', 0)
dsm.set('primaryObsStation','T74468031', 0)
dsm.set('primaryLat',39.36388, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','IND', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-85.825, 0)
dsm.set('primaryForecastName','Flat Rock', 0)
dsm.set('primaryZone','INZ056', 0)
dsm.set('climoRegion','3', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST CABLE COMMUNICATIONS,', 0)
dsm.set('headendId','022500', 0)
dsm.set('msoName','COMCAST COMMUNICATIONS', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST CABLE COMMUNICATIONS,', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - FLAT ROCK - DOM', 0)
dsm.set('affiliateNumber','09461', 0)
dsm.set('zipCode','46176', 0)
dsm.set('Config.1.irdAddress','0000315595907127', 0)
dsm.set('Config.1.starId','TWCD02040071', 0)
dsm.set('Config.1.irdSlave','0', 0)
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
d.airportId = ['IND','CVG','SDF',]
d.airportLocName = ['Indianapolis','Cincinnati','Louisville',]
d.obsStation = ['T72438000','T72421000','T72423000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['616006','304003',]
d.coopId = ['72638041','72412024',]
d.resortName = ['Crystal Mtn, MI','Winterplace, WV',]
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
#
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.2')
scmtRemove('Config.1.Ldl_HurricaneWatch')
scmtRemove('Config.1.Local_NWSHeadlines')
scmtRemove('Config.1.NationalLdl_5DayForecast.4')
scmtRemove('Config.1.NationalLdl_5DayForecast.1')
scmtRemove('Config.1.TimeTemp_Default')
scmtRemove('Config.1.NationalLdl_WeatherBulletin.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.Local_SchoolDayWeather')
scmtRemove('Config.1.Ldl_3DayForecast')
scmtRemove('Config.1.Local_AirQualityForecast')
scmtRemove('Config.1.Local_Tides')
scmtRemove('Config.1.Local_GetawayForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.3')
scmtRemove('Config.1.Local_Almanac')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.0')
scmtRemove('Config.1.Local_RecordHighLow')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.5')
scmtRemove('Config.1.Ldl_CurrentObs.1')
scmtRemove('Config.1.Local_Climatology')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.1')
scmtRemove('Config.1.Fcst_ExtendedForecast')
scmtRemove('Config.1.Local_TrafficOverview')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.5')
scmtRemove('Config.1.Local_MarineForecast')
scmtRemove('Config.1.Fcst_DaypartForecast')
scmtRemove('Config.1.Ldl_CurrentObs.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.Ldl_AirportDelayConditions')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.2')
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.NationalLdl_5DayForecast.2')
scmtRemove('Config.1.Local_TextForecast')
scmtRemove('Config.1.Ldl_CurrentObs.0')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.Local_LocalObservations')
scmtRemove('Config.1.Local_HeatSafetyTips')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.0')
scmtRemove('Config.1.Ldl_StarIDMessage')
scmtRemove('Config.1.NationalLdl_5DayForecast.5')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.3')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.Local_CurrentConditions')
scmtRemove('Config.1.Ldl_CurrentObs.2')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.1')
scmtRemove('Config.1.Ldl_HourlyForecast')
scmtRemove('Config.1.Local_ExtendedForecast')
scmtRemove('Config.1.Local_7DayForecast')
scmtRemove('Config.1.Cc_CurrentConditions')
scmtRemove('Config.1.NationalLdl_5DayForecast.0')
scmtRemove('Config.1.Local_TrafficFlow')
scmtRemove('Config.1.Ldl_Almanac')
scmtRemove('Config.1.Ldl_UVForecast')
scmtRemove('Config.1.Local_TrafficReport')
scmtRemove('Config.1.Ldl_Almanac.1')
scmtRemove('Config.1.Ldl_DailyForecast.1')
scmtRemove('Config.1.Local_OutdoorActivityForecast')
scmtRemove('Config.1.NationalLdl_5DayForecast.3')
scmtRemove('Config.1.Ldl_AirQualityForecast')
scmtRemove('Config.1.Ldl_TravelForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.4')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.4')
scmtRemove('Config.1.Local_EventForecast')
scmtRemove('Config.1.Local_DaypartForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.Fcst_TextForecast')
scmtRemove('Config.1.Ldl_DailyForecast')
#
d = twc.Data()
d.obsStation = 'T74468031'
d.locName = 'FLAT ROCK'
d.heatIndexThreshold = 100
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.3', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.3', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.5', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.5', d, 0, 1)
#
d = twc.Data()
d.locName = 'Flat Rock'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '74468031'
d.prodLabel = 'UV Index'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 1
d.locName = ['Flat Rock','Columbus','Milford',]
d.coopId = ['74468031','72438048','74468032',]
dsm.set('Config.1.Ldl_DailyForecast.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048',]
d.locName = ['Columbus',]
d.coopId = ['72438048',]
dsm.set('Config.1.NationalLdl_5DayForecast.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['FLAT ROCK',]
d.coopId = ['74468031',]
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Flat Rock','Columbus','Milford',]
d.coopId = ['74468031','72438048','74468032',]
dsm.set('Config.1.Ldl_DailyForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.5', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.5', d, 0, 1)
#
#
d = twc.Data()
d.zone = 'INZ056'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74468031','KGEZ',]
d.dataTypes = ['SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Shelbyville','Flat Rock','Shelbyville',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['Hope',]
d.zone = 'INZ056'
dsm.set('Config.1.NationalLdl_WeatherBulletin.0', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '74468031'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['Flat Rock',]
d.coopId = ['74468031',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.0', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecast.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.3', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.3', d, 0, 1)
#
d = twc.Data()
d.location = 'FLAT ROCK'
d.coopId = '74468031'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Flat Rock'
d.hrsGrid = (((0, 4), 6, 12, 18), ((4, 8), 9, 12, 18), ((8, 11), 12, 15, 18), ((11, 14), 15, 18, 21), ((14, 17), 18, 21, 24), ((17, 20), 21, 24, 30), ((20, 24), 30, 36, 42),)
d.coopId = '74468031'
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'FLAT ROCK'
d.coopId = '74468031'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468032',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Milford',]
d.primaryObsProduct = 0
dsm.set('Config.1.Ldl_CurrentObs.2', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031','KGEZ',]
d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
d.coopId = '74468031'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['Flat Rock',]
dsm.set('Config.1.NationalLdl_CurrentConditions.0', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['IND',]
d.obsStation = ['T72438000',]
d.locName = ['Indianapolis Int\'l',]
d.displayFlag = [1,]
d.prodLabel = 'Airport'
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['Flat Rock',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468032',]
d.locName = ['Milford',]
d.coopId = ['74468032',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecast.5', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.5', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.5', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74468032',]
d.locName = ['Milford',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['FLAT ROCK',]
dsm.set('Config.1.NationalLdl_RadarSatellite', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468032',]
d.locName = ['Milford',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.2', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.4', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.4', d, 0, 1)
#
d = twc.Data()
d.locName = 'Flat Rock'
d.coopId = '74468031'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['Flat Rock',]
d.coopId = ['74468031',]
dsm.set('Config.1.NationalLdl_5DayForecast.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_DaypartForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Flat Rock'
d.coopId = '74468031'
d.prodLabel = '3 Day'
dsm.set('Config.1.Ldl_3DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.4', d, 0, 1)
#
#
d = twc.Data()
d.url = ['','','',]
d.locNameList = ['Monticello, IN','Deer Creek, IN','Indiana Dunes, IN',]
d.coopId = ['74466005','74466030','74465033',]
dsm.set('Config.1.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Central Indiana'
d.startDate = (1,1)
d.endDate = (12,31)
d.prodLabel = 'Air Quality'
d.aq = 'in004'
dsm.set('Config.1.Ldl_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.4', d, 0, 1)
#
#
d = twc.Data()
d.locName = ['Central Indiana',]
d.actionDayPhrase = 'Knozone Action Day'
d.aq = ['in004',]
dsm.set('Config.1.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 8
d.locName = 'FLAT ROCK'
d.coopId = '74468031'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468032',]
d.locName = ['Milford',]
d.coopId = ['74468032',]
dsm.set('Config.1.NationalLdl_5DayForecast.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','T74468031','KGEZ',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74468031','KGEZ',]
d.locName = ['Shelbyville','FLAT ROCK','SHELBYVILLE',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Columbus',]
d.primaryObsProduct = 0
dsm.set('Config.1.Ldl_CurrentObs.1', d, 0, 1)
#
#
d = twc.Data()
d.crawlRate = 3
dsm.set('Config.1.Ldl_HurricaneWatch', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048','T72438038','T72438012','T74468029','T74468032','T72438070','T72438029','T74468023',]
d.locName = ['Columbus','Edinburgh','Franklin','Greensburg','Milford','Rushville','Shelbyville','Westport',]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048',]
d.locName = ['Columbus',]
d.coopId = ['72438048',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.1', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecast.4', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.4', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.4', d, 0, 1)
#
d = twc.Data()
d.trafficActive = 0
d.trafficReverseActive = [1,1,1,1,1,1,]
d.prodLabel = 'Traffic'
d.routes=[]
d.routeDisplayTime=[]
dsm.set('Config.1.Ldl_TrafficTripTimes', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74468031','KGEZ',]
d.dataTypes = ['StarId', 'SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp', 'Dewpoint', 'Pressure', 'Ceiling', 'Visibility', 'MTDPrecip']
d.prodLabel = 'Now'
d.obsLocName = ['Shelbyville','Flat Rock','Shelbyville',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.3', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74468031',]
d.locName = ['FLAT ROCK',]
dsm.set('Config.1.NationalLdl_DopplerRadar', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048',]
d.locName = ['Columbus',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T74468031'
d.climId = '127999'
d.latitude = 39.52
d.longitude = -85.78
d.dataTypes = ['Sunrise', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Flat Rock'
dsm.set('Config.1.Ldl_Almanac.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72438048',]
d.locName = ['Columbus',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T74468031'
d.climId = '127999'
d.latitude = 39.52
d.longitude = -85.78
d.dataTypes = ['Sunrise', 'AvgHiLo', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Flat Rock'
dsm.set('Config.1.Ldl_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.displayMessage = 1
dsm.set('Config.1.Ldl_StarIDMessage', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
d.coopId = ['',]
dsm.set('Config.1.NationalLdl_5DayForecastSmall.3', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_DaypartForecastSmall.3', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['T74468031','KGEZ',]
d.locName = ['Flat Rock','Shelbyville',]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Flat Rock'
d.coopId = '74468031'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Cincinnati','Louisville','Dayton',]
d.coopId = ['72421000','72423000','72429000',]
d.prodLabel = 'Travel'
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.climId = '127999'
d.latitude = 39.52
d.longitude = -85.78
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Flat Rock'
d.coopId = '74468031'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 0
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 0
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 1
d.activeLocal_RecordHighLow = 0
d.activeLocal_Satellite = 0
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 0
d.activeLocal_TrafficFlow = 0
d.activeLocal_TrafficOverview = 0
d.activeLocal_TrafficReport = 0
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
d = [[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
[             [(0,00),(0,59),'NationalLdl.nationalLdlUp',],
             [(1,00),(1,59),'NationalLdl.nationalLdlUp',],
             [(2,00),(2,59),'NationalLdl.nationalLdlUp',],
             [(3,00),(3,59),'NationalLdl.nationalLdlUp',],
             [(4,00),(4,59),'NationalLdl.nationalLdlUp',],
             [(5,00),(5,59),'NationalLdl.nationalLdlUp',],
             [(6,00),(6,59),'NationalLdl.nationalLdlUp',],
             [(7,00),(7,59),'NationalLdl.nationalLdlUp',],
             [(8,00),(8,59),'NationalLdl.nationalLdlUp',],
             [(9,00),(9,59),'NationalLdl.nationalLdlUp',],
             [(10,00),(10,59),'NationalLdl.nationalLdlUp',],
             [(11,00),(11,59),'NationalLdl.nationalLdlUp',],
             [(12,00),(12,59),'NationalLdl.nationalLdlUp',],
             [(13,00),(13,59),'NationalLdl.nationalLdlUp',],
             [(14,00),(14,59),'NationalLdl.nationalLdlUp',],
             [(15,00),(15,59),'NationalLdl.nationalLdlUp',],
             [(16,00),(16,59),'NationalLdl.nationalLdlUp',],
             [(17,00),(17,59),'NationalLdl.nationalLdlUp',],
             [(18,00),(18,59),'NationalLdl.nationalLdlUp',],
             [(19,00),(19,59),'NationalLdl.nationalLdlUp',],
             [(20,00),(20,59),'NationalLdl.nationalLdlUp',],
             [(21,00),(21,59),'NationalLdl.nationalLdlUp',],
             [(22,00),(22,59),'NationalLdl.nationalLdlUp',],
             [(23,00),(23,59),'NationalLdl.nationalLdlUp',],
],
]
dsm.set('Config.1.Playlist.NationalLdl.scheduleA', d, 0)
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,0,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,4,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUp', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimationSmall',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',0,12,12,4,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',0,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',0,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',1,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',1,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',2,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',2,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',3,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',3,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',4,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',4,20,20,10,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',5,16,16,8,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',5,20,20,10,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpB', d, 0)
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
('CurrentConditions',0,8,11,4,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,8,10,6,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,9,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,6,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,6,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,10,14,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,12,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,16,0,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,3,3,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,10,3,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,10,12,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,12,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,0,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,4,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpSoCali', d, 0)
ds.commit()
d = twc.Data()
d.prodPrefix = 'NationalLdl'
d.childPrefixes = ['Logo']
d.units = 'seconds'
d.loadHeuristic = 'loadPriority_v1'
d.overHeuristic = 'overPriority_v1'
d.underHeuristic = 'underPriority_v1'
d.playlist=[
('IntroAnimation',0,2,2,2,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,6,24,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,4,12,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,16,16,4,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,10,10,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,10,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('Void',0,1,600,1,1,1,0,["nationalLdlLogo1"]),
]
dsm.set('Config.1.Playlist.NationalLdl.nationalLdlUpNConus', d, 0)
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
('Climatology',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,10,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('GetawayForecast',0,8,10,7,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,12,16,12,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,8,8,7,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,7,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,7,11,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,7,12,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,5,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,4,1,1,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,14,16,12,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,10,4,["tag1", "bkgMusic1", "ldl1"]),
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
('7DayForecast',0,10,16,10,1,1,1,["tag1", "bkgMusic1", "ldl1"]),
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
d = [
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
    [[(0,0), (23,59), 'NationalLdl.nationalLdlUpB',],],
]
dsm.set('Config.1.Playlist.NationalLdl.scheduleB', d, 0)
## End of SCMT Configuration
#
ds.commit()
Log.info('scmt config finished')
# Finished generation on Mon May 03 14:37:15 GMT 2010
