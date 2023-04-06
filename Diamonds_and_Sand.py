# Problema Uri 1069

n = int(input())

for i in range(n):
    linha = [i for i in input()]
    open = 0
    diamonds = 0
    for i in linha:
        if i == '<':
            open += 1
        else:
            if i == '>' and open > 0:
                diamonds += 1
                open -= 1

    print(diamonds)