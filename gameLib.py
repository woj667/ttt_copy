# gameLib.py

from window import *
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
    win = exchangeList[4]

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

    # display board
    gameBoard = Board()
    gameBoard.draw(win)

    # create logics
    gameLogics = Logics()

    # create Players' instances
    playerO = Player()
    playerX = Player()

    # create faceplates
    circle = FigureO(win)
    cross = FigureX(win)

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
            #gameBoard.drawO(zone)
            circle.draw(zone)
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
            #gameBoard.drawX(zone)
            cross.draw(zone)
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
    gameBoard.undraw()
    circle.undraw()
    cross.undraw()
    #win.close()

    exchangeList[1] = score
    #return score

def gameScores(exchangeList):

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    lastScore = exchangeList[1]
    scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    win = exchangeList[4]


    scoreboard = Scoreboard()
    scoreboard.appendScore(scoreList, lastScore)
    scoreboard.draw(win)
    buttonPressed =  scoreboard.getMode()


    exchangeList[3] = buttonPressed

    scoreboard.undraw()

    #win.close()
    #return buttonPressed

def initExchangeData():

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]
    # win = exchangeList[4]

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

def __undrawAll(objectList):
    for object in objectList:
        object.undraw()