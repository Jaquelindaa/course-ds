import sys

lista = [int(i) for i in sys.argv[1:]]
print(lista)

for i in range(0, len(lista)):
    if lista[i] < 0:
        lista[i] = 0

print(lista)