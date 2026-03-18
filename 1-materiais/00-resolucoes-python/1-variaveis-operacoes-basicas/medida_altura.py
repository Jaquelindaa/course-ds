grupo = []
soma = 0

quantidade = int(input("Quantas pessoas no grupo? "))

for i in range(quantidade):
    altura = float(input(f"Informe a altura da {i+1}ª pessoa: "))
    grupo.append(altura)
    soma += altura 

media = soma/quantidade
print(f"A média de altura dos grupos: {media}cm")