#10954
# André e Ailton

import heapq

while True:
    n = input().split()[0]
    n = int(n)
    if n == 0:
        break
    numeros = input().split()
    numeros = [int(x) for x in numeros]
    soma = [None] * (len(numeros) -1 )
    i = 0
    s = 0
    heapq.heapify(numeros)
    while len(numeros) > 0:
        s = 0
        s = heapq.heappop(numeros)
        if len(numeros) != 0:
            s += heapq.heappop(numeros)
        soma[i] = s
        i += 1
        if len(numeros) != 0:
            heapq.heappush(numeros, s)
    somaTotal = 0
    for i in soma:
        somaTotal += i
    print(somaTotal)