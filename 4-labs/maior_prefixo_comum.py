import random
import time


#ABORDAGEM 1
# Para cada índice i da primeira string:
# Se todas as outras strings têm o mesmo caractere em i, continua.
# Senão, retorna o que foi acumulado até agora.
#COMPLLEXIDADE ASSINTÓTICA: 

def abordagem_vertical(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]

print(abordagem_vertical(["flower","flow","flight"]))  # Saída: "fl"
print(abordagem_vertical(["dog","racecar","car"]))      # Saída: ""

#ABORDAGEM 2
#Ordena o array.
#Compara apenas a primeira e a última string caractere por caractere.
#O prefixo comum entre elas é o prefixo de todas.

def abordagem_sort(strs):
        if not strs: return ""
        strs.sort()
        p, u = strs[0], strs[-1]
        i = 0
        while i < len(p) and i < len(u) and p[i] == u[i]:
            i += 1
        return p[:i]

def gerador_instancias(N):
    alfabeto = ['A', 'B', 'C', 'D']
    tamanho_base = random.randint(5, 10)
    base = "".join(random.choice(alfabeto) for _ in range(tamanho_base))
    colecao = []
    
    for _ in range(N):
        copy_str = list(base)
        for i in range(len(copy_str)):
            prob = (i + 1) / len(copy_str)
            if random.random() < prob:
                copy_str[i] = random.choice(alfabeto)
        colecao.append("".join(copy_str))
    return colecao

for exp in range(1, 21):
    N = 2**exp
    data = gerador_instancias(N)
    
    # Teste Vertical
    start = time.time() 
    abordagem_vertical(data[:])
    end_v = time.time() - start
    
    # Teste Sort
    start = time.time()
    abordagem_sort(data[:])
    end_s = time.time() - start
    
    print(f"N: 2^{exp} | Vertical: {end_v:.6f}s | Sort: {end_s:.6f}s")

            