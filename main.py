# tictactoe's main program

from Board  import *
from Logics import *
from Player import *
from Bot    import *
from gameLib import *


def main():

    # open game menu
    #win = GraphWin("Menu", 300, 300)
    mode = gameMenu()

    # open game board
    win = GraphWin("Tic-Tac-Toe", 300, 300)

    #init game
    gameLogics, gameBoard, playerO, playerX, pOzones, pXzones, turn, zone, gameover = gameStart(win)

    # main event loop
    while gameover == "":

        turn += 1

        if turn % 2:                                             # first loop iteration: turn = 1, "O" starst
            # player's O turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                p = win.getMouse()
                zone = gameLogics.getZone(p)

            playerO.appendZone(zone)
            pOzones = playerO.listZones()
            gameBoard.drawO(zone)
            gameBoard.setMsg("Player's X turn")                  # after O is drawn, set message

        else:
            # player's X turn
            while zone == "" or zone in gameLogics.listZones():  # ask for a new zone as long it is not clicked
                if mode == "pvb":
                    p = Point(randrange(0, 6), randrange(0, 6))
                elif mode == "pvp":
                    p = win.getMouse()
                zone = gameLogics.getZone(p)

            playerX.appendZone(zone)
            pXzones = playerX.listZones()
            gameBoard.drawX(zone)
            gameBoard.setMsg("Player's O turn")

        gameLogics.appendZone(zone)                              # append only when zone is clicked first time

        # check status
        if   gameLogics.isWinner(pOzones):    gameover = "Player O wins!"
        elif gameLogics.isWinner((pXzones)):  gameover = "Player X wins!"
        elif turn == 9:                       gameover = "Draw!"

        if gameover != "":  gameBoard.setMsg(gameover)

    win.getMouse()
    gameBoard.setMsg("Press any key to exit")
    win.getKey()
    win.close()


if __name__ == "__main__": main()
