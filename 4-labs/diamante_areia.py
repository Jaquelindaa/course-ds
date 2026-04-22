def contar_diamantes(mina):
    pilha = []
    diamantes = 0

    for char in mina:
        if char == '<':
            pilha.append(char) 
        elif char == '>':
            if len(pilha) > 0:
                pilha.pop()
                diamantes += 1
    return diamantes