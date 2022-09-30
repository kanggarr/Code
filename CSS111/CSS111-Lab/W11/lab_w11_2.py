# ab138g579b h54325b1 ab12b 54ab56
text_index = []
text_append = []
text_output = []


def check(input='0'):
    if input == '0':
        print("Invalid parameter")
    else:
        text = (''.join(filter(str.isdigit, input)))
        for i in text:
            text_int = int(i)
            text_append.append(text_int)
        text_sort = sorted(text_append)
        for j in range((len(text_sort))-1):
            if text_sort[j] == text_sort[j+1]:
                text_output.append(text_sort[j])
                break
            else:
                pass
        if len(text_output) == 0:
            return ('None')
        else:
            return text_output


print(check())
