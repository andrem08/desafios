# Problema Uva 119
import sys

linhas = sys.stdin.read().strip().split('\n')
linhas = list(linhas)
index = 0

while True:
    n = int(linhas[index])
    d = dict((sub, 0) for sub in linhas[index + 1].split())
    dados = [i.split(' ') for i in linhas[index + 2:index + 2 + n]]

    for i in dados:
        if int(i[2]) != 0:
            divisor = int(i[2])
            aux = int(i[1]) - (int(i[1]) % divisor)
        else:
            d[i[0]] = d[i[0]] + int(i[1])
            aux = int(i[1])
            divisor = 1

        d[i[0]] = d[i[0]] - aux
        for j in range(int(i[2])):
            d[i[3 + j]] = d[i[3 + j]] + (aux / divisor)
    index = index + n + 2

    for i in d: print(i, round(d[i]))
    if len(linhas) <= index:
        break
    print()
