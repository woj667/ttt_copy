# Player class

class Player:

    def __init__(self):
        self.zList = []

    def appendZone(self, zone):

        self.zone = zone
        self.zList.append(zone)

    def zoneList(self):
        return self.zList