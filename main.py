# tictactoe's main program

# TO DO:
# --OK-- delay after bot's turn
# file with constants
# --OK-- data exchange between fx via table, not variables
# change order after each play

from gameLib import *

def main():

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]

    exchangeList = initExchangeData()

    # main event loop
    while exchangeList[3] == "retry":

        # open game menu
        gameMenu(exchangeList)

        # start game
        gamePlay(exchangeList)

        # open scoreboard
        gameScores(exchangeList)


if __name__ == "__main__": main()
