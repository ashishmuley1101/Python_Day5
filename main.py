

number = int(input("Enter the Harmonic Number : "))
number_range = range(number)
harmonic_number = 0

if number == 0:
        print("Enter the valid Harmonic Number..!")
else:
        for i in number_range:
                i += 1
                harmonic_number += (1/i)
        print("Harmonic number for ", number, " is : ", round(harmonic_number, 2), type(harmonic_number))
