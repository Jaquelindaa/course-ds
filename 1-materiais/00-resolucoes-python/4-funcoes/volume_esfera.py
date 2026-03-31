import math
def volume_esfera(r):
    volume = 4 * math.pi * r **3/3 
    return volume

volume = volume_esfera(2)
print(f"Volume da esfera: {volume:.2f}")