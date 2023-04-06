# Problema Uri 1519

def quantidade_letras(palavra, lista):
    quantidade = 0
    for palavra2 in lista:
        if palavra == palavra2:
            quantidade += len(palavra) - 2
    return quantidade


def pular(palavra, lista, qletras):
    if len(palavra) <= 2:
        return True
    q1 = quantidade_letras(palavra, lista)
    for i in range(len(lista)):
        if palavra[0] == lista[i][0]:
            if palavra != lista[i]:
                if q1 < qletras[i]:
                    return True
    return False


def esta_abreviada(palavra, abreviacoes):
    for abreviacao in abreviacoes:
        if palavra == abreviacao:
            return True
    return False


def main():
    palavras = input()
    palavras = palavras.split()
    abreviacoes = []
    qletras = []
    while palavras[0] != '.':
        for palavra in palavras:
            qletras.append(quantidade_letras(palavra, palavras))
        nabreviacoes = 0
        for i in range(len(palavras)):
            if i != 0:
                print(' ',end='')
            if pular(palavras[i], palavras, qletras):
                print(palavras[i], end='')
            else:
                if not (esta_abreviada(palavras[i], abreviacoes)):
                    abreviacoes.append(palavras[i])
                    nabreviacoes += 1
                print(palavras[i][0], end='.')
        print('')
        print(nabreviacoes)
        abreviacoes = sorted(abreviacoes)
        for abreviacao in abreviacoes:
            print(abreviacao[0], end='. = ')
            print(abreviacao)

        palavras = input()
        palavras = palavras.split()
        abreviacoes = []
        qletras = []


if __name__ == '__main__':
    main()