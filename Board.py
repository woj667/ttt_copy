# Board.py

from graphics import *


class Board:

    def __init__(self, win):

        """ win is the GraphWin to display the board.
            Before using class Board, define it:
            win = GraphWin("name",width, height)
            gameBoard = Board(win)"""

        self.win = win

        # Prepare board
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # draw vertical lines
        self.line1 = Line(Point(2, 0), Point(2, 6)).draw(self.win)
        self.line2 = Line(Point(4, 0), Point(4, 6)).draw(self.win)

        # draw horizontal lines
        self.line3 = Line(Point(0, 4), Point(6, 4)).draw(self.win)
        self.line4 = Line(Point(0, 2), Point(6, 2)).draw(self.win)

        # send initial message to user
        self.message = Text(Point(3, -0.5), "O starts!")
        self.message.draw(win)

        self.objectList = [self.message, self.line1, self.line2, self.line3, self.line4]
        
    def drawX(self, zone):

        """Draw X in a given zone"""

        self.zone = zone

        if   self.zone == 'dl':          self.x, self.y = 1, 1
        elif self.zone == 'dm':          self.x, self.y = 3, 1
        elif self.zone == 'dr':          self.x, self.y = 5, 1
        elif self.zone == 'ml':          self.x, self.y = 1, 3
        elif self.zone == 'mm':          self.x, self.y = 3, 3
        elif self.zone == 'mr':          self.x, self.y = 5, 3
        elif self.zone == 'ul':          self.x, self.y = 1, 5
        elif self.zone == 'um':          self.x, self.y = 3, 5
        elif self.zone == 'ur':          self.x, self.y = 5, 5

        self.lineX1 = Line(Point(self.x - 0.6, self.y - 0.6), Point(self.x + 0.6, self.y + 0.6)).draw(self.win)
        self.lineX2 = Line(Point(self.x - 0.6, self.y + 0.6), Point(self.x + 0.6, self.y - 0.6)).draw(self.win)

        self.objectList.append(self.lineX1)
        self.objectList.append(self.lineX2)

    def drawO(self, zone):

        """Draw O in a given zone"""

        self.zone = zone

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
        self.objectList.append(self.circle)

    def setMsg(self, msg):
        self.message.setText(msg)

    def undraw(self):
        for object in self.objectList:
            object.undraw()
def test():
    win = GraphWin("class Board test", 300, 300)
    gameBoard = Board(win)

    for zone in ['ul','mm','dr']:
        gameBoard.drawX(zone)

    win.getMouse()
    win.close()

if __name__ == "__main__": test()