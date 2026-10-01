import time

CSI = "\x1b["
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'
SIZE = 7

def drawline(offset, filled, color):
    offsetpart = f'{' '*offset}'
    filledpart = f'{CSI}48;5;{color}m{' '*filled}{RESET}'
    line = f'{offsetpart}{filledpart}'
    print(line)

def animated():
    colors = range(1, 231)
    while True:
        for color in colors:
            drawromb(SIZE, color)
            print(f'{CSI}{SIZE}A{ZERO}{ERASE}',end = '',flush=True)
            time.sleep(1)


def drawromb(size, color):
    center = size // 2
    offset = center
    filled = 1

    for line in range(size):
        drawline(offset, filled, color)
        if line < center:
           offset -= 1
           filled += 2
        else:
            offset += 1
            filled -= 2

if __name__ == '__main__':
    animated()