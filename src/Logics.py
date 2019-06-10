# logics.py

from random import randrange
from vendor.graphics import *

class Logics:

    def __init__(self):

        # initial game settings
        zone = ""  # zone belongs to ['dl', 'dm', 'dr', 'ml', 'mm', 'mr', 'ul', 'um', 'ur']
        gameover = ""  # condition to leave event loop
        score = 0  # score of current game

        self.zone = "empty"
        self.zList = [self.zone]


    def getTurn(self, lastScore):

        """Decide who starts the game"""

        if lastScore == 3:
            turn = 1
        elif lastScore == -3:
            turn = 0
        else:
            turn = randrange(0, 2, 1)  # randomize if first game or draw

        return  turn

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

    def requestZone(self, win, mode, modeList):
        while self.zone in self.zList:  # ask for a new zone as long it is not clicked
            if mode == modeList:    p = Point(randrange(0, 6), randrange(0, 6))
            else:                   p = win.getMouse()
            self.zone = self.getZone(p)
        return self.zone

    def getMouse(self):
        pass

    def __isWinner(self, list):
        if ('dl' in list and 'dm' in list and 'dr' in list) or ('ml'in list and 'mm' in list and 'mr' in list) or ('ul' in list and 'um' in list and 'ur' in list) or ('ul' in list and 'ml' in list and 'dl' in list) or ('um' in list and 'mm' in list and 'dm' in list) or ('ur' in list and 'mr' in list and 'dr' in list) or ('ul' in list and 'mm' in list and 'dr' in list) or ('dl' in list and 'mm' in list and 'ur' in list):
            return 1
        else:
            return 0

    def appendZone(self, zone):
        self.zList.append(self.zone)

    def listZones(self):
        return self.zList

    def getStatus(self, playerO, playerX):
        if self.__isWinner(playerO.listZones()):
            gameover = "Player O wins!"
            score = 3
        elif self.__isWinner(playerX.listZones()):
            gameover = "Player X wins!"
            score = -3
        elif len(self.zList) == 9:      # each zone occupied
            gameover = "Draw!"
            score = 1
        else:
            gameover = ""
            score = 0

        return gameover, score

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

    def move(self):
        pass