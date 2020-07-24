#Board

"""
A class that creates a Board Object
Input:
    p0Symbol: symbol to display for player ID 0 (generally X or O)
    p1Symbol: symbol to display for player ID 1 (generally X or O)
"""
class Board:
    def __init__(self, p0Symbol: str, p1Symbol: str):
        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.p0 = p0Symbol
        self.p1 = p1Symbol

    #For now we will code the game with a command line representation
    #We will then display it on pygame
    def __str__(self):
        boardToPrint = ""
        for i in range(len(self.board)):
            boardToPrint += " " #Space at beginning for cleanliness
            for j in range(len(self.board[i])): 
                #Print our symbols
                if self.board[i][j] == 0:
                    boardToPrint += self.p0
                elif self.board[i][j] == 1:
                    boardToPrint += self.p1
                else:
                    boardToPrint += " "
                #Print Dividers / new lines
                if (j == (len(self.board[i]) - 1)):
                    boardToPrint += " \n"
                else:
                    boardToPrint += " | "  
        return boardToPrint

    #Checks if moveMade causes 3 on a row on itself
    def threeInARow(self):
        if ((self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] and self.board[0][0] > -1) or
            (self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2] and self.board[1][0] > -1) or
            (self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2] and self.board[2][0] > -1) or
            (self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0] and self.board[0][0] > -1) or
            (self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1] and self.board[0][1] > -1) or
            (self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2] and self.board[0][2] > -1) or
            (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] > -1) or
            (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] > -1)):
            return True
        return False
                


    