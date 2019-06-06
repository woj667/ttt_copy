# window.py

from Button import *

class Menu:

    def __init__(self):

        """ win is the GraphWin to display the board.
            Before using class Board, define it:
            win = GraphWin("name",width, height)
            gameBoard = Board(win)"""

        self.objectList = []

    def draw(self, win):

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # ...with welcome text
        text0 = Text(Point(3, 6.25), "MENU")
        text0.draw(self.win)

        text1 = Text(Point(3, 5.5), "Choose your oponent:")
        text1.draw(self.win)

        text2 = Text(Point(3, 2.75), "or")
        text2.draw(self.win)

        # activate PVP button
        self.pvp = Button(self.win, Point(3, 4), 2, 1, "PVP")
        self.pvp.activate()

        # activate PVB button
        self.pvb = Button(self.win, Point(3, 1.5), 2, 1, "PVB")
        self.pvb.activate()

        # activate BVB button
        self.bvb = Button(self.win, Point(3, 0), 2, 1, "BVB")
        self.bvb.activate()

        self.objectList += [text0, text1, text2, self.pvp, self.pvb, self.bvb]

    def undraw(self):
        for object in self.objectList:
            object.undraw()

    def getMode(self):

        mode = ""
        while mode == "":
            p = self.win.getMouse()
            if self.pvp.clicked(p):
                mode = "pvp"
            elif self.pvb.clicked(p):
                mode = "pvb"
            elif self.bvb.clicked(p):
                mode = "bvb"

        return mode

class Board:

    def __init__(self):

        """ win is the GraphWin to display the board.
            Before using class Board, define it:
            win = GraphWin("name",width, height)
            gameBoard = Board(win)"""

        self.objectList = []

    def draw(self, win):

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # draw vertical lines
        line1 = Line(Point(2, 0), Point(2, 6)).draw(self.win)
        line2 = Line(Point(4, 0), Point(4, 6)).draw(self.win)

        # draw horizontal lines
        line3 = Line(Point(0, 4), Point(6, 4)).draw(self.win)
        line4 = Line(Point(0, 2), Point(6, 2)).draw(self.win)

        # send initial message to user
        self.message = Text(Point(3, -0.5), "O starts!")
        self.message.draw(self.win)

        self.objectList += [self.message, line1, line2, line3, line4]

    def setMsg(self, msg):
        self.message.setText(msg)

    def undraw(self):
        for object in self.objectList:
            object.undraw()

class Scoreboard:

    def __init__(self):
        """ win is the GraphWin to display the board.
            Before using class Board, define it:
            win = GraphWin("name",width, height)
            gameBoard = Board(win)"""

        # initial scores
        self.scoresPlayerO = []
        self.scoresPlayerX = []
        self.sumPlayerO = 0
        self.sumPlayerX = 0

        self.objectList = []

    def draw(self, win):

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # draw header
        text0 = Text(Point(3, 6.25), "SCOREBOARD")
        text0.draw(win)

        # draw labels
        text1 = Text(Point(1, 5), "PlayerO")
        text1.draw(win)
        text2 = Text(Point(1, 4.5), "PlayerX")
        text2.draw(win)

        # draw list of last 5 scores
        text3 = Text(Point(3, 5), str(self.scoresPlayerO))
        text3.draw(win)
        text4 = Text(Point(3, 4.5), str(self.scoresPlayerX))
        text4.draw(win)

        # draw summary
        text5 = Text(Point(5, 5), str(self.sumPlayerO))
        text5.draw(win)
        text6 = Text(Point(5, 4.5), str(self.sumPlayerX))
        text6.draw(win)

        # draw system buttons
        self.quit = Button(win, Point(1.5, 0.5), 2, 1, "quit")
        self.quit.activate()

        self.retry = Button(win, Point(4.5, 0.5), 2, 1, "retry")
        self.retry.activate()

        self.objectList += [text0,text1, text2, text3, text4, text5, text6, self.quit, self.retry]

    def appendScore(self, scoreList, lastScore):

        for i in range(4):
            scoreList[i] = scoreList[i + 1]
        scoreList[4] = lastScore

        for score in scoreList:
            if score == 3:
                self.scoresPlayerO.append(3)
                self.sumPlayerO += 3
                self.scoresPlayerX.append(0)
            elif score == -3:
                self.scoresPlayerO.append(0)
                self.scoresPlayerX.append(3)
                self.sumPlayerX += 3
            elif score in [0, 1]:
                self.scoresPlayerO.append(score)
                self.sumPlayerO += score
                self.scoresPlayerX.append(score)
                self.sumPlayerX += score

    def undraw(self):
        for object in self.objectList:
            object.undraw()

    def getMode(self):

        # wait for action
        buttonPressed = ""
        while buttonPressed == "":
            p = self.win.getMouse()
            if self.quit.clicked(p):
                buttonPressed = "close"
            elif self.retry.clicked(p):
                buttonPressed = "retry"

        return buttonPressed

class FigureX:

    def __init__(self, win):
        self.win = win
        self.objectList = []

    def draw(self, zone):

        """Draw X in a given zone"""
        x, y = midpoint(zone)

        lineX1 = Line(Point(x - 0.6, y - 0.6), Point(x + 0.6, y + 0.6)).draw(self.win)
        lineX2 = Line(Point(x - 0.6, y + 0.6), Point(x + 0.6, y - 0.6)).draw(self.win)

        self.objectList += [lineX1, lineX2]

    def undraw(self):
        for object in self.objectList:
            object.undraw()

class FigureO:

    def __init__(self, win):
        self.win = win
        self.objectList = []

    def draw(self, zone):

        """Draw O in a given zone"""
        x, y = midpoint(zone)

        circle = Circle(Point(x, y), 0.7).draw(self.win)
        self.objectList.append(circle)

    def undraw(self):
        for object in self.objectList:
            object.undraw()

def midpoint(zone):

    if zone == 'dl':
        x, y = 1, 1
    elif zone == 'dm':
        x, y = 3, 1
    elif zone == 'dr':
        x, y = 5, 1
    elif zone == 'ml':
        x, y = 1, 3
    elif zone == 'mm':
        x, y = 3, 3
    elif zone == 'mr':
        x, y = 5, 3
    elif zone == 'ul':
        x, y = 1, 5
    elif zone == 'um':
        x, y = 3, 5
    elif zone == 'ur':
        x, y = 5, 5

    return x, y

def test():
    win = GraphWin("class Board test", 300, 300)
    gameBoard = Board(win)

    for zone in ['ul','mm','dr']:
        gameBoard.drawX(zone)

    win.getMouse()
    win.close()

if __name__ == "__main__": test()