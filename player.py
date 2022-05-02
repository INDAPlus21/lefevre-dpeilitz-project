import pygame
from constants import *
vec = pygame.math.Vector2


class Player:
    def __init__(self, grid):
        self.grid = grid
        self.position = vec(200, 400) 
        self.grid_position = self.position // TILELENGTH
        self.direction = vec(0, 1)
        self.speed = 1
        self.radius = 8
        self.color = YELLOW
        self.stored_direction = None

    def update(self):
        # Check collisions
        #if self.collision() == true:

        self.position += self.direction*self.speed
        self.grid_position = self.position // TILELENGTH
        direction = self.get_keypress()
        if direction != vec(0, 0):
            self.direction = direction

    def get_keypress(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            return vec(0, -1)
        elif key_pressed[pygame.K_DOWN]:
            return vec(0, 1)
        elif key_pressed[pygame.K_LEFT]:
            return vec(-1, 0)
        elif key_pressed[pygame.K_RIGHT]:
            return vec(1, 0)
        else:
            return vec(0, 0)
    def render(self, screen):
        p = self.position
        pygame.draw.circle(screen, self.color, p, self.radius)
        self.collision()

    #check the tile pacman is currently on is a wall, returns false otherwise
    def collision(self):
         xval = int(self.grid_position.x + self.direction.x)
         yval = int(self.grid_position.y + self.direction.y)
         if self.grid[yval][xval] == 1:
            print("HEUREKA")
            return True
         else:
            return False
      