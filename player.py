import pygame
from constants import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, grid, pos):
        self.grid = grid
        self.grid_position = pos
        self.prev_pos = pos
        self.pxl_pos = vec(self.grid_position.y * TILELENGTH, self.grid_position.x * TILELENGTH)
        print(self.pxl_pos / TILELENGTH)
        self.direction = vec(-1, 0)
        self.speed = 1
        self.radius = 8
        self.color = YELLOW
        self.stored_direction = None
        self.score = 0

    def update(self):
        self.pxl_pos += self.direction*self.speed           
        self.grid_position = vec((self.pxl_pos.x + TILELENGTH / 2) // TILELENGTH  , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)
        self.move_grid()
        #print(self.pxl_pos / TILELENGTH)


        direction = self.get_keypress(self.direction)

        #Collision handling 
        if self.collision(direction) and direction != self.direction:
            self.stored_direction = direction

        if self.stored_direction != None :
            if self.collision(self.stored_direction) == False:
                self.direction = self.stored_direction
                self.stored_direction = None
        else:
            self.direction = direction
            
        if self.collision(self.direction):
            self.direction = vec(0,0)


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
            return prev_dir

    def render(self, screen):
        p = (self.pxl_pos.x + TILELENGTH / 2, self.pxl_pos.y + TILELENGTH / 2)
        pygame.draw.circle(screen, self.color, p, self.radius)

    def move_grid(self):
        if self.prev_pos != self.grid_position:
            
            xval = int(self.prev_pos.x)
            yval = int(self.prev_pos.y)

            #Score points 
            if self.grid[int(self.grid_position.y)][int(self.grid_position.x)] == 3:
                self.score += 10
                print(self.score)
            
            self.grid[yval][xval] = 0
            self.grid[int(self.grid_position.y)][int(self.grid_position.x)] = 2
            self.prev_pos = self.grid_position


    #check the tile pacman is currently on is a wall, returns false otherwise
    def collision(self, dir):
         xval = int(self.grid_position.x + dir.x)
         yval = int(self.grid_position.y + dir.y)
         if self.grid[yval][xval] == 1:

            return True
         else:
            return False
      