def imprime_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento != linha[len(linha) - 1]:
                print(elemento, end=" ")
            else:
                print(elemento)