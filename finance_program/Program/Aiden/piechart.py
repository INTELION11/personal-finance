# Import libraries
from matplotlib import pyplot as plt
from faker import Faker
import random

fake = Faker()

# Creating dataset


def piechart(categories, data):
    total = sum(data)
    t_categories = []

    for x in range(0, len(categories)-1):
        t_categories.append(f"{categories[x]} ({(int(data) / total)*100})")

    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=t_categories)
    plt.show()

for i in range(1, 10):
    items = [str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word())]
    data = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

    piechart(items, data)