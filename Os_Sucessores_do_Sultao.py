def testa_rainhas(queens, test):
    for i in queens:
        if i[0] == test[0] or i[1] == test[1] or abs(i[0] - test[0]) == abs(i[1] - test[1]):
            return False
    return True


def get_queen(queens, pd):
    queens.sort()
    for i in pd:
        # i.sort()
        if queens == i:
            return []
    pd.append(queens.copy())
    row = [0, 1, 2, 3, 4, 5, 6, 7]
    col = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in queens:
        row.remove(i[0])
        col.remove(i[1])
    q = [None] * len(row) * len(col)
    index = 0
    for i in row:
        for j in col:
            if testa_rainhas(queens, [i, j]):
                q[index] = [i, j]
                index += 1
    return [i for i in q if i is not None]


def coloca_rainhas(chess, maior, queens, pd):
    if len(queens) == 8:
        m = 0
        for i in queens:
            m += chess[i[0]][i[1]]
        print(queens, m)
        if maior < m:
            return m
        else:
            return maior

    q = get_queen(queens, pd)
    if len(q) == 0:
        return maior
    for i in q:
        queens.append(i)
        maior = coloca_rainhas(chess, maior, queens, pd)
        queens.remove(i)
    if len(queens) == 0:
        return maior
    return maior


k = int(input()[0])
for i in range(k):
    chess = list()
    for j in range(8):
        chess.append([int(x) for x in input().split()])
    maior = 0
    queens = [None]
    print(coloca_rainhas(chess, maior, [], []))
