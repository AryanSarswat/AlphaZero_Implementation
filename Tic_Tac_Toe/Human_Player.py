from Player import *

class Human_Player(Player):
    def __init__(self, marker):
        super().__init__(marker)
    
    def get_move(self, board):
        move = input(f"Player {self.marker} enter move: ")
        move = move.split(",")
        move = (int(move[0]), int(move[1]))
        return move