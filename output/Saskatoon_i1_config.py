# IntelliStar Configuration
# Generated for: SASKATOON
# Lat/Lon: 53.01, -110.07
# ============================================================

Log.info('scmt config started')

def scmtRemove(key):
    try:
        dsm.remove(key)
    except:
        pass

import os
dsm.set('scmt_configType', 'domestic',0)
dsm.set('scmt.ProductTypes',['Animated_Logo_Sponsor','Copy_Split','Custom','Logo_Sponsor', 'Dealer'], 0)

# ============================================================
# Interest Lists
# ============================================================
wxdata.setInterestList('airportId','1',[])
        wxdata.setInterestList('coopId','1',['71866000', '71876000', '71869000', '71456000', '71865000', '71871005', '71102002'])
        wxdata.setInterestList('indexId','1',[''])
        #wxdata.setInterestList('pollenId','1',[])
        wxdata.setInterestList('obsStation','1',['T71866000', 'T71876000', 'T71869000', 'T71456000', 'T71865001', 'T71871005', 'T71102002'])
        wxdata.setInterestList('climId','1',['CNST71866', 'CNTR71876', 'CNUK71869', 'CNSC71865'])
        wxdata.setInterestList('zone','1',['065100', '066260', '065263', '065343', '065641', '066223', '075256'])
        #wxdata.setInterestList('aq','1',[])
        wxdata.setInterestList('skiId','1',[])
        wxdata.setInterestList('county','1',['CCC999'])

# ============================================================
# Metadata Settings
# ============================================================
dsm.set('Config.1.countyNameList',[('CCC999', 'Dummy  County')], 0)
dsm.set('dmaCode','None', 0)
dsm.set('secondaryObsStation','T71876000', 0)
dsm.set('primaryClimoStation','CNST71866', 0)
dsm.set('primaryIndexId','', 0)
dsm.set('ThemeOverride','standard', 0)
dsm.set('stateCode','SK', 0)
dsm.set('primaryAqStation','None', 0)
dsm.set('primPollenSiteName','Saskatoon', 0)
dsm.set('primaryCoopId','71866000', 0)
dsm.set('Config.1.PlaylistOverride','DefaultUS', 0)
dsm.set('wda','', 0)
dsm.set('primaryCounty','CCC999', 0)
dsm.set('primaryObsStation','T71866000', 0)
dsm.set('hasTraffic',0, 0)
dsm.set('primaryPollenStation','', 0)
dsm.set('Config.1.Clock','scmt.clock', 0)
dsm.set('primaryLon',-110.07, 0)
dsm.set('primaryLat',53.01, 0)
dsm.set('primaryForecastName','Saskatoon', 0)
dsm.set('primaryZone','065100', 0)
dsm.set('climoRegion','3', 0)
dsm.set('Config.1.SevereClock','scmt_severe.clock', 0)
dsm.set('countryCode','CA', 0)

# ============================================================
# Airport Data
# ============================================================
scmtRemove('Config.1.Tag.General.airportData')
d = twc.Data()
d.airportId = []
d.airportLocName = []
d.obsStation = []
dsm.set('Config.1.Tag.General.airportData', d, 0, 1)

# ============================================================
# Current Conditions Products
# ============================================================

        d = twc.Data()
        d.obsStation = ['T71866000']
        d.locName = ['Saskatoon']
        d.elementDuration = 6
        dsm.set('Config.1.Cc_CurrentConditions', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000']
        d.locName = ['Saskatoon']
        d.activeVocalCue = 1
        d.activeVocal = 1
        dsm.set('Config.1.Local_CurrentConditions', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000']
        d.schedule = [((11,20,16,0,0), (11,23,16,0,0)),((12,16,16,0,0), (1,4,16,0,0)),((5,25,16,0,0), (9,1,16,0,0)),]
        d.coopId = '71866000'
        dsm.set('Config.1.Local_SchoolDayWeather', d, 0, 1)
        #
        d = twc.Data()
        d.climId = 'CNST71866'
        d.latitude = 53.01
        d.longitude = -110.07
        dsm.set('Config.1.Ldl_SunriseSunset', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000']
        d.timeDuration = 5
        d.tempDuration = 8
        dsm.set('Config.1.TimeTemp_Default', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000']
        d.obsLocName = ['Saskatoon']
        dsm.set('Config.1.Ldl_CurrentApparentTemp', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000']
        d.obsLocName = ['Saskatoon']
        dsm.set('Config.1.Ldl_CurrentMTDPrecip', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = 'T71866000'
        d.climId = ['CNST71866']
        d.latitude = 53.01
        d.longitude = -110.07
        d.locName = 'SASKATOON'
        d.coopId = '71866000'
        dsm.set('Config.1.Local_Climatology', d, 0, 1)
        #
        d = twc.Data()
        d.obsStation = ['T71866000', 'T71876000', 'T71869000', 'T71456000', 'T71865001', 'T71871005', 'T71102002']
        d.locName = ['Saskatoon', 'North Battleford', 'PRINCE ALBERT', 'Melfort', 'Wynyard', 'Waseca', 'Rivercourse']
        dsm.set('Config.1.Local_LocalObservations', d, 0, 1)
        

# ============================================================
# Forecast Products
# ============================================================

        d = twc.Data()
        d.locName = 'Saskatoon'
        d.coopId = '71866000'
        dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
        #
        d = twc.Data()
        d.location = 'SASKATOON'
        d.coopId = '71866000'
        d.activeVocalCue = 1
        d.activeVocal = 1
        dsm.set('Config.1.Local_ExtendedForecast', d, 0, 1)
        #
        d = twc.Data()
        d.locName = 'SASKATOON'
        d.coopId = '71866000'
        d.activeVocalCue = 1
        dsm.set('Config.1.Local_7DayForecast', d, 0, 1)
        #
        d = twc.Data()
        d.minPageDuration = 8
        d.locName = 'SASKATOON'
        d.coopId = '71866000'
        d.maxPageDuration = 14
        d.activeVocalCue = 1
        d.activeVocal = 1
        dsm.set('Config.1.Local_TextForecast', d, 0, 1)
        #
        d = twc.Data()
        d.locName = 'Saskatoon'
        d.coopId = '71866000'
        dsm.set('Config.1.Fcst_ExtendedForecast', d, 0, 1)
        #
        d = twc.Data()
        d.locName = 'Saskatoon'
        d.coopId = '71866000'
        dsm.set('Config.1.Fcst_TextForecast', d, 0, 1)
        #
        ds.commit()
        dsm.set('Config.1.Ldl_HourlyForecast', d, 0, 1)
        dsm.set('Config.1.Ldl_Shortcast', d, 0, 1)
        dsm.set('Config.1.Ldl_SummaryForecast', d, 0, 1)
        

Log.info('scmt config completed')