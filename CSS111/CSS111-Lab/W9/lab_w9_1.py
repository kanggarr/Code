'''

def triangle(nline, diff):
    for j in range(1, nline*diff, diff):
        print("*"*j)


triangle(4, 3)
triangle(5, 2)
'''

'''
def triangle(nline, diff):
    for x in range(1, nline+1):
        print("*" * (1 + diff*(x - 1)), end="")
        print(" ")


triangle(4, 3)
triangle(5, 2)
'''
