import numpy as np
import csv



a=[]
b=[]
with open('input.csv',newline='') as file:
    data_reader = csv.reader(file, delimiter=' ')
    for row in data_reader:
        a.append(int(row[0]))
        b.append(int(row[-1]))
# test case
#a = [1,2,2,2,3,26,6,1]
#b=[2,3,3,2,1,4,2,1]


# sort both lists
sorted_a = np.sort(a)
sorted_b = np.sort(b)
# built difference
list_distance = np.sum(np.abs(sorted_a-sorted_b))
print(list_distance)
# similarity score
b_numbers, counts = np.unique(sorted_b,return_counts=True)
look_up  =dict(zip(b_numbers, counts))
i = 0
similarity_index = 0
for number in sorted_a:
    if number in look_up:
        multiplier = look_up[number]
        similarity_index += number * multiplier
print(similarity_index)
print('Yeah')