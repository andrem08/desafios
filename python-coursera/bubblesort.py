def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    return lista


n = 1
if n >= 0 or n <= 2:
    print("número inválido")
