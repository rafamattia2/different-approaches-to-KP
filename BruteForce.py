import itertools
import time
import csv

nome_arq = "input20.txt"

with open(nome_arq, newline='') as file:
    leitor = csv.reader(file, delimiter=',')
    itens = []
    for linha in leitor:
        peso = int(linha[0])
        valor = int(linha[1])
        itens.append([peso, valor])

W = 100
melhor_valor = 0
melhor_solucao = []

start_time = time.time()
# gera todas as combinações possíveis de escolha de itens
for possibilidade in itertools.product([0, 1], repeat=len(itens)):
    peso_atual = sum([itens[i][0]
                      for i in range(len(itens))
                      if possibilidade[i] == 1])
    valor_atual = sum([itens[i][1]
                       for i in range(len(itens))
                       if possibilidade[i] == 1])

    # verifica se a combinação atual é válida (não ultrapassa o peso máximo)
    if peso_atual <= W:
        # verifica se a combinação atual tem um valor maior que a melhor solução encontrada até agora
        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_solucao = [i for i in range(len(itens))
                              if possibilidade[i] == 1]
end_time = time.time()

print("Melhor Solução:")
print("Itens: ", [itens[i] for i in melhor_solucao])
print("Peso Total: ", sum([itens[i][0] for i in melhor_solucao]))
print("Valor Total: ", melhor_valor)

print("Tempo gasto:", end_time - start_time, "segundos")