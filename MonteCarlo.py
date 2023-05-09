import random
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

N = 100000  # número de soluções aleatórias geradas

melhor_valor = 0
melhor_solucao = []

start_time = time.time()
for i in range(N):
    peso_atual = 0
    valor_atual = 0
    solucao_atual = []
    for j in range(len(itens)):
        if random.random(
        ) > 0.5:  # escolha aleatória do item para incluir ou não na mochila
            peso_item = itens[j][0]
            valor_item = itens[j][1]
            if peso_atual + peso_item <= W:
                peso_atual += peso_item
                valor_atual += valor_item
                solucao_atual.append(j)
    if valor_atual > melhor_valor:
        melhor_valor = valor_atual
        melhor_solucao = solucao_atual
end_time = time.time()

print("Melhor Solução:")
print("Itens: ", [itens[i] for i in melhor_solucao])
print("Peso Total: ", sum([itens[i][0] for i in melhor_solucao]))
print("Valor Total: ", melhor_valor)

print("Tempo gasto:", end_time - start_time, "segundos")