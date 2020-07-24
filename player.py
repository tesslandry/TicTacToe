#player
from abc import ABC, abstractmethod
"""
An abstract Player class that will be used to make HumanPlayers and ComputerPlayers
Input:
    pid: player ID (0 or 1)
    name: string, name of player
"""
class Player(ABC):
    def __init__(self, pid: int, name: str):
        self.pid = pid #0 or 1
        self.name = name #Name of player

    @abstractmethod
    def play(self):
        pass


"""
A class for Human Players
Input:
    pid: player ID (0 or 1)
    name: string, name of player
"""
class HumanPlayer(Player):
    def __init__(self, pid: int, name: str):
        super().__init__(pid, name)

    def inputMoveChoice(self, board):
        while(True):
            numRow = -1
            numCol = -1
            while(numRow < 0 or numRow > 2):
                print("\nRows:\n0\n-\n1\n-\n2\n\n ") #Fix this to work with pygame
                numRow = int(input("Please enter a row: "))
            while(numCol < 0 or numCol > 2):
                print("\nColumns: 0 | 1 | 2 ")
                numCol = int(input("Please enter a column: "))

            #If we have made a valid move, break out of loop
            if (board[numRow][numCol] < 0):
                break
            
            print("\nPlease enter a valid move.")

        return (numRow, numCol)
    
    def play(self, board):

        if (any(-1 in row for row in board.board)):

            print(self.name + ", it's your turn!")     
            moveChoice = self.inputMoveChoice(board.board)

            print()
            print(moveChoice)

            board.board[moveChoice[0]][moveChoice[1]] = self.pid
            print(board)

            #Valid Move was Played
            return True
        return False

        
"""
A class for Computer Players
Input:
    pid: player ID (0 or 1)
    name: string, name of player
"""
class ComputerPlayer(Player):
    def __init__(self, pid: int, name: str):
        super().__init__(pid, name)
    
    def play(self):
        print("Play for computer player, please implement me!")