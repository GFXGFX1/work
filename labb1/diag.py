import os

CSI = "\x1b["
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
R = f'{CSI}0m'
up = f'{CSI}20A'
red = 9
white = 15
black = 0
green = 10
yellow = 11
blue = 12

with open ('testedseq.txt') as seq:
    a = seq.readlines()
q = []
for i in a:
    q.append(float(i[:-1]))

tri = [i for i in q if (i >= - 3 and i <= 3)]
netri = [i for i in q if i not in tri]
# print(len(tri), len(netri), len(q))
#         76         174        250
#print(len(tri) / 2.5)
#         30.4%
# print((len(netri)* 100) / 250)
#         69.6%
# Поскольку требований к видк=у диаграммы нет, выведу столбиками
urtri = (len(tri) / (2.5)) / 5
urnetri = (len(netri) / (2.5)) / 5
diag = f''


def coordx(x):
    return f'{CSI}{x}G'


def draw(color, leng):
    lengp = ' ' * leng
    filled = f'{CSI}48;5;{color}m'  # Цвет
    return (f'{filled}{lengp}')  # Полоска leng длины


for y in range(20, 0, -1):
    if y - 0.5 > urtri:
        a = '______'
    else:
        a = f'{draw(green, 6)}'
    if y - 0.5 > urnetri:
        b = '______'
    else:
        b = f'{draw(red, 6)}'
    diag += f'{y * 5 if y != 1 else ' 5'}%|_________{a}{R}______{b}{R}_________\n'
diag += f'   |         [-3:3]       Other\n'
print(diag)

seq.close()

