# gameLib.py

from graphics import *
from Board import *
from Player import *
from Logics import *
from Button import *
from random import randrange

def gameMenu(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]

    win = GraphWin("Menu", 300, 300)
    win.setCoords(-1.0, -1.0, 7.0, 7.0)

    Text(Point(3, 5.5), "Choose your oponent:").draw(win)
    Text(Point(3, 2.5), "or").draw(win)


    pvp = Button(win, Point(3,4),2,1,"PVP")
    pvp.activate()

    pvb = Button(win, Point(3,1.5), 2,1,"PVB")
    pvb.activate()

    bvb = Button(win, Point(3,0), 2,1,"BVB")
    bvb.activate()

    mode = ""
    while mode == "":
        p = win.getMouse()
        if pvp.clicked(p):   mode = "pvp"
        elif pvb.clicked(p): mode = "pvb"
        elif bvb.clicked(p): mode = "bvb"

    win.close()
    exchangeList[0] = mode
    #return mode

def gamePlay(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]]

    # open game board
    win = GraphWin("Tic-Tac-Toe", 300, 300)

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

    # main event loop
    while gameover == "":

        score = 0     # score of this game
        turn += 1

        if turn % 2:  # first loop iteration: turn = 1, "O" starst
            # player's O turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "bvb":
                    p = Point(randrange(0, 6), randrange(0, 6))
                elif mode == "pvp" or mode == "pvb":
                    p = win.getMouse()
                zone = gameLogics.getZone(p)

            update(3)
            playerO.appendZone(zone)
            pOzones = playerO.listZones()
            gameBoard.drawO(zone)
            gameBoard.setMsg("Player's X turn")  # after O is drawn, set message

        else:
            # player's X turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "pvb" or mode == "bvb":
                    p = Point(randrange(0, 6), randrange(0, 6))
                elif mode == "pvp":
                    p = win.getMouse()
                zone = gameLogics.getZone(p)

            update(3)
            playerX.appendZone(zone)
            pXzones = playerX.listZones()
            gameBoard.drawX(zone)
            gameBoard.setMsg("Player's O turn")

        gameLogics.appendZone(zone)  # append only when zone is clicked first time

        # check status
        if gameLogics.isWinner(pOzones):
            gameover = "Player O wins!"
            score = 3
        elif gameLogics.isWinner((pXzones)):
            gameover = "Player X wins!"
            score = -3
        elif turn == 9:
            gameover = "Draw!"
            score = 1

        if gameover != "":  gameBoard.setMsg(gameover)

    win.getMouse()
    win.close()

    exchangeList[1] = score
    #return score

def gameScores(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    lastScore = exchangeList[1]
    scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]

    win = GraphWin("Scoreboard", 300, 300)
    win.setCoords(-1.0, -1.0, 7.0, 7.0)

    scoresPlayerO = []
    scoresPlayerX = []
    sumPlayerO = 0
    sumPlayerX = 0

    # shift scores <<
    for i in range(4):
        scoreList[i] = scoreList[i+1]
    scoreList[4] = lastScore

    # build score table for each player
    for score in scoreList:

        if score == 3:
            scoresPlayerO.append(3)
            sumPlayerO += 3
            scoresPlayerX.append(0)
        elif score == -3:
            scoresPlayerO.append(0)
            scoresPlayerX.append(3)
            sumPlayerX += 3
        elif score in [0,1]:
            scoresPlayerO.append(score)
            sumPlayerO += score
            scoresPlayerX.append(score)
            sumPlayerX += score

    # draw labels
    Text(Point(1,5), "PlayerO").draw(win)
    Text(Point(1,4.5), "PlayerX").draw(win)

    # draw list of last 5 scores
    Text(Point(3,5),str(scoresPlayerO)).draw(win)
    Text(Point(3,4.5),str(scoresPlayerX)).draw(win)

    # sum points
    Text(Point(5,5),str(sumPlayerO)).draw(win)
    Text(Point(5,4.5), str(sumPlayerX)).draw(win)

    # draw system buttons
    quit = Button(win,Point(1.5,0.5),2,1,"quit")
    quit.activate()

    retry = Button(win, Point(4.5,0.5), 2, 1, "retry")
    retry.activate()

    # wait for action
    buttonPressed = ""
    while buttonPressed == "":
        p = win.getMouse()

        if quit.clicked(p):
            buttonPressed = "close"
        elif retry.clicked(p):
            buttonPressed = "retry"

    win.close()
    exchangeList[3] = buttonPressed
    #return buttonPressed

def fillZeroes(scoreList, zeroes):
    for i in range(5):
        scoreList.append(0)

def initExchangeData():

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]

    # init exchange data
    mode = ""
    lastScore = 0
    buttonPressed = "retry"
    scoreList = []

    # produce empty scoreboard
    fillZeroes(scoreList, 5)

    exchangeList = [mode, lastScore, scoreList, buttonPressed]

    return exchangeList