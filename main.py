
# Calculating Quadratic Equation using I/P value a, b and c
import math

a = int(input(" Enter a : "))
b = int(input(" Enter b : "))
c = int(input(" Enter b : "))

def root(a, b, c):

    delta = (b * b - 4 * a * c);
    x1 = (-b + math.sqrt(delta)) / (2 * a);
    x2 = (-b - math.sqrt(delta)) / (2 * a);

    print("Root of x1 : ", round(x1,2))
    print("Root of x2 : ", round(x2,2))

root(a, b, c)


