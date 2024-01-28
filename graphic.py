import colorama
from objects import pos
from math import sin,cos,sqrt,pi
import numpy as np
from mathing import rad, fround

colorama.just_fix_windows_console()
colorama.init()

RAD = 180 / pi
CLEAR = colorama.Style.RESET_ALL
FORE = {'black': colorama.Fore.BLACK,
        'white': colorama.Fore.WHITE,
        'blue':colorama.Fore.BLUE,
        'green':colorama.Fore.GREEN,
        'yellow':colorama.Fore.YELLOW,
        'cyan':colorama.Fore.CYAN,
        'purple':colorama.Fore.MAGENTA,
        'red':colorama.Fore.RED,}
BACK = {'black': colorama.Back.BLACK,
        'white': colorama.Back.WHITE,
        'blue': colorama.Back.BLUE,
        'green': colorama.Back.GREEN,
        'yellow': colorama.Back.YELLOW,
        'cyan': colorama.Back.CYAN,
        'purple': colorama.Back.MAGENTA,
        'red': colorama.Back.RED}
STYLE = {'bold': colorama.Style.BRIGHT,
         'dim': colorama.Style.DIM,
         'normal': colorama.Style.NORMAL}

def radians(degrees):
    return degrees / RAD

def render_block(type, sides : list[str], color) -> str:
    match type:
        case 0: return '..'
        case 3: 
            if 'top' in sides:
                if 'left' in sides:
                    return color + '█▀' + CLEAR
                elif 'right' in sides:
                    return color + '▀█' + CLEAR
                return color + '▀▀' + CLEAR
            elif 'bottom' in sides:
                if 'left' in sides:
                    return color + '█▄' + CLEAR
                elif 'right' in sides:
                    return color + '▄█' + CLEAR
                return color + '▄▄' + CLEAR
            elif 'left' in sides:
                return color + '█ ' + CLEAR
            elif 'right' in sides:
                return color + ' █'+ CLEAR
        case 2: return colorama.Fore.CYAN + '~~' + CLEAR
        case 1: return color + '██' + CLEAR
        case -1: return '  '
        case _: return colorama.Fore.RED + 'ER' + CLEAR
