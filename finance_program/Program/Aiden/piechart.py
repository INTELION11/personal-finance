# Import libraries
from matplotlib import pyplot as plt
from faker import Faker
import random
import csv

fake = Faker()

# Creating dataset

def piechart(categories, data):
    total = sum(data)
    t_categories = []

    for x in range(0, len(categories)):
        t_categories.append(f"{categories[x]} ({round((data[x] / total)*100, 2)}%)")
    
    
    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=t_categories)
    plt.show()

    for i in t_categories:
        print(i)

def pull_info(chosen_file, username, categories, data):
    pass