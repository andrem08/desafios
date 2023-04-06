# Problema Uri 1279

import sys

linhas = sys.stdin.read().split('\n')
index = 1
for i in linhas:
    if i != '':
        ano = int(i)
    else:
        continue
    normal = True
    if ((ano % 4 == 0) and (ano % 100 != 0)) or ano % 400 == 0:
        print('This is leap year.')
        normal = False
    if ano % 15 == 0:
        print('This is huluculu festival year.')
        normal = False
    if (((ano % 4 == 0) and (ano % 100 != 0)) or ano % 400 == 0) and ano % 55 == 0:
        print('This is bulukulu festival year.')
    if normal:
        print('This is an ordinary year.')

    index += 1
    if index < len(linhas):
        print()
