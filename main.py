import pygame

from constants import *
from player import Player
from ghosts.ghost import Ghost
from ghosts.vec2int import Vec2Int

"""
from food import Food
from wall import Wall
"""
vec = pygame.math.Vector2


# PAC_MAN = pygame.image.load(os.path.join('Assets', 'pacman.png')) TODO
# BLUE_GHOST = pygame.image.load(os.path.join('Assets', 'blueghost.png')) TODO
# RED_GHOST = pygame.image.load(os.path.join('Assets', 'redghost.png')) TODO
# ORANGE_GHOST = pygame.image.load(os.path.join('Assets', 'orangeghost.png')) TODO
# PINK_GHOST = pygame.image.load(os.path.join('Assets', 'pinkghost.png')) TODO

class Game(object):
    def init(self):
        pygame.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

        self.background = None
        self.state = 'start'
        self.running = True
        self.grid  = PACMAN_GRID
        self.game_objects = []

        self.player = Player(self.grid, self.init_pacman())
        self.ghost = Ghost(self.grid, Vec2Int(TILELENGTH, TILELENGTH))

    def run(self):
        self.clock = pygame.time.Clock()
        self.setBackground()

        while self.running:
            self.clock.tick(FPS)
            if self.state == 'start':
                self.check_events()
                self.render_start()

            elif self.state == 'playing':
                self.update(1)
                self.render_play()
                self.check_events()

            elif self.state == 'paused':
                self.check_events()
            
            pygame.display.update()

        pygame.quit()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
    
    def init_pacman(self):
        for x in range(COLS):
            for y in range(ROWS):
                if self.grid[y][x] == 2:
                    return vec(y, x)
                    
    """ 
    borde väl fungera som initiering? får circular import så vette tusan   

    def init_grid(self):
        for x in range(COLS):
            for y in range(ROWS):
                if self.grid[y][x] == WALL:
                    self.game_objects.append(Wall(self.grid, vec(y,x)))
                if self.grid[y][x] == PACMAN:
                    self.game_objects.append(self.player)
                if self.grid[y][x] == CANDY:
                    self.game_objects.append(Food(self.grid, vec(y,x)))
                if self.grid[y][x] == SUPER_CANDY:
                    self.game_objects.append(Food(self.grid, vec(y,x)))
                if self.grid[y][x] == GHOST_BASIC:
                    self.game_objects.append(Ghost(self.grid, vec(y,x)))
                if self.grid[y][x] == GHOST_RED:
                    self.game_objects.append(Ghost(self.grid, vec(y,x)))
                if self.grid[y][x] == GHOST_CYAN:
                    self.game_objects.append(Ghost(self.grid, vec(y,x)))
                if self.grid[y][x] == GHOST_PINK:
                    self.game_objects.append(Ghost(self.grid, vec(y,x)))
                if self.grid[y][x] == GHOST_ORANGE:
                    self.game_objects.append(Ghost(self.grid, vec(y,x))) 
    """
                

    def update(self, delta_time: float):
        self.player.update()
        self.grid = self.player.grid
        self.ghost.update(delta_time, Vec2Int(self.player.grid_position.x, self.player.grid_position.y))
        self.check_gameover()

    def check_gameover(self):

        if self.player.grid_position.x - 0.5 == self.ghost.get_grid_pos().x and self.player.grid_position.y - 0.5 == self.ghost.get_grid_pos().y:
            exit()

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

    def draw_grid(self):
        for x in range(COLS):
            for y in range(ROWS):
                pygame.draw.rect(self.screen, GREY, (x*TILELENGTH, y*TILELENGTH,
                                TILELENGTH, TILELENGTH), 1)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, BLUE, (x*TILELENGTH, y*TILELENGTH,
                                TILELENGTH, TILELENGTH))
                # Draw Candy
                if self.grid[y][x] == 3:
                    pygame.draw.circle(self.screen, WHITE, (x*TILELENGTH + TILELENGTH/2, y*TILELENGTH + TILELENGTH/2), TILELENGTH / 6)
                # Draw super candy
                if self.grid[y][x] == 4:
                    pygame.draw.circle(self.screen, YELLOW, (x*TILELENGTH + TILELENGTH/2, y*TILELENGTH + TILELENGTH/2), TILELENGTH / 3)

    def render_play(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        self.player.render(self.screen)
        self.ghost.draw(self.screen)
        
        text = self.font.render("SCORE: " + str(self.player.score), False, WHITE)
        self.screen.blit(text, (SCREENWIDTH/18, 10.65*SCREENHEIGHT/12))
        

    def render_start(self):
        text = self.font.render("PRESS SPACE BAR", False, CERISE)
        self.screen.blit(text, (SCREENWIDTH/6, SCREENHEIGHT/2))

if __name__ == "__main__":
    game = Game()
    game.init()
    game.run()
