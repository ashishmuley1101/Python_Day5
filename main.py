import math

BASE_VALUE = 2
exponent_value = int(input("Enter the exponent value : "))

print("Number : ", exponent_value)

if (exponent_value >= 0) and (exponent_value < 31):
        result = (math.pow(exponent_value, BASE_VALUE))
        print("Power 2 for exponent ", exponent_value, " is : ", result)
else:
        print("Enter Exponent value in between 0 to 30")
