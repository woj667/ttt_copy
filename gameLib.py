# gameLib.py

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

    # display window...
    win = GraphWin("Menu", 300, 300)
    win.setCoords(-1.0, -1.0, 7.0, 7.0)

    # ...with welcome text
    Text(Point(3, 5.5), "Choose your oponent:").draw(win)
    Text(Point(3, 2.75), "or").draw(win)

    # activate PVP button
    pvp = Button(win, Point(3,4),2,1,"PVP")
    pvp.activate()

    # activate PVB button
    pvb = Button(win, Point(3,1.5), 2,1,"PVB")
    pvb.activate()

    # activate BVB button
    bvb = Button(win, Point(3,0), 2,1,"BVB")
    bvb.activate()

    # wait for button press
    mode = ""
    while mode == "":
        p = win.getMouse()
        if pvp.clicked(p):   mode = "pvp"
        elif pvb.clicked(p): mode = "pvb"
        elif bvb.clicked(p): mode = "bvb"


    # close & return
    win.close()
    exchangeList[0] = mode

def gamePlay(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    mode = exchangeList[0]
    lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]]

    # display board
    win = GraphWin("Tic-Tac-Toe", 300, 300)
    gameBoard = Board(win)

    # create logics
    gameLogics = Logics()

    # create Players' instances
    playerO = Player()
    playerX = Player()

    # initial game settings
    zone = ""               # zone belongs to ['dl', 'dm', 'dr', 'ml', 'mm', 'mr', 'ul', 'um', 'ur']
    gameover = ""           # condition to leave event loop
    score = 0               # score of current game

    if   lastScore == 3:    turn = 1
    elif lastScore == -3:   turn = 0
    else:                   turn = randrange(0, 2, 1) # randomize if first game or draw

    # main event loop
    while gameover == "":

        turn += 1

        if turn % 2:
            # player's O turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "bvb":
                    p = Point(randrange(0, 6), randrange(0, 6))
                else:   # if pvp or pvb
                    p = win.getMouse()
                zone = gameLogics.getZone(p)

            update(3)                           # time delay
            playerO.appendZone(zone)
            gameBoard.drawO(zone)
            gameBoard.setMsg("Player's X turn")  # after O is drawn, set message

        else:
            # player's X turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "pvp":
                    p = win.getMouse()
                else:   # if pvb pr bvb
                    p = Point(randrange(0, 6), randrange(0, 6))
                zone = gameLogics.getZone(p)

            update(3)
            playerX.appendZone(zone)
            gameBoard.drawX(zone)
            gameBoard.setMsg("Player's O turn")

        gameLogics.appendZone(zone)  # append only when zone is clicked first time

        # check status
        if gameLogics.isWinner(playerO.listZones()):
            gameover = "Player O wins!"
            score = 3
        elif gameLogics.isWinner(playerX.listZones()):
            gameover = "Player X wins!"
            score = -3
        elif len(gameLogics.listZones()) == 9:      # each zone occupied
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

    # display scoreboard
    win = GraphWin("Scoreboard", 300, 300)
    win.setCoords(-1.0, -1.0, 7.0, 7.0)

    # initial scores
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

    # draw summary
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
    __fillZeroes(scoreList, 5)

    exchangeList = [mode, lastScore, scoreList, buttonPressed]

    return exchangeList

def __fillZeroes(scoreList, zeroes):
    for i in range(5):
        scoreList.append(0)