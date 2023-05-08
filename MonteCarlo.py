import random
import csv

file_name = "output100.txt"


def pretty_print_items(items):
  num_items = len(items)
  num_cols = 4
  num_rows = (num_items + num_cols - 1) // num_cols

  for i in range(num_rows):
    row_items = items[i * num_cols:(i + 1) * num_cols]
    row_str = ""
    for j in range(num_cols):
      if j < len(row_items):
        row_str += f"[{row_items[j][0]:2d}, {row_items[j][1]:2d}]  "
      else:
        row_str += "           "
    print(row_str)


with open(file_name, newline='') as file:
  reader = csv.reader(file, delimiter=',')
  items = []
  for row in reader:
    weight = int(row[0])
    value = int(row[1])
    items.append([weight, value])

pretty_print_items(items)
print("\n\n")
max_weight = 100
N = 10000  # número de soluções aleatórias geradas

best_value = 0
best_solution = []

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

print("Best solution found:")
print("Items: ", [items[i] for i in best_solution])
print("Total weight: ", sum([items[i][0] for i in best_solution]))
print("Total value: ", best_value)
