import urllib2
import json

class GetData():
    """
        class stores the latest JSON CitiBike data in a dictionary
        with execution time and tabular data
    """
    
    def __init__(self):
        self.site = 'http://citibikenyc.com/stations/json'
        self.data = {}
        
    def read(self):
        json_data=urllib2.urlopen(self.site)
        self.data = json.load(json_data)


class Station():
    """
        stores the docking station data
    """
    def __init__(self, stationName, totalDocks, fullDocks, asOf, latitude, longitude):
        self.stationName = stationName
        self.totalDocks = totalDocks
        self.fullDocks = fullDocks
        self.pctFull = float(self.fullDocks)/self.totalDocks
        self.asOf = asOf
        self.latitude = latitude
        self.longitude = longitude
