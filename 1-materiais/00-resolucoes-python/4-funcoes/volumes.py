import math

def cubo(s):
    return s**3

def paralelepipedo(l, c, h):
    return l * c * h

def cilindro(r, h):
    return math.pi * r**2 * h

def esfera(r):
    return 4 * math.pi*r**3 / 3

def cone(r, h):
    return math.pi * r**2 * h / 3

print("(Cb) Cubo")
print("(P) Paralelepípedo")
print("(Cl) Cilindro")
print("(E) Esfera")
print("(Cn) Cone")
tipo = input("Informe a figura geométrica: ")

if tipo == "Cb":
    s = float(input("Informe o comprimento do lado: "))
    print(f"Volume: {cubo(s)}")
elif tipo == "P":
    l = float(input("Informe a largura: "))
    c = float(input("Informe o comprimento: "))
    h = float(input("Informe a altura: "))
    print(f"Volume: {paralelepipedo(l, c, h):.2f}")
elif tipo == "Cl":
    r = float(input("Informe o raio: "))
    h = float(input("Informe a altura: "))
    print(f"Volume: {cilindro(r, h):.2f}")
elif tipo == "E":
    r = float(input("Informe o raio: "))
    print(f"Volume: {esfera(r):.2f}")
elif tipo == "Cn":
    r = float(input("Informe o raio: "))
    h = float(input("Informe a altura: "))
    print(f"Volume: {cone(r, h):.2f}")
else:
    print("Tipo informado incorreto")