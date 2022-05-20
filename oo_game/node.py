import pygame

from vector import Vector2
from constants import *

class Node:
    def __init__(self, x, y):
        self.pos = Vector2(x, y) * TILELENGTH
        self.neighbors = {UP:None, DOWN:None, RIGHT:None, LEFT:None}

    
    def draw(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.pos.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.pos.asInt(), 12)

