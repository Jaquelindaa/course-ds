import sys

lista = [float(item) for item in sys.argv[1:]]

x = float(input("Informe o valor que deseja buscar: "))
posicao = "Valor não encontrado"

for i in range(0, len(lista)):
    if lista[i] == x:
        posicao = i
        break

print(posicao)