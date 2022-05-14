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
        self.dir = self.find_dir(player_pos: Vec2Int)


        self.move()

    # Helper methods
    def find_dir(self, target):
        next_node = self.pathfinder.find_path(player_pos)[1]
    def move(self):
        