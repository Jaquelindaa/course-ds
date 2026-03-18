trab_lab = float(input("Informe a nota do trabalho de laboratório: "))
prova = float(input("Informe a nota da prova semestral: "))
exame = float(input("Informe a nota do exame: "))

media = ((trab_lab * 2) + (prova * 3) + (exame * 5)) / 10

if media < 5:
    conceito = "E"
elif media < 6:
    conceito = "D"
elif media < 7:
    conceito = "C"
elif media < 8:
    conceito = "B"
else:
    conceito = "A"

print(f"Média: {media}")
print(f"Conceito: {conceito}")