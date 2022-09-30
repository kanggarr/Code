number = int(input())
numberhex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
answer = ''
while(number > 0):
    index = number % 16
    number = number // 16
    answer += str(numberhex[index])
print(answer[::-1])
