import colorama
from os import system
from keyboard import wait

colorama.init()
CLEAR_COLOR = colorama.Style.RESET_ALL
def clear():system('cls')

graphic_pack = {
    'floor':"..",
    'wall':"██",
    'player':"@@"
}

def Manual():
    clear()
    with open('Manual.txt','r',encoding='utf-8') as f:
        print(f.read())

def MainMenu():
    clear()
    ui =  '╔══════════════════════════════╗\n'
    ui += '║ Caverned Console Game v1.0.0 ║\n'
    ui += '║       H to open Manual       ║\n'
    ui += '║     Enter to start game      ║\n'
    ui += '╚══════════════════════════════╝'
    print(ui)
    wait('4')

def createWorld():
    clear()
    try:
        size = int(input("Enter the size of the world: "))
    except TypeError or ValueError:
        createWorld()

MainMenu()