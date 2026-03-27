cont_time = 0
cont_jogador = 0
cont_idade_menor = 0
cont_peso = 0
soma_idade = 0
soma_altura = 0
media_idade = []

while cont_time < 5:
    cont_time = cont_time + 1
    while cont_jogador < 11:
        altura = float(input("Informe a altura: "))
        idade = int(input("Informe a idade: "))
        peso = float(input("Informe o peso: "))

        cont_jogador = cont_jogador + 1
        soma_idade = soma_idade + idade
        soma_altura = soma_altura + altura

        if peso > 80:
            cont_peso = cont_peso + 1
        if idade < 18:
            cont_idade_menor = cont_idade_menor + 1
        if cont_jogador == 11:
            media_idade.append(soma_idade / 11)
            cont_jogador = 0
            soma_idade = 0

media_altura = soma_altura / 55
per_peso = cont_peso * 100 / 55

print(f"Jogadores com menos de 18 anos: {cont_idade_menor}")
print(f"Média de idade por time:")
for i in range(0, 5):
    print(f"Time {i+1}: {media_idade[i]}")

print(f"Média de altura do campeonato: {media_altura}")
print(f"Percentual de jogadores acima de 80kg: {per_peso}")
