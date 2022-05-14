from node_grid import Node_grid
from vec2int import Vec2Int

class Pathfinder:
    def __init__(self, grid: list[list[int]]):
        self.node_grid = Node_grid(grid)

    # Actual pathfinding
    def find_path(self):
        pass

    # Helper methods
    def dist_to_point(self, start_pos: Vec2Int, target_pos: Vec2Int):
        x_diff = abs(start_pos.x - target_pos.x)
        y_diff = abs(start_pos.y - target_pos.y)
        return x_diff + y_diff
    def get_adjacents(self):
        pass
    def find_best_node(self):
        pass
    def find_lowest_h_cost(self):
        pass
    def find_lowest_f_cost(self):
        pass
    