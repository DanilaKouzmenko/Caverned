from math import sin, cos, sqrt
from typing import Any
from mathing import rad, deg

class pos:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'x:{self.x}; y:{self.y}'
    def __add__(self, other):
        return pos(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return pos(self.x - other.x, self.y - other.y)

class vector:
    def __init__(self, angle:float, step : float):
        self.angle = angle
        self.step = step
    def __pos__(self) -> pos:
        x = round(cos(rad(self.angle)) * self.step)
        y = round(sin(rad(self.angle)) * self.step)
        return pos(x, y)

class Game:
    def __init__(self, map) -> Any:
        self.map = map
    def element_by_pos(self, pos : pos) -> object:
        return self.map[pos.y][pos.x]
    def map_slice(self, _from : pos, width : int, height: int) -> list:
        result = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            for x in range(width):
                result[y][x] = self.element_by_pos(pos(x + _from.x,_from.y + y))
        return result

class Player:
    def __init__(self, x : int, y : int):
        self.pos = pos(x, y)