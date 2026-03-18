import sys

num = float(sys.argv[1])

fracionario = num % 1 
inteiro = num - fracionario
para_decimal = round(num, 1)
para_inteiro = round(num)

print(f"Número: {num}")
print(f"Parte inteira: {inteiro}")
print(f"Parte fracionária: {fracionario:.2f}")
print(f"Arredondamento para 1 casa decimal: {para_decimal}")
print(f"Arredondamento para inteiro: {para_inteiro}")