qtd_km = float(input(f"Informe a quantidade de km percorridos: "))
qtd_dias = int(input(f"Informe a quantidade de dias que você usou o carro: "))

preco = (qtd_km * 0.15) + (60 * qtd_dias)

print(f"Valor a pagar: {preco}")