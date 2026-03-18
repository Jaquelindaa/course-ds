valor = float(input(f"Informe o preço da mercadoria: "))
desconto = float(input(f"Informe o percentual do desconto: "))

v_desc = valor * (desconto / 100)
v_final = valor - v_desc

print(f"Preço: {valor}")
print(f"Desconto: -{v_desc}")
print(f"Total: {v_final}")