import pygame

from main import Game
from entity import Entity

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self, game: Game, pos: vec, img):
        # A set value for speed
        super().__init__(game, pos, img, 1)

    
    def update(self, delta_time: float):
        self.move(delta_time)

    
    # Samma gamla vanliga inputs 
    def get_dir(self):
        pass


    # Här sker kollisionskoll för allt: spöken, pickups och väggar (väggar inte lika säkert så den kan experimenteras)
    def collides(self, hitbox):
        pass