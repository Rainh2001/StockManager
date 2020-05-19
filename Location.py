import math

class Location:
    
    def __init__(self, address=None, coords=(None, None)):
        self.address = address
        self.lat = coords[0]
        self.long = coords[1]
        self.coords = coords

    def setAddress(self, address):
        self.address = address
        return address

    def setLatitude(self, latitude):
        self.latitude = latitude
        return latitude

    def setLongitude(self, longitude):
        self.longitude = longitude
        return longitude

    def setCoords(self, coords):
        self.coords = coords
        return coords

    def getCoordsString(self):
        coords = str(self.lat)
        coords += "S, " if self.lat < 0 else "N, "
        coords += str(self.long)
        coords += "W" if self.long < 0 else "E"
        return coords

    def getCoordsStringValue(self):
        coords = ""
        if(self.lat < 0): coords += "-"
        coords += str(self.lat) + ", "
        if(self.long < 0): coords += "-"
        coords += str(self.long)
        return coords
    
    def getStraightDistance(self, loc):

        if(not isinstance(loc, Location)):
            print("fail1")
            return None
        if(type(loc) is tuple):
            if(len(loc) < 2):
                return None

        R = 6371000
        locLat = 0
        locLong = 0

        if type(loc) is tuple:
            locLat = loc[0]
            locLong = loc[1]
        else:
            locLat = loc.lat
            locLong = loc.long

        lat1 = self.lat * math.pi/180
        lat2 = locLat * math.pi/180
        lat = (locLat - self.lat) * math.pi/180
        long = (locLong - self.long) * math.pi/180
        a = math.sin(lat/2) * math.sin(lat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(long/2) * math.sin(long/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c

        return d/1000

        
        
