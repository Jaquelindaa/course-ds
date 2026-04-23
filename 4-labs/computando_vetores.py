import random
import time
import heapq
import bisect

def cenario_1(A, a, b, k):
    soma = sum(x for x in A if a <= x <= b)
    k_esimo = heapq.nsmallest(k, A)[-1]
    return soma, k_esimo

def cenario_2(A, a, b, k):
    A_ordenado = sorted(A) 
    
    # Busca binária para encontrar os limites do intervalo
    idx_a = bisect.bisect_left(A_ordenado, a)
    idx_b = bisect.bisect_right(A_ordenado, b)
    
    # Soma apenas a fatia (slice)
    soma = sum(A_ordenado[idx_a:idx_b])
    k_esimo = A_ordenado[k - 1]
    return soma, k_esimo

def executar_benchmark():
    tamanhos = [10**2, 10**4, 10**6, 10**7] 
    a, b, k = 580, 788, 73
    
    print(f"{'Tamanho (n)':<12} | {'Cenário 1 (s)':<15} | {'Cenário 2 (s)':<15}")
    print("-" * 50)
    
    for n in tamanhos:
        A = [random.randint(0, 1000) for _ in range(n)]
        
        # Teste Cenário 1
        t1 = time.time()
        res1 = cenario_1(A, a, b, k)
        tempo_c1 = time.time() - t1
        
        # Teste Cenário 2
        t2 = time.time()
        res2 = cenario_2(A, a, b, k)
        tempo_c2 = time.time() - t2
        
        assert res1 == res2, "Erro: os resultados divergem!"
        
        print(f"{n:<12} | {tempo_c1:<15.6f} | {tempo_c2:<15.6f}")

if __name__ == "__main__":
    executar_benchmark()