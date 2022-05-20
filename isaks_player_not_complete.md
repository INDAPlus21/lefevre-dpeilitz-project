import pygame

from constants import *

vec = pygame.math.Vector2

class Player:
    def __init__(self, grid, pos):
        self.grid = grid
        self.grid_pos = pos
        self.last_grid_pos = pos
        self.pos = vec(self.grid_pos.y * TILELENGTH, self.grid_pos.x * TILELENGTH)
        self.last_pos = self.pos

        print("Player starts at: ", self.pos / TILELENGTH)
        self.dir = vec(-1, 0)
        self.speed = 2
        self.radius = TILELENGTH / 2.1
        self.color = YELLOW
        self.last_dir = None
        self.score = 0

    def update(self):
        self.pos += self.dir*self.speed
        
        # if self.direction == (0,1) or self.direction == (1,0):
        #     self.grid_position = vec((self.pxl_pos.x) // TILELENGTH  , (self.pxl_pos.y) // TILELENGTH)
        #     #self.grid_position = vec((self.pxl_pos.x + TILELENGTH / 2) // TILELENGTH  , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)

        # if self.direction == (0,-1) or self.direction == (-1,0):
        #     #self.grid_position = vec((self.pxl_pos.x +  TILELENGTH / 2) // TILELENGTH  , (self.pxl_pos.y + TILELENGTH / 2) // TILELENGTH)
        #     self.grid_position = vec((self.pxl_pos.x) // TILELENGTH  , (self.pxl_pos.y) // TILELENGTH)

        last_num = (self.last_pos.x / TILELENGTH)
        num = (self.pos.x / TILELENGTH)
        closest_pos = round(num)
        diff_prod = (last_num - closest_pos) * (num - closest_pos)

        if diff_prod < 0:
            self.grid_pos.x = closest_pos

        last_num = (self.last_pos.y / TILELENGTH)
        num = (self.pos.y / TILELENGTH)
        closest_pos = round(num)
        diff_prod = (last_num - closest_pos) * (num - closest_pos)

        if diff_prod < 0:
            self.grid_pos.y = closest_pos

        self.move_grid()
        #print(self.pxl_pos / TILELENGTH)

        new_dir = self.get_dir()
        self.dir = self.check_dir(new_dir)

        self.last_pos = self.pos
        self.last_grid_pos = self.last_grid_pos
        self.last_dir = self.dir

        

    # Change direction based on player input
    def get_dir(self):
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
            return self.dir

    # Control that the proposed direction is viable / Wall handling
    def check_dir(self, new_dir):
        if self.check_if_in_wall(new_dir) and new_dir != self.dir:
            return new_dir
        else:
            return self.dir

    # Render the player
    def render(self, screen):
        const = TILELENGTH / 2
        render_pos = (self.pos.x + const, self.pos.y + const)
        pygame.draw.circle(screen, self.color, render_pos, self.radius)

    # Update grid state if player has moved onto a new tile
    def move_grid(self):
        if self.last_grid_pos != self.grid_pos:
            print("wat")
            xval = int(self.last_grid_pos.x)
            yval = int(self.last_grid_pos.y)

            #Score points 
            if self.grid[int(self.grid_pos.y)][int(self.grid_pos.x)] == 3:
                self.score += 10
                print(self.score)
            if self.grid[int(self.grid_pos.y)][int(self.grid_pos.x)] == 4:
                self.score += 50
            
            self.grid[yval][xval] = 0
            self.grid[int(self.grid_pos.y)][int(self.grid_pos.x)] = 2


    #check the tile pacman is currently on is a wall, returns false otherwise
    def check_if_in_wall(self, dir):
         x_wall = int((self.grid_pos.x + dir.x)) 
         y_wall = int((self.grid_pos.y + dir.y))
         
         if self.grid[y_wall][x_wall] == 1:
            return True
         else:
            return False
      



"""

if self.check_if_in_wall(new_dir) and new_dir != self.dir:
            self.last_dir = new_dir

        if self.last_dir != None:
            if self.check_if_in_wall(self.last_dir) == False:
                self.dir = self.last_dir
                self.last_dir = None
        else:
            self.dir = new_dir
            
        if self.check_if_in_wall(self.dir):
            self.dir = vec(0,0)

"""







EVEN MORE NOT COMPLETED:



    # Returns the movement vector so that it doesn't go through walls
    def hits_wall(self, move_vec: vec, walls: list[Wall]):
        new_hb = rect(move_vec.x, move_vec.y, TILELENGTH, TILELENGTH)
        for i in range(len(walls)):
            wall_hb = walls[i].hitbox

            if new_hb.colliderect(wall_hb):
                print("new: ", new_hb, "wall: ", wall_hb)

                # Collide with wall to the right of entity
                if new_hb.left < wall_hb.right and int(self.dir.x) == -1:
                    # Calculate how far into the wall the entity is
                    coll_dist = wall_hb.right - new_hb.left
                    # Recalculate move_vec to prevent collision
                    move_vec = vec(move_vec.x + coll_dist, move_vec.y)

        return move_vec
"""
(new_hb.left >= wall_hb.right or new_hb.top >= wall_hb.bottom or new_hb.right <= wall_hb.left or new_hb.bottom <= wall_hb.top) == False
                # Collide with wall above entity
                if (new_hb.top >= wall_hb.bottom) == False:
                    coll_dist = new_hb.top - wall_hb.bottom
                    move_vec = vec(move_vec.x, move_vec.y + coll_dist)

                # Collide with wall to the right of entity
                if (new_hb.right <= wall_hb.left) == False:
                    coll_dist = new_hb.right - wall_hb.left
                    move_vec = vec(move_vec.x + coll_dist, move_vec.y)

                # Collide with wall below entity
                if (new_hb.bottom <= wall_hb.top) == False:
                    coll_dist = new_hb.bottom - wall_hb.top
                    move_vec = vec(move_vec.x, move_vec.y + coll_dist)
"""
        