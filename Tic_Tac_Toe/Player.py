from abc import abstractmethod


class Player:
    def __init__(self, marker):
        self.marker = marker
    
    def get_marker(self) -> str:
        return self.marker
    
    @abstractmethod
    def get_move(self, board):
        pass