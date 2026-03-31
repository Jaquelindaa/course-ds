massa = float(input("Informe a massa inicial: "))
print(f"Massa inicial: {massa}")

def reduzir_massa(massa):
    segundos = 0
    while massa >= 0.5:
        massa = massa / 2
        segundos = segundos + 50
    
    return massa, segundos

def converte_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return horas, minutos, segundos_restantes

massa, segundos = reduzir_massa(massa)
horas, minutos, segundos_restantes= converte_tempo(segundos)
print(f"Massa final: {massa}")
print(f"{horas}h {minutos}m {segundos_restantes}s")