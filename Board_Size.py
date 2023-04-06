import sys

linhas = sys.stdin.read().split('\n')
while '' in linhas:
    linhas.remove('')

i = 0
while i < len(linhas) - 1:
    dim = linhas[i].split()
    for j in range(int(dim[2])):
        aux = linhas[i + j + 1].split()
        if (int(aux[0]) <= int(dim[0]) and int(aux[1]) <= int(dim[1])) or (int(aux[0]) <= int(dim[1]) and int(aux[1]) <= int(dim[0])):
            print("Sim")
        else: print("Nao")