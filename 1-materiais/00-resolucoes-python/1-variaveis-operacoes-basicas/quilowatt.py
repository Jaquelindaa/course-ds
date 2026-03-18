salario = float(input(f"Salário minímo: "))
qtd_qw = float(input(f"Informe a quantidade de quilowatt consumidos: "))

custo_qw = (salario / 5)
consumo = custo_qw * qtd_qw
desconto = consumo - (consumo * 0.15)

print(f"Valor quilowatt: R${custo_qw}")
print(f"Conta de energia: R${consumo}")
print(f"Desconto: R${desconto}")