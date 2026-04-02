n = int(input("Informe quantos leementos terá a lista: "))
lista = []

for i in range(n):
    num = int(input(f"Informe o {i+1}° valor: "))
    lista.append(num)

for i in range(1, n):
    lista[i] = lista[i] + lista[i-1]

print(lista)