#Board
class Board:
    def __init__(self, p0Symbol: str, p1Symbol: str):
        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.p0 = p0Symbol
        self.p1 = p1Symbol

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
                



myBoard = Board("X", "O")
print(myBoard)

    