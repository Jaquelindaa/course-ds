
m = int(input("m: "))
n = int(input("n: "))

while not m >= n:
    soma = 0
    for i in range(m, n+1):
        soma = soma + i

    print(soma)
    m = int(input("m: "))
    n = int(input("n: "))

print("Programa encerrado!")