def encontra_impares(lista):
    lista2 = []
    if len(lista) >= 1:
        if lista[0] % 2 != 0:
            lista2.append(lista[0])
        lista2 = lista2 + encontra_impares(lista[1:])
    return lista2
