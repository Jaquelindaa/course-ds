distancia = float(input("Informe a distância que deseja percorrer: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Valor da passagem: R${preco}")