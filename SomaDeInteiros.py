# Exercício adicional

# Constrói um dicionário com 41 elementos (1 ao 41), e cada chave do 1 ao 41 possui um valor
# representando a quantidade de chaves i que o vetor possui, sendo 1 <= i <= 41.
# Uma forma de ordenação parecida com o counting sort, porém utilizando hashing.
# Verifica se existem 2 21, e em seguida faz uma iteração do 1 até o 20 verificando para cada
# número se existe o respectivo número, que sua soma resulta em 42.
# Complexidade O(n)
def soma42(numeros):

    # Complexidade O(n)
    dicionario = {i: 0 for i in range(1, 42, 1)}
    for num in numeros:
        if num < 42:
            dicionario.update({num: dicionario.get(num) + 1})

    # Caso exista pelo menos 2 números 21, sua soma daria 42
    if dicionario.get(21) >= 2:
        return True

    # Verifica se existe pelo menos um elemento i e um elemento 42-i, que sua soma daria 42.
    # Complexidade O(1)
    for i in range(1, 21, 1):
        if dicionario.get(i) > 0 and dicionario.get(42 - i) > 0:
            return True
    return False


# Usar como exemplo:
# if __name__ == '__main__':
#     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
#     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21]
#     numeros = [1, 6, 34, 129, 36]
#     numeros = [4, 9, 13, 55, 24, 32]
#     print(soma42(numeros))
