# tictactoe's main program

# TO DO:
# --OK-- delay after bot's turn
# file with constants
# --OK-- data exchange between fx via table, not variables
# --OK-- change order after each play <-- looser starts
# --OK -- draw all in the same window
# prepare desctiption
# --OK-- fix BVB draw bug
# --OK-- move every graphic object to window.py
# refine gamePlay

from gameLib import *

def main():

    # declare initial conditions
    exchangeList = initExchangeData()

    # -- DECODE EXCHANGE LIST: --
    # mode = exchangeList[0]
    # lastScore = exchangeList[1]
    # scoreList = exchangeList[2]
    buttonPressed = exchangeList[3]
    win = exchangeList[4]
    # ---------------------------

    # main event loop
    while buttonPressed == "retry":

        # open game menu
        gameMenu(exchangeList)

        # start game
        gamePlay(exchangeList)

        # print scoreboard
        gameScores(exchangeList)

        # update button status
        buttonPressed = exchangeList[3]

    win.close()

if __name__ == "__main__": main()
