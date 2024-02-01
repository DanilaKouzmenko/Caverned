from objects import Player, Map, pos
import keyboard
from random import randint as rand
from time import sleep
from graphic import draw_matrix

def moving(side : str, matrix : Map, player : Player):
    using_plate = matrix.map_slice(player.pos - pos(1, 1), 3, 3).content
    match side:
        case "up":
            if using_plate[0][1] != 1:
                player.pos -= pos(0, 1)
        case "down":
            if using_plate[2][1] != 1:
                player.pos += pos(0, 1)
        case "left":
            if using_plate[0][1] != 1:
                player.pos -= pos(1, 0)
        case "right":
            if using_plate[0][1] != 1:
                player.pos += pos(1, 0)

def _key(_function, map : Map, player : Player):
    _function()
    draw_matrix(map, player.pos)
    sleep(0.09)

