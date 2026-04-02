def preencher_lista_a(quantidade):
    lista_a =[]
    print("---- Lista A ----")
    for i in range(quantidade):
        num = int(input(f"Informe o {i+1}° valor: "))
        lista_a.append(num)
    return lista_a
    
def preencher_lista_b(quantidade):
    lista_b =[]
    print("---- Lista B ----")
    for i in range(quantidade):
        num = int(input(f"Informe o {i+1}° valor: "))
        lista_b.append(num)
    return lista_b
    
def preencher_lista_c(lista_a, lista_b):
    lista_c = []

    for i in range(len(lista_a)):
        if i % 2 == 0:
            lista_c.append(lista_a[i])
        else:
            lista_c.append(lista_b[i])
    return lista_c

quantidade = int(input("Informe a quantidade de elementos nas listas: "))
lista_a = preencher_lista_a(quantidade)
lista_b = preencher_lista_b(quantidade)
lista_c = preencher_lista_c(lista_a, lista_b)

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C: {lista_c}")