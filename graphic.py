import colorama
from objects import pos, Game
from math import sin,cos,sqrt
from numpy import ndarray
from mathing import rad, fround
from cons_ui import cls

colorama.just_fix_windows_console()
colorama.init()

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

def raycast(start : pos, angle : float, matrix : ndarray, step) -> list[pos]:
    result = []
    for i in range(round(20 / step)):
        this_step = {}
        x = round(cos(angle + 90) * (i + 1) * step)
        y = round(sin(angle + 90) * (i + 1) * step)
        if matrix[y, x] == 1:
            this_step['pos'] = pos(x, y)
            this_step['type'] = 1
        result.append(this_step)
    return result

def render_matrix(matrix : Game, player_pos : pos, see : str) -> None: # see ( w - see all, f - fast )
    cls()
    arr = matrix.slice(player_pos, 11)
    print(f'╔══════════════════════╗')
    if 'w' in see:
        for indi, row in enumerate(arr):
            print('║', end='')
            for indj, el in enumerate(arr[row]):
                print(render_block(el.any(),0,FORE['white']), end='')
            print('║')
    print(f"╚══════════════════════╝")

