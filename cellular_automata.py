# Created by: Noel Angelo Pastrana and Patricia Nicole Martinez
# References:
# https://www.geeksforgeeks.org/convert-python-list-to-numpy-arrays/
# https://devenum.com/how-to-create-a-2d-python-array/#:~:text=How%20to%20Create%20a%202D%20Python%20array%201,...%206%206.%20Create%202D%20using%20NumPy%20Module
# https://www.w3schools.com/python/matplotlib_intro.asp
# https://www.youtube.com/watch?v=vhHuHXY04no

import matplotlib.pyplot as plt
import numpy as np

def convertToBinary(val):
    initial = 128
    i = 0
    arr = []
    while i < 8:
        if val >= initial:
            val -= initial
            arr.append(1)
        else:
            arr.append(0)
        initial = initial // 2
        i += 1
    return arr


val = int(input("Enter value from [0, 255]: "))
binary_pattern = convertToBinary(val)
# print(binary_pattern)

# Pattern
arr = [ [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]]

arr = np.array(arr)
# print(arr)

# Determining Size
column = 21
row = column // 2 + 1

# To Visualize
visual = [[0 for i in range(column + 2)] for j in range(row)]

# Input first row of the cellular automata
first_row = list(input("Input " + str(column + 2) +" digits, 1 or 0, ex. 00000000000100000000000: "))
for i in range(column + 2):
    visual[0][i] = int(first_row[i])

visual = np.array(visual)
print(visual)

print()

for i in np.arange(0, row - 1):
    for j in np.arange(0, column):
        for k in range(8):
            if np.array_equal(arr[k, ], visual[i, j: j + 3]):
                print(arr[k, ], visual[i, j: j + 3], binary_pattern[k])
                visual[i + 1, j + 1] = binary_pattern[k]


# To be graphed
print()
# print(visual)

# Graph
plt.imshow(visual[:, 1:column + 1], cmap='Greys', interpolation='nearest')
plt.title("Elementary Cellular Automata Rule " + str(val))
plt.show()