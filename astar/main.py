import pygame
from vec2int import Vec2Int
from node import Node
from const import *
from pathfinder import Pathfinder


grid = [
    [9, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
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


def calc_new_path(target_pos: Vec2Int) -> list[list[int]]:
    new_grid = [[grid[y][x] for x in range(10)] for y in range(10)]
    
    pf = Pathfinder(grid)
    path = pf.find_path(Vec2Int(0, 9), target_pos)
    new_grid[target_pos.y][target_pos.x] = 9
    for i in range(1, len(path) - 1):
        new_grid[path[i].y][path[i].x] = 2

    return new_grid

new_grid = calc_new_path(Vec2Int(0, 0))
grid[0][0] = 0

# Start game loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_vec = Vec2Int(mouse_pos[0] // BOXSIZE, mouse_pos[1] // BOXSIZE)

        if grid[mouse_vec.y][mouse_vec.x] != 1:
            new_grid = calc_new_path(mouse_vec)
            

    draw_grid(new_grid)
    pygame.display.update()