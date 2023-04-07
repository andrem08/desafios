def ordenada(lista):
    for i in range(len(lista) - 1):
        aux_min = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[aux_min]:
                return False
        aux = lista[aux_min]
        lista[aux_min] = lista[i]
        lista[i] = aux
    return True
