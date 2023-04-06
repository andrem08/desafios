# Problema 2674

#André Miyazawa
#11796187
import sys

def is_prime(n):
    #Caso seja 1 ou 0
    if n == 1 or n ==0:
        return False
    #Caso seja 2
    if n == 2:
        return True
    #Caso seja divisivel por 2 porém nao 2
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5) +1, 2):
        if n%i == 0:
            return False
    return True

linhas = sys.stdin.read()
linhas = linhas.replace('\n', ' ')
linhas = linhas.split(" ")
for linha in linhas:
    if linha == "":
        continue
    #Verifica se o numero é primo
    if is_prime(int(linha)):
        #Verifica se os algarismos são primos
        algarismos = [int(d) for d in str(linha)]
        for alg in range (0,len(algarismos)):
            if not is_prime(int(algarismos[alg])):
                print("Primo")
                break
            #Se chegar no ultimo indice e nao ter saido do for, ele também é um super primo
            if alg == len(algarismos) - 1:
                print("Super")
                break
    else: print("Nada")