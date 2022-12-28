
year = int(input("Enter Year : "))

print("Year : ", year)

if year == 0:
        print("Enter the valid year..!")

elif (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        print("Specified year is a leap year.")

else:
        print("Specified year is not a leap year.")
