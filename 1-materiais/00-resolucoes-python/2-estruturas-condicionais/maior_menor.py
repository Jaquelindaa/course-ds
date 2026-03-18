num_1 = float(input("Informe um número: "))
num_2 = float(input("Informe um número: "))
num_3 = float(input("Informe um número: "))

maior = 0.0
menor = 0.0

if num_1 >= num_2 and num_1 >= num_3:
    maior = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    maior = num_2
else:
    maior = num_3

if num_1 <= num_2 and num_1 <= num_3:
    menor = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    menor = num_2
else:
    menor = num_3

print(f"Maior: {maior}")
print(f"Menor: {menor}")

