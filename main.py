#Main
from board import *
from player import *

def main():
    #Put our main running code here
    myBoard = Board("X", "O")
    print(myBoard)
    p1 = HumanPlayer(0, "Tess")
    p2 = HumanPlayer(1, "Mo")

    while(True):
        tookATurn = p1.play(myBoard)
        if (tookATurn == False):
            print("Draw")
            break

        if (myBoard.threeInARow()):
            print(p1.name + " wins!")
            break

        tookATurn = p2.play(myBoard)
        if (tookATurn == False):
            print("Draw")
            break
        
        if (myBoard.threeInARow()):
            print(p2.name + " wins!")
            break


if __name__ == "__main__":
    main()
