def mochila_pessoa(carrega, objetos, tamanho):
    if carrega == 0 or tamanho == 0:
        return 0
    # Se não é possivel carregar
    if objetos[tamanho - 1][1] > carrega:
        return mochila_pessoa(carrega, objetos, tamanho - 1)
    # Se é possivel carregar
    nao_usa = mochila_pessoa(carrega, objetos, tamanho - 1)
    objetos2 = objetos.copy()
    objetos2.pop(objetos[tamanho - 1])
    usa = mochila_pessoa(carrega, objetos2, tamanho - 1) + int(objetos[tamanho - 1][0])
    return max(usa, nao_usa)

k = input().split()[0]
k = int(k)

for i in range(k):
    n = input().split()[0]
    n = int(n)
    objetos = list()
    for j in range(n):
        # Primeiro valor, depois peso
        objetos.append(input().split())
    g = input().split()[0]
    g = int(g)
    pessoas = list()
    for j in range(g):
        aux = input().split()[0]
        pessoas.append(int(aux))
    for j in range(len(objetos)):

        objetos[j][0] = int(objetos[j][0])
        objetos[j][1] = int(objetos[j][1])
        print(objetos[j])
    soma = 0
    for j in pessoas:
        soma = soma + mochila_pessoa(int(i[0]), objetos, n)
    print(soma)



