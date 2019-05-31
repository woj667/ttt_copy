# tictactoe's main program

from classes import *


def main():
    # draw game board
    win = GraphWin("Tic-Tac-Toe", 300, 300)
    gameBoard = Board(win)

    # create game logic
    gameLogics = Logics()

    # possible elements of zList = ['dl','dm','dr','ml','mm','mr','ul','um','ur']


    # create Players' instances
    playerO = Player()
    playerX = Player()

    pOlist = pXlist = []

    turn = 0
    gameover = ""

    # main event loop
    while gameover == "":

        turn += 1

        p = win.getMouse()                      # take a point from mouse click
        zone = gameLogics.getZone(p)            # assign the point to a proper zone

        while zone in gameLogics.listZone():    # ask for a new zone as long it is not clicked
            p = win.getMouse()
            zone = gameLogics.getZone(p)

        gameLogics.appendZone(zone)             # append only when zone is clicked first time

        print("turn: ", turn)
        if not turn % 2:                        # first loop iteration: turn = 0, "O" starst
            # player's O turn
            playerO.appendZone(zone)
            pOlist = playerO.zoneList()
            print("PlayerO: ", pOlist)
            gameBoard.drawO(zone)
            gameBoard.setMsg("Player's X turn")  # after O is drawn, set message

        else:
            # player's X turn
            playerX.appendZone(zone)
            pXlist = playerX.zoneList()
            print("PlayerX: ", pXlist)
            gameBoard.drawX(zone)
            gameBoard.setMsg("Player's O turn")

        # check status
        if   gameLogics.isWinner(pOlist):     gameover = "Player O wins!"
        elif gameLogics.isWinner((pXlist)):   gameover = "Player X wins!"
        elif turn == 9:                       gameover = "Draw!"

        if gameover != "":  gameBoard.setMsg(gameover)

    win.getMouse()
    gameBoard.setMsg("Press any key to exit")
    win.getKey()
    win.close()


if __name__ == "__main__": main()
