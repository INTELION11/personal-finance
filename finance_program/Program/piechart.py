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

def pull_info(chosen_file, username):
    with open(chosen_file, mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == username:
                data = line[2].split()
                num_data = []
                for i in data:
                    num_data.append(int(i))
                piechart(line[1].split(), num_data)
            else:
                pass

def finance_tracking(chosen_file, username, categories, data):
    all = []
    with open(chosen_file, mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Username':
                pass
            else:
                all.append({'Username':line[0] ,'Categories':line[1] ,'Data':line[2]})
        for line in all:
            if line["Username"] == username:
                newline = line
                all.remove(line)
                newline['Categories'] = categories
                newline['Data'] = data
            else:
                pass
        try:
            all.append(newline)
        except:
            all.append({'Username':username ,'Categories':categories ,'Data':data})
        for i in all:
            if i["Username"] == 'username':
                all.remove(i)
            else:
                pass
    with open(chosen_file, mode= 'w', newline= '') as sample:
        fieldnames = ['Username','Categories','Data']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)

def finance_tracking_single(chosen_file, username, category, inputing):
    all = []
    with open(chosen_file, mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Username':
                pass
            else:
                all.append({'Username':line[0] , category:line[1]})
        for line in all:
            if line["Username"] == username:
                newline = line
                all.remove(line)
                newline[category] = inputing
            else:
                pass
        try:
            all.append(newline)
        except:
            all.append({'Username':username ,category:inputing})
        for i in all:
            if i["Username"] == 'username':
                all.remove(i)
            else:
                pass
    with open(chosen_file, mode= 'w', newline= '') as sample:
        fieldnames = ['Username',category]
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)

