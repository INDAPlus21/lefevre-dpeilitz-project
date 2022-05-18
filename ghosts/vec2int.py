import pygame

class Vec2Int:
    def __init__(self, x: int, y: int, vec = None):
        self.x = x
        self.y = y
    

    def __eq__(self, other_vec):
        return self.x == other_vec.x and self.y == other_vec.y


    def __add__(self, other_vec):
        return Vec2Int(self.x + other_vec.x, self.y + other_vec.y)


    def __sub__(self, other_vec):
        return Vec2Int(self.x - other_vec.x, self.y - other_vec.y)


    def __mul__(self, scalar: float):
        return Vec2Int(self.x * scalar, self.y * scalar)