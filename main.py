
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second numbers : "))
num3 = int(input("Enter the third numbers : "))

if num1 > num2 and num1 > num3:
    print("The largest number is : ",num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is : ", num2)
elif num3 > num1 and num3 > num2:
    print("The largest number is : ", num3)
else:
    print("The numbers are same.")






