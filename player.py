import pygame
from constants import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, grid, pos):
        self.grid = grid
        self.grid_position = pos
        self.prev_pos = pos
        self.pxl_pos = vec(self.grid_position.y * TILELENGTH, self.grid_position.x * TILELENGTH + TILELENGTH / 2)
        self.pxl_pos.x += TILELENGTH/2
        print(self.pxl_pos)
        self.direction = vec(0, 1)
        self.speed = 1
        self.radius = 8
        self.color = YELLOW
        self.stored_direction = None

    def update(self):
        # Check collisions
        #if self.collision() == true:
        if self.pxl_pos == self.grid_position:
            if self.direction.x == 1 or self.direction.y == 1:
                self.pxl_pos += self.direction*self.speed
                self.grid_position = vec((self.pxl_pos.x - TILELENGTH / 2) // TILELENGTH , (self.pxl_pos.y - TILELENGTH / 2) // TILELENGTH)
                print(self.grid_position)
                direction = self.get_keypress(self.direction)
                self.direction = direction

            else:
                self.pxl_pos += self.direction*self.speed
                self.grid_position = vec((self.pxl_pos.x + TILELENGTH / 2) // TILELENGTH , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)
                print(self.grid_position)
                direction = self.get_keypress(self.direction)
                self.direction = direction

        else: 
            self.pxl_pos += self.direction*self.speed
            self.grid_position = vec((self.pxl_pos.x - TILELENGTH / 2) // TILELENGTH , (self.pxl_pos.y - TILELENGTH / 2) // TILELENGTH)
            print(self.grid_position)
            direction = self.get_keypress(self.direction)
            self.direction = direction
        self.move_grid()


    def get_keypress(self, prev_dir):
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
            #return prev_dir

    def render(self, screen):
        p = self.pxl_pos
        pygame.draw.circle(screen, self.color, p, self.radius)
        self.collision()

    def move_grid(self):
        if self.prev_pos != self.grid_position:
            
            xval = int(self.prev_pos.x)
            yval = int(self.prev_pos.y)
            self.grid[yval][xval] = 0
            self.grid[int(self.grid_position.y)][int(self.grid_position.x)] = 2
            self.prev_pos = self.grid_position


    #check the tile pacman is currently on is a wall, returns false otherwise
    def collision(self):
         xval = int(self.grid_position.x + self.direction.x)
         yval = int(self.grid_position.y + self.direction.y)
         if self.grid[yval][xval] == 1:
            print("HEUREKA")
            self.direction = vec(0, 0)
            return True
         else:
            return False
      