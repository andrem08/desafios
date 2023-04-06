# Problema Uri 1022

def computeGCD(x, y):
    while (y):
        x, y = y, x % y
    return abs(x)


def simplificar(num):
    div = computeGCD(abs(num[0]), abs(num[1]))
    num = [int(num[0] / div), int(num[1] / div)]
    return num


n = int(input())
for i in range(n):
    linha = input().split(' ')
    n1 = [int(linha[0]), int(linha[2])]
    n2 = [int(linha[4]), int(linha[6])]
    d = [n1[1], n2[1]]

    if (linha[3] is '+') or (linha[3] is '-'):
        n1 = [n1[0] * d[1], n1[1] * d[1]]
        n2 = [n2[0] * d[0], n2[1] * d[0]]
        if linha[3] is '+':
            num = [n1[0] + n2[0], n1[1]]
        else:
            num = [n1[0] - n2[0], n1[1]]
    elif linha[3] is '*':
        num = [n1[0] * n2[0], n1[1] * n2[1]]
    elif linha[3] is '/':
        num = [n1[0] * n2[1], n1[1] * n2[0]]
    num2 = simplificar(num)
    print(num[0], '/', num[1], ' = ', num2[0], '/', num2[1], sep='')
