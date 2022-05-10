import pygame

# The node class
class Node:
    def __init__(self, passable: bool):
        self.passable = passable
        self.g_cost = 1000
        self.h_cost = 1000
        self.f_cost = 1000
        # pick_state: 0 = inte uppdaterad, 1 = uppdaterad och pickable, 2 = redan använd
        self.pick_state = 0
        
    def update(self, gcost: int, hcost: int, activator: tuple[int, int]):
        # Check if most efficient path from point a before changing the g_cost
        if self.g_cost > gcost:
            self.g_cost = gcost
            self.activator = activator
        # Set h_cost to distance to point b
        self.h_cost = hcost
        # The f_cost, a node's rating so to speak, is the sum of the g_cost and the h_cost
        self.f_cost = gcost + hcost
        # Check if node has been picked previously before making it pickable
        if self.pick_state != 2:
            self.pick_state = 1
        print(self.g_cost, self.h_cost, self.f_cost)


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
            
# Calculates the distance between two points on the grid (diagonal paths not allowed)
def calc_dist_to_point(a_cord: tuple[int, int], b_cord: tuple[int, int]):
    x_diff = abs(a_cord[0] - b_cord[0])
    y_diff = abs(a_cord[1] - b_cord[1])
    return x_diff + y_diff

# Return the adjacent nodes to a coordinate that are passable (diagonal paths once again not allowed)
def get_adjacents(node_grid: list[list[Node]], cord):
    adjacents = []
    
    # Check Up
    if cord[1] - 1 > -1:
        if node_grid[cord[0]][cord[1] - 1].passable:
            adjacents.append((cord[0], cord[1] - 1))

    # Check Down
    if cord[1] + 1 < len(node_grid[0]):
        if node_grid[cord[0]][cord[1] + 1].passable:
            adjacents.append((cord[0], cord[1] + 1))

    # Check Right
    if cord[0] + 1 < len(node_grid):
        if node_grid[cord[0] + 1][cord[1]].passable:
            adjacents.append((cord[0] + 1, cord[1]))

    # Check Left
    if cord[0] - 1 > -1:
        if node_grid[cord[0] - 1][cord[1]].passable:
            adjacents.append((cord[0] - 1, cord[1]))

    return adjacents

# Goes through all nodes in the node_grid with pick_state = 1 and picks the one with lowest f_cost
def find_node(node_grid: list[list[Node]]):
    lowest_cord = (0, 0)
    lowest_fcost = []
    for y in range(len(node_grid)):
        for x in range(len(node_grid[0])):
            if node_grid[x][y].pick_state == 1:
                if node_grid[x][y].f_cost < node_grid[lowest_cord[0]][lowest_cord[1]].f_cost:
                    lowest_fcost.clear()
                    lowest_fcost.append((x, y))
                elif node_grid[x][y].f_cost == node_grid[lowest_cord[0]][lowest_cord[1]].f_cost:
                    lowest_fcost.append((x, y))
    
    lowest_hcost = []
    lowest_cord = lowest_fcost[0]
    lowest_hcost.append(lowest_fcost[0])
    for i in range(1, len(lowest_fcost)):
        if node_grid[lowest_cord[0][0]][lowest_cord[0][1]].h_cost < node_grid[lowest_cord[i][0]][lowest_cord[i][1]].h_cost:
            lowest_hcost.clear()
            lowest_hcost.append(lowest_cord[i])
        elif node_grid[lowest_cord[0][0]][lowest_cord[0][1]].h_cost < node_grid[lowest_cord[i][0]][lowest_cord[i][1]].h_cost:
            lowest_hcost.append(lowest_cord[i])
    
    return lowest_hcost[0]
        


# Draws the newfound path on the original grid with 2's
def draw_path(grid: list[list[int]], node_grid: list[list[Node]]):
    while node_grid[cur_cord[0]][cur_cord[1]].activator != cur_cord:
        cur_cord = node_grid[cur_cord[0]][cur_cord[1]].activator
        grid[cur_cord[0]][cur_cord[1]] = 2

    return grid

# Define A* function
def find_path(grid: list[list[int]], a_cord: tuple[int, int], b_cord: tuple[int, int]):
    # Create a grid of passable and non-passable nodes based on game state grid
    node_grid = [[Node(grid[x][y] != 1) for y in range(len(grid))] for x in range(len(grid[0]))]

    ## Pathfinding algorithm ##

    # Update starting node
    node_grid[a_cord[0]][a_cord[1]].update(0, calc_dist_to_point(a_cord, b_cord) * 10, a_cord)

    cur_cord = a_cord

    # Run loop until destination is reached
    while cur_cord != b_cord:
        print("Nuvarande koordinater: " + str(cur_cord))
        
        # Find movable adjacent nodes, returns tuple
        adj = get_adjacents(node_grid, cur_cord)

        print("Adjacents: " + str(adj))        

        cur_node = node_grid[cur_cord[0]][cur_cord[1]]
        for i in range(len(adj)):
            # Update g_cost and h_cost values in adjacent nodes
            node_grid[adj[i][0]][adj[i][1]].update(cur_node.g_cost + 10, calc_dist_to_point(adj[i], b_cord) * 10, cur_cord)
        # Find the node on the grid that has the lowest f_cost, and as a tie breaker h_cost
        cur_cord = find_node(node_grid)

        hej = input()

    #grid = draw_path(grid, node_grid)

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