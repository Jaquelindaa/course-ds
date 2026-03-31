def triangulo(x, y, z):
    if x + y > z and x + z > y and z + y > x:
        if x == y and x == z:
            return "Equilátero"
        elif x == y or y == z or z == x:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triangulo"


def perimetro(x, y, z):
    return x + y + z


cont = 0
tipos = []
perimetros = []

eq = 0
iso = 0
esc = 0
n = 0

soma_per = 0

while cont < 5:
    cont += 1

    x = int(input("Informe o lado X do triângulo: "))
    y = int(input("Informe o lado Y do triângulo: "))
    z = int(input("Informe o lado Z do triângulo: "))

    tri = triangulo(x, y, z)

    if tri != "Não é um triangulo":
        per = perimetro(x, y, z)
        soma_per += per
    else:
        per = 0

    tipos.append(tri)
    perimetros.append(per)


for t in range(5):
    print(f"Tipo: {tipos[t]}")
    print(f"Perímetro: {perimetros[t]}")

    if tipos[t] == "Equilátero":
        eq += 1
    elif tipos[t] == "Isósceles":
        iso += 1
    elif tipos[t] == "Escaleno":
        esc += 1
    else:
        n += 1


total_validos = eq + iso + esc

if total_validos > 0:
    media_per = soma_per / total_validos
else:
    media_per = 0


print(f"Total perímetro: {soma_per}")
print(f"Média dos perímetros: {media_per}")
print(f"Quantidade equiláteros: {eq}")
print(f"Quantidade isósceles: {iso}")
print(f"Quantidade escaleno: {esc}")
print(f"Quantidade que não são triângulos: {n}")