num = 2500

left = 0; right = num
ans = right / 2

while abs(ans**2 - abs(num)) > 0.0001 and ans <= right:
    ans = (left + right) / 2.0
    if ans**2 < num:
        left = ans
    else:
        right = ans
    print(ans)

print('The square root of', num, 'is', ans)