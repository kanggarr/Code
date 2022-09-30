
import math

x = int(input("number:"))

f = x*math.pi - 3/x + 7 * x**5 - math.log10(x) - math.e ** (-x)
print("value x :", x, "value f:", f)

"""
:.6f จุดทศนิยม 6 ตำแหน่ง
:.4f จุดทศนิยม 4 ตำแหน่ง
"""
