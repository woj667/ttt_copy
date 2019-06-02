# Player class

class Player:

    def __init__(self):
        self.zList = []

    def getZone(self, p):

        self.xcoord = p.getX()
        self.ycoord = p.getY()

        if   0 <= self.xcoord < 2:
            if   0 <= self.ycoord < 2:     self.zone = 'dl'
            elif 2 <= self.ycoord < 4:     self.zone = 'ml'
            elif 4 <= self.ycoord < 6:     self.zone = 'ul'
        elif 2 <= self.xcoord < 4:
            if   0 <= self.ycoord < 2:     self.zone = 'dm'
            elif 2 <= self.ycoord < 4:     self.zone = 'mm'
            elif 4 <= self.ycoord < 6:     self.zone = 'um'
        elif 4 <= self.xcoord < 6:
            if   0 <= self.ycoord < 2:     self.zone = 'dr'
            elif 2 <= self.ycoord < 4:     self.zone = 'mr'
            elif 4 <= self.ycoord < 6:     self.zone = 'ur'

        return self.zone

    def appendZone(self, zone):

        self.zone = zone
        self.zList.append(zone)

    def listZones(self):
        return self.zList