casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o seu salário: "))
anos = int(input("Informe a quantidade de anos: "))

meses = anos * 12
parcela = round((casa / meses),2)
limite = salario * 0.30

if parcela > limite:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!!")
    print(f"{meses} parcelas de R${parcela}")