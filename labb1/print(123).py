import time

CSI = "\x1b["
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'

def drawline(offset, filled, color):
    offsetpart = f'{' '*offset}'
    filledpart = f'{CSI}48;5;{color}m{' '*filled}{RESET}'
    line = f'{offsetpart}{filledpart}'
    print(line)

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
    drawromb(7, 93)