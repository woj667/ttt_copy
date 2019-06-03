# tictactoe's main program

# TO DO:
# --OK-- delay after bot's turn
# file with constants
# --OK-- data exchange between fx via table, not variables
# --OK-- change order after each play <-- looser starts
# draw all in the same window
# prepare desctiption
# --OK-- fix BVB draw bug

from gameLib import *

def main():

    exchangeList = initExchangeData()

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    # buttonPressed = exchangeList[3]


    # main event loop
    while exchangeList[3] == "retry":

        # open game menu
        gameMenu(exchangeList)

        # start game
        gamePlay(exchangeList)

        # open scoreboard
        gameScores(exchangeList)


if __name__ == "__main__": main()
