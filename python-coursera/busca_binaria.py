def busca(lista, elemento):
    first = 0
    last = len(lista) - 1
    while first <= last:
        m = (first + last) // 2
        print(m)
        if lista[m] == elemento:
            return m
        else:
            if elemento < lista[m]:
                last = m - 1
            else:
                first = m + 1
    return False
