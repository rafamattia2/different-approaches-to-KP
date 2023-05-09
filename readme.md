# Comparando algoritmos para o problema da mochila (Knapsack problem)
O problema da mochila (Knapsack problem) é um problema de otimização combinatória, no qual é preciso escolher um 
subconjunto de itens com um valor máximo possível, sem ultrapassar uma capacidade máxima de peso.

Existem diversas abordagens para resolver esse problema, e neste trabalho iremos comparar três algoritmos: bruteforce, 
genético e Monte Carlo.

### Algoritmo Brute Force
O algoritmo Brute Force é uma abordagem exata, que consiste em testar todas as possibilidades de combinações de itens até 
encontrar a solução ótima. Embora seja uma abordagem simples, o Brute Force tem uma complexidade exponencial, o que o 
torna inviável para instâncias grandes do Knapsack problem.

### Algoritmo Genético
O algoritmo Genético é uma abordagem baseada em evolução, inspirada na seleção natural. A ideia é gerar uma população inicial 
aleatória de soluções e aplicar operadores genéticos, como cruzamento e mutação, para gerar novas soluções. A seleção das 
soluções mais aptas é feita com base em uma função de fitness, que mede o quão boa é uma solução. O algoritmo Genético pode 
encontrar soluções razoáveis em instâncias grandes do Knapsack problem, mas ainda assim pode ser lento para problemas muito 
grandes.

### Algoritmo Monte Carlo
O algoritmo Monte Carlo é uma abordagem baseada em amostragem aleatória, que gera soluções aleatórias e avalia sua 
qualidade com base na função de fitness. A ideia é repetir esse processo várias vezes e selecionar a melhor solução 
encontrada. O algoritmo Monte Carlo pode ser rápido para instâncias grandes do Knapsack problem, mas a qualidade da 
solução pode ser baixa, dependendo da quantidade de amostras geradas.



