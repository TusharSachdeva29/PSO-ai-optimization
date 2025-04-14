import numpy as np

class WarehouseGrid:
    def __init__(self, rows, cols, start, goal, obstacles):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.obstacles = obstacles  # Properly expose obstacles as an attribute
        self.grid = np.zeros((rows, cols))
        for (i, j) in obstacles:
            self.grid[i, j] = 1  # Mark obstacles

    def display(self):
        for row in self.grid:
            print(row)
            
    def is_valid(self, pos):
        i, j = pos
        return (0 <= i < self.rows and 
                0 <= j < self.cols and 
                pos not in self.obstacles)
