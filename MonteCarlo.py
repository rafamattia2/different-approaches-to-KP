import random
import time
import csv

file_name = "input500.txt"


with open(file_name, newline='') as file:
  reader = csv.reader(file, delimiter=',')
  items = []
  for row in reader:
    weight = int(row[0])
    value = int(row[1])
    items.append([weight, value])

# pretty_print_items(items)
# print("\n\n")
max_weight = 100
totalResTime = 0
totalResValue = 0
for i in range(50):

  N = 100000  # número de soluções aleatórias geradas

  best_value = 0
  best_solution = []


  start_time = time.time()
  for i in range(N):
    current_weight = 0
    current_value = 0
    current_solution = []
    for j in range(len(items)):
      if random.random(
      ) > 0.5:  # escolha aleatória do item para incluir ou não na mochila
        item_weight = items[j][0]
        item_value = items[j][1]
        if current_weight + item_weight <= max_weight:
          current_weight += item_weight
          current_value += item_value
          current_solution.append(j)
    if current_value > best_value:
      best_value = current_value
      best_solution = current_solution
  end_time = time.time()
  print("Best solution found:")
  print("Items: ", [items[i] for i in best_solution])
  print("Total weight: ", sum([items[i][0] for i in best_solution]))
  print("Total value: ", best_value)
  totalResValue += best_value
  print("Tempo gasto:", end_time - start_time, "segundos")
  totalResTime += end_time-start_time
print(totalResTime/50)
print(totalResValue/50)
