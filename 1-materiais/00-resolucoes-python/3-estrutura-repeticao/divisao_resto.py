import sys

dividendo = int(sys.argv[1]) #10
divisor = int(sys.argv[2]) # 3

# dividendo = int(input("Informe o dividendo"))
# divisor = int(input("Informe o divisor"))

quociente = 0
resto = dividendo #10

while resto >= divisor:
    resto = resto - divisor # 7
    quociente += 1 #1

print(f"Quociennte = {quociente}")
print(f"Resto = {resto}")