# Bot.py
# class created to replace Player
# contains mirror classes
# instead of acquiring point draws random one

from random import randrange

class Bot:

    def __init__(self):
        self.zList = []

    def appendZone(self, zone):
        self.zone = zone
        self.zList.append(zone)

    def zoneList(self):
        return self.zList
