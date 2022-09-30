a = int(input())
for colum in range(a):
    for row in range(a,a-(colum+1),-1):
        print(row,end=' ')
        row -= 1
    print('')