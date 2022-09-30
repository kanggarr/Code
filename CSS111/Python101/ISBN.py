a = [int(i) for i in input()]
b = [10,9,8,7,6,5,4,3,2]
c = []
for i in range(9):
    c.append(a[i]*b[i])
d = 11 - (sum(c)%11)
if d == 11:
    a.append(0)
else: 
    a.append(d)
print("".join([str(i) for i in a]))
