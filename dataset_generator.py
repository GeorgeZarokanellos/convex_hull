import random

file = open('dataset.txt', 'w')

for _ in range(500):
    value1 = random.random()
    value2 = random.random()
    value1 = "{:.3f}".format(value1 * 100)
    value2 = "{:.3f}".format(value2 * 100)
    # f_v1 = str(value1)
    # f_v2 = str(value2)
    file.write(value1 + " " + value2 + " ")

file.close()
