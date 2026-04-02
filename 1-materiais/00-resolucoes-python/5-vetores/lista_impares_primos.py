def gerar_impares(quantidade):
    lista_impares = []
    numero = 1
    while len(lista_impares) < quantidade:
        if not numero % 2 == 0:
            lista_impares.append(numero)
        numero += 1
    return lista_impares

def gerar_primos(quantidade):
    lista_primos = []
    numero = 2

    while len(lista_primos) < quantidade:
        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

        if primo:
            lista_primos.append(numero)
        
        numero += 1
    return lista_primos

print(gerar_impares(20))
print(gerar_primos(20))