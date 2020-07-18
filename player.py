#player
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, pid: int, name: str):
        self.pid = pid #0 or 1
        self.name = name #Name of player

    @abstractmethod
    def play(self):
        pass

class HumanPlayer(Player):
    def __init__(self, pid: int, name: str):
        super().__init__(pid, name)
    
    def play(self):
        print("Play for human player, please implement me!")

class ComputerPlayer(Player):
    def __init__(self, pid: int, name: str):
        super().__init__(pid, name)
    
    def play(self):
        print("Play for computer player, please implement me!")