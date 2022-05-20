import pygame

from pickup import Pickup

vec = pygame.math.Vector2

class Food(Pickup):
    def __init__(self, pos: vec, img):
        super().__init__(vec, img)


    def pick_up(self):
        self.game.score += 10
        self.game.game_objects.remove(self)