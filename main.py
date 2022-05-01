import pygame
from constants import *
from player import Player

# PAC_MAN = pygame.image.load(os.path.join('Assets', 'pacman.png')) TODO
# BLUE_GHOST = pygame.image.load(os.path.join('Assets', 'blueghost.png')) TODO
# RED_GHOST = pygame.image.load(os.path.join('Assets', 'redghost.png')) TODO
# ORANGE_GHOST = pygame.image.load(os.path.join('Assets', 'orangeghost.png')) TODO
# PINK_GHOST = pygame.image.load(os.path.join('Assets', 'pinkghost.png')) TODO

# Gameboard representation 13x13


class Pacman(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()

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

    def update(self):
        self.clock.tick(FPS)
        self.player.update()
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(self.screen)
        pygame.display.update()
        self.draw_grid()

    def draw_grid(self):
        for x in range(COLS):
            pygame.draw.line(self.screen, YELLOW, (x*TILELENGTH, 0),
                             (x*TILELENGTH, SCREENHEIGHT))
        for y in range(ROWS):
            pygame.draw.line(self.screen, YELLOW, (0, y*TILELENGTH),
                             (SCREENWIDTH, y*TILELENGTH))


if __name__ == "__main__":
    game = Pacman()
    game.startGame()
    while True:
        game.update()
