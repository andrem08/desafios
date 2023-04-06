# Problema Uri 1972

class No:
    def __init__(self, value, index):
        self.value = value
        self.index = index


def insert_heap(array, elemento):
    array


dim = input().split(' ')
dim = [int(dim[1]), int(dim[0])]

matrix = []
for i in range(dim[1]):
    matrix.append(list(input().replace('.', '0')))

s = (-1, -1)
for i in matrix:
    if 'H' in i:
        s = (matrix.index(i), i.index('H'))
        break
end = (-1, -1)
for i in matrix:
    if 'E' in i:
        end = (matrix.index(i), i.index('E'))
        i[i.index('E')] = 0
        break

# Dijskra
heap = [[None for i in range(dim[0])] for j in range(dim[1])]
distancia = [[1e10 for i in range(dim[0])] for j in range(dim[1])]
passou = [[False for i in range(dim[0])] for j in range(dim[1])]

p = [s[0], s[1]]
distancia[s[0]][s[1]] = 0
passou[s[0]][s[1]] = True

# (V)
hap = 0
while True:
    # (4)
    for i, j in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        i = i + p[0]
        j = j + p[1]
        if (0 <= i <= dim[1] - 1) and (0 <= j <= dim[0] - 1):
            if matrix[i][j] is not '#':
                if not passou[i][j] and (distancia[p[0]][p[1]] + int(matrix[i][j]) < distancia[i][j]):
                    distancia[i][j] = distancia[p[0]][p[1]] + int(matrix[i][j])
    menor = 1e10
    p = None
    # (V)
    for i in range(dim[1]):
        for j in range(dim[0]):
            hap += 1
            if not passou[i][j] and menor > distancia[i][j]:
                menor = distancia[i][j]
                p = [i, j]
    if p is None or (p[0] is end[0] and p[1] is end[1]):
        if p is None:
            print('ARTSKJID', hap)
        else:
            print(distancia[end[0]][end[1]], hap)
        break
    passou[p[0]][p[1]] = True
