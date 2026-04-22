from collections import deque

def descarte(qtd_cartas):
    fila = deque(range(1, qtd_cartas + 1))
    descartadas = []

    while len(fila) >= 2:
        topo = fila.popleft()
        descartadas.append(topo)
        
        proxima = fila.popleft()
        fila.append(proxima)

    restante = fila[0]
    return descartadas, restante

cartas = descarte(10)
descartadas, remaining = list(cartas)
print(f"Descartadas: {descartadas}")
print(f"Remaining: {remaining}")

