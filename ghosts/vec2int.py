class Vec2Int:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    

    def __eq__(self, other_vec):
        return self.x == other_vec.x and self.y == other_vec.y