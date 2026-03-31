import math

def bhaskara(a, b, c):
    delta = b**2 - 4 * a *c

    if delta < 0:
        x1 = "Sem raízes reais"
        x2 = ""
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

print(bhaskara(1, -4, 4))