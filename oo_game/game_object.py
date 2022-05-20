import pygame

from vector import Vector2
from constants import *

rect = pygame.Rect

# My idea is to have a list that consists of all game objects, and that is looped through at the game's update and draw/render methods. When an object ceases to
# exist - for example when the player eats a bit of food - that object should be removed from the main game object-list. 
class GameObject:
    def __init__(self, pos: Vector2, img):
        self.pos = pos * TILELENGTH
        self.img = img
        self.hitbox = rect(self.pos.x, self.pos.y, img.get_width(), img.get_height())

    
    def update(self, delta_time: float):
        pass


    def draw(self, screen):
        screen.blit(self.img, self.pos)


    def override_hitbox(self, hitbox: rect):
        self.hitbox = hitbox