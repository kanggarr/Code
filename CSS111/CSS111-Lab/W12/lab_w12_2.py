# # May the force be with me


# def maytheforcebewithme():
#     print("May the force be with me")


import random

list_number = []
while len(list_number) < 10:
    random_number = random.randint(0, 9)
    if random_number not in list_number:
        list_number.append(random_number)
print(list_number)

while True:
    number = int(input('>'))
    if number < 0:
        exit()
    list_number.remove(number)
    list_number.insert(0, number)
    print(list_number)
