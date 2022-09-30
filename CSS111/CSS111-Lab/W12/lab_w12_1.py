# # May the force be with me


# def maytheforcebewithme():
#     print("May the force be with me")


def mypi(n):
    var1 = 3
    var2 = 2
    for i in range(n):
        var3 = 4/(var2*(var2+1)*(var2+2))
        if i % 2 == 0:
            var1 += var3
        else:
            var1 -= var3
        var2 += 2
    return var1


for i in range(1, 31):
    print(mypi(i))

