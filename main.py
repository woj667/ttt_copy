# tictactoe's main program

# TO DO:
# delay after bot's turn
# file with constants
# data exchange between fx via table, not variables

from gameLib import *

def main():

    # produce empty scoreboard
    scoreList = []
    fillZeroes(scoreList,5)

    # main event loop
    buttonPressed = "retry"
    while buttonPressed == "retry":

        # open game menu
        mode = gameMenu()

        # start game
        lastScore = gamePlay(mode)

        # open scoreboard
        buttonPressed = gameScores(lastScore, scoreList)


if __name__ == "__main__": main()
