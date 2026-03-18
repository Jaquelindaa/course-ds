print("Menu opções:\n1. Imposto\n2. Novo Saalário\n3. Classificação")
opcao = int(input("Informe a opção: "))

if opcao == 1:
    salario = float(input("Informe seu salário: "))
    if salario < 500:
        imposto = salario * 0.05
        print(f"Imposto: R${imposto}")
    elif salario <= 850:
        imposto = salario * 0.1
        print(f"Inposto: R${imposto}")
    else:
        imposto = salario * 0.15
        print(f"Inposto: R${imposto}")
elif opcao == 2:
    salario = float(input("Informe seu salário: "))
    if salario < 450:
        n_salario = salario + 100
        print(f"Novo salário: R${n_salario}")
    elif salario < 750:
        n_salario = salario + 75
        print(f"Novo salário: R${n_salario}") 
    elif salario <=1500:
        n_salario = salario + 50
        print(f"Novo salário: R${salario}")
    else:
        salario = salario + 25
        print(f"Novo salário: R${salario}")
elif opcao == 3:
    salario = float(input("Informe seu salário: "))
    if salario <= 700:
        classificacao = "Mal remunerado"
        print(classificacao)
    else:
        classificacao = "Bem remunerado"
        print(classificacao)
else:
    print("Opção inválida!")