# Problema Uri 1110

numero = int(input())

while numero > 0:
    cartas = [i for i in range(1, numero + 1, 1)]
    descarte = []
    k = 0
    while len(cartas) > 1:
        l = len(cartas)
        descarte = descarte + [cartas[i] for i in range(0 + k, len(cartas), 2)]
        cartas = [cartas[i] for i in range(1 - k, len(cartas), 2)]
        if l%2 is 1:
            if k is 1:k = 0
            else: k = 1
    if len(cartas) is 1:
        descarte = ' '.join(map(str, descarte))
        descarte = descarte.replace(' ', ', ')
        print('Discarded cards:', descarte)
        print('Remaining card:', cartas[0])
    numero = int(input())