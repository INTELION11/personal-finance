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
        all = []
    with open("Documents/A_Highscores.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Username':
                pass
            else:
                all.append({'Username':line[0] ,'Highscore':line[1] ,'Latest Score':line[2]})
        for line in all:
            if line["Username"] == username:
                newline = line
                all.remove(line)
                newline['Latest Score'] = score
                if score > int(newline['Highscore']):
                    newline['Highscore'] = score
                else:
                    pass
            else:
                pass
        try:
            all.append(newline)
        except:
            all.append({'Username':username ,'Highscore':score ,'Latest Score':score})
    with open("Documents/A_Highscores.csv", mode= 'w', newline= '') as sample:
        fieldnames = ['Username','Highscore','Latest Score']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)