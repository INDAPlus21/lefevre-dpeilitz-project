import pygame

from vector import Vector2
from game_object import GameObject
from wall import Wall
from constants import *

rect = pygame.Rect

class Entity(GameObject):
    def __init__(self, pos: Vector2, img, speed: int):
        super().__init__(pos, img)

        self.dir = Vector2(-1, 0)
        self.speed = speed
        self.last_pos = pos

    
    def update(self, delta_time: float, walls: list[Wall]):
        self.last_pos = self.pos

        move_vec = self.move(delta_time)
        self.hitbox.move(move_vec.x, move_vec.y)
        self.pos += move_vec

        if (self.pos.x / TILELENGTH).is_integer() and (self.pos.y / TILELENGTH).is_integer():
            print(self.pos.x / TILELENGTH, self.pos.y / TILELENGTH)


    def move(self, delta_time: float) -> Vector2:
        return self.dir * self.speed * delta_time