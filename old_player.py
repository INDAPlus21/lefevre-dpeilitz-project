import pygame

from oo_game.constants import *

vec = pygame.math.Vector2

class Player:
    def __init__(self, grid, pos):
        self.grid = grid
        self.grid_position = pos
        self.prev_pos = pos
        self.pxl_pos = vec(self.grid_position.y * TILELENGTH + TILELENGTH/2, self.grid_position.x * TILELENGTH + TILELENGTH/2 )
        print(self.pxl_pos / TILELENGTH)
        self.direction = vec(0,0)
        self.speed = 1
        self.radius = TILELENGTH / 2.1
        self.color = YELLOW
        self.stored_direction = None
        self.score = 0

    def update(self):

        #Movement forwards and backwards
        if self.collision(self.direction) == False:
            self.pxl_pos += self.direction*self.speed
        else:
                self.direction = vec(0,0)


        if (self.pxl_pos.x / TILELENGTH - 0.5).is_integer():
            if self.stored_direction != None:
                if self.collision(self.stored_direction) == False:
                    self.direction = self.stored_direction
                    self.stored_direction = None
                    print("wat")
            self.grid_position.x = self.pxl_pos.x / TILELENGTH


        if (self.pxl_pos.y / TILELENGTH - 0.5).is_integer():
            if self.stored_direction != None:
                if self.collision(self.stored_direction) == False:
                    self.direction = self.stored_direction
                    self.stored_direction = None
                    print("water")
            self.grid_position.y = (self.pxl_pos.y / TILELENGTH)

        
        self.move_grid()
        
        dir = self.get_dir(self.direction)
        if dir != self.direction:

            if (self.direction == LEFT or self.direction == RIGHT) and (dir == UP or dir == DOWN):
                self.stored_direction = dir
            elif (self.direction == UP or self.direction == DOWN) and (dir == LEFT or dir== RIGHT):
                self.stored_direction = dir
            else:
                self.direction = dir
                self.stored_direction = None

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
        pygame.draw.rect(screen, RED, ((self.grid_position.x-0.5)*TILELENGTH, (self.grid_position.y-0.5)*TILELENGTH,
                                TILELENGTH, TILELENGTH), 1)

    def move_grid(self):
        if self.prev_pos != self.grid_position:
            xval = int(self.prev_pos.x)
            yval = int(self.prev_pos.y)

            #Score points 
            if self.grid[int(self.grid_position.y)][int(self.grid_position.x)] == 3:
                self.score += 10
            if self.grid[int(self.grid_position.y)][int(self.grid_position.x)] == 4:
                self.score += 50
            
            self.grid[yval][xval] = 0
            self.grid[int(self.grid_position.y)][int(self.grid_position.x)] = 2
            self.prev_pos = self.grid_position


    #check the tile pacman is currently on is a wall, returns false otherwise
    def collision(self, dir):
         xval = self.pxl_pos.x + (dir.x * TILELENGTH) 
         yval = self.pxl_pos.y + (dir.y * TILELENGTH)
         x_wall = int((self.grid_position.x + dir.x)) 
         y_wall = int((self.grid_position.y + dir.y))
         
         if self.grid[y_wall][x_wall] == 1:
            return True
         else:
            return False
      