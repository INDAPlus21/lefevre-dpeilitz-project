import pygame

from constants import *

vec = pygame.math.Vector2

class Player:
    def __init__(self, grid, pos):
        self.grid = grid
        self.grid_position = pos
        self.prev_pos = pos

        self.pxl_pos = vec(self.grid_position.y * TILELENGTH + TILELENGTH/2, self.grid_position.x * TILELENGTH + TILELENGTH/2 )
        print(self.pxl_pos / TILELENGTH)
        self.direction = vec(-1, 0)
        self.speed = 2
        self.radius = TILELENGTH / 2.1
        self.color = YELLOW
        self.stored_direction = None
        self.score = 0

    def update(self):
        self.pxl_pos += self.direction*self.speed
        
        # if self.direction == (0,1) or self.direction == (1,0):
        #     self.grid_position = vec((self.pxl_pos.x) // TILELENGTH  , (self.pxl_pos.y) // TILELENGTH)
        #     #self.grid_position = vec((self.pxl_pos.x + TILELENGTH / 2) // TILELENGTH  , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)

        # if self.direction == (0,-1) or self.direction == (-1,0):
        #     #self.grid_position = vec((self.pxl_pos.x +  TILELENGTH / 2) // TILELENGTH  , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)
        #     self.grid_position = vec((self.pxl_pos.x) // TILELENGTH  , (self.pxl_pos.y) // TILELENGTH)

        if (self.pxl_pos.x / TILELENGTH - 0.5).is_integer():
            self.grid_position.x = self.pxl_pos.x / TILELENGTH

        if (self.pxl_pos.y / TILELENGTH - 0.5).is_integer():
            self.grid_position.y = (self.pxl_pos.y / TILELENGTH)

        self.move_grid()
        #print(self.pxl_pos / TILELENGTH)

        direction = self.get_dir(self.direction)

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


    def get_dir(self, prev_dir):
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
            #return vec (0,0)

    def render(self, screen):
        p = (self.pxl_pos.x , self.pxl_pos.y)
        pygame.draw.circle(screen, self.color, p, self.radius)

    def move_grid(self):
        if self.prev_pos != self.grid_position:
            print("wat")
            xval = int(self.prev_pos.x)
            yval = int(self.prev_pos.y)

            #Score points 
            if self.grid[int(self.grid_position.y)][int(self.grid_position.x)] == 3:
                self.score += 10
                print(self.score)
            if self.grid[int(self.grid_position.y)][int(self.grid_position.x)] == 4:
                self.score += 50
            
            self.grid[yval][xval] = 0
            self.grid[int(self.grid_position.y)][int(self.grid_position.x)] = 2
            self.prev_pos = self.grid_position


    #check the tile pacman is currently on is a wall, returns false otherwise
    def collision(self, dir):
         xval = int((self.grid_position.x + dir.x)* TILELENGTH) 
         yval = int((self.grid_position.y + dir.y) * TILELENGTH)
         x_wall = int((self.grid_position.x + dir.x)) 
         y_wall = int((self.grid_position.y + dir.y))
         
         if self.grid[y_wall][x_wall] == 1:

            return True
         else:
            return False
      