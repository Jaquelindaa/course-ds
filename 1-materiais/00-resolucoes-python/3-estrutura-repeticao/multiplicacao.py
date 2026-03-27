import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
resultado = 0

for n in range(1, num2+1):
    resultado += num1

print(resultado)