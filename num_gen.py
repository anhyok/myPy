import random

with open('num_data', 'w') as file:
    for _ in range(50000000):
        num = random.randint(1, 100000000)
        file.write(f"{num}\n")