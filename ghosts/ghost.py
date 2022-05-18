import pygame
from ghosts.pathfinder import Pathfinder
from ghosts.vec2int import Vec2Int
from constants import *
vec = pygame.math.Vector2


class Ghost:

    def __init__(self, pos: Vec2Int, grid: list[list[int]]):
        self.grid = grid
        self.pos = pos

        self.radius = TILELENGTH / 2
        self.color = RED
        self.speed = 1
        self.dir = Vec2Int(1, 0)
        self.pathfinder = Pathfinder(grid)
        
        self.last_target_pos = Vec2Int(0, 0)


    # Called every frame of the game
    def update(self, delta_time: float, player_pos: Vec2Int):
        # Non-Scatter mode
        self.dir = self.find_new_dir(player_pos)

        self.move(delta_time)

    
    # Draws the game object every frame of the game
    def draw(self, screen):
        pos = vec(self.pos.x + TILELENGTH/2, self.pos.y + TILELENGTH/2)
        pygame.draw.circle(screen, self.color, pos, self.radius)


    ## Helper methods ##
    def find_new_dir(self, target):
        
        # Check if player has the same grid coordinates as last frame 
        # to reduce unnecessary computing
        if target == self.last_target_pos:
            return self.dir

        # Select second node in path (aka the one after start)  
        path_to_target = self.pathfinder.find_path(self.get_grid_pos(), target)
        next_node_pos = Vec2Int(0, 0)
        if len(path_to_target) > 1:
            next_node_pos = path_to_target[1]

        self.last_target_pos = target
        return next_node_pos - self.get_grid_pos()


    # Move the entity in the direction of its choice
    def move(self, delta_time: float):
        const = delta_time * self.speed
        self.pos = self.pos + Vec2Int(self.dir.x * const, self.dir.y * const)


    def get_grid_pos(self):
        return Vec2Int(self.pos.x // TILELENGTH, self.pos.y // TILELENGTH)