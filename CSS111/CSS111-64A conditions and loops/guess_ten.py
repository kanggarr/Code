import random

print("what is my magic number (1 - 100)")

mynumber = random.randint(1, 100)

loop = 0
x = 0
while loop < 6:
    a = int(input())
    if (a == mynumber):
        x = 1
        break
    elif(a < mynumber):
        print("too high")
    else:
        print("too low")

print("yes ,it's" if x == 1 else "no, my magic number is ", mynumber)
