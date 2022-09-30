import random

name = ['Xingui', 'Raiden', 'Eula', 'Riktor', 'Aleister', 'Vincent']
rate_all = random.random()
rate_all = rate_all*100  # เพื่อให้เป็น 100%
print(rate_all)  # rate ออกมาเป็นเท่าไร
if rate_all <= 10:
    print("Xinhui")
elif rate_all <= 35:
    rate_1 = random.random()
    rate_1 = rate_1 * 100
    if rate_1 <= 50:
        print("Raiden")
    else:
        print("Eula")
elif rate_all <= 65:
    rate_2 = random.random()
    rate_2 = rate_2*100
    if rate_2 <= 50:
        print("Riktor")
    else:
        print("Aleister")
else:
    print("Vincent")
