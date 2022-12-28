
number = int(input("Enter a number the Prime Number : "))
number_range = range(number)

for i in number_range:
        i += 2
        while number % i == 0:
                        print(i, " ")
                        number /= i
if number > 2:
    print(number)