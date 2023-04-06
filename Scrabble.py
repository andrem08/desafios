# Exercício adicional

# Coloca as letras e pontos em uma tabela hashing, e verifica a pontuação
# para cada letra da palavra recebida, fazendo a soma dos pontos totais.
def scrabble(palavra):
    palavra = palavra.lower()

    # Colocar as letras e pontos em um dicionário
    lista_letras = [['e', 'a', 'o', 'r', 't', 'l', 's'],
                    ['d', 'g'],
                    ['b', 'c', 'm', 'p', 'u'],
                    ['f', 'h', 'v', 'w', 'y'],
                    ['i', 'k', 'n'],
                    ['j', 'x'],
                    ['q', 'z']]

    pontos = [1, 2, 3, 4, 5, 8, 10]
    dicionario = {}

    for letras, ponto in zip(lista_letras, pontos):
        for letra in letras:
            dicionario.update({letra: ponto})
    soma = 0

    # Encontrar um elemento no dicionário O(1)
    # Para todas as letras O(n)
    for letra in palavra:
        soma = soma + dicionario.get(letra)
    return soma

# Usar como exemplo:
#
# if __name__ == '__main__':
#     word = 'arvore'
#     print(scrabble(word))

