# gameLib.py

from src.window import Menu, Board, Scoreboard, FigureO, FigureX
from src.Logics import Logics, Player
from vendor.graphics import *
from random import randrange

def gameMenu(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    win = exchangeList[4]
    # ---------------------------

    # display window...
    menu = Menu()
    menu.draw(win)

    # ... and wait for button pess
    mode = menu.getMode()

    # undraw after all
    menu.undraw()

    # return game mode
    exchangeList[0] = mode

def gamePlay(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    mode = exchangeList[0]
    lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    win = exchangeList[4]
    # ---------------------------

    echangeListDict = { "mode": "BVB", "last_score": 2 }

    mode = echangeListDict["mode"]

    # display board
    gameBoard = Board()
    gameBoard.draw(win)

    # create logics
    gameLogics = Logics()

    # create Players' instances
    playerO = Player()
    playerX = Player()

    # create faceplates
    nought = FigureO(win)
    cross = FigureX(win)

    # initial game settings
    zone = "empty"               # zone belongs to ['dl', 'dm', 'dr', 'ml', 'mm', 'mr', 'ul', 'um', 'ur']
    gameover = ""           # condition to leave event loop
    score = 0               # score of current game

    # check who starts
    turn = gameLogics.getTurn(lastScore)

    # main event loop
    while gameover == "":

        turn += 1

        if turn % 2:
            # player's O turn
            while zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "bvb":
                    p = Point(randrange(0, 6), randrange(0, 6))
                else:
                    p = win.getMouse()
                zone = gameLogics.getZone(p)

            update(3)                           # time delay
            playerO.appendZone(zone)
            nought.draw(zone)
            gameBoard.setMsg("Player's X turn")  # after O is drawn, set message

        else:
            # player's X turn
            while zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "pvp":        p = win.getMouse()
                else:                    p = Point(randrange(0, 6), randrange(0, 6))
                zone = gameLogics.getZone(p)

            update(3)
            playerX.appendZone(zone)
            cross.draw(zone)
            gameBoard.setMsg("Player's O turn")

        gameLogics.appendZone(zone)  # append only when zone is clicked first time

        # check status
        gameover, score = gameLogics.getStatus(playerO, playerX)

        if gameover != "":  gameBoard.setMsg(gameover)

    win.getMouse()
    __undraw([gameBoard, nought, cross])

    exchangeList[1] = score

def gameScores(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    lastScore = exchangeList[1]
    scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    win = exchangeList[4]
    # ---------------------------

    # create scoreboard
    scoreboard = Scoreboard()

    # append lastScore to the scoreList
    scoreboard.appendScore(scoreList, lastScore)

    # draw obtained scores
    scoreboard.draw(win)

    # wait for action
    buttonPressed = scoreboard.getMode()

    # update button status
    exchangeList[3] = buttonPressed

    scoreboard.undraw()

def initExchangeData():

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    # win = exchangeList[4]
    # ---------------------------

    # init exchange data
    mode = ""
    lastScore = 0
    scoreList = []
    buttonPressed = "retry"
    win = GraphWin("Tic-Tac-Toe", 300, 300)

    # produce empty scoreboard
    __fillZeroes(scoreList, 5)

    exchangeList = [mode, lastScore, scoreList, buttonPressed, win]

    return exchangeList

def __fillZeroes(scoreList, zeroes):
    for i in range(zeroes):
        scoreList.append(0)

def __undraw(objectList):
    for object in objectList:
        object.undraw()