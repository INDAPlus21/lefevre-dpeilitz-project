import pygame

from vector import Vector2
from entity import Entity
from wall import Wall
from constants import *

rect = pygame.Rect

class Player(Entity):
    def __init__(self, pos: Vector2):
        # A set value for speed
        self.pos = pos * TILELENGTH

        self.radius = TILELENGTH / 2
        self.speed = 120
        self.dir = Vector2(-1, 0)
        self.hitbox = rect(self.pos.x, self.pos.y, TILELENGTH, TILELENGTH)

    
    def update(self, delta_time: float, walls: list[Wall]):
        self.dir = self.get_dir()
        
        super().update(delta_time, walls)


    def draw(self, screen):
        offset = TILELENGTH / 2
        pygame.draw.circle(screen, YELLOW, (self.pos.x + offset, self.pos.y + offset), self.radius)

    
    def get_dir(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            return Vector2(0, -1)
        elif key_pressed[pygame.K_DOWN]:
            return Vector2(0, 1)
        elif key_pressed[pygame.K_LEFT]:
            return Vector2(-1, 0)
        elif key_pressed[pygame.K_RIGHT]:
            return Vector2(1, 0)
        else: 
            return self.dir


    # Här sker kollisionskoll för allt: spöken, pickups och väggar (väggar inte lika säkert så den kan experimenteras)
    def collides(self, hitbox):
        pass