from node import Node
from vec2int import Vec2Int

class Node_grid:
    # Grid made for (y, x) coordinates

    def __init__(self, grid: list[list[int]]):
        self.create_grid(grid)
    
    def get_node(self, pos: Vec2Int):
        return self.node_grid[pos.y][pos.x]
    
    # Initialization functions
    def create_grid(self, grid: list[list[int]]):
        self.node_grid = [[Node(grid[y][x] != 1) for y in range(len(grid))] for x in range(len(grid[0]))]