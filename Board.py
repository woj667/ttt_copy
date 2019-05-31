# Board.py

from graphics import *


class Board:
    def __init__(self, win):

        self.win = win
        self.zone = ''

        # Prepare board
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        message = Text(Point(3, -0.5), "X starts!")
        message.draw(self.win)

        # draw vertical lines
        Line(Point(2, 0), Point(2, 6)).draw(self.win)
        Line(Point(4, 0), Point(4, 6)).draw(self.win)

        # draworizontal lines
        Line(Point(0, 4), Point(6, 4)).draw(self.win)
        Line(Point(0, 2), Point(6, 2)).draw(self.win)

    def getZone(self, p):

        self.xcoord = p.getX()
        self.ycoord = p.getY()

        if 0 <= self.xcoord < 2:
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

    def drawX(self):

        if   self.zone == 'dl':            self.x, self.y = 1, 1
        elif self.zone == 'dm':          self.x, self.y = 3, 1
        elif self.zone == 'dr':          self.x, self.y = 5, 1
        elif self.zone == 'ml':          self.x, self.y = 1, 3
        elif self.zone == 'mm':          self.x, self.y = 3, 3
        elif self.zone == 'mr':          self.x, self.y = 5, 3
        elif self.zone == 'ul':          self.x, self.y = 1, 5
        elif self.zone == 'um':          self.x, self.y = 3, 5
        elif self.zone == 'ur':          self.x, self.y = 5, 5

        self.line1 = Line(Point(self.x - 0.6, self.y - 0.6), Point(self.x + 0.6, self.y + 0.6)).draw(self.win)
        self.line2 = Line(Point(self.x - 0.6, self.y + 0.6), Point(self.x + 0.6, self.y - 0.6)).draw(self.win)


    def drawO(self):

        if   self.zone == 'dl':            self.x, self.y = 1, 1
        elif self.zone == 'dm':          self.x, self.y = 3, 1
        elif self.zone == 'dr':          self.x, self.y = 5, 1
        elif self.zone == 'ml':          self.x, self.y = 1, 3
        elif self.zone == 'mm':          self.x, self.y = 3, 3
        elif self.zone == 'mr':          self.x, self.y = 5, 3
        elif self.zone == 'ul':          self.x, self.y = 1, 5
        elif self.zone == 'um':          self.x, self.y = 3, 5
        elif self.zone == 'ur':          self.x, self.y = 5, 5

        self.circle = Circle(Point(self.x, self.y), 0.7).draw(self.win)

