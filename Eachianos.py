# Problema Uri 2018

#André Miyazawa
#11796187
import sys
#Guarda os inputs
linhas = sys.stdin.read().split("\n")
#Lista de dicionarios utilizado
dictionary = []


for j in range(0, len(linhas), 4):
    #Para cada modalidade
    #Se nao tiver modalidade nenhuma, sai do for
    if linhas[j] == "":
        break
    for i in range(j + 1, j + 4):
        #Para cada país:
        #Determina se este país ja exste, se não, adiciona na lista
        filtro = list(filter(lambda pais: pais['nome'] == linhas[i], dictionary))
        if filtro == []:
            pais = {
                'nome': linhas[i], 1: 0, 2: 0, 3: 0
            }
            dictionary.insert(-1, pais)
        # determina qual medalha ganhou e da update
        pais = list(filter(lambda pais: pais['nome'] == linhas[i], dictionary))[0]
        pais.update({i - j: pais[i - j] + 1})
    #Primeiro ordena pelo nome
    #Depois reordena pela quantidade de medalhas de ouro, depois de prata e em seguida de bronze
    #Segunda ordenação é reversa, dos maiores para os menores
    dictionary = sorted(dictionary, key = lambda x: x['nome'])
    dictionary = sorted(dictionary, key = lambda x: (x[1], x[2], x[3]), reverse=True)
#Imprime
print("Quadro de Medalhas")
for d in dictionary:
    print(d['nome'], d[1], d[2], d[3])