import BikeData
import show

data = BikeData.GetData()
data.read()
def dirEval(direction, fullness, minFull):
    if direction == 'less':
        if fullness < minFull:
            return True
        else:
            return False
    else:
        if fullness < minFull:
            return False
        else:
            return True
        
def fullness(data, direction):
    if direction =='less':
        minFull = 100
    else:
        minFull = 0
    for row in data.data['stationBeanList']:
        fullness = row['availableDocks']/float(row['totalDocks'])
        if dirEval(direction, fullness, minFull):
##            print row['stationName']
##            print fullness, minFull
            minFull = fullness
            try: del emptiest
            except: pass
            fullest = BikeData.Station(row['stationName'],
                               row['totalDocks'],
                               (row['totalDocks'] - row['availableDocks']),
                                       data.data['executionTime'],
                                       row['latitude'],
                                       row['longitude']
                                        )
    return fullest
            


fullest = fullness(data, 'less')
emptiest = fullness(data, 'more')
centerLat = sum([fullest.latitude, emptiest.latitude])/2
centerLong = sum([fullest.longitude, emptiest.longitude])/2

mapReschuffel = show.Map(fullest.latitude, fullest.longitude,
                         emptiest.latitude, emptiest.longitude,
                         [centerLat,centerLong],
                         fullest.pctFull,
                         emptiest.pctFull
                         )
                         

mapReschuffel.write()
