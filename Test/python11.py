import math

Hour = int(input())
Min = int(input())

print("ชัวโมงละ 30 บาท")


def price(Hour, Min):
    convert = math.ceil(Min/60)
    value = (Hour+convert) * 30
    print("ราคา", value, "บาท")


price(Hour, Min)
