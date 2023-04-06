# Problema Uri 2065

N = input()
tempo = input()
tempo = tempo.split()
iteins = input()
iteins = iteins.split()

fila = [0 for x in range(len(tempo))]

for i in iteins:
    index = fila.index(min(fila))
    fila[index] += int(tempo[index]) * int(i)
print(max(fila))