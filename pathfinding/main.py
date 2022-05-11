import pygame

grid = [
    [9, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [8, 0, 0, 0, 0],
]

pygame.init()

screen = pygame.display.set_mode((500, 500))

def draw_grid():
    for x in range(5):
        for y in range(5):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*100, y*100, 100, 100), 1)

            if grid[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x*100, y*100, 100, 100))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_grid()
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 100, 100))

