import pygame

from ghosts.pathfinder import Pathfinder
from ghosts.vec2int import Vec2Int
from constants import *

vec = pygame.math.Vector2


class Ghost:

    def __init__(self, grid: list[list[int]], spawn_point: Vec2Int):
        self.grid = grid
        self.spawn_point = spawn_point
        self.pos = spawn_point

        self.side_size = TILELENGTH
        self.color = RED
        self.speed = 2
        self.dir = Vec2Int(1, 0)
        self.pathfinder = Pathfinder(grid)
        
        self.last_target_pos = Vec2Int(0, 0)
        self.last_grid_pos = Vec2Int(0, 0)


    # Called every frame of the game
    def update(self, delta_time: float, player_pos: Vec2Int):
        # Non-Scatter mode
        new_dir = self.find_new_dir(player_pos)
        self.dir = new_dir

        self.move(delta_time) 

    
    # Draws the game object every frame of the game
    def draw(self, screen):
        pos = vec(self.pos.x + TILELENGTH/2, self.pos.y + TILELENGTH/2)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos.x, self.pos.y, self.side_size, self.side_size))


    ## Helper methods ##
    def find_new_dir(self, target_pos):
        
        curr_grid_pos = self.get_grid_pos()

        # Check if player has the same grid coordinates as last frame 
        # to reduce unnecessary computing
        if target_pos == self.last_target_pos and curr_grid_pos == self.last_grid_pos:
            return self.dir

        # Select second node in path (aka the one after start)  
        path_to_target = self.pathfinder.find_path(curr_grid_pos, target_pos)
        next_node_pos = Vec2Int(0, 0)
        if len(path_to_target) > 1:
            next_node_pos = path_to_target[1]

        self.last_target_pos = target_pos
        self.last_grid_pos = curr_grid_pos

        return next_node_pos - curr_grid_pos


    # Move the entity in the direction of its choice
    def move(self, delta_time: float):
        const = delta_time * self.speed
        x = int(self.dir.x * const)
        y = int(self.dir.y * const)
        self.pos = self.pos + vec(x, y)


    def get_grid_pos(self):
        return Vec2Int(int(self.pos.x // TILELENGTH), int(self.pos.y // TILELENGTH))