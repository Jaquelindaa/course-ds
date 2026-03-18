salario = 3600.00
aumento = 23
#aumento = 0.23

valor_aumento = salario * (aumento/100)
#valor_aumento = salario * aumento

novo_salario = salario + valor_aumento

print(f"Valor do amento: {valor_aumento}")
print(f"Valor do novo salário: {novo_salario}")