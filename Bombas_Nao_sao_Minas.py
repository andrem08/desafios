class casa:
    def __init__(self, dist=1000 ** 2, done=False, notB=True):
        self.dist = dist
        self.done = done
        self.notB = notB


def menor_distancia(m, dim, start, end):
    inf = dim[0] * dim[1]

    m[start[0]][start[1]].dist = 0
    atual = start
    nexts = [None] * inf
    index = 0
    indexRem = 0

    while True:
        if ((0 <= atual[0] + 1 < dim[0]) and (0 <= atual[1] < dim[1])) and m[atual[0] + 1][atual[1]].notB and m[atual[0] + 1][atual[1]].dist == inf and not m[atual[0] + 1][atual[1]].done:
            nexts[index] = [atual[0] + 1, atual[1]]
            index += 1
            m[atual[0] + 1][atual[1]].dist = m[atual[0]][atual[1]].dist + 1

        if ((0 <= atual[0] < dim[0]) and (0 <= atual[1] + 1 < dim[1])) and m[atual[0]][atual[1] + 1].notB and m[atual[0]][atual[1] + 1].dist == inf and not m[atual[0]][atual[1] + 1].done:
            nexts[index] = [atual[0], atual[1] + 1]
            index += 1
            m[atual[0]][atual[1] + 1].dist = m[atual[0]][atual[1]].dist + 1

        if ((0 <= atual[0] < dim[0]) and (0 <= atual[1] - 1 < dim[1])) and m[atual[0]][atual[1] - 1].notB and m[atual[0]][atual[1] - 1].dist == inf and not m[atual[0]][atual[1] - 1].done:
            nexts[index] = [atual[0], atual[1] - 1]
            index += 1
            m[atual[0]][atual[1] - 1].dist = m[atual[0]][atual[1]].dist + 1

        if ((0 <= atual[0] - 1 < dim[0]) and (0 <= atual[1] < dim[1])) and m[atual[0] - 1][atual[1]].notB and m[atual[0] - 1][atual[1]].dist == inf and not m[atual[0] - 1][atual[1]].done:
            nexts[index] = [atual[0] - 1, atual[1]]
            index += 1
            m[atual[0] - 1][atual[1]].dist = m[atual[0]][atual[1]].dist + 1

        m[atual[0]][atual[1]].done = True
        if atual == end:
            return m[end[0]][end[1]].dist
        if index != indexRem:
            atual = nexts[indexRem]
            # nexts[indexRem] = None
            indexRem += 1
        else:
            return m[end[0]][end[1]].dist


while True:
    dim = [int(i) for i in input().split()]
    if dim == [0, 0]:
        break

    nbomb_row = [int(i) for i in input().split()][0]
    if nbomb_row == 0:
        start = [int(i) for i in input().split()]
        end = [int(i) for i in input().split()]
        print(abs(start[0] - end[0]) + abs(start[1] - end[1]))

    else:
        inf = dim[0] * dim[1]
        m = [[casa(dist=inf) for j in range(dim[1])] for i in range(dim[0])]

        for i in range(nbomb_row):
            l = [int(i) for i in input().split()]
            for j in range(l[1]):
                m[l[0]][l[j + 2]].notB = False
        start = [int(i) for i in input().split()]
        end = [int(i) for i in input().split()]
        print(menor_distancia(m, dim, start, end))


