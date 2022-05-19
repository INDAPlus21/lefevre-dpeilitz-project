import pygame

from main import Game
from game_object import GameObject

vec = pygame.math.Vector2

class Entity(GameObject):
    def __init__(self, game: Game, pos: vec, img, speed: int):
        super().__init__(game, pos, img)

        self.dir = (-1, 0)
        self.speed = speed

    
    def update(self, delta_time: float):
        self.move(delta_time)


    def move(self, delta_time: float):
        self.pos += self.dir * self.speed * delta_time


    