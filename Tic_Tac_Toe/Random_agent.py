import numpy as np
from .Player import *

class RandomAgent(Player):
    def __init__(self, marker):
        super().__init__(marker)

    def get_move(self, board):
        print(f"{self.marker} is thinking...")
        moves = board.get_possible_moves()
        ind = np.random.randint(0, len(moves))
        return (moves[ind][0], moves[ind][1])