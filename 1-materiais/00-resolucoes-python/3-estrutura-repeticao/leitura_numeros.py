media = 0
soma = 0
cont = 0
num=''

while not num == 0:
    num = int(input("Informe um número: "))
    if num == 0:
        media = soma / cont
        break    
    soma += num
    cont = cont + 1

print(f"Quantidade de números: {cont}")
print(f"Soma: {soma}")
print(f"Média {media:.2f}")

