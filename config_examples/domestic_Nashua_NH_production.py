# Created on Thu Dec 30 18:15:14 GMT 2010
Log.info('scmt config started')
# EXP: 14202
# VIW: 12726
# CLN: 572
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
# MAP: 78532
# NationalLdl_DopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32493,13445),
             mapcutSize=(1440,821),
             mapFinalSize=(193,110),
             mapMilesSize=(134,92),
             datacutType='radar.us',
             datacutCoordinate=(3581,1309),
             datacutSize=(176,101),
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
              ( ( (101,55),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (101,55),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (49,61),'Nashua',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (49,61),'Nashua',),
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
# MAP: 74144
# Radar_LocalDoppler (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32340,13446),
             mapcutSize=(1440,822),
             mapFinalSize=(240,137),
             mapMilesSize=(134,92),
             datacutType='radar.us',
             datacutCoordinate=(3562,1310),
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
              ( ( (150,69),),
                ( (154,92),),
                ( (187,27),),
                ( (116,17),),
              ),
             ),
             (
               ('locatorDotSmall',0,1,0,),
              ( ( (150,69),),
                ( (154,92),),
                ( (187,27),),
                ( (116,17),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',14,(229,229,229,205),1,0,0,(20,20,20,68),1,0,0,),
              ( ( (98,75),'Nashua',),
                ( (130,108),'Manchester',),
                ( (154,40),'Boston',),
                ( (127,17),'Worcester',),
              ),
             ),
             (
               ('Interstate-Bold',14,(229,229,229,255),1,0,0,(20,20,20,68),2,0,0,),
              ( ( (98,75),'Nashua',),
                ( (130,108),'Manchester',),
                ( (154,40),'Boston',),
                ( (127,17),'Worcester',),
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
# MAP: 52115
# Local_MetroDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32570,13384),
             mapcutSize=(1440,960),
             mapFinalSize=(720,480),
             mapMilesSize=(134,107),
             datacutType='radar.us',
             datacutCoordinate=(3590,1302),
             datacutSize=(177,118),
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
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (388,328),'101',),
                ( (534,192),'128',),
              ),
             ),
             (
               (('interstateSignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (307,141),'495',),
                ( (477,199),'95',),
                ( (68,339),'91',),
                ( (338,354),'93',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (388,328),'101',),
                ( (534,192),'128',),
                ( (228,175),'2',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (307,141),'495',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (228,175),'2',),
              ),
             ),
             (
               (('usHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (351,211),'3',),
              ),
             ),
             (
               (('usHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (351,211),'3',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (477,199),'95',),
                ( (68,339),'91',),
                ( (338,354),'93',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('airplaneOutline',0,2,1,),
              ( ( (474,120),),
                ( (354,292),),
              ),
             ),
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (399,290),),
                ( (297,271),),
                ( (355,254),),
                ( (353,319),),
                ( (541,335),),
                ( (135,303),),
                ( (460,128),),
                ( (248,99),),
                ( (256,196),),
                ( (209,194),),
                ( (433,230),),
                ( (390,211),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (399,290),),
                ( (297,271),),
                ( (355,254),),
                ( (353,319),),
                ( (541,335),),
                ( (135,303),),
                ( (460,128),),
                ( (248,99),),
                ( (256,196),),
                ( (209,194),),
                ( (433,230),),
                ( (390,211),),
              ),
             ),
             (
               ('airplane',0,1,0,),
              ( ( (474,120),),
                ( (354,292),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (419,293),'Derry',),
                ( (222,274),'Milford',),
                ( (375,257),'Nashua',),
                ( (233,322),'Manchester',),
                ( (489,318),'Portsmouth',),
                ( (113,324),'Keene',),
                ( (432,149),'Boston',),
                ( (142,102),'Worcester',),
                ( (216,217),'Fitchburg',),
                ( (125,197),'Gardner',),
                ( (453,233),'Lawrence',),
                ( (366,194),'Lowell',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (419,293),'Derry',),
                ( (222,274),'Milford',),
                ( (375,257),'Nashua',),
                ( (233,322),'Manchester',),
                ( (489,318),'Portsmouth',),
                ( (113,324),'Keene',),
                ( (432,149),'Boston',),
                ( (142,102),'Worcester',),
                ( (216,217),'Fitchburg',),
                ( (125,197),'Gardner',),
                ( (453,233),'Lawrence',),
                ( (366,194),'Lowell',),
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
# MAP: 74513
# Local_RadarSatelliteComposite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4698,2124),
             mapcutSize=(936,624),
             mapFinalSize=(720,480),
             mapMilesSize=(879,590),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1521,751),
             datacutSize=(481,322),
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
# MAP: 79828
# NationalLdl_RadarSatellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4649,2111),
             mapcutSize=(1072,611),
             mapFinalSize=(193,110),
             mapMilesSize=(1006,578),
             datacutType='radarSatellite.us',
             datacutCoordinate=(1496,744),
             datacutSize=(551,315),
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
# MAP: 75136
# Local_MetroObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32476,13563),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(147,117),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroObservationMap', d, 0)
#
# Local_MetroObservationMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (427,214),'101',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (229,83),'2',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (594,345),'95',),
                ( (80,142),'91',),
                ( (246,293),'89',),
                ( (318,314),'93',),
              ),
             ),
        ],
  obsValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( 'T72604029',(147,344),),
                ( 'T72605000',(342,258),),
                ( 'T72605016',(342,166),),
                ( 'T72605034',(375,347),),
                ( 'T72605047',(514,302),),
                ( 'T72605067',(532,208),),
                ( 'T74484017',(162,175),),
                ( 'T74490035',(478,111),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'T72604029',(150,308),),
                ( 'T72605000',(345,222),),
                ( 'T72605016',(345,130),),
                ( 'T72605034',(378,311),),
                ( 'T72605047',(517,266),),
                ( 'T72605067',(535,172),),
                ( 'T74484017',(165,139),),
                ( 'T74490035',(481,75),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (107,380),'Lebanon',),
                ( (304,294),'Concord',),
                ( (283,202),'Manchester',),
                ( (339,383),'Laconia',),
                ( (463,338),'Rochester',),
                ( (472,244),'Portsmouth',),
                ( (135,211),'Keene',),
                ( (431,147),'Lawrence',),
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
# MAP: 71427
# Local_MetroForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(32476,13563),
             mapcutSize=(1584,1056),
             mapFinalSize=(720,480),
             mapMilesSize=(147,117),
             vectors=['mercator.us.ushighways.vg','mercator.us.counties.vg','mercator.us.states.vg','mercator.us.coastlines.vg','mercator.us.statehighways.vg','mercator.us.otherroutes.vg','mercator.us.interstates.vg',],
)
wxdata.setMapData('Config.1.Local_MetroForecastMap', d, 0)
#
# Local_MetroForecastMap (PRODUCT DATA)
#
d = twc.Data(
  labeledTiffImage = [
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (427,214),'101',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (229,83),'2',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (318,314),'93',),
                ( (594,345),'95',),
                ( (80,142),'91',),
                ( (246,293),'89',),
              ),
             ),
        ],
  fcstIcon = [
             (
               (0,2,0,),
              ( ( '72604029',(150,308),),
                ( '72605000',(345,222),),
                ( '72605016',(345,130),),
                ( '72605034',(378,311),),
                ( '72605047',(517,266),),
                ( '72605067',(535,172),),
                ( '74484017',(165,139),),
                ( '74490035',(481,75),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '72604029',(147,344),),
                ( '72605000',(342,258),),
                ( '72605016',(342,166),),
                ( '72605034',(375,347),),
                ( '72605047',(514,302),),
                ( '72605067',(532,208),),
                ( '74484017',(162,175),),
                ( '74490035',(478,111),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (107,380),'Lebanon',),
                ( (304,294),'Concord',),
                ( (283,202),'Manchester',),
                ( (339,383),'Laconia',),
                ( (463,338),'Rochester',),
                ( (472,244),'Portsmouth',),
                ( (135,211),'Keene',),
                ( (431,147),'Lawrence',),
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
# MAP: 48106
# Local_RegionalForecastMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(31084,12606),
             mapcutSize=(6544,4363),
             mapFinalSize=(720,480),
             mapMilesSize=(597,478),
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
              ( ( '71610000',(226,277),),
                ( '72509000',(264,76),),
                ( '72518000',(98,92),),
                ( '72606000',(308,157),),
                ( '72617000',(129,206),),
                ( '72619031',(407,305),),
                ( '72619048',(394,216),),
              ),
             ),
        ],
  fcstValue = [
             (
               ('Interstate-BlackCondensed',38,(212,212,0,255),1,0,'temp',1,(),2,0,),
              ( ( '71610000',(223,313),),
                ( '72509000',(261,112),),
                ( '72518000',(95,128),),
                ( '72606000',(305,193),),
                ( '72617000',(126,242),),
                ( '72619031',(404,341),),
                ( '72619048',(391,252),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (167,349),'Sherbrooke',),
                ( (228,148),'Boston',),
                ( (63,164),'Albany',),
                ( (264,229),'Portland',),
                ( (74,278),'Burlington',),
                ( (349,377),'Millinocket',),
                ( (359,288),'Bangor',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalForecastMap', d, 0)
# MAP: 50670
# Local_RegionalObservationMap (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(31084,12606),
             mapcutSize=(6544,4363),
             mapFinalSize=(720,480),
             mapMilesSize=(597,478),
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
              ( ( 'CYSC',(223,313),),
                ( 'T72509000',(261,112),),
                ( 'T72518000',(95,128),),
                ( 'T72606000',(305,193),),
                ( 'T72617000',(126,242),),
                ( 'T72619031',(404,341),),
                ( 'T72619048',(391,252),),
              ),
             ),
        ],
  obsIcon = [
             (
               (0,2,0,),
              ( ( 'CYSC',(226,277),),
                ( 'T72509000',(264,76),),
                ( 'T72518000',(98,92),),
                ( 'T72606000',(308,157),),
                ( 'T72617000',(129,206),),
                ( 'T72619031',(407,305),),
                ( 'T72619048',(394,216),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',24,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (167,349),'Sherbrooke',),
                ( (228,148),'Boston',),
                ( (63,164),'Albany',),
                ( (264,229),'Portland',),
                ( (74,278),'Burlington',),
                ( (349,377),'Millinocket',),
                ( (359,288),'Bangor',),
              ),
             ),
        ],
  vector = [
             (( 4,(20,20,20,255),1,),(('states',),),),
             (( 2,(20,20,20,255),1,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_RegionalObservationMap', d, 0)
# MAP: 71820
# Local_Satellite (MAP DATA)
#
d = twc.Data(mapName='lambert.us.tif',
             mapcutCoordinate=(4471,1491),
             mapcutSize=(2196,1464),
             mapFinalSize=(720,480),
             mapMilesSize=(2006,1349),
             datacutType='satellite.us',
             datacutCoordinate=(1180,452),
             datacutSize=(590,394),
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
              ( ( (240,260),),
                ( (201,209),),
                ( (185,186),),
                ( (181,115),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Bold',21,(212,212,212,255),1,0,0,(),2,0,0,),
              ( ( (166,273),'Boston',),
                ( (98,220),'New York',),
                ( (76,167),'Philadelphia',),
                ( (103,111),'Norfolk',),
              ),
             ),
        ],
  vector = [
             (( 2,(20,20,20,255),2,),(('states',),),),
             (( 2,(20,20,20,255),2,),(('coastlines',),),),
             ],
)
dsm.set('Config.1.Local_Satellite', d, 0)
# MAP: 53179
# Local_RegionalDopplerRadar (MAP DATA)
#
d = twc.Data(mapName='mercator.us.bfg',
             mapcutCoordinate=(31726,12821),
             mapcutSize=(3124,2083),
             mapFinalSize=(720,480),
             mapMilesSize=(292,233),
             datacutType='radar.us',
             datacutCoordinate=(3487,1233),
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
              ( ( (466,337),'95',),
                ( (211,260),'91',),
                ( (324,348),'93',),
                ( (274,327),'89',),
              ),
             ),
             (
               (('stateHwySignOutline',0,2,1,),'Interstate-BoldCondensed',16,(212,212,212,255),0,0,(),),
              ( ( (443,117),'3',),
                ( (285,204),'2',),
              ),
             ),
             (
               (('stateHwySign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (443,117),'3',),
                ( (285,204),'2',),
              ),
             ),
             (
               (('interstateSign',0,1,0,),'Interstate-BoldCondensed',18,(212,212,212,255),0,0,(),),
              ( ( (466,337),'95',),
                ( (211,260),'91',),
                ( (324,348),'93',),
                ( (274,327),'89',),
              ),
             ),
        ],
  tiffImage = [
             (
               ('locatorDotOutline',0,2,1,),
              ( ( (358,245),),
                ( (63,222),),
                ( (197,104),),
                ( (335,306),),
                ( (434,286),),
                ( (355,108),),
                ( (404,185),),
                ( (305,173),),
              ),
             ),
             (
               ('locatorDot',0,1,0,),
              ( ( (358,245),),
                ( (63,222),),
                ( (197,104),),
                ( (335,306),),
                ( (434,286),),
                ( (355,108),),
                ( (404,185),),
                ( (305,173),),
              ),
             ),
        ],
  textString = [
             (
               ('Interstate-Black',22,(212,212,212,205),1,-35,0,(20,20,20,128),2,0,0,),
              ( ( (378,248),'Nashua',),
                ( (83,225),'Albany',),
                ( (106,107),'Hartford',),
                ( (249,309),'Concord',),
                ( (454,289),'Portsmouth',),
                ( (308,91),'Providence',),
                ( (424,188),'Boston',),
                ( (199,176),'Worcester',),
              ),
             ),
             (
               ('Interstate-Black',22,(212,212,212,255),1,-35,0,(),1,0,0,),
              ( ( (378,248),'Nashua',),
                ( (83,225),'Albany',),
                ( (106,107),'Hartford',),
                ( (249,309),'Concord',),
                ( (454,289),'Portsmouth',),
                ( (308,91),'Providence',),
                ( (424,188),'Boston',),
                ( (199,176),'Worcester',),
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
wxdata.setInterestList('radarSatellite.us.cuts','1',['Config.1.Local_RadarSatelliteComposite','Config.1.NationalLdl_RadarSatellite',])
wxdata.setInterestList('satellite.us.cuts','1',['Config.1.Local_Satellite',])
wxdata.setInterestList('radar.us.cuts','1',['Config.1.NationalLdl_DopplerRadar','Config.1.Radar_LocalDoppler','Config.1.Local_MetroDopplerRadar','Config.1.Local_RegionalDopplerRadar',])
#
wxdata.setInterestList('mapData','1',['mercator.us','lambert.us',])
#
wxdata.setInterestList('imageData','1',['radarSatellite.us','radar.us','satellite.us',])
# END OF MAPS
# commit for map stuff to avoid missing updates
ds.commit()
#
wxdata.setInterestList('tideStation','1',['E8421897','E8423745',])
wxdata.setInterestList('airportId','1',['BOS','MHT','PWM',])
wxdata.setInterestList('coopId','1',['71610000','72202000','72507000','72508000','72509000','72518000','72604029','72605000','72605016','72605024','72605034','72605036','72605047','72605067','72606000','72613012','72617000','72619031','72619048','74484017','74484049','74490035','74490044','74490056',])
wxdata.setInterestList('indexId','1',['KASH',])
wxdata.setInterestList('obsStation','1',['CYSC','KASH','T72509000','T72518000','T72604029','T72605000','T72605015','T72605016','T72605021','T72605034','T72605038','T72605047','T72605067','T72605069','T72606000','T72617000','T72619031','T72619048','T74484017','T74490035','T74490044','T74490055','T74490056',])
wxdata.setInterestList('climId','1',['275712',])
wxdata.setInterestList('metroId','1',['18',])
wxdata.setInterestList('zone','1',['NHZ012',])
wxdata.setInterestList('aq','1',['ma014','nh007','nh008',])
wxdata.setInterestList('zone.cwf','1',['ANZ150',])
wxdata.setInterestList('skiId','1',['603009','603017',])
wxdata.setInterestList('county','1',['NHC011',])
dsm.set('Config.1.countyNameList',[('NHC011','Hillsborough'),], 0)
#
dsm.set('dmaCode','506', 0)
dsm.set('secondaryObsStation','KASH', 0)
dsm.set('primaryClimoStation','275712', 0)
dsm.set('primaryIndexId','KASH', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','NH', 0)
dsm.set('primaryAqStation','nh008', 0)
dsm.set('expRev','4339650', 0)
dsm.set('primaryCoopId','74490056', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','MHT', 0)
dsm.set('primaryCounty','NHC011', 0)
dsm.set('primaryObsStation','T74490056', 0)
dsm.set('primaryLat',42.70833, 0)
dsm.set('hasTraffic',0, 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-71.46139, 0)
dsm.set('primaryForecastName','Nashua', 0)
dsm.set('primaryZone','NHZ012', 0)
dsm.set('climoRegion','1', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('onAirName','COMCAST', 0)
dsm.set('headendId','021965', 0)
dsm.set('msoName','COMCAST COMMUNICATIONS', 0)
dsm.set('countryCode','US', 0)
dsm.set('cableSystemName','COMCAST', 0)
dsm.set('msoCode','01174', 0)
dsm.set('headendName','DOM - NASHUA - DOM', 0)
dsm.set('affiliateNumber','21478', 0)
dsm.set('zipCode','50820', 0)
dsm.set('Config.1.irdAddress','0000315595395011', 0)
dsm.set('Config.1.bcNetMask','255.255.255.252', 0)
dsm.set('Config.1.bcConnectMethod','E', 0)
dsm.set('Config.1.irdSlave','0', 0)
dsm.set('Config.1.starId','TWCD12030110', 0)
dsm.set('Config.1.bcExtIpAddress','24.128.113.146', 0)
dsm.set('Config.1.bcGateWay','24.128.113.145', 0)
dsm.set('Config.1.bcIpAddress','24.128.113.146', 0)
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
d.airportId = ['MHT','BOS','PWM',]
d.airportLocName = ['Manchester','Boston/Logan','Portland',]
d.obsStation = ['T72605016','T72509000','T72606000',]
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)
#
scmtRemove('Config.1.Tag.General.snowboardData')
d = twc.Data()
d.permCode = ['603009','603017',]
d.coopId = ['72605024','72605036',]
d.resortName = ['Gunstock, NH','Mt Sunapee, NH',]
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
scmtRemove('Config.1.Ldl_HurricaneWatch')
scmtRemove('Config.1.NationalLdl_5DayForecast.4')
scmtRemove('Config.1.Ldl_UVForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditions.3')
scmtRemove('Config.1.Local_HeatSafetyTips')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.1')
scmtRemove('Config.1.Local_RecordHighLow')
scmtRemove('Config.1.Ldl_3DayForecast')
scmtRemove('Config.1.NationalLdl_5DayForecast.2')
scmtRemove('Config.1.NationalLdl_5DayForecast.3')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.0')
scmtRemove('Config.1.NationalLdl_5DayForecast.5')
scmtRemove('Config.1.Ldl_AirportDelayConditions')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.5')
scmtRemove('Config.1.NationalLdl_WeatherBulletin.0')
scmtRemove('Config.1.Ldl_HourlyForecast')
scmtRemove('Config.1.Ldl_DailyForecast')
scmtRemove('Config.1.Local_TrafficFlow')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.4')
scmtRemove('Config.1.TimeTemp_Default')
scmtRemove('Config.1.Ldl_CurrentObs.0')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.2')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.0')
scmtRemove('Config.1.Local_TrafficReport')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.1')
scmtRemove('Config.1.Ldl_CurrentObs.3')
scmtRemove('Config.1.Local_GetawayForecast')
scmtRemove('Config.1.Local_LocalObservations')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.2')
scmtRemove('Config.1.Fcst_ExtendedForecast')
scmtRemove('Config.1.Ldl_AirQualityForecast')
scmtRemove('Config.1.Ldl_CurrentObs.1')
scmtRemove('Config.1.Ldl_CurrentObs.2')
scmtRemove('Config.1.Ldl_TravelForecast')
scmtRemove('Config.1.Ldl_Almanac')
scmtRemove('Config.1.Ldl_StarIDMessage')
scmtRemove('Config.1.NationalLdl_CurrentConditions.0')
scmtRemove('Config.1.Fcst_TextForecast')
scmtRemove('Config.1.Local_Tides')
scmtRemove('Config.1.NationalLdl_CurrentConditions.1')
scmtRemove('Config.1.Local_TextForecast')
scmtRemove('Config.1.Local_OutdoorActivityForecast')
scmtRemove('Config.1.Local_Climatology')
scmtRemove('Config.1.Local_DaypartForecast')
scmtRemove('Config.1.Local_CurrentConditions')
scmtRemove('Config.1.Fcst_DaypartForecast')
scmtRemove('Config.1.Ldl_DailyForecast.1')
scmtRemove('Config.1.NationalLdl_5DayForecast.0')
scmtRemove('Config.1.Local_AirQualityForecast')
scmtRemove('Config.1.Local_MarineForecast')
scmtRemove('Config.1.Ldl_Almanac.1')
scmtRemove('Config.1.Cc_CurrentConditions')
scmtRemove('Config.1.Local_NWSHeadlines')
scmtRemove('Config.1.Local_Almanac')
scmtRemove('Config.1.Local_SchoolDayWeather')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.4')
scmtRemove('Config.1.Local_7DayForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditionsSmall.3')
scmtRemove('Config.1.Local_TrafficOverview')
scmtRemove('Config.1.NationalLdl_5DayForecast.1')
scmtRemove('Config.1.Ldl_TrafficTripTimes')
scmtRemove('Config.1.Local_EventForecast')
scmtRemove('Config.1.Local_ExtendedForecast')
scmtRemove('Config.1.NationalLdl_CurrentConditions.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.4')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.5')
scmtRemove('Config.1.NationalLdl_CurrentConditions.2')
scmtRemove('Config.1.NationalLdl_5DayForecastSmall.3')
#
d = twc.Data()
d.obsStation = 'T74490056'
d.locName = 'NASHUA'
d.heatIndexThreshold = 97
dsm.set('Config.1.Local_HeatSafetyTips', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['KASH',]
d.climId = ['275712',]
d.latitude = 42.78
d.longitude = -71.48
d.locName = ['Nashua',]
d.coopId = ['74490056',]
d.fcstHighOffset = 0
d.fcstLowOffset = 0
dsm.set('Config.1.Local_RecordHighLow', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['',]
d.locName = ['',]
dsm.set('Config.1.NationalLdl_CurrentConditions.3', d, 0, 1)
#
#
d = twc.Data()
d.tideStation = ['E8423745','E8421897',]
d.locName = ['Portsmouth','Dover Point',]
dsm.set('Config.1.Local_Tides', d, 0, 1)
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
d.locName = 'Nashua'
d.startDate = (5,1)
d.endDate = (9,30)
d.coopId = '74490056'
d.prodLabel = 'UV Index'
dsm.set('Config.1.Ldl_UVForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 1
d.locName = ['Nashua','Manchester','Hudson',]
d.coopId = ['74490056','72605016','74490044',]
dsm.set('Config.1.Ldl_DailyForecast.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72605016',]
d.locName = ['Manchester',]
d.coopId = ['72605016',]
dsm.set('Config.1.NationalLdl_5DayForecast.1', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.1', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.1', d, 0, 1)
#
d = twc.Data()
d.locName = ['NASHUA',]
d.coopId = ['74490056',]
dsm.set('Config.1.Local_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Nashua','Manchester','Hudson',]
d.coopId = ['74490056','72605016','74490044',]
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
d.zone = 'NHZ012'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_NWSHeadlines', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74490056','KASH',]
d.dataTypes = ['SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Nashua','Nashua','Nashua',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['Nashua',]
d.zone = 'NHZ012'
dsm.set('Config.1.NationalLdl_WeatherBulletin.0', d, 0, 1)
#
#
d = twc.Data()
d.coopId = '74490056'
dsm.set('Config.1.Local_OutdoorActivityForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['Nashua',]
d.coopId = ['74490056',]
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
d.location = 'NASHUA'
d.coopId = '74490056'
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Nashua'
d.hrsGrid = (((0, 4), 6, 12, 18), ((4, 8), 9, 12, 18), ((8, 11), 12, 15, 18), ((11, 14), 15, 18, 21), ((14, 17), 18, 21, 24), ((17, 20), 21, 24, 30), ((20, 24), 30, 36, 42),)
d.coopId = '74490056'
dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'NASHUA'
d.coopId = '74490056'
d.activeVocalCue = 1
dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490044',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Hudson',]
d.primaryObsProduct = 0
dsm.set('Config.1.Ldl_CurrentObs.2', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056','KASH',]
d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
d.coopId = '74490056'
dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['Nashua',]
dsm.set('Config.1.NationalLdl_CurrentConditions.0', d, 0, 1)
#
#
d = twc.Data()
d.airportId = ['MHT','BOS',]
d.obsStation = ['T72605016','T72509000',]
d.locName = ['Manchester Arpt','Logan Int\'l',]
d.displayFlag = [1,1,]
d.prodLabel = 'Airport'
dsm.set('Config.1.Ldl_AirportDelayConditions', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['Nashua',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.0', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490044',]
d.locName = ['Hudson',]
d.coopId = ['74490044',]
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
d.obsStation = ['T74490044',]
d.locName = ['Hudson',]
dsm.set('Config.1.NationalLdl_CurrentConditions.2', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['NASHUA',]
dsm.set('Config.1.NationalLdl_RadarSatellite', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490044',]
d.locName = ['Hudson',]
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
d.locName = 'Nashua'
d.coopId = '74490056'
dsm.set('Config.1.Fcst_DaypartForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['Nashua',]
d.coopId = ['74490056',]
dsm.set('Config.1.NationalLdl_5DayForecast.0', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_DaypartForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.0', d, 0, 1)
dsm.set('Config.1.NationalLdl_TextForecast.0', d, 0, 1)
#
d = twc.Data()
d.locName = 'Nashua'
d.coopId = '74490056'
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
d.locNameList = ['Green Mtns., VT','White Mtns., NH','Miami, FL',]
d.coopId = ['74484049','72613012','72202000',]
dsm.set('Config.1.Local_GetawayForecast', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Nashua'
d.startDate = (1,1)
d.endDate = (12,31)
d.prodLabel = 'Air Quality'
d.aq = 'nh008'
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
d.locName = ['Nashua','Stow','Manchester',]
d.actionDayPhrase = 'Ozone Action Day'
d.aq = ['nh008','ma014','nh007',]
dsm.set('Config.1.Local_AirQualityForecast', d, 0, 1)
#
#
d = twc.Data()
d.minPageDuration = 6
d.locName = 'NASHUA'
d.coopId = '74490056'
d.maxPageDuration = 14
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490044',]
d.locName = ['Hudson',]
d.coopId = ['74490044',]
dsm.set('Config.1.NationalLdl_5DayForecast.2', d, 0, 1)
#
ds.commit()
dsm.set('Config.1.NationalLdl_36HourForecast.2', d, 0, 1)
dsm.set('Config.1.NationalLdl_HourlyForecast.2', d, 0, 1)
#
d = twc.Data()
d.obsStation = ['SENSOR','T74490056','KASH',]
d.timeDuration = 5
d.tempDuration = 8
dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74490056','KASH',]
d.locName = ['Nashua','NASHUA','NASHUA',]
d.activeVocalCue = 1
d.activeVocal = 1
dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72605016',]
d.dataTypes = ['SkyTemp']
d.prodLabel = 'Now'
d.obsLocName = ['Manchester',]
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
d.obsStation = ['T72605000','T72605069','T74490044','T74490055','T72605016','T72605038','T72605015','T72605021',]
d.locName = ['Concord','Jaffrey','Hudson','Windham','Manchester','Milford','Hillsborough','Raymond',]
dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72605016',]
d.locName = ['Manchester',]
d.coopId = ['72605016',]
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
d.locName = 'NEW HAMPSHIRE COASTAL WATERS '
d.zone = 'ANZ150'
dsm.set('Config.1.Local_MarineForecast', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['SENSOR','T74490056','KASH',]
d.dataTypes = ['StarId', 'SkyTemp', 'Winds', 'Gusts', 'Humidity', 'ApparentTemp', 'Dewpoint', 'Pressure', 'Ceiling', 'Visibility', 'MTDPrecip']
d.prodLabel = 'Now'
d.obsLocName = ['Nashua','Nashua','Nashua',]
d.primaryObsProduct = 1
dsm.set('Config.1.Ldl_CurrentObs.3', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T74490056',]
d.locName = ['NASHUA',]
dsm.set('Config.1.NationalLdl_DopplerRadar', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72605016',]
d.locName = ['Manchester',]
dsm.set('Config.1.NationalLdl_CurrentConditions.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T74490056'
d.climId = '275712'
d.latitude = 42.78
d.longitude = -71.48
d.dataTypes = ['Sunrise', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Nashua'
dsm.set('Config.1.Ldl_Almanac.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'KASH'
d.climId = ['275712',]
d.latitude = 42.78
d.longitude = -71.48
d.locName = 'NASHUA'
d.coopId = '74490056'
dsm.set('Config.1.Local_Climatology', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = ['T72605016',]
d.locName = ['Manchester',]
dsm.set('Config.1.NationalLdl_CurrentConditionsSmall.1', d, 0, 1)
#
#
d = twc.Data()
d.obsStation = 'T74490056'
d.climId = '275712'
d.latitude = 42.78
d.longitude = -71.48
d.dataTypes = ['Sunrise', 'AvgHiLo', 'MTDPrecip', 'HourlyRain', 'HourlySnow']
d.prodLabel = 'Almanac'
d.obsLocName = 'Nashua'
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
d.obsStation = ['T74490056','KASH',]
d.locName = ['Nashua','Nashua',]
d.elementDuration = 6
dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Nashua'
d.coopId = '74490056'
dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
#
#
d = twc.Data()
d.dayOfs = 0
d.locName = ['Boston','Providence','Windsor Locks',]
d.coopId = ['72509000','72507000','72508000',]
d.prodLabel = 'Travel'
dsm.set('Config.1.Ldl_TravelForecast', d, 0, 1)
#
#
d = twc.Data()
d.climId = '275712'
d.latitude = 42.78
d.longitude = -71.48
dsm.set('Config.1.Local_Almanac', d, 0, 1)
#
#
d = twc.Data()
d.locName = 'Nashua'
d.coopId = '74490056'
dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
#
#
# Product statues:
d = twc.Data()
d.activeLocal_AirQualityForecast = 1
d.activeLocal_Climatology = 1
d.activeLocal_GetawayForecast = 1
d.activeLocal_HeatSafetyTips = 1
d.activeLocal_MarineForecast = 1
d.activeLocal_MetroDopplerRadar = 1
d.activeLocal_MetroForecastMap = 1
d.activeLocal_MetroObservationMap = 1
d.activeLocal_OutdoorActivityForecast = 1
d.activeLocal_RadarSatelliteComposite = 1
d.activeLocal_RecordHighLow = 1
d.activeLocal_Satellite = 1
d.activeLocal_SchoolDayWeather = 1
d.activeLocal_Tides = 1
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
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
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
('DaypartForecastSmall',1,16,16,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',1,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',2,16,16,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',2,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',3,16,16,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',3,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',4,16,16,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',4,20,20,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditionsSmall',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecastSmall',5,16,16,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecastSmall',5,20,20,0,0,1,0,["nationalLdlLogo1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,8,8,0,0,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,17,0,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,24,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,7,10,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,7,10,6,1,15,0,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,7,8,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,7,8,6,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,7,8,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,7,8,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,6,18,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,21,21,18,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,8,8,6,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,29,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,0,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,11,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,10,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,17,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,9,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,9,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,8,10,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,8,10,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,8,8,0,0,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,17,0,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,8,8,8,0,24,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,15,0,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,8,8,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,8,10,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,7,10,6,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,12,14,10,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,10,10,8,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,8,10,7,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,21,21,18,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,8,8,6,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,29,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,11,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,10,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,15,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,13,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,13,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,7,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,9,9,9,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,9,9,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,1,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,36,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,9,9,9,0,1,0,["nationalLdlLogo1"]),
('RadarSatellite',0,8,8,8,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,9,9,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,9,9,0,0,1,0,["nationalLdlLogo1"]),
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
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('DaypartForecast',0,30,30,30,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
('WeatherBulletin',0,5,5,0,0,1,0,["nationalLdlLogo1"]),
('DopplerRadar',0,8,8,4,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',0,12,12,12,0,1,0,["nationalLdlLogo1"]),
('HourlyForecast',0,0,0,0,0,1,0,["nationalLdlLogo1"]),
('TextForecast.1',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.2',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('TextForecast.3',0,18,18,3,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',0,11,11,11,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',1,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',1,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',1,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',2,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',2,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',2,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',3,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',3,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',3,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',4,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',4,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',4,11,11,0,0,1,0,["nationalLdlLogo1"]),
('CurrentConditions',5,12,12,0,0,1,0,["nationalLdlLogo1"]),
('36HourForecast',5,10,10,0,0,1,0,["nationalLdlLogo1"]),
('5DayForecast',5,11,11,0,0,1,0,["nationalLdlLogo1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,0,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,7,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,14,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,16,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,10,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,8,11,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,8,12,6,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,7,10,6,1,12,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,11,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,10,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,17,4,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,0,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,16,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,10,12,9,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,8,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,12,7,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,7,10,6,1,13,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,7,10,6,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,10,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,10,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
('NWSHeadlines.1',0,7,8,6,1,4,0,["tag1", "bkgMusic1", "ldl1"]),
('NWSHeadlines.2',0,7,7,6,1,5,0,["tag1", "bkgMusic1", "ldl1"]),
('CurrentConditions',0,8,11,6,1,3,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroObservationMap',0,7,10,6,1,6,0,["tag1", "bkgMusic1", "ldl1"]),
('LocalObservations',0,12,14,10,1,20,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalObservationMap',0,8,10,6,1,18,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalDopplerRadar',0,8,8,8,0,8,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroDopplerRadar',0,12,12,0,0,7,4,["tag1", "bkgMusic1", "ldl1"]),
('RadarSatelliteComposite',0,8,8,8,0,14,4,["tag1", "bkgMusic1", "ldl1"]),
('Climatology',0,8,10,7,1,15,3,["tag1", "bkgMusic1", "ldl1"]),
('Almanac',0,8,10,7,1,16,3,["tag1", "bkgMusic1", "ldl1"]),
('RecordHighLow',0,6,8,6,1,11,0,["tag1", "bkgMusic1", "ldl1"]),
('AirQualityForecast',0,7,10,6,1,14,0,["tag1", "bkgMusic1", "ldl1"]),
('MarineForecast',0,10,12,8,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('Tides',0,8,10,7,1,19,0,["tag1", "bkgMusic1", "ldl1"]),
('DaypartForecast',0,8,10,7,1,17,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.1',0,7,10,6,1,9,0,["tag1", "bkgMusic1", "ldl1"]),
('MetroForecastMap.2',0,7,10,6,1,10,6,["tag1", "bkgMusic1", "ldl1"]),
('TextForecast',0,28,36,24,0,1,0,["tag1", "bkgMusic1", "ldl1"]),
('7DayForecast',0,12,16,10,1,2,0,["tag1", "bkgMusic1", "ldl1"]),
('HeatSafetyTips',0,8,8,6,1,23,0,["tag1", "bkgMusic1", "ldl1"]),
('SchoolDayWeather',0,8,10,7,1,24,0,["tag1", "bkgMusic1", "ldl1"]),
('OutdoorActivityForecast',0,8,10,7,1,25,0,["tag1", "bkgMusic1", "ldl1"]),
('Satellite',0,20,20,8,0,22,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.1',0,8,10,6,1,21,0,["tag1", "bkgMusic1", "ldl1"]),
('RegionalForecastMap.2',0,8,10,6,1,26,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.1',0,7,11,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('GetawayForecast',0,8,10,7,1,27,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.2',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficOverview.3',0,10,11,8,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.1',0,7,12,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.2',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficReport.3',0,8,12,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('ExtendedForecast',0,10,12,8,1,28,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.1',0,7,10,5,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
('TrafficFlow.2',0,7,10,7,1,99,0,["tag1", "bkgMusic1", "ldl1"]),
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
# Finished generation on Thu Dec 30 18:15:16 GMT 2010
