def triangulo(x, y, z):
    if x + y > z and x + z > y and z + y > x:
        if x == y and x == z:
            tipo = "Equilátero"
        elif x == y or y == z or z == x:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
    else:
        tipo = "Não é um triangulo"
    return tipo

cont = 0
tipos = []
eq = 0
i = 0
es = 0 
n = 0
while cont < 5:
    cont = cont + 1
    x = int(input("Informe o lado X do triângulo: "))
    y = int(input("Informe o lado Y do triângulo: "))
    z = int(input("Informe o lado Z do triângulo: "))
    
    tri = triangulo(x, y, z)
    tipos.append(tri)

for t in range(0, 5):
    print(f"Tipo: {tipos[t]}")
    if tipos[t] =="Equilátero":
        eq = eq + 1
    elif tipos[t] =="Isósceles":
        i = i + 1
    elif tipos[t] =="Escaleno":
        es = es + 1
    else:
        n = n + 1

print(f"Quantidade equiláteros: {eq}")
print(f"Quantidade isósceles: {i}")
print(f"Quantidade escaleno: {es} ")
print(f"Quantidade que não são triângulos: {n} ")
