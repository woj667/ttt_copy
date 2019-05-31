# logics.py

from graphics import *

class Logics:


    def __init__(self):
        self.zone = ""
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

    def isWinner(self, list):
        if ('dl' in list and 'dm' in list and 'dr' in list) or ('ml'in list and 'mm' in list and 'mr' in list) or ('ul' in list and 'um' in list and 'ur' in list) or ('ul' in list and 'ml' in list and 'dl' in list) or ('um' in list and 'mm' in list and 'dm' in list) or ('ur' in list and 'mr' in list and 'dr' in list) or ('ul' in list and 'mm' in list and 'dr' in list) or ('dl' in list and 'mm' in list and 'ur' in list):
            return 1
        else:
            return 0


    def appendZone(self, zone):
        self.zList.append(self.zone)

    def listZone(self):
        return self.zList

    def zoneFree(self):
        if self.zone in self.zList:
            return 0
        else:
            return 1
