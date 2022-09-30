
import math

r = float(input("radius:"))

if r < 0:
    print("r < 0")
else:
    # r >= 0
    area = math.pi * r ** 2
    print("area:", "{:.5f}".format(area))
