import math
from select import select
from numba import prange
import numpy as np

class MCTS_Node:
    def __init__(self, board, parent = None):
        self.board = board
        self.children = []
        self.parent = parent
        self.value = 0
        self.visits = 0
        self.probability = 0
    
    """
    Select the child with the highest UCB1 value if the node is expanded
    """
    def selection(self):
        if self.children != []:
            ucb_1_values = []
            #Append each child's ucb_1 value to the list
            for child_ind in range(len(self.children)):
                ucb_1_values.append(self.children[child_ind].UCB1())
            #Find the index of the child with the highest ucb_1 value
            node = self.children[np.argmax(ucb_1_values)]
            return node
        return self
    
    """
    Expand the node if it is not fully expanded
    """
    def expansion(self):
        node = self.board
        if node.get_winner() == None:
            moves = node.get_possible_moves()
            children = []
            for ind in prange(len(moves)):
                child = node.make_move(node.turn, moves[ind])
                children.append(MCTS_Node(child, self))
            self.children = children
        
    
    """
    Simulations are done by selecting the next node at random from the children of the current node until a final state is reached
    """
    def simulation(self):
        node = self.board
        while node.get_winner() == None:
            moves = node.get_possible_moves()
            random_ind = np.random.randint(0, len(moves))
            move = moves[random_ind]
            node = node.make_move(node.turn, move)
        value = node.get_winner()
        return value
    
    """
    Backpropagation is done by updating the value of the node and the visits of the node and all of its parents
    """
    def backpropagation(self, value):
        node = self
        while node != None:
            node.update(value)
            node.update_probability()
            node = node.parent
            
    def update(self, value):
        self.value += value
        self.visits += 1
        
    def update_probability(self):
        if self.parent != None:
            self.probability = abs(self.visits / self.parent.visits)
        else:
            self.probability = 1
        
    def __repr__(self):
        out = ""
        out += str(self.board)
        out += "Value: " + str(self.value) + "\n"
        out += "Visits: " + str(self.visits) + "\n"
        out += "Probability: " + str(self.probability) + "\n"
        return out
    
    def run(self, num_rollout):
        node = self.selection()
        while node.is_expanded():
            node = node.selection()
        node.expansion()
        for _ in prange(num_rollout):
            reward = node.simulation()
            node.backpropagation(reward)
            
    
    def is_expanded(self):
        return self.children != []
        
    def UCB1(self):
        if self.parent != None and self.visits != 0:
            confidence_value = 0.5
            parent_visits = self.parent.visits
            board_evaluation = self.value / self.visits
            return board_evaluation + confidence_value * math.sqrt(math.log(parent_visits) / self.visits)
        else:
            return 1