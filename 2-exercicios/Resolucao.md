## COMPLEXIDADE DE ALGORITMOS

1. Desenhe o gráfico das funções 8n, 4n log n, 2n², n³ e 2<sup>n</sup> usando uma escala logarítmica para os eixos x e
y, isto é, se o valor da função f(x) é y, desenhe esse ponto com a coordenada x em log x e a coordenada
y em log y.

    ```mermaid
    xychart-beta
        title "Crescimento de Funções (Escala Log-Log)"
        x-axis "log(n)" [1, 2, 4, 8, 16, 32, 64]
        y-axis "log(f(n))" 0 --> 20
        line "8n (Linear)" [3, 4, 5, 6, 7, 8, 9]
        line "4n log n" [2, 4.3, 7.3, 10.6, 14.3, 18.3, 22.6]
        line "2n^2 (Quadrática)" [1, 3, 5, 7, 9, 11, 13]
        line "n^3 (Cúbica)" [0, 3, 6, 9, 12, 15, 18]
        line "2^n (Exponencial)" [1, 2, 4, 8, 16, 32, 64]
        
    ```
    <span style="color:blue">■</span> 8n <span style="color: green">■</span> 4n log n <span style="color: red">■</span> 2n² <span style="color: yellow">■</span> n<sup>3</sup> <span style="color: white">■</span> 2<sup>n</sup>
<br><br>

2. Ordene as funções a seguir por sua taxa assintótica de crescimento.

    | Exercício | Resultado |
    | ------------- | ------------- |
    |4n log n + 2n | 2<sup>10</sup>
    2<sup>10</sup> | 2n
    3n + 100 log n | 3n + 100 log n
    4n | 4n
    2n |n log n
    n<sup>2</sup> + 10n | 4n log n + 2n 
    n <sup>3</sup>| n<sup>2</sup> + 10n 
    n log n| n 3
<br>

3. Qual a complexidade assintótica no pior caso (em termos de O) do algoritmo abaixo?
    ``` Python
    1 # Returns the sum of the integers in given array.
    2 def alg1(arr):
    3   n = len(arr)
    4   total = 0
    5   for j in range(n):
    6       total += arr[j]
    7   return total
    ```
    Como só tem um for a complexidade assintótica seria O(n)
<br>

4. Qual a complexidade assintótica no pior caso (em termos de O) do algoritmo abaixo?
    ``` Python
    1 # Returns the sum of the integers with even index in given array.
    2 def alg2(arr):
    3   n = len(arr)
    4   total = 0
    5   for j in range(0, n, 2):
    6       total += arr[j]
    ```
    Como só tem um for a complexidade assintótica seria O(n)
<br>

5. Qual a complexidade assintótica no pior caso (em termos de O) do algoritmo abaixo?
    ``` Python
    1 # Returns the sum of the prefix sums of given array.
    2 def alg3(arr):
    3   n = len(arr)
    4   total = 0
    5   for j in range(n):
    6       for k in range(j + 1):
    7       total += arr[k]
    8   return total
    ```
    Como tem dois for a complexidade assintótica seria O(n²)
<br>

6. Qual a complexidade assintótica no pior caso (em termos de O) do algoritmo abaixo?
    ``` Python
    # Returns the sum of the prefix sums of given array.
    def alg4(arr):
        n = len(arr)
        prefix = 0
        total = 0
        for j in range(n):
            prefix += arr[j]
            total += prefix
        return total
    ```
    Como tem apenas um for, a complexidade assintótica seria O(n)
<br>

7. Qual a complexidade assintótica no pior caso (em termos de O) do algoritmo abaixo?
    ``` Python
    # Returns the number of times second array stores sum of prefix sums from first.
    def alg5(first, second):
        n = len(first)
        count = 0
        for i in range(n):
            total = 0
            for j in range(n):
                for k in range(j + 1):
                    total += first[k]
            if second[i] == total:
                count += 1
        return count
    ```
    Como temos 3 for e um if é ocntante, a complexidade assintótica é O(n<sup>3</sup>)
<br>

8. O algoritmo A executa uma computação em tempo O(log n) para cada entrada de um arranjo de n elementos. Qual o pior caso em relação ao tempo de execução de A? <br> Como temos n elementos, e cada um exige o mesmo esforço do algortimo que é O(log n) no fim teremos O(n log n)
<br>

9. Dado um arranjo X de n elementos, o algoritmo B escolhe log n elementos de X, aleatoriamente, e executa um cálculo em tempo O(n) para cada um. Qual o pior caso em relação ao tempo de execução de B? <br> 
Como o arranjo X tem n elementos, para cada um dele O(log n) será exigido, resultando em n x log n, no fim teremos O(n log n)
<br>

10. Dado um arranjo X de n elementos inteiros, o algoritmo C executa uma computação em tempo O(n) para cada número par de X e uma computação em tempo O(log n) para cada elemento ímpar de X. Qual o melhor caso e o pior caso em relação ao tempo de execução de C?<br>
No pior caso o arranjo X seria completamente composto por números inteiros par, exigindo O(n) no melhor caso, seria totalmente composto por números ímpares, exigindo O(log n)

11. Dado um arranjo X de n elementos, o algoritmo D chama o algoritmo E para cada elemento X[i]. O algoritmo E executa em tempo O(i) quando é chamado sobre um elemento X[i]. Qual o pior caso em relação ao tempo de execução do algoritmo D?<br>
    * Um loop que percorre n elementos → chama E para cada i
    * O algoritmo E custa O(i)<br>
    Resposta: O(n²)

12. Implemente os algoritmos disjoint1 e disjoint2 (apresentados nos materiais de aula), e execute uma análise experimental dos seus tempos de execução. Visualize seus tempos de execução como uma função do tamanho da entrada usando um gráfico di-log.
    ```Python
    #O(n³)
    def disjoint1(A, B, C):
        for a in A:
            for b in B:
                for c in C:
                    if a == b == c:
                        return False
        return True

    #O(n²)
    def disjoint2(A, B, C):
        for a in A:
            for b in B:
                if a == b:
                    for c in C:
                        if a == c:
                            return False
        return True
    ```
<br>

13. Execute uma análise experimental para testar a hipótese de que o método de ordenação do python (sort ou sorted) executa em um tempo médio O(n log n).
    ```Python
    import time
    import random
    import matplotlib.pyplot as plt

    tamanhos = [100, 500, 1000, 5000, 10000, 20000]
    tempos = []

    for n in tamanhos:
        lista = [random.randint(0, n) for _ in range(n)]

        inicio = time.time()
        sorted(lista)
        tempos.append(time.time() - inicio)

    plt.loglog(tamanhos, tempos, label="sort")
    plt.xlabel("n")
    plt.ylabel("tempo")
    plt.legend()
    plt.show()
    ```
<br>

14. Execute uma análise experimental para determinar o maior valor de n para os algoritmos unique1 e unique2 (apresentados nos materiais de aula), de modo que o algoritmo execute em um minuto ou menos.
    ```Python
    #O(n²)
    def unique1(S):
    n = len(S)
    for j in range(n):
        for k in range(j+1, n):
            if S[j] == S[k]:
                return False
    return True

    #O(n log n)
    def unique2(S):
        S = sorted(S)
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return False
        return True
    ```
<br>


## ESTRUTURAS FUNDAMENTAIS E LISTAS
1. Forneça uma implementação para o método size() da classe LinkedList, considerando que a mesma não mantenha o tamanho armazenado em uma variável. Qual a implicação dessa modificação na complexidade assintótica do método?
    ```Python
    def size(self):
        count = 0
        walk = self._header._next 
        
        while walk != self._trailer:
            count += 1
            walk = walk._next
            
        return count
    ```
    Resultaria em uma aumento da complxidade, pois seria necessário percorrer a linkdList inteira O(n)
<br>

2. Descreva um método para encontrar o nodo central de uma lista duplamente encadeada com nodos sentinelas, sem o uso de informações sobre o tamanho da lista. No caso de um número par de nodos, o método deve devolver o nodo à esquerda do ponto central. Qual a complexidade desse algoritmo?
    ```Python
    def find_middle(self):
        if self.is_empty():
            raise ValueError("A lista está vazia")

        left = self.header.next
        right = self.trailer.prev

        while left != right and left.next != right
            left = left.next
            right = rigth.prev
        return left
    ```
    A complexidade assintótica seria O(n)
<br>

3. Descreva um algoritmo para concatenar duas listas duplamente encadeadas L e M com sentinelas, em uma lista única L′.
    Crie duas variéveis temporáris, Temp1 como o Trailer de L e Header de M como Temp2. Depois definimmoas que o Header de 'L é o header de L, que o next de temp1 é temp 2 e como é duplamente encadeada, que o prev de temp 2 é temp 1, por fim que o trailer de 'L é o trailer de M
<br>

4. Descreva em detalhes como trocar dois nodos x e y de posição (não apenas seu conteúdo) em uma lista simplesmente encadeada L, dadas as referências para x e y somente. Repita este exercício para o caso em que L é uma lista duplamente encadeada. Qual algoritmo possui maior complexidade?
    ```Python
    def swap_nodes(head, x, y):
    if x == y:
        return head

    prevX = prevY = None
    curr = head

    # encontrar prevX e prevY
    while curr and (prevX is None or prevY is None):
        if curr.next == x:
            prevX = curr
        if curr.next == y:
            prevY = curr
        curr = curr.next

    # se x ou y não estão na lista
    if not x or not y:
        return head

    # atualizar prevs
    if prevX:
        prevX.next = y
    else:
        head = y

    if prevY:
        prevY.next = x
    else:
        head = x

    # trocar next
    x.next, y.next = y.next, x.next

    return head
    ```
<br>

5. Implemente uma lista simplesmente encadeada que forneça operações de inserção e remoção nas duas extremidades, além dos métodos size e is_empty.
    ```Python
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None
        
        class LinkedList:
            def __init__(self):
                self.head = None
                self.tail = None
                self.size = 0

            def size(self):
                return self.size

            def insert_first(self, value):
                new_node = Node(value)
                if self.is_empty():
                    self.head = self.tail = new_node
                else:
                    new_node.next = self.head
                    self.head = new_node
                self_size += 1
            
            def remove_first(self, value):
                if self.is_empty():
                    return None
                
                removed_value = self.head.value
                self.head = self.head.next
                self.size -= 1

                if self.is_empty():
                    self.tail = None
                
                return renomed_value
            
            def insert_last(self, value):
                new_node = Node(value)
                if self.is_empty():
                    self.head = self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self_size += 1

            def remove_last(self, value):
                if self.is_empty():
                    return None

                if self.head == self.tail:
                    self. head = None
                    self.tail = None
                else:
                    current = self.head
                    while current.next != self.tail:
                        current = current.next
                    
                    self.tail = current
                    self.tail.next = None

                self.size -= 1
                return removed_value
    ```

6. Uma forma de melhorar o desempenho de uma lista duplamente encadeada é buscar pelo nodo desejado (para inserção ou remoção) “de trás para frente”, quando conveniente. Como essa abordagem pode ser implementada? Qual o impacto na complexidade do procedimento de busca?<br>
    Poderia ser implementada dividindo a lista duplamentee encadeada, pela metada, assim supondo que eu soubessa a posição do valor que eu quero buscar, verifica que a posição é menor que o indíce do meio ou maior, se for menor coomeço pelo head, se for maior começo pelo trailer. Em relação a sua complexidade, ficaria n/2, então O(n) 
<br>

7. Forneça uma representação de uma lista L, inicialmente vazia, após realizar as seguintes operações: insert(0, 4), insert(0, 3), insert(0, 2), insert(2, 1), insert(1, 5), insert(1, 6), insert(3, 7), insert(0, 8).
<br>
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    |-- |-- |-- | --| --| --| --| --|
    | 8 | 2 | 6 | 5 | 7 | 3 | 1 | 4 |

8. Supondo que estamos mantendo uma coleção C de elementos de tal modo que, cada vez que adicionamos um novo elemento na coleção, copiamos o conteúdo de C em uma nova lista baseada em arranjo do tamanho exato ao necessário. Qual o tempo de processamento da adição de n elementos em uma coleção C inicialmente vazia?
<br>
    Para inserir um novo elemennto é O(n) como será necessário inserir todos os elementos novamente será O(n²)
<br>

9. Considere a implementação de uma lista duplamente encadeada fornecida pela classe LinkedList. Implemente a função toArray que retorna uma lista baseada em arranjo com os elementos da lista encadeada.
    ```Python
        def to_arrya(self):
            resultado = []
            altual = selfs.head

            while atual is not None:
                resultado.append(atual.data)
                atual = atual.next
            
            return resultado
    ```
<br>

10. A lista baseada em arranjo fornece uma função index(e), que retorna o índice onde o elemento e está armazenado, e dispara uma exceção, caso o elemento não é encontrado na estrutura. Implemente essa função na classe LinkedList.
    ```Python
        def index(self, e):
            atual = self.head.next
            position = 0

            while atual != self.tail:
                if atual.data == e:
                    return position

                position += 1
                atual = atual.next
            
            raise ValueError("Elemento não encontrado")
    ```
<br>

11. A lista baseada em arranjo fornece uma função clear(), que remove todos os elementos da coleção. Implemente essa função na classe LinkedList.
    ```Python
    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        
    ```
<br>

12. Desenvolva um experimento para testar a eficiência de n chamadas sucessivas à função insert de uma lista baseada em arranjo para vários n diferentes, e analise os resultados empíricos sob os seguintes cenários:
    a. Cada insert acontece no índice 0. O(n²)
    b. Cada insert acontece no índice size()/2. O(n²)
    c. Cada insert acontece no índice size(). O(n)

    ```Python
    import time
    import matplotlib.pyplot as plt

    def experimento(n, modo):
        lista = []
        inicio = time.time()

        for i in range(n):
            if modo == "inicio":
                lista.insert(0, i)
            elif modo == "meio":
                lista.insert(len(lista)//2, i)
            elif modo == "fim":
                lista.append(i)  # equivalente a insert no final

        return time.time() - inicio


    tamanhos = [1000, 2000, 5000, 10000, 20000, 50000]

    tempos_inicio = []
    tempos_meio = []
    tempos_fim = []

    for n in tamanhos:
        tempos_inicio.append(experimento(n, "inicio"))
        tempos_meio.append(experimento(n, "meio"))
        tempos_fim.append(experimento(n, "fim"))

    # gráfico di-log
    plt.loglog(tamanhos, tempos_inicio, label="insert início")
    plt.loglog(tamanhos, tempos_meio, label="insert meio")
    plt.loglog(tamanhos, tempos_fim, label="insert fim")

    plt.xlabel("n")
    plt.ylabel("tempo")
    plt.legend()
    plt.show()
    ```
<br>


## BUSCAS COM ESTRUTURAS LINEARES
1. Implemente uma versão recursiva do algoritmo de busca binária, conforme as ideias do Capítulo 4 (Recursão) de Goodrich et al. (2013) – Data Structures and Algorithms in Python.
    ```Python
    def busca_binaria_recursiva(lista, alvo, inicio, fim):
    # caso base: não encontrou
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
    

    lista = [1, 3, 5, 7, 9, 11, 13]
    resultado = busca_binaria_recursiva(lista, 7, 0, len(lista) - 1)
    print(resultado)  # saída: 3
    
    ```
<br>

2. Simule o algoritmo de busca binária para os seguintes casos:
    a. x = 15, v = {15, 27, 33, 46, 51, 63, 71, 82, 90}.
    b. x = 33, v = {15, 27, 33, 46, 51, 63, 71, 82, 90}.
    c. x = 63, v = {15, 27, 33, 46, 51, 63, 71, 82, 90}.
    d. x = 81, v = {15, 27, 33, 46, 51, 63, 71, 82, 90}.
    e. x = 22, v = {15, 27, 33, 46, 51, 63, 71, 82, 90}.
    Compare o número de avaliações realizadas pelas buscas binária e sequencial.

    | Busca binária | Busca Sequencia |
    | ------------- | --------------- |
    | 51, 27, 15 (3 avaliações) | 15 (1 avaliação) |
    | 51, 27, 33 (3 avaliações) | 15, 27, 33 (3 avaliações) |
    | 51, 71, 63 (3 avaliações) | 15, 27, 33, 46, 51, 53 (6 avaliações) |
    | 51, 71, 82 (3 avaliações) | todos os elemetnso (9 avaliações) |
    | 51, 27, 15 (3 avaliações) | todos os elemetnso (9 avaliações) |
<br>

3. Quando o vetor está ordenado, a busca sequencial não precisa percorrer toda a lista para saber que o elemento buscado não existe. Ela pode parar quando o elemento analisado for maior que o buscado. Implemente as modificações necessárias para essa estratégia. Qual o impacto na complexidade assintótica do novo algoritmo?
    ```Python
    def busca_sequencial_ordenada(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
        elif lista[i] > alvo:
            return -1  # pode parar cedo

    return -1

    lista = [2, 4, 6, 8, 10]
    print(busca_sequencial_ordenada(lista, 6))  # 2
    print(busca_sequencial_ordenada(lista, 5))  # -1 (para no 6)
    ```
<br>

## ORDENAÇÃO DE ESTRUTURAS LINEARES
1. Mostre o conteúdo do array de inteiros (5, 7, 4, 9, 8, 5, 6, 3) para cada vez que o algoritmo insertion sort o modifica durante o processo de ordenação.
    |5, 7, 4, 9, 8, 5, 6, 3| 5 |
    |5, 7, 4, 9, 8, 5, 6, 3| 7 |
    |4, 5, 7, 9, 8, 5, 6, 3| 4 |
    |4, 5, 7, 9, 8, 5, 6, 3| 9 |
    |4, 5, 7, 8, 9, 5, 6, 3| 8 |
    |4, 5, 5, 7, 8, 9, 6, 3| 5 |
    |4, 5, 5, 6, 7, 8, 9, 3| 6 |
    |3, 4, 5, 5, 6, 7, 8, 9| 3 |
<br>

2. Qual modificação é necessária para que o algoritmo insertion sort ordene os elementos de forma decrescente?
    ```Python
    #Crescente: lista[j] > chave
    #Decrescente: lista[j] < chave
    
    def insertion_sort_decrescente(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] < chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista
    
    ```
    <br>

3. O algoritmo bubble sort ordena um array de n elementos em ordem crescente, executando n−1 passagens pelo array. Em cada passagem, ele compara elementos adjacentes e os troca se estiverem fora de ordem. Por exemplo, na primeira passagem ele compara o primeiro e o segundo elementos, depois o segundo e o terceiro elementos, e assim por diante. No final da primeira passagem, o maior elemento está em sua
posição adequada no final do array. Cada passagem subsequente ignora os elementos no final do array, pois eles estão ordenados e são maiores que qualquer um dos elementos restantes. Assim, cada passagem faz uma comparação a menos que a passagem anterior. A figura abaixo ilustra seu funcionamento.

    ```Python
        def bubble_sort(array):
            for last_index in range(len(array) - 1, 0, -1):
                for index in range(last_index):
                    if array[index] > array[index + 1]:
                            array[index], array[index + 1] = array[index + 1], array[index]
    ```
<br>

4. Qual a complexidade assintótica de tempo do bubble sort? A complexidade assintótica é O(n²), mas caso o elemento seja encontrado, pode ser interrompido passando a ser O(n)<br>

5. Implemente um algoritmo para verificar se um array está em ordem não-decrescente. Você pode usar esse método para verificar se um algoritmo de ordenação executou corretamente.<br>
    ```Python
        def esta_ordenado(v):
        for i in range(len(v) - 1):
            if v[i] > v[i+1]:
                return False
                
        return True
    ```

6. No algoritmo insertion sort, podemos usar uma busca binária para encontrar a posição de inserção de cada elemento. Qual o impacto na complexidade assintótica do algoritmo?
    <br>A complexidade assintótica NÃO muda: continua O(n²)<br>
    
7. Estude os seguintes algoritmos de ordenação:
• Merge sort;
• Quick sort;
• Radix sort.

    ```Python
    def merge_sort(v):
        if len(v) > 1:
            meio = len(v) // 2
            esquerda = v[:meio]
            direita = v[meio:]

            # Divisão recursiva
            merge_sort(esquerda)
            merge_sort(direita)

            i = j = k = 0

            # Intercalação (Merge)
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    v[k] = esquerda[i]
                    i += 1
                else:
                    v[k] = direita[j]
                    j += 1
                k += 1

            # Copia elementos restantes
            while i < len(esquerda):
                v[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                v[k] = direita[j]
                j += 1
                k += 1

    def quick_sort(v):
    if len(v) <= 1:
        return v
    else:
        pivo = v[len(v) // 2]
        menores = [x for x in v if x < pivo]
        iguais  = [x for x in v if x == pivo]
        maiores = [x for x in v if x > pivo]
        
        return quick_sort(menores) + iguais + quick_sort(maiores)

    def counting_sort_aux(v, exp):
    n = len(v)
    saida = [0] * n
    count = [0] * 10

    for i in range(n):
        index = v[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = v[i] // exp
        saida[count[index % 10] - 1] = v[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        v[i] = saida[i]

def radix_sort(v):
    if not v: return
    max_num = max(v)
    exp = 1
    while max_num // exp > 0:
        counting_sort_aux(v, exp)
        exp *= 10
    ```


## PILHAS FILAS E DECKS
1.  Considere uma lista dinâmica L, uma pilha P e uma fila F, inicialmente vazias. Apresente a configuração final das estruturas L, P e F, após a execução dessas operações. As seguintes operações são executadas, nesta ordem: 
    * P.push(1)
    * P.push(2)
    * F.enqueue(3)
    * F.enqueue(4)
    * F.enqueue(5)
    * L.insert(0, 6)
    * L.insert(0, 7)
    * L.insert(1, 8)
    * P.push(9)
    * L.insert(1 P.top())
    * L.insert(2, F.dequeue())
    * L.insert(0, P.pop()) 
    * P.push(F.dequeue())
    * P.push(L.get(3))
    * F.enqueue(L.remove(2))
    * L.set(2, F.first())

    | PILHA (P) |
    |-----------|
    |(topo)3, 4, 2, 1 (base)|

    | FILA (F) |
    |----------|
    |(inicio) 5, 9 (fim) |

    
    | LISTA (L) |
    |----------|
    | 9, 7, 5, 8, 6 |
   <br> 

2. Suponha que inicialmente uma pilha vazia S tenha realizado um total de 25 operações push, 12 operações top e 10 operações pop, 3 das quais retornaram null, indicando uma pilha vazia. Qual é o tamanho atual de S?
<br>
    Inicia vazia, tamanho = 0, quando ocorre 25 push tamanho = 25, top só retorna, então não altera o tamanho, e 10 pop, mas 3 retornando null, então apenas 7 elementos foram kexcluídos, resultando no tamanho final de de 18 elementos (25 - 7 = 18)
<br>

3. Sendo a pilha do exercício anterior implementada usando um arranjo seguindo as ideias estudadas em sala de aula, qual o valor final da variável t? a variavél t = 17 (n-1)
<br>

4. Quais valores são retornados durante as seguintes operações, se executadas em uma pilha inicialmente vazia? 
    * push(5)
    * push(3)
    * pop()
    * push(2)
    * push(8)
    * pop()
    * pop()
    * push(9)
    * push(1)
    * pop()
    * push(7)
    * push(6)
    * pop()
    * pop()
    * push(4)
    * pop()
    * pop()
<br>
    Retorno = 3, 8, 2, 1, 6, 7, 4, 9
<br>

5. Implemente uma função com a assinatura transfer(S, T) que transfere todos os elementos da pilha S para a pilha T, de modo que o elemento que iniciou no topo de S é o primeiro elemento a ser inserido em T, e o último elemento de S termina no topo de T.
    ```Python
        def transfer(S, T):
            while S != is_empty():
                T.push(S.pop())
    ```
6. Apresente um método recursivo que remove todos os elementos de uma pilha.
    ```Python
        def esvaziar_pilha_recursivo(pilha):
            if pilha.is_empty():
                return
            
        pilha.pop()
        esvaziar_pilha_recursivo(pilha)
    ```
7. Suponha que uma fila vazia Q realizou um total de 32 operações de enqueue, 10 operações first e 15 operações dequeue, 5 das quais retornaram null, indicando uma fila vazia. Qual é o tamanho atual de Q?
    A fila começa vazia, com o enqueue o tamanho passa a ser 32, a operação first apenas retorna o primeiro elemento da fila, e os 15 dequeue tiram os elementos ficando com 17 (32 - 15), porém 5 retornaram null 22 (17 + 5)
    <br>

8. Sendo a fila do exercício anterior implementada seguindo as ideias estudadas em sala de aula e usando um arranjo com uma capacidade de 30 elementos nunca excedida, qual o valor final da variável f?<br>
    Isso ocorre porque a fila é implementada com arranjo circular e a variável f (frente) só é incrementada quando ocorre um dequeue válido. Como houve 10 remoções válidas, temos: f=(0+10)mod30=10 As operações enqueue e first não alteram f, e os dequeue que retornaram null também não causam mudança.
<br>
9. Quais são os valores retornados após as seguintes operações, se executadas em uma fila inicialmente vazia?
    * enqueue(5)
    * enqueue(3)
    * dequeue()
    * enqueue(2)
    * enqueue(8)
    * dequeue()
    * dequeue()
    * enqueue(9)
    * enqueue(1)
    * dequeue()
    * enqueue(7)
    * enqueue(6)
    * dequeue()
    * dequeue()
    * enqueue(4)
    * dequeue()
    * dequeue()
    <br>
    Retorno: 5, 3, 2, 8, 9, 1, 7, 6
<br>

10. Faça um adaptador simples (classe) que implemente uma pilha usando um deque para armazenamento. Use a implementação de deque fornecido pelo módulo collections.deque.
    ```Python
        
    from collections import deque

    class Pilha:
        def __init__(self):
            # Inicializa o deque como a estrutura de armazenamento interna
            self._dados = deque()

        def push(self, elemento):
            """Adiciona um elemento ao topo da pilha."""
            self._dados.append(elemento)

        def pop(self):
            """Remove e retorna o elemento do topo. Levanta erro se estiver vazia."""
            if self.is_empty():
                raise IndexError("pop de uma pilha vazia")
            return self._dados.pop()

        def top(self):
            """Retorna o elemento do topo sem removê-lo."""
            if self.is_empty():
                raise IndexError("top de uma pilha vazia")
            return self._dados[-1]

        def is_empty(self):
            """Verifica se a pilha está vazia."""
            return len(self._dados) == 0

        def __len__(self):
            """Retorna o número de elementos na pilha."""
            return len(self._dados)

        def __str__(self):
            """Representação visual da pilha."""
            return f"Pilha(topo <- {list(self._dados)})"
    ```
<br>

11. Faça um adaptador simples (classe) que implemente uma fila usando uma instância de deque para armazenamento. Use a implementação de deque fornecido pelo módulo collections.deque

12. Quais são os valores retornados após as seguintes operações, se executadas em um deque inicialmente vazio? 
    * add_first(3)
    * add_last(8)
    * add_last(9)
    * add_first(1)
    * last()
    * is_empty()
    * add_first(2)
    * remove_last()
    * add_last(7)
    * first()
    * last()
    * add_last(4)
    * size()
    * remove_first()
    * remove_first()
<br> Retorno: 9, False, 9 2, 7, 6 2, 1

13. Suponha que você tenha um deque D contendo os números (1, 2, 3, 4, 5, 6, 7, 8), nessa ordem. Supondo que além disso você tenha uma fila Q incialmente vazia. Apresente um pseudocódigo que utilize somente D e Q (mais nenhuma variável) e resulte em D armazenando os elementos na ordem (1, 2, 3, 5, 4, 6, 7, 8).
    ```Python
       D.add_last(D.remove_first())
       D.add_last(D.remove_first()) 
       D.add_last(D.remove_first())
       Q.enqueue(D.remove_first())
       Q.enqueue(D.remove_first())
       D.add_first(Q.dequeue())
       D.add_first(Q.dequeue())
       D.add_first(D.remove_last())
       D.add_first(D.remove_last())
       D.add_first(D.remove_last())
    ```

14. Repita o exercício anterior usando o deque D e uma pilha S, inicialmente vazia
    ```Python
       D.add_last(D.remove_first())
       D.add_last(D.remove_first()) 
       D.add_last(D.remove_first())
       S.push(D.remove_first())
       S.push(D.remove_first())
       D.add_first(S.pop())
       D.add_first(S.pop())
       D.add_first(D.remove_last())
       D.add_first(D.remove_last())
       D.add_first(D.remove_last())
    ```