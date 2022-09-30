max = 8
n = 6
for i in range(1, max+1):
    print("Multplication table of", i)
    if i < 5:
        for j in range(1, max+1):
            print(i*j, end=' ')
        print()
    else:
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()
