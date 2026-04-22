import random
import time
import heapq
import bisect

def cenario_1(A, a, b, k):
    # Soma de valores no intervalo [a, b]
    soma = sum(x for x in A if a <= x <= b)
    # Encontrar o k-ésimo menor elemento sem alterar A
    k_esimo = heapq.nsmallest(k, A)[-1]
    return soma, k_esimo

def cenario_2(A, a, b, k):
    A_ordenado = sorted(A)
    
    idx_a = bisect.bisect_left(A_ordenado, a)
    idx_b = bisect.bisect_right(A_ordenado, b)
    soma = sum(A_ordenado[idx_a:idx_b])
    
    # Encontrar o k-ésimo menor elemento (acesso direto)
    k_esimo = A_ordenado[k - 1]
    return soma, k_esimo

def executar_benchmark():
    tamanhos = [10**2, 10**4, 10**6]
    a, b, k = 580, 788, 73
    
    print(f"{'Tamanho (n)':<15} | {'Cenário 1 (s)':<15} | {'Cenário 2 (s)':<15}")
    print("-" * 50)
    
    for n in tamanhos:
        A = [random.randint(0, 1000) for _ in range(n)]
        
        # Medindo Cenário 1
        inicio = time.time()
        cenario_1(A, a, b, k)
        tempo_c1 = time.time() - inicio
        
        # Medindo Cenário 2
        inicio = time.time()
        cenario_2(A, a, b, k)
        tempo_c2 = time.time() - inicio
        
        print(f"{n:<15} | {tempo_c1:<15.6f} | {tempo_c2:<15.6f}")

executar_benchmark()