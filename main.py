
# creating 2 Dimensional Array by user input values
import numpy as np

matrix = []

row = int(input("Enter numbers of rows : "))
column = int(input("Enter numbers of columns : "))

for i in range(row):
    a = []
    for j in range(column):
        val = int(input("Enter the value : "))
        a.append(val)
    matrix.append(a)
arr = np.array(matrix)
for i in range(row):
    for j in range(column):
        print("\t", arr[i][j], end=" ")
    print()
print(type(arr))

