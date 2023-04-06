
def verificar_Mercado(compras, i, mercado, j, dp):
    if i == len(compras):
        return 0
    elif j == len(mercado):
        return 100000000000
    if dp[i][j] != 100000000000:
        return dp[i][j]
    if compras[i] == mercado[j][0]:
        dp[i][j] = min(
            mercado[j][1] + verificar_Mercado(compras, i + 1, mercado, j + 1, dp),
            verificar_Mercado(compras, i, mercado, j + 1, dp))
        return dp[i][j]
    else:
        dp[i][j] = verificar_Mercado(compras, i, mercado, j + 1, dp)
        return dp[i][j]


def lcs(compras, mercado):
    # find the length of the strings
    m = len(compras)
    n = len(mercado)

    # declaring the array for storing the dp values
    c = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                c[i][j] = 10000000000
            elif compras[i - 1] == mercado[j - 1][0]:
                if c[i - 1][j - 1] is 10000000000:
                    aux = 0
                else:
                    aux = c[i - 1][j - 1]
                c[i][j] = mercado[j - 1][1] + aux
            else:
                c[i][j] = min(c[i - 1][j], c[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return c[m][n]


while True:
    dim = [int(x) for x in input().split()]
    if dim[0] == dim[1] == 0:
        break
    compras = [int(x) for x in input().split()]
    mercado = []
    for i in range(dim[1]):
        aux = input().split()
        aux[0] = int(aux[0])
        if compras.__contains__(aux[0]):
            aux[1] = float(aux[1])
            mercado.append(aux)
    while len(mercado) > 0:
        if mercado[- 1][0] != compras[-1]:
            mercado.pop(- 1)
        else:
            break

    while len(mercado) > 0:
        if mercado[0][0] != compras[0]:
            mercado.pop(0)
        else:
            break
    # dp = [[100000000 for i in range(len(mercado) + 1)] for j in range(len(compras) + 1)]
    # res = verificar_Mercado(compras, 0, mercado, 0, dp)
    res = lcs(compras, mercado)
    if res == 10000000:
        print('Impossible')
    else:
        print('{:.2f}'.format(round(res, 2)))
