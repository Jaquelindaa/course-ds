import sys

def somar_posicoes():
    argumentos = sys.argv[1:]

    if len(argumentos) < 12:
        print("Erro: Forneça 10 números para a lista e depois os índices X e Y.")
        print("Exemplo: python programa.py 1 2 3 4 5 6 7 8 9 10 0 9")
        sys.exit(1)
    
    lista = [float(i) for i in argumentos[:10]]
    x = int(argumentos[10])
    y = int(argumentos[11])

    resultado = lista[x] + lista[y]

    print(f"Lista: {lista}")
    print(f"Valor na posição {x}: {lista[x]}")
    print(f"Valor na posição {y}: {lista[y]}")
    print(f"Soma: {resultado}")

if __name__ == "__main__":
    somar_posicoes()
