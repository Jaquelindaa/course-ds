def calPoints(operations):
    pilha = []
    
    for op in operations:
        if op == '+':
            # Soma os dois últimos e adiciona
            pilha.append(pilha[-1] + pilha[-2])
        elif op == 'D':
            # Dobra o último e adiciona
            pilha.append(2 * pilha[-1])
        elif op == 'C':
            # Invalida/Remove o último
            pilha.pop()
        else:
            # É um número, converte para int e adiciona
            pilha.append(int(op))
            
    return sum(pilha)

print(calPoints(["5", "2", "C", "D", "+"])) # Saída esperada: 30
print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])) # Saída esperada: 27
print(calPoints(["1", "C"])) # Saída esperada: 0