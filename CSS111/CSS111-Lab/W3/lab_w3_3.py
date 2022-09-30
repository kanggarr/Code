
import math

a, b, c = [float(r) for r in input().split()]
var_x = b ** 2 - 4 * a * c 

if var_x == 0:
    x1 = -b / (2*a)
    print(x1)
elif var_x > 0:
    x2 = (-b + math.sqrt(var_x)) / (2*a)
    x3 = (-b - math.sqrt(var_x)) / (2*a)
    print(x2, x3)
else:
    print("No Soution in real number")
