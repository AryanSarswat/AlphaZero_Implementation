from Board import *
from Random_agent import *
from Human_Player import *

"""
Class for Playing the game
Player1 is always denoted by X and Player 2 is always denoted by O

Parameters:
    Player1: Player object
    Player2: Player object
"""
class Game:
    def __init__(self, Player1, Player2):
        self.board = Board(3)
        self.ended = False
        #Player 1 is X and Player 2 is O
        self.PlayerX = Player1
        self.PlayerY = Player2
    
    def play(self):
        while not self.ended:
            print(self.board)
            turn =  self.board.get_turn()
            move = self.PlayerX.get_move(self.board) if turn == 1 else self.PlayerY.get_move(self.board)
            self.board.make_move(turn, move)
            winner = self.board.get_winner()
            if winner != None:
                self.ended = True
                winner = "X" if winner == 1 else "O" if winner == -1 else "Tie"
                if winner == "Tie":
                    print("Tie")
                else:
                    print("Winner is:", winner)
                print("\n")
                print(self.board)