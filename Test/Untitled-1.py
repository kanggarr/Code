p1,p2,p3,n1,n2=[int(i) for i in input().split()]
a=0
for i in range(int(n1),int(n2)+1):
    if i==int(p1):
        a+=10000
    if i%100==int(p2):
        a+=25
    if i%1000==int(p3):
        a+=100
print(a)