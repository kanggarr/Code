import random

name = ['Xingui', 'Raiden', 'Eula', 'Riktor', 'Aleister', 'Vincent']
print(name)
ans = [0, 0, 0, 0, 0, 0]
for i in range(1, 1001):
    r1 = random.random()
    r2 = random.random()
    if r1 <= 0.1:
        ans[0] += 1
    elif r1 <= 0.35:
        if r1 >= 0.5:
            ans[1] += 1
        else:
            ans[2] += 1
    elif r1 <= 0.65:
        if r2 >= 0.5:
            ans[3] += 1
        else:
            ans[4] += 1
    else:
        ans[5] += 1
    if i % 100 == 0:
        print(ans)
        if 0.3499 >= ans[5]/sum(ans) and ans[5]/sum(ans) <= 0.3501:
            print(ans[5]/sum(ans))
            print(i)
            exit()
