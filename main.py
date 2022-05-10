import pygame
from constants import *
from player import Player
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

        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid  = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 4, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 4, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
            [1, 4, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 4, 1],
            [1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1],
            [1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1],
            [1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1],
            [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
            [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
            [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.player = Player(self.grid, self.init_pacman())

    def run(self):
        while self.running:
            self.checkEvents()
            self.update()
            self.render()
        pygame.quit()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.setBackground()
    
    def init_pacman(self):
        for x in range(COLS):
            for y in range(ROWS):
                if self.grid[y][x] == 2:
                    return vec(y, x)
                

    def update(self):
        self.clock.tick(FPS)
        self.player.update()
        self.grid = self.player.grid
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render(self.screen)
        self.draw_grid()
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



if __name__ == "__main__":
    game = Pacman()
    game.startGame()
    while True:
        game.update()
