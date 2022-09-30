
x = input("Please enter a positive integer value:")
x = int(x)



for i in range(x):
    #y = []
    print('|' + (i) * ' ' + '\\')
    #print((i-1) + '\\' + (i) * ' ' + '|')
    #print((i) * ' ' + '\\' + ' ' + '|') 
print("    |<") # หัวตรงกลาง
for i in range(x):
    print('|' + (x-i) * ' ' + '/')



'''
x = input("Please enter number: ")
print("1     1") 
print(" 2   2 ")
print("  3 3  ")
print("   4   ")
print("  5 5  ")
print(" 6   6 ")
print("7     7")
'''