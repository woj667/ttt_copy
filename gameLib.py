# gameLib.py

from graphics import *
from Board import *
from Player import *
from Logics import *
from Button import *

def gameMenu():
    win = GraphWin("Menu", 300, 300)
    win.setCoords(-1.0, -1.0, 7.0, 7.0)
    pvp = Button(win, Point(3,4),2,1,"PVP")
    pvp.activate()

    pvb = Button(win, Point(3,1), 2,1,"PVB")
    pvb.activate()

    mode = ""
    while mode == "":
        p = win.getMouse()
        if pvp.clicked(p):   mode = "pvp"
        elif pvb.clicked(p): mode = "pvb"

    win.close()
    return mode

def gameStart(win):
    # draw game board
    gameBoard = Board(win)

    # create game logic
    gameLogics = Logics()

    # create Players' instances
    playerO = Player()
    playerX = Player()

    # possible elements of zoneList = ['dl', 'dm', 'dr', 'ml', 'mm', 'mr', 'ul', 'um', 'ur']
    pOzones = pXzones = []

    # init game
    turn = 0
    zone = ""
    gameover = ""

    return gameLogics, gameBoard, playerO, playerX, pOzones, pXzones, turn, zone, gameover