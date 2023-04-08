#André Miyazawa
#11796187

import sys
def main():
    linhas = sys.stdin.read().split('\n')
    for i in range(0, len(linhas) - 1, 3):
        N = int(linhas[i])
        largada = linhas[i + 1]
        largada = largada.split()
        chegada = linhas[i + 2]
        chegada = chegada.split()

        ultrapassadas = 0
        for i in range (N):
            for j in range (N - i):
                if int(largada[j]) != int(chegada[i]):
                    ultrapassadas += 1
                else:
                    largada.pop(j)
                    break
        print(ultrapassadas)

if __name__ == '__main__':
    main()