import os
import time

CSI = "\x1b["
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
R = f'{CSI}0m'
up = f'{CSI}20A'
red = 9
white = 15
black = 0


# Просто вводные данные

def draw(color, leng):
    lengp = ' ' * leng
    filled = f'{CSI}48;5;{color}m'  # Цвет
    return (f'{filled}{lengp}')  # Полоска leng длины


def nx():
    print()

def swit():  # Алгоритм рисования флага швейцарии, длина около-произвольная (попытка нарисовать квадрат, т.к. флаг Швейцарии - 1 из 2-х квадратных флагов в мире)
    for i in range(2):
        print(draw(red, 31), R)
    for i in range(2):
        print(draw(red, 11), draw(white, 7), draw(red, 11), R)
    for i in range(3):
        print(draw(red, 6), draw(white, 17), draw(red, 6), R)
    for i in range(2):
        print(draw(red, 11), draw(white, 7), draw(red, 11), R)
    for i in range(2):
        print(draw(red, 31), R)

if __name__ == '__main__':
    swit()