from math import pi

def fround(n, a):
    return round(n*a) / a

def rad(n:float) -> float:
    return n * pi / 180

def deg(n:float) -> float:
    return n * 180 / pi