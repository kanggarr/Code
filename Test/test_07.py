t = []
a = [int(i) for i in input().split()]
t.append((a[1]-a[0])-1)
t.append((a[2]-a[1])-1)
print(max(t))