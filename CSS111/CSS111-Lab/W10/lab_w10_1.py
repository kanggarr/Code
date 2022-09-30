

def sum_is_even(a, b):
    for i in range(a+1, b):
        summary_digit = 0
        for digit in str(i):
            summary_digit += int(digit)
        if summary_digit % 2 == 0:
            print(i, end=",")
    print()


sum_is_even(6, 20)
sum_is_even(95, 110)
sum_is_even(990, 1010)
sum_is_even(89, 101)
