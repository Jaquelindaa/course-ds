import math

def calcular_diagonal(a, b, c):
    return math.sqrt(a**2 + b**2 + c**2)

def exibir_relatorio(e10, e15, e20, e25, excedentes):
    total_esferas = e10 + e15 + e20 + e25

    print("\n" + "="*30)
    print(f"{' RELATÓRIO DE EMBALAGEM ':^30}")
    print("="*30)
    print(f"Esferas 10cm: {e10:>10}")
    print(f"Esferas 15cm: {e15:>10}")
    print(f"Esferas 20cm: {e20:>10}")
    print(f"Esferas 25cm: {e25:>10}")
    print("-"*30)
    print(f"TOTAL ESFERAS: {total_esferas:>9}")
    print(f"CAIXAS GRANDES: {excedentes:>8}")
    print("="*30)


def main():
    e10 = e15 = e20 = e25 = nao_cabe = 0

    while True:
        try:
            a = float(input("\nDimensão A (0 ou negativo para sair): "))
            if a <= 0:
                break
            
            b = float(input("Dimensão B: "))
            c = float(input("Dimensão C: "))
            
            d = calcular_diagonal(a, b, c)
            print(f"Diagonal calculada: {d:.2f} cm")

            if d <= 10:
                e10 += 1
            elif d <= 15:
                e15 += 1
            elif d <= 20:
                e20 += 1
            elif d <= 25:
                e25 += 1
            else:
                print("Caixa maior que a maior esfera disponível!")
                nao_cabe += 1
                
        except ValueError:
            print("Erro: Por favor, insira apenas números.")

    exibir_relatorio(e10, e15, e20, e25, nao_cabe)

if __name__ == "__main__":
    main()