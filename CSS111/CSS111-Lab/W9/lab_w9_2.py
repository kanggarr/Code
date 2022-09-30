'''

import math


def trigonometry(x):
    var_sin_x = round(math.sin(math.radians(x)), 3)
    var_cos_x = round(math.cos(math.radians(x)), 3)
    return x, var_sin_x, var_cos_x


for i in range(0, 3601, 225):
    print(trigonometry(i))


'''
# ของเพื่อน 444 รวิษฏา
'''

import math


def trigonometry(x):
    math.radians(x)
    sin = round(math.sin(x), 3)
    cos = round(math.cos(x), 3)
    return(sin, cos)


value_sin = []
value_cos = []
x = 0
print("Degree", end=" ")
for i in range(1, 18):
    sin, cos = trigonometry(x)
    value_sin.append(sin)
    value_cos.append(cos)
    print(x, end=" ")
    x += 22.5


print("\nsin", value_sin)
print("cos", value_cos)


'''