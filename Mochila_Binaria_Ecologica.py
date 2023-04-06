# Problema Uva 102
import sys

linhas = sys.stdin.read().strip().split('\n')
linhas = list(linhas)

k1 = [0, 1, 2]
bottles = ['B', 'G', 'C']
letters = ''
for linha in linhas:
    numeros = list(map(int, linha.split()))
    total = sum(numeros)
    menor = total

    for i in k1:
        k2 = k1.copy()
        k2.remove(i)
        for l in k2:
            k3 = k2.copy()
            k3.remove(l)
            aux = total - numeros[i] - numeros[3 + l] - numeros[6 + k3[0]]
            auxl = ''
            auxl = auxl.join((bottles[i], bottles[l], bottles[k3[0]]))
            if aux < menor:
                letters = auxl
                menor = aux
            else:
                if aux == menor:
                    if letters > auxl:
                        letters = auxl
    print(letters, menor)






