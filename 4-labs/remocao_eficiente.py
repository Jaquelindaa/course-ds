class ListaGerimundos:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        # Inserção padrão do Python (pode ser O(n))
        self.data.insert(index, value)

    def remove_gerimundos(self, index):
        """
        Implementação da lógica:
        1. Identifica o índice do último elemento (n-1)
        2. Troca o elemento do índice 'i' com o do índice 'n-1'
        3. Remove o último elemento
        """
        n = len(self.data)
        
        if not (0 <= index < n):
            raise IndexError("Índice fora de alcance")

        # Passo 1 e 2: Troca os elementos
        # O elemento no índice i recebe o valor do último elemento
        # (Não precisamos da troca completa, apenas mover o último para a vaga do i)
        self.data[index] = self.data[n - 1]
        
        # Passo 3: Remove o último elemento (O(1))
        self.data.pop()

    def __str__(self):
        return str(self.data)

# --- Testando com o fluxo da Questão 3 (b) ---

L = ListaGerimundos()

L.insert(0, "B")    # [B]
L.insert(0, "C")    # [C, B]
L.insert(1, "A")    # [C, A, B]
L.insert(2, "D")    # [C, A, D, B]

# L.remove(0) -> Troca o índice 0 ("C") pelo último ("B") e remove o último
L.remove_gerimundos(0) 
print(f"Após remove(0): {L}") # Esperado: [B, A, D]

L.insert(1, "E")    # [B, E, A, D]

# L.remove(2) -> Troca o índice 2 ("A") pelo último ("D") e remove o último
L.remove_gerimundos(2)
print(f"Após remove(2): {L}") # Esperado: [B, E, D]

# L.remove(0) -> Troca o índice 0 ("B") pelo último ("D") e remove o último
L.remove_gerimundos(0)
print(f"Após remove(0): {L}") # Esperado: [D, E]

L.insert(1, "R")    # [D, R, E]

# L.remove(2) -> Troca o índice 2 ("E") pelo último ("E") e remove
L.remove_gerimundos(2)
print(f"Após remove(2): {L}") # Esperado: [D, R]

L.insert(0, "S")    # [S, D, R]

print(f"\nConfiguração Final: {L}")