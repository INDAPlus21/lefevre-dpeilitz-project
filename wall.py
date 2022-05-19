import pygame

from main import Game
from game_object import GameObject

vec = pygame.math.Vector2

class Wall(GameObject):
    def __init__(self, game: Game, pos: vec, img):
        super().__init__(game, pos, img)
        is_static = True