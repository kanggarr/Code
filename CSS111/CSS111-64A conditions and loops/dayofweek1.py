d = int(input("วันที่  = "))
m = int(input("เลขเดือน = "))
y = int(input("ปี (ค.ศ.) = "))

if m < 3 :
    m += 12
    y -= 1
c = y // 100
k = y % 100
w = (d + 26*(m+1)//10 + k + k//4 + c//4 + 5*c) % 7

if w == 0 :
    print("เสาร์")
if w == 1 :
    print("อาทิตย์")
if w == 2 :
    print("จันทร์")
if w == 3 :
    print("อังคาร")
if w == 4 :
    print("พุธ")
if w == 5 :
    print("พฤหัสบดี")
if w == 6 :
    print("ศุกร์")