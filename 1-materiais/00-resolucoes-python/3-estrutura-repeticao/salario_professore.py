
classe = input("Informe a classe (A), (B) ou (X) para sair \n")
soma_a = 0
soma_b = 0
cont_a = 0
cont_b = 0
nomes = []
salarios = []
salarios_liquidos = []
salarios_brutos = []

while classe == "A" or classe == "B":
    nome = input("Informe seu nome: ")
    nomes.append(nome)
    horas_aula = float(input("Informe as horas/aulas dadas mensalmente:"))
    salario_bruto = 146 *  horas_aula
    salarios_brutos.append(salario_bruto)

    if classe == "A":
        salario_liquido = salario_bruto - (salario_bruto * 0.1)
        soma_a = soma_a + salario_liquido
        salarios_liquidos.append(salario_liquido)
        cont_a = cont_a + 1
    if classe == "B":
        salario_liquido = salario_bruto - (salario_bruto * 0.05)
        soma_b = soma_b + salario_liquido
        salarios_liquidos.append(salario_liquido)
        cont_b = cont_b + 1
    
    classe = input("Informe a classe (A), (B) ou (X) para sair \n")
    
media_a = soma_a / cont_a
media_b = soma_b / cont_b

print("====================================")
print(f"MÉDIA SALARIAL CLASSE A: {media_a:.2f}")
print(f"MÉDIA SALARIAL CLASSE B: {media_b:.2f}")
print("====================================")
print("LISTA DE PROFESSORES:")
for n in range(0, cont_a + cont_b):
    print(f"Nome: {nomes[n]}")
    print(f"Salário Bruto: {salarios_brutos[n]:.2f}")
    print(f"Salário Liquído: {salarios_liquidos[n]:.2f}")
    print("------------------------------------")

