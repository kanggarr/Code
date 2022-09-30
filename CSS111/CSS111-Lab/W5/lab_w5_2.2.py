import random

name = ['Xingui', 'Raiden', 'Eula', 'Riktor', 'Aleister', 'Vincent']
print(name)
rateall = random.random()
rateall = rateall*100
print(rateall)
ratesub = random.random()
ratesub = ratesub*100
print(ratesub)
if rateall <= 10:
    print("Xinggui")
elif rateall <= 35:
    if ratesub <= 50:
        print("Raiden")
    else:
        print("Eula")
elif rateall <= 65:
    if ratesub <= 50:
        print("Riktor")
    else:
        print("Aleister")
else:
    print("Vincent")
