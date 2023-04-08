#André Miyazawa
#11796187

import sys

parenteses = 0
linhas = sys.stdin.read().strip().split('\n')
for l in linhas:
    for i in l:
        if i == '(':
            parenteses += 1
        elif i == ')':
            if parenteses == 0:
                parenteses -= 1
                break
            parenteses -= 1
    if parenteses == 0:
        print("correct")
    else:
        print("incorrect")
    parenteses = 0