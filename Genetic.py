import random
import csv

# def generate_population(size, file_name):
#     items = []
#     with open(file_name, newline='') as file:
#         reader = csv.reader(file, delimiter=',')
#         for row in reader:
#             weight = int(row[0])
#             value = int(row[1])
#             items.append([weight, value])
#
#         population = []
#         for _ in range (size):
#             genes = [0, 1]
#             chromosome = []
#             for _ in range(len(items)):
#                 chromosome.append(random.choice(genes))
#             population.append(chromosome)
#         print("Generated a random population of size", size)
#         return population
def generate_population(size):
    population = []
    for _ in range (size):
        genes = [0, 1]
        chromosome = []
        for _ in range(len(items)):
            chromosome.append(random.choice(genes))
        population.append(chromosome)
    print("Generated a random population of size", size)
    return population

def calculate_fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range (len(chromosome)):
        if chromosome[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]
    if total_weight > max_weight:
        return 0
    else:
        return total_value

def select_chromosomes(population):
    fitness_values = []
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))

    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]
    parent1 = random.choices(population, weights = fitness_values, k=1)[0]
    parent2 = random.choices(population, weights = fitness_values, k=1)[0]

    #print("Selected two chromosomes for crossover")
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(items)-1)
    child1 = parent1[0:crossover_point] + parent2[crossover_point:]
    child2 = parent2[0:crossover_point] + parent1[crossover_point:]

    #print("Performed crossover between two chromosomes")
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(items)-1)
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    #print("Performed mutation on a chromosome")
    return chromosome

def get_best(population):
    fitness_values = []
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))

    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    return population[max_index]

file_name = "output100.txt"

with open(file_name, newline='') as file:
    reader = csv.reader(file, delimiter=',')
    items = []
    for row in reader:
        weight = int(row[0])
        value = int(row[1])
        items.append([weight, value])
# items = [
#             [1, 2],
#             [2, 4],
#             [3, 7],
#             [4, 5],
#             [5, 7],
#             [6, 9]
#         ]

print("Avaliable items:\n", items)

max_weight = 250
population_size = 1000
mutation_probability = 0.2
generations = 100

print("\nGenetic algorithm parameters")
print("Max_weight: ", max_weight)
print("Population: ", population_size)
print("Mutation probability: ", mutation_probability)
print("Generations: ", generations)
print("Performing genetic evolution: ")

# population, items = generate_population(population_size, file_name)
population = generate_population(population_size)

for _ in range(generations):
    parent1, parent2 = select_chromosomes(population)

    child1, child2 = crossover(parent1, parent2)

    if random.uniform(0, 1) < mutation_probability:
        child1 = mutate(child1)

    if random.uniform(0, 1) < mutation_probability:
        child2 = mutate(child2)

    population = [child1, child2] + population[2:]

best = get_best(population)

total_weight = 0
total_value = 0
for i in range(len(best)):
    if best[i] == 1:
        total_weight += items[i][0]
        total_value += items[i][1]

print(best)
print("\nThe best solution: ")
print("Weight: ", total_weight)
print("Value: ", total_value)