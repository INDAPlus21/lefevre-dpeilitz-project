import pygame
from constants import *
vec = pygame.math.Vector2


class Player:
    def __init__(self):
        self.position = vec(200, 400)
        self.direction = (0, 0)
        self.speed = 100
        self.radius = 10
        self.color = YELLOW

    def update(self):
        self.position += self.direction*self.speed
        direction = self.get_keypress()
        self.direction = direction

    def get_keypress(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            return vec(0, -1)
        if key_pressed[pygame.K_DOWN]:
            return vec(0, 1)
        if key_pressed[pygame.K_LEFT]:
            return vec(-1, 0)
        if key_pressed[pygame.K_RIGHT]:
            return vec(1, 0)

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)
