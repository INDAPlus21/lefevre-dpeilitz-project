import pygame

from main import Game
from game_object import GameObject

vec = pygame.math.Vector2

class PickUp(GameObject):
    def __init__(self, game: Game, pos: vec, img):
        super().__init__(game, pos, img)
    
    # Also remove from GO-list
    def pick_up(self):
        pass # Do some fancy logic here for its children