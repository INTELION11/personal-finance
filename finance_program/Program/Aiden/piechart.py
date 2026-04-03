# Import libraries
from matplotlib import pyplot as plt
from faker import Faker

fake = Faker()

# Creating dataset
items = [str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word()), str(fake.word())]

data = [1000, 500, 2000, 200, 300]
#def piechart(categories, data):
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=items)

# show plot
plt.show()