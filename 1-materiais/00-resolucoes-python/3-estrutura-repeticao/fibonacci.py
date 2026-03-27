import sys

num = int(sys.argv[1])

fibonacci = [0, 1, 1]
anterior_1 = 1
anterior_2 = 1
contador = 3
proximo = 0

while len(fibonacci) <= num-1:
    proximo = anterior_1 + anterior_2
    fibonacci.append(proximo)
    contador = contador + 1
    anterior_1 = anterior_2
    anterior_2 = proximo

print(fibonacci)