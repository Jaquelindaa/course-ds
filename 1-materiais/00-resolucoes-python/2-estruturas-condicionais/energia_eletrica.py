kWh = float(input("Informe a quantidade de kWh consumidos: "))
instalacao = input("Informe o tipo de intalação:\n(R) Residencia\n(I) Industrial\n(C) Comercial")

if instalacao == "R":
    if kWh <= 500 and kWh >= 0:
        valor = 0.40 * kWh
    else:
        valor = 0.65 * kWh
elif instalacao == "C":
    if kWh <= 1000:
        valor = 0.55 * kWh
    else:
        valor = 0.60 * kWh
if instalacao == "I":
    if kWh <= 5000:
        valor = 0.57 * kWh
    else:
        valor = 0.68 * kWh

print(f"Conta de energia R${round(valor,2)}")