from math import pi
from random import randint as rand

def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def rand_percent(per : float) -> bool:
    return True if rand(0, 999999999999999999) / 10 ^ 16 < per else False

def fround(n, a):
    return round(n*a) / a

def rad(n:float) -> float:
    return n * pi / 180

def deg(n:float) -> float:
    return n * 180 / pi