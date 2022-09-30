

def calculate(text):
    text_split = text.split()

    if text_split[0] == '-':
        vars = float('-' + text_split[0])

    else:
        vars = float(text_split[0])

    for i in text_split[1:]:
        if i.isnumeric():
            i = float(i)
            if operator == '+':
                vars = vars + i
            elif operator == '-':
                vars = vars - i
            elif operator == '*':
                vars = vars * i
            elif operator == '/':
                vars = vars / i

        elif i.isnumeric() == 0:
            operator = i

    print(vars)



'''
def calculate(text):
    number = []
    operator = []
    ans = 0
    text_split = text.split()
    if len(text_split) == 1:
        return print(text)
    for i in text_split:
        if i in "+-*/":
            operator.append(i)
        else:
            number.append(float(i))
    if operator[0] == '+':
        ans += number[0] + number[0+1]
    if operator[0] == '-':
        ans += number[0] - number[0+1]
    if operator[0] == '*':
        ans += number[0] * number[0+1]
    if operator[0] == '/':
        ans += number[0] / number[0+1]
    for i in range(1,len(operator)):
        if operator[i] == '+':
            ans += number[i+1]
        if operator[i] == '-':
            ans -= number[i+1]
        if operator[i] == '*':
            ans *= number[i+1]
        if operator[i] == '/':
            ans /=  number[i+1]
    return print(ans)
'''


calculate("50")
calculate("1023.5 + 4 - 17")
calculate("50 + 2 * 3 / 2")
