from collections import deque
import sys

def resolver_problema_cartas():
    # Lendo todas as linhas da entrada padrão
    for linha in sys.stdin:
        n = int(linha.strip())
        
        # Condição de parada: o número 0
        if n == 0:
            break
        
        #apenas 1 carta
        if n == 1:
            print("Discarded cards:")
            print("Remaining card: 1")
            continue

        fila = deque(range(1, n + 1))
        descartadas = []

        while len(fila) >= 2:
            # 1. Joga fora a do topo
            descartadas.append(fila.popleft())
            # 2. Move a nova do topo para o fim
            fila.append(fila.popleft())

        # O join transforma [1, 2, 3] em "1, 2, 3"
        string_descartadas = ", ".join(map(str, descartadas))
        
        print(f"Discarded cards: {string_descartadas}")
        print(f"Remaining card: {fila[0]}")

if __name__ == "__main__":
    resolver_problema_cartas()