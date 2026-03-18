distancia = float(input("Informe a distância em km: "))
velocidade = float(input("Informa a velociadade média em km/h: "))

tempo = distancia / velocidade

if isinstance(tempo, int):
   print(f"Levará {tempo}horas")
else:
    decimos = tempo % 1
    tempo = tempo - decimos
    minutos = decimos * 60
    print(f"Levará aproximadamente {int(tempo)} horas e {int(minutos)} minutos")

