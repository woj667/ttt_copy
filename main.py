# tictactoe's main program

from gameLib import *

def main():
    scoreList = [0,0,0,0,0]

    buttonPressed = "retry"
    while buttonPressed == "retry":

        # open game menu
        mode = gameMenu()

        # start game
        score = gamePlay(mode)
        scoreList.append(score)

        # open scoreboard
        buttonPressed = gameScores(scoreList)


if __name__ == "__main__": main()
