def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        coluna = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            coluna.append(valor)
        matriz.append(coluna)
    return matriz

print(cria_matriz(3, 3))