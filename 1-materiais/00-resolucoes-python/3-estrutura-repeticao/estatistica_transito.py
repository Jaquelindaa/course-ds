import sys

cont = 1
soma_veiculos = 0
cont_menos = 0
soma_menos = 0
maior_acidente = -sys.maxsize - 1
menor_acidente = sys.maxsize
codigo_maior = 0
codigo_menor = 0

while cont <= 5:
    cod_cidade = int(input("Informe o código da cidade: "))
    num_veiculos = int(input("Nºde veículos de passeio: "))
    acidentes = int(input("Informe o número de acidentes de trânsito com vítimas: "))
    cont = cont + 1
    soma_veiculos = soma_veiculos + num_veiculos

    if num_veiculos < 2000:
        soma_menos = soma_menos + acidentes
        cont_menos = cont_menos + 1
    
    if acidentes > maior_acidente:
        maior_acidente = acidentes
        codigo_maior = cod_cidade
    
    if acidentes < menor_acidente:
        menor_acidente = acidentes
        codigo_menor = cod_cidade
    

media_total = soma_veiculos / 5

if not cont_menos == 0:
    media_menos = soma_menos / cont_menos
else:
    media_menos = 0

print("=====================")
print("INDÍCES")
print("=====================")
print(f"Acidentes: {maior_acidente}")
print(f"Código da cidade: {codigo_maior}")
print("")
print("=====================")
print("MEDIA DE VEÍCULOS")
print("=====================")
print(f"Média TOTAL de veículos: {media_total:.2f}")
print(f"Média <2000 de veículos: {media_menos:.2f}")