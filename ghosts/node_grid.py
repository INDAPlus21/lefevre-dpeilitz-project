from ghosts.node import Node
from ghosts.vec2int import Vec2Int

class Node_grid:
    # Grid made for (y, x) coordinates

    def __init__(self, grid: list[list[int]]):
        self.create_grid(grid)
        self.width = len(self.node_grid[0])
        self.height = len(self.node_grid)
        self.size = self.width * self.height
    
    def get_node(self, pos: Vec2Int):
        return self.node_grid[pos.y][pos.x]
    
    # Initialization functions
    def create_grid(self, grid: list[list[int]]):
        self.node_grid = [[Node(grid[y][x] != 1) for x in range(len(grid[0]))] for y in range(len(grid))]


    # Clear grid
    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.node_grid[y][x].clear()