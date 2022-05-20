import pygame

from vector import Vector2
from game_object import GameObject
from constants import BLUE, TILELENGTH

rect = pygame.Rect

class Wall(GameObject):
    def __init__(self, pos: Vector2):
        self.pos = pos * TILELENGTH
        self.hitbox = rect(self.pos.x, self.pos.y, TILELENGTH, TILELENGTH)


    def update(self, delta_time: float):
        pass


    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.hitbox)