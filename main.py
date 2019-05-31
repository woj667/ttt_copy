# tictactoe's main program

from classes import *


def main():
    # draw game board
    win = GraphWin("Tic-Tac-Toe", 300, 300)
    gameBoard = Board(win)

    # create game logic
    gameLogics = Logics()

    #posList = ['dl','dm','dr','ml','mm','mr','ul','um','ur']
    posList = []
    gameover = 0

    while gameover < 9:
        gameover += 1

        # get pos from mouse click
        p = win.getMouse()
        pos = gameBoard.getZone(p)

        gameBoard.drawO()
        gameLogics.appendPos(pos)
        winner = gameLogics.isWinner()

        print("pos: ", gameLogics.printPos())

        print("status: ", winner)



    win.getMouse()
    win.close()


if __name__ == "__main__": main()
