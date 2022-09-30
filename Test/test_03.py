'''
max = 10 # max number
n = 5 # number
'''
import random

ans = [0, 0, 0, 0, 0, 0]
for i in range(1, 1001):
    r = random.random()
    r1 = random.random()
    if r <= 0.1:
        ans[0] += 1
    elif r <= 0.35:
        if r1 >= 0.5:
            ans[1] += 1
        else:
            ans[2] += 1
    elif r <= 0.65:
        if r1 >= 0.5:
            ans[3] += 1
        else:
            ans[4] += 1
    else:
        ans[5] += 1
print(ans)
