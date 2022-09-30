max = 10
n = 5
for i in range(1, max+1):
    if i < n:
        k = max+1
    else:
        k = n+1
    print("Multplication table of", i)
    for j in range(1, k):
        print(i*j, end=" ")
    print()
