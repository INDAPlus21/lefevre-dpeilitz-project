import pygame

from constants import *
from player import Player
from ghosts.ghost import Ghost
from ghosts.vec2int import Vec2Int

vec = pygame.math.Vector2


# PAC_MAN = pygame.image.load(os.path.join('Assets', 'pacman.png')) TODO
# BLUE_GHOST = pygame.image.load(os.path.join('Assets', 'blueghost.png')) TODO
# RED_GHOST = pygame.image.load(os.path.join('Assets', 'redghost.png')) TODO
# ORANGE_GHOST = pygame.image.load(os.path.join('Assets', 'orangeghost.png')) TODO
# PINK_GHOST = pygame.image.load(os.path.join('Assets', 'pinkghost.png')) TODO

class Pacman(object):
    def __init__(self):
        pygame.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.state = 'start'
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid  = PACMAN_GRID
        self.player = Player(self.grid, self.init_pacman())
        self.ghost = Ghost(self.grid, Vec2Int(TILELENGTH, TILELENGTH))

    def run(self):
        while self.running:
            print(self.state)
            if self.state == 'start':
                self.check_events()
                self.start_render()
                print("wewo")

            elif self.state == 'playing':
                self.update()
                self.render()
                self.check_events()
                print("fasen")

            elif self.state == 'paused':
                self.check_events()

        pygame.quit()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def start_game(self):
        self.setBackground()
    
    def init_pacman(self):
        for x in range(COLS):
            for y in range(ROWS):
                if self.grid[y][x] == 2:
                    return vec(y, x)
                

    def update(self):
        self.clock.tick(FPS)

        # Update game objects
        self.player.update()
        self.grid = self.player.grid
        self.ghost.update(1, Vec2Int(int(self.player.grid_position.x), int(self.player.grid_position.y)))
        
        # Game logic
        self.checkEvents()
        self.render()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state == "playing":
                    self.state = 'paused'
                else:
                    self.state = 'playing'  

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        self.player.render(self.screen)
        self.ghost.draw(self.screen)
        text = self.font.render("SCORE: " + str(self.player.score), False, WHITE)
        self.screen.blit(text, (100,500))

        pygame.display.update()

    def draw_grid(self):
        for x in range(COLS):
            for y in range(ROWS):
                pygame.draw.rect(self.screen, GREY, (x*TILELENGTH, y*TILELENGTH,
                                TILELENGTH, TILELENGTH), 1)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, BLUE, (x*TILELENGTH, y*TILELENGTH,
                                TILELENGTH, TILELENGTH))
                if self.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, RED, (x*TILELENGTH, y*TILELENGTH,
                                TILELENGTH, TILELENGTH), 1)
                # Draw Candy
                if self.grid[y][x] == 3:
                    pygame.draw.circle(self.screen, WHITE, (x*TILELENGTH + TILELENGTH/2, y*TILELENGTH + TILELENGTH/2), TILELENGTH / 6)
                # Draw super candy
                if self.grid[y][x] == 4:
                    pygame.draw.circle(self.screen, YELLOW, (x*TILELENGTH + TILELENGTH/2, y*TILELENGTH + TILELENGTH/2), TILELENGTH / 3)

    def start_render(self):
        self.clock.tick(FPS)
        text = self.font.render("PRESS SPACE BAR", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH/6, SCREENHEIGHT/2))
        pygame.display.update()


if __name__ == "__main__":
    game = Pacman()
    game.start_game()
    while True:
        game.run()
