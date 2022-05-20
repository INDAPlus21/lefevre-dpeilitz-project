import pygame

from vector import Vector2
from constants import *
from game_object import GameObject
from wall import Wall
from player import Player
from node_group import NodeGroup

class Game:
    def init(self):
        pygame.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

        self.background = None
        self.state = 'start'
        self.running = True
        self.grid  = GAME_GRID
        self.game_score = 0

        self.walls = []
        self.player = None
        self.nodes = NodeGroup()

        self.init_game()


    def init_game(self):
        for x in range(COLS):
            for y in range(ROWS):
                if self.grid[y][x] == WALL:
                    self.walls.append(Wall(Vector2(x, y)))
                elif self.grid[y][x] == PLAYER:
                    self.player = Player(Vector2(x, y))


    def run(self):
        self.clock = pygame.time.Clock()
        self.setBackground()

        ticks_last_frame = pygame.time.get_ticks()

        while self.running:

            self.clock.tick(FPS)
            delta_time = (pygame.time.get_ticks() - ticks_last_frame) / 1000.0

            if self.state == 'start':
                self.check_events()
                self.render_start()

            elif self.state == 'playing':
                self.update(delta_time)
                self.render_play()
                self.check_events()

            elif self.state == 'paused':
                self.check_events()
            
            pygame.display.update()
            ticks_last_frame = pygame.time.get_ticks()

        pygame.quit()


    def update(self, delta_time):
        self.player.update(delta_time, self.walls)

    
    def render_play(self):
        self.screen.blit(self.background, (0, 0))

        # Draw all game objects
        self.nodes.draw(self.screen)
        for i in range(len(self.walls)):
            self.walls[i].draw(self.screen)
        self.player.draw(self.screen)
        
        text = self.font.render("SCORE: " + str(self.game_score), False, WHITE)
        self.screen.blit(text, (SCREENWIDTH/18, 10.65*SCREENHEIGHT/12))
        

    def render_start(self):
        text = self.font.render("PRESS SPACE BAR", False, CERISE)
        self.screen.blit(text, (SCREENWIDTH/6, SCREENHEIGHT/2))


    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)


    def check_events(self):
        for event in pygame.event.get():
            # Exit event
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()
            # Pause event
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state == "playing":
                    self.state = 'paused'
                else:
                    self.state = 'playing'  