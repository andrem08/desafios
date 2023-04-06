# Problema Uri 2450

#André Miyazawa
#11796187
def zeros(lin, col):
    esquerda = 0
    jump = 0

    for i in range(lin):
        #Le uma linha
        matrix = (input().split())
        while matrix == []:
            matrix = (input().split())
        #Verifica se deu falso
        if jump == 1:
            continue
        #Verifica se  todos os elementos anteriores
        #a esquerda, sao zero
        for j in range(0, min(esquerda, col)):
            if int(matrix[j]) != 0:
                jump = 1
        #Atualiza esquerda
        for j in range(esquerda, col):
            if int(matrix[j]) != 0:
                esquerda = j + 1
                break
            esquerda += 1
    #imprime
    if jump == 1:
        print("N")
        return
    print("S")

dim = input().split()
zeros(int(dim[0]), int(dim[1]))