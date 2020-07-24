#Game

from board import *
from player import *

class Game:
    def __init__(self):
        self.player0 = None
        self.player1 = None
        self.gameBoard = None

        self.initPlayers()
        self.initBoard()
    
    #This will be changed to interact with pygame
    def nameEntry(self, num):
        name = str(input("Player " + str(num) + ", please enter your name: "))
        return name
    
    #This will be removed once we switch off of command line (clicks instead)
    def cmdPromptGameType(self):
        print("Game Types\n")
        print("    1. Human vs Human")
        print("    2. Human vs Computer")
        print("    3. Computer vs Computer\n\n")

        while(True):
            choice = int(input("Please pick a number: "))
            if (choice > 0 and choice < 4):
                return choice
            print("Please make a valid selection.")


    def initPlayers(self):
        gameType = self.cmdPromptGameType()

        if(gameType == 1):           
            self.player0 = HumanPlayer(0, self.nameEntry(1))
            self.player1 = HumanPlayer(1, self.nameEntry(2))
        elif(gameType == 2):
            self.player0 = HumanPlayer(0, self.nameEntry(1))
            self.player1 = ComputerPlayer(1, "Computer Player")
        else:
            self.player0 = ComputerPlayer(0, "CPU 1")
            self.player1 = ComputerPlayer(1, "CPU 2")
    

    def initBoard(self):
        self.gameBoard = Board("X", "O") #Change this to be input once pygame set up
        print(self.gameBoard) #Make sure all is well

    def playGame(self):
        while(True):
            tookATurn = self.player0.play(self.gameBoard)
            if (tookATurn == False):
                print("Draw")
                break

            if (self.gameBoard.threeInARow()):
                print(self.player0.name + " wins!")
                break

            tookATurn = self.player1.play(self.gameBoard)
            if (tookATurn == False):
                print("Draw")
                break
            
            if (self.gameBoard.threeInARow()):
                print(self.player1.name + " wins!")
                break

