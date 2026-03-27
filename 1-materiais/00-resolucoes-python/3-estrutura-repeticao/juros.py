import sys 

capital = float(sys.argv[1])
taxa_juros = float(sys.argv[2]) / 100

montante = capital

print("MONTANTE")
print("==============")
for i in range(1, 25):
    montante = montante * (1 + taxa_juros)
    print(f"{i}° mês: R${montante:.2f}")