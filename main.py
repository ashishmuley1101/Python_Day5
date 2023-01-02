
# Calculating the wind chill using formula
import math

temp = float(input(" Enter temperature in Fahrenheit : "))
wind_speed = int(input("Enter wind speed in miles per hour : "))

def wind_chill(f, ws):

    w = 35.74 + 0.62158 * f + (0.4275 * f - 35.75) * math.pow(ws, 0.16)
    print("National Weather Service defines the effective temperature : ", w)

if ( abs(temp)> 50 or wind_speed > 120 or wind_speed < 3):
    print("Enter correct input")
else:
    wind_chill(temp, wind_speed)