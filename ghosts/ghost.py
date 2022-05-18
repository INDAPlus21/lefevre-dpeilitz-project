import pygame
from pathfinder import Pathfinder
from vec2int import Vec2Int


class Ghost:
    def __init__(self, pos: Vec2Int, grid: list[list[int]]):
        self.grid = grid
        self.pos = pos

        self.speed = 1
        self.dir = Vec2Int(1, 0)
        self.pathfinder = Pathfinder()
    def update(self, delta_time: float, player_pos: Vec2Int):
        # Non-Scatter mode
        self.dir = self.find_new_dir(player_pos)


        self.move()

    # Helper methods
    def find_new_dir(self, target):
        # Select second node in path (aka the one after start)
        next_node_pos = self.pathfinder.find_path(target)[1]
        self.dir = next_node_pos - self.get_grid_pos()
    def move(self):
        pass
    def get_grid_pos(self):
        pass