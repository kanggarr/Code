import random

name = ['Xingui', 'Raiden', 'Eula', 'Riktor', 'Aleister', 'Vincent']
print(name)
ans = [0, 0, 0, 0, 0, 0]
for i in range(1, 1001):
    rate_1 = random.random()
    rate_2 = random.random()
    if rate_1 <= 0.1:
        ans[0] += 1
    elif rate_1 <= 0.35:
        if rate_1 >= 0.5:
            ans[1] += 1
        else:
            ans[2] += 1
    elif rate_1 <= 0.65:
        if rate_2 >= 0.5:
            ans[3] += 1
        else:
            ans[4] += 1
    else:
        ans[5] += 1
    if i % 100 == 0:
        print(ans)
