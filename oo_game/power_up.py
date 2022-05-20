import pygame

from main import Game
from pickup import PickUp

vec = pygame.math.Vector2

class PowerUp(PickUp):
    def __init__(self, game: Game, pos: vec, img):
        super().__init__(game, pos, img)


    def pick_up(self):
        self.game.game_state = "scatter"
        self.game.game_objects.remove(self)