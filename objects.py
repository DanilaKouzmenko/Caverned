from math import sin, cos, sqrt
from mathing import rad, deg
from numpy import array as np_arr

class pos:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return str(self.y) + "|" + str(self.x)
    def __add__(self, other):
        return pos(self.x + other.x, self.y + other.y)

class vector:
    def __init__(self, angle:float, step : float):
        self.angle = angle
        self.step = step
    def __pos__(self) -> pos:
        x = round(cos(rad(self.angle)) * self.step)
        y = round(sin(rad(self.angle)) * self.step)
        return pos(x, y)

class Game:
    def __init__(self, map):
        self.map = map
    def get_element_by_pos(self, pos: pos) -> int:
        return self.map[pos.y][pos.x]
    def slice(self, posit : pos, diameter : int):
        result = [[-1 for _ in range(diameter)] for _ in range(diameter) ]
        for i in range(diameter):
            for j in range(diameter):
                result[i][j] = self.get_element_by_pos(pos(round(posit.x + j - diameter / 2), round(posit.y + i - diameter / 2)))
        return np_arr(result)

class Player:
    def __init__(self, x : int, y : int):
        self.pos = pos(x, y)