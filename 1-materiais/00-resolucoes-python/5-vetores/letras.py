import sys

n = int(input("Informe a quantidade de elementos na lista: "))
lista_a = []
lista_b = []
cont_a = 0
cont_b = 0
for i in range(n):
    num = int(input(f"Informe o {i+1}° elemento: "))
    lista_a.append(num)

for i in range(n):
    num = int(input(f"Informe o {i+1}° elemento: "))
    lista_b.append(num)

for i in range(len(lista_a)):
    cont_a = cont_a + 1
    for j in range(len(lista_b)):
        cont_b = cont_b + 1
        if lista_a[i] == lista_b[j]:
            break
        if cont_a == n:
            print("Listas são diferentes")
            break

print("As listas contém o mesmo conteúdo")
