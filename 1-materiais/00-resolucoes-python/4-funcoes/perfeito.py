
def ehperfeito(num):
    soma = 0
    divisores = []
    for n in range(1, num):
        if num % n == 0:
            divisores.append(n)
            soma += n

    return soma == num, divisores

    
num = int(input("Informe o número: "))
resultado, lista = ehperfeito(num)

if resultado:
    print("É perfeito")
    print(lista)
else:
    print("Não é perfeito")