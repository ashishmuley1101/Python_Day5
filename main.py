import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, -3, 8, -5, 4 ])

for i in range(0, 6):
    first_num = a[i]
    for j in range(i+1, 6):
        second_num = a[j]
        for k in range(j+1, 6):
            third_num = a[k]
            result = first_num + second_num + third_num
            if result == 0:
                print(first_num, second_num, third_num, "= 0")






