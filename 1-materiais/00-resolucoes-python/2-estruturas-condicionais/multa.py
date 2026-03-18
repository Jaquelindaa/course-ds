velocidade = float(input("Informe a valociade do carro: "))

if velocidade > 80:
    valor = (velocidade - 80) * 30
    print("Você foi multado!")
    print("=================")
    print(f"Valor da multa: {valor}")
else:
    print("Você não foi multado")