horas= int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

h_min = horas * 60
m_seg = (minutos + h_min) * 60
total = segundos + m_seg

print(f"{total}segundos")