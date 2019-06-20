# window.py

from src.Button import *


class UIComponent:
    def __init__(self, win):
        self.objectList = []
        self.win = win

    def draw(self):
        for obj in self.objectList:
            obj.draw(self.win)

    def undraw(self):
        for obj in self.objectList:
            obj.undraw()


class Menu(UIComponent):

    def __init__(self, win):

        # super();
        UIComponent.__init__(self, win)

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # ...with welcome text
        self.text0 = Text(Point(3, 6.25), "MENU")
        self.text1 = Text(Point(3, 5.5), "Choose your oponent:")
        self.text2 = Text(Point(3, 2.75), "or")

        # activate PVP button
        self.pvp = Button(self.win, Point(3, 4), 2, 1, "PVP")
        self.pvp.activate()

        # activate PVB button
        self.pvb = Button(self.win, Point(3, 1.5), 2, 1, "PVB")
        self.pvb.activate()

        # activate BVB button
        self.bvb = Button(self.win, Point(3, 0), 2, 1, "BVB")
        self.bvb.activate()

        self.objectList += [self.text0, self.text1, self.text2, self.pvp, self.pvb, self.bvb]

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


class Board(UIComponent):

    def __init__(self, win):
        # super();
        UIComponent.__init__(self, win)

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # draw vertical lines
        line1 = Line(Point(2, 0), Point(2, 6))
        line2 = Line(Point(4, 0), Point(4, 6))

        # draw horizontal lines
        line3 = Line(Point(0, 4), Point(6, 4))
        line4 = Line(Point(0, 2), Point(6, 2))

        # send initial message to user
        self.message = Text(Point(3, -0.5), "O starts!")
        #self.message.draw(self.win)

        self.objectList += [self.message, line1, line2, line3, line4]

    def setMsg(self, msg):
        self.message.setText(msg)


class Scoreboard(UIComponent):

    def __init__(self, win):
        # super();
        UIComponent.__init__(self, win)

        # initial scores
        self.scoresPlayerO = []
        self.scoresPlayerX = []
        self.sumPlayerO = 0
        self.sumPlayerX = 0

        self.win = win
        self.win.setCoords(-1.0, -1.0, 7.0, 7.0)

        # draw header
        text0 = Text(Point(3, 6.25), "SCOREBOARD")

        # draw labels
        text1 = Text(Point(1, 5), "PlayerO")
        text2 = Text(Point(1, 4.5), "PlayerX")

        # draw list of last 5 scores
        self.text3 = Text(Point(3, 5), "dummy")
        self.text4 = Text(Point(3, 4.5), "dummy")

        # draw summary
        self.text5 = Text(Point(5, 5), "dummy")
        self.text6 = Text(Point(5, 4.5), "dummy")

        # draw system buttons
        self.quit = Button(win, Point(1.5, 0.5), 2, 1, "quit")
        self.quit.activate()

        self.retry = Button(win, Point(4.5, 0.5), 2, 1, "retry")
        self.retry.activate()

        self.objectList += [text0, text1, text2, self.quit, self.retry]


    def updateScores(self):

        # draw list of last 5 scores
        self.text3.setText(str(self.scoresPlayerO))
        self.text4.setText(str(self.scoresPlayerX))

        # draw summary
        self.text5.setText(str(self.sumPlayerO))
        self.text6.setText(str(self.sumPlayerX))

        self.objectList += [self.text3, self.text4, self.text5, self.text6]



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

class FigureX(UIComponent):

    def __init__(self, win):
        # super();
        UIComponent.__init__(self, win)

    def draw(self, zone):

        """Draw X in a given zone"""
        x, y = midpoint(zone)

        lineX1 = Line(Point(x - 0.6, y - 0.6), Point(x + 0.6, y + 0.6)).draw(self.win)
        lineX2 = Line(Point(x - 0.6, y + 0.6), Point(x + 0.6, y - 0.6)).draw(self.win)

        self.objectList += [lineX1, lineX2]


class FigureO(UIComponent): #todo fix covered draw method

    def __init__(self, win):
        # super();
        UIComponent.__init__(self, win)

    def draw(self, zone):

        """Draw O in a given zone"""
        x, y = midpoint(zone)

        circle = Circle(Point(x, y), 0.7).draw(self.win)
        self.objectList.append(circle)

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