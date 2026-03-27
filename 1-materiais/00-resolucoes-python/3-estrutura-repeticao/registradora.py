codigo = ""
total = 0.0

codigo = int(input("Informe o código do produto: "))
    
while not codigo == 0:
    qtd = int(input("Informe a quantidade comprada: "))

    if codigo == 0:
        break;
    if codigo == 1:
        total = total + (0.50 * qtd)
    elif codigo == 2:
        total = total + (1 * qtd)
    elif codigo == 3:
        total = total + (4 * qtd)
    elif codigo == 5:
        total = total + (7 * qtd)
    elif codigo == 9:
        total = total + (8 * qtd)
    else:
        print("Código Inválido")
        break
    codigo = int(input("Informe o código do produto: "))

print(f"valor total da compra: {total}")