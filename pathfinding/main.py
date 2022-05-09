import pygame

# The node class
class Node:
    def __init__(self, passable: bool):
        self.passable = passable
        
    def update(self, gcost: int, hcost: int, activator: tuple[int, int]):
        self.g_cost = gcost
        self.h_cost = hcost
        self.f_cost = gcost + hcost
        self.activator = activator


# Initialize constants
SCREENSIZE = (500, 500)
BOXSIZE = 50;
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
grid = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Transpose grid to allow for [x][y] indexing
grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]

# Initialize game
pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill(WHITE)
            

def calc_dist_to_point(a_cord: tuple[int, int], b_cord: tuple[int, int]):
    x_diff = abs(a_cord[0] - b_cord[0])
    y_diff = abs(a_cord[1] - b_cord[1])
    return x_diff + y_diff

def get_adjacents(node_grid: list[list[Node]], cord):
    adjacents = []
    
    # Check Up
    if cord[1] - 1 > -1:
        if node_grid[cord[0]][cord[1] - 1].passable:
            adjacents.append(node_grid[cord[0]][cord[1] - 1])

    # Check Down
    if cord[1] + 1 < len(node_grid[0]):
        if node_grid[cord[0]][cord[1] + 1].passable:
            adjacents.append(node_grid[cord[0]][cord[1] + 1])

    # Check Right
    if cord[0] + 1 < len(node_grid):
        if node_grid[cord[0] + 1][cord[1]].passable:
            adjacents.append(node_grid[cord[0] + 1][cord[1]])

    # Check Left
    if cord[0] - 1 > -1:
        if node_grid[cord[0] - 1][cord[1]].passable:
            adjacents.append(node_grid[cord[0] - 1][cord[1]])

    return adjacents



# Define A* function
def find_path(grid: list[list[int]], a_cord: tuple[int, int], b_cord: tuple[int, int]):
    # Create a grid of passable and non-passable nodes based on game state grid
    node_grid = [[Node(grid[x][y] != 1) for y in range(len(grid))] for x in range(len(grid[0]))]

    # Pathfinding algorithm
    node_grid[a_cord[0]][a_cord[1]].update(0, calc_dist_to_point(a_cord, b_cord), a_cord)

    cur_cord = a_cord
    while cur_cord != b_cord:
        adj = get_adjacents(node_grid, cur_cord)
        cur_cord = b_cord


    while node_grid[cur_cord[0]][cur_cord[1]].activator != cur_cord:
        cur_cord = node_grid[cur_cord[0]][cur_cord[1]].activator
        grid[cur_cord[0]][cur_cord[1]] = 2

    return grid

# Define function that draws a square on screen
def draw_rect(x: int, y: int, color):
    pygame.draw.rect(screen, color, pygame.Rect(x*BOXSIZE, y*BOXSIZE, BOXSIZE, BOXSIZE))

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

grid = find_path(grid, (0, 9), (0, 0))

# Start game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(grid)
    pygame.display.update()