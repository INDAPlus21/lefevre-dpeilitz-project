import pygame

from main import Game

vec = pygame.math.Vector2
rect = pygame.Rect

# My idea is to have a list that consists of all game objects, and that is looped through at the game's update and draw/render methods. When an object ceases to
# exist - for example when the player eats a bit of food - that object should be removed from the main game object-list. 
class GameObject:
    def __init__(self, game: Game, pos: vec, img):
        self.game = game
        self.pos = pos
        self.img = img
        self.hitbox = rect(pos.x, pos.y, img.get_width(), img.get_height())

        self.is_static = False

    
    def update(self, delta_time: float):
        self.update_hitbox()


    def draw(self, screen):
        screen.blit(self.img, self.pos)


    def override_hitbox(self, hitbox: rect):
        self.hitbox = hitbox


    def update_hitbox(self):
        if self.is_static == False:
            self.hitbox = rect(self.pos.x, self.pos.y, self.hitbox.width, self.hitbox.height)