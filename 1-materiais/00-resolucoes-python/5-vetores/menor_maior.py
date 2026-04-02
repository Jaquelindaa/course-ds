import sys

lista = [int(i) for i in sys.argv[1:]]

maior = -sys.maxsize -1
menor = sys.maxsize

for i in range(0, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    
    if lista[i] < menor:
        menor = lista[i]

print(f"Maior: {maior}")
print(f"Menor: {menor}")
    