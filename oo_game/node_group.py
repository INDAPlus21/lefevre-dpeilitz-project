import pygame

from vector import Vector2
from constants import *
from node import Node

class NodeGroup:
    def __init__(self):
        self.nodes = []


    def draw(self, screen):
        for i in range(len(self.nodes)):
            self.nodes[i].draw(screen)


    def set_nodes(self, grid: list[list[int]]):
        for x in range(COLS):
            for y in range(ROWS):
                if grid[y][x] != 1:
                    neighbor_val = Vector2()
                    if grid[y][x+1] != 1:
                        neighbor_val += Vector2(1, 0)
                    if grid[y][x-1] != 1:
                        neighbor_val += Vector2(1, 0)
                    if grid[y+1][x] != 1:
                        neighbor_val += Vector2(0, 1)
                    if grid[y-1][x] != 1:
                        neighbor_val += Vector2(0, 1)
                    if neighbor_val.x > 0 and neighbor_val.y > 0:
                        self.nodes.append(Node(x, y))
