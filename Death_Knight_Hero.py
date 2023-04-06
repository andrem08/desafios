#Problema Uri 3249

n = int(input())
count = 0

#Se não tiver CD na palavra, soma +1
for i in range(n):
    palavra = input()
    if not ("CD" in palavra):
        count+= 1
print(count)