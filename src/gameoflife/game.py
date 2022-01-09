import numpy as np


LIVE = 1
DEAD = 0


class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def make_board(self, p=0.5, random_seed=42):
        size = (self.width, self.height)
        sample = np.random.uniform(low=0, high=1, size=size)
        self._board = np.empty(size, dtype=np.int8)
        self._board[sample <= p] = 0
        self._board[sample > p] = 1
        
        self._board_next = np.empty(size)
        
    def render(self):
        print(self._board)
        
    def step(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                neighbors = []
                if (i > 0) and (j > 0):
                    neighbors.append(self._board[i-1, j-1])
                if (i > 0):
                    neighbors.append(self._board[i-1, j])
                if (i > 0) and (j < self.width - 1):
                    neighbors.append(self._board[i-1, j+1])
                if (j < self.width - 1):
                    neighbors.append(self._board[i, j+1])
                if (i < self.height - 1) and (j < self.width - 1):
                    neighbors.append(self._board[i+1, j+1])
                if (i < self.height - 1):
                    neighbors.append(self._board[i+1, j])
                if (i < self.height - 1) and (j > 0):
                    neighbors.append(self._board[i+1, j-1])
                    
                total = sum(neighbors)
                if self._board[i, j] == LIVE:
                    if total in [0, 1]:
                        self._board_next[i, j] = DEAD
                    elif total in [2, 3]:
                        self._board_next[i, j] = LIVE
                    else:
                        self._board_next[i, j] = DEAD
                else:
                    if total == 3:
                        self._board_next[i, j] = LIVE        
                    else:
                        self._board_next[i, j] = DEAD
                        
        tmp = self._board
        self._board = self._board_next
        self._board_next = tmp
        

g = Game(3, 4)
g.make_board()
g.render()
g.step()
g.render()