import numpy as np

"""
Board representation for Tic_Tac_Toe game.
"""
class Board:
    def __init__(self, size):
        # Initialize the board
        self.size = size
        self.state = np.zeros(shape=(size, size))
        #Turn 1 is X, -1 is O
        self.turn = 1
    
    def get_state(self):
        return self.state
    
    def get_turn(self):
        return self.turn
    
    """
    Make a move for the player
    
        Parameters:
            player: The player to make the move where X is represented by 1 and O by -1
            move: The move to make in the format (row, column)
    """
    def make_move(self, player, move):
        #Check if move is valid
        if self.state[move] != 0 or self.turn != player:
            print("Invalid move")
            print(self.state)
            print(self.turn)
            print(move)
            return
        #Make move
        self.state[move] = player
        #Change turn
        self.turn *= -1
    
    """
    Checks if the game is over
        Returns:
            True if the game is over
            False otherwise
    """
    def get_winner(self):
        #Check rows
        for row in range(self.size):
            if abs(np.sum(self.state[row])) == self.size:
                return self.state[row][0]
        #Check columns
        transposed = np.transpose(self.state)
        for col in range(self.size):
            if abs(np.sum(transposed[col])) == self.size:
                return self.state[0][col]
        #Check diagonals
        diag1 = np.diagonal(self.state)
        if abs(np.sum(diag1)) == self.size:
            return diag1[0]
        diag2 = np.diagonal(np.fliplr(self.state))
        if abs(np.sum(diag2)) == self.size:
            return diag2[0]
        #Check if board is full
        if np.count_nonzero(self.state) == self.size**2:
            return 0
        return None      
    
    def get_possible_moves(self):
        moves = np.where(self.state == 0)
        moves = np.dstack((moves[0], moves[1]))[0]
        return moves
    
    def __repr__(self) -> str:
        out = "⏤"*(self.size*2 - 1) + "\n"
        converted_str = np.where(self.state == 1, "X", np.where(self.state == -1, "O", "-"))
        for i in range(self.size):
            out+= "⏐".join(converted_str[i].tolist()) + "\n"
            out+= "⏤"*(self.size*2 - 1) + "\n"
        return out