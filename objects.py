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

class Map:
    def __init__(self, width : int, height : int):
        self.content = ([ 0 for _ in range(width)] for _ in range(height))
    def element_by_pos(self, pos : pos) -> object:
        return self.content[pos.y][pos.x]
    def map_slice(self, _from : pos, width : int, height: int) -> list:
        result = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            for x in range(width):
                result[y][x] = self.element_by_pos(pos(x + _from.x,_from.y + y))
        mapped = Map(width, height)
        mapped.content = result
        return mapped
    def set_by_pos(self, pos : pos, value : object) -> None:
        self.content[pos.y][pos.x] = value

class Player:
    def __init__(self, x : int, y : int):
        self.pos = pos(x, y)