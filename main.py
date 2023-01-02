
# Calculating distance between two points from the origin.
import math

point_x = int(input(" Enter the point x : "))
point_y = int(input(" Enter the point y : "))

def distance_cal(x, y):
    result = math.sqrt(x*x + y*y)
    return result

distance = distance_cal(point_x, point_y)

print("Distance for the origin is  : ", round(distance, 2))