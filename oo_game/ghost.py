import pygame

from main import Game
from entity import Entity
from ghosts.pathfinder import Pathfinder
from ghosts.vec2int import Vec2Int
from constants import *

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self, game: Game, pos: vec, img):
        # A set value for speed
        super().__init__(game, pos, img, 1)

        self.pathfinder = Pathfinder(self.game.grid)

        self.last_target_pos = Vec2Int(0, 0)
        self.last_grid_pos = Vec2Int(0, 0)

    
    def update(self, delta_time: float):
        self.dir = self.find_new_dir(self.game.player.pos)

        self.move(delta_time)

    
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
        
    # Implementera bättre om du vill
    def get_grid_pos(self):
        return Vec2Int(int(self.pos.x // TILELENGTH), int(self.pos.y // TILELENGTH))