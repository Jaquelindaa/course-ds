lista = list(range(1,17))
print(f"ORIGINAL: {lista}")

for i in range(0,len(lista) // 2):
    j = i + len(lista) // 2
    lista[i], lista[j] = lista[j], lista[i]

print(f"ALTERADA:  {lista}")