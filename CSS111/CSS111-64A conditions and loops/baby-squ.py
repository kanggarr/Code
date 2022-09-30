a = 2500
x = 100

while x**2 != a:
  x = (x + a/x) / 2
  print(x)

print("sqrt(", a, ") =", x)

"""
a = 2500
x = a / 4

while abs(x**2 - a) > 0.0001:
  x = (x + a/x) / 2
  print(x)

print("sqrt(", a, ") =", x)
"""