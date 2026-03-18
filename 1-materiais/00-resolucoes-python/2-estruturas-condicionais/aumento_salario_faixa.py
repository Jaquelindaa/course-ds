salario = float(input("Informe seu salário: "))

if salario > 1250:
    aumento = salario * 0.1
    novo_salario = salario + aumento
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento

print(f"Aumento de: R$: {aumento} | Novo salário: {novo_salario}")