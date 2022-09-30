h_in = int(input("hour_in="))
m_in = int(input("minute_in="))
h_out = int(input("hour_out="))
m_out = int(input("minute_out="))

m = m_out - m_in
h = h_out - h_in
money = 0

if m <= 15 and h == 0:
    print("0")
elif m > 15 or h > 1:
    if m > 0:
        m = 1
        t = h + m
        if t > 6:
            print("200")
        elif t <= 3:
            money = t * 10
            print(money)
        else:
            t = t - 3
            money = 30 + t * 200
            print(money)
    elif m == 0:
        m = 0
        t = m + h
        if t > 6:
            print("200")
        elif t <= 3:
            money = t * 10
            print(money)
        else:
            t = t - 3
            money = 30 + t * 20
            print(money)
