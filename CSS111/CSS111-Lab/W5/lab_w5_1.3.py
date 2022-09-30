max, n = input("Enter two inputs here:").split()
max = int(max)
n = int(n)
for i in range(1, max+1):
    print("Multiplication table of", i)
    if i < 5:
        for j in range(1, max+1):
            print(i*j, end=' ')
        print()
    else:
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()
