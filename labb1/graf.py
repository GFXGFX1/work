import os

CSI = "\x1b["
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
R = f'{CSI}0m'
up = f'{CSI}20A'
red = 9
white = 15
black = 0
#           1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
grafic = f''

def draw(color, leng):
    lengp = ' ' * leng
    filled = f'{CSI}48;5;{color}m'  # Цвет
    return (f'{filled}{lengp}')  # Полоска leng длины

def coordx(x):
    return f'{CSI}{x}G'


for y in range(9, 0, -1):
    if y != 1:
        grafic += f'{coordx(0)}{y}|{coordx((int((3 / y)+ 0.5)) + 3)}{draw(red, 1)}{R}\n'
    else:
        grafic += f'{coordx(0)}{y}|{coordx((int(3 / y)) + 3)}{draw(red, 100)}{R}\n'
grafic += f'{coordx(0)}0----------------------------------------------------'
print(grafic)