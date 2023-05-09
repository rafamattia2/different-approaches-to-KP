import random

with open("input40.txt", "w") as file:
    for i in range(40):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        file.write("{}, {}\n".format(a,b))