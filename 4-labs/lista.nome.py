def organizar_nomes(lista_nomes):
    linhas = [] 
    
    for nome in lista_nomes:
        tamanho = len(nome)
        alocado = False
        
        # Tenta encaixar o nome em uma linha existente
        for linha in linhas:
            if tamanho not in linha:
                linha[tamanho] = nome
                alocado = True
                break
        
        # Se não coube em nenhuma linha existente, cria uma nova linha
        if not alocado:
            linhas.append({tamanho: nome})
            
    for linha in linhas:
        tamanhos_ordenados = sorted(linha.keys())
        nomes_na_ordem = [linha[t] for t in tamanhos_ordenados]
        
        print(", ".join(nomes_na_ordem))

if __name__ == "__main__":
    nomes_exemplo = [
        "sergio", "ana", "maria", "carlos", "eva", "joaquim",
        "jo", "mara", "laura", "lucas", "ari", "paulo"
    ]

    organizar_nomes(nomes_exemplo)