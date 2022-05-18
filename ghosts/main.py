import pygame
from vec2int import Vec2Int
from node import Node
from const import *
from pathfinder import Pathfinder


grid = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Initialize game
pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill(WHITE)


# Define function that draws a square on screen
def draw_rect(x: int, y: int, color):
    pygame.draw.rect(screen, color, pygame.Rect(y*BOXSIZE, x*BOXSIZE, BOXSIZE, BOXSIZE))

# Define function that draws the grid on screen
def draw_grid(grid: list[list[int]]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[x][y] == 0:
                draw_rect(x, y, WHITE)
            elif grid[x][y] == 1:
                draw_rect(x, y, BLACK)
            elif grid[x][y] == 9:
                draw_rect(x, y, RED)
            elif grid[x][y] == 8:
                draw_rect(x, y, GREEN)
            elif grid[x][y] == 2:
                draw_rect(x, y, YELLOW)


pf = Pathfinder(grid)
path = pf.find_path(Vec2Int(0, 9), Vec2Int(0, 0))
for i in range(len(path)):
    grid[path[i].y][path[i].x] = 2

# Start game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(grid)
    pygame.display.update()