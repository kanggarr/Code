# ab138g579b h54325b1 ab12b 54ab56
input = "ab138g579b"
text = (''.join(filter(str.isdigit, input)))
text_index  = []
text_append = []
text_output = []
for i in text:
    text_int = int(i)
    text_append.append(text_int)
text_sort = sorted(text_append)
for j in range((len(text_sort))-1):
    if text_sort[j] == text_sort[j+1]:
        if text_sort[j] in text_output:
            pass
        else:
            text_output.append(text_sort[j])
    else:
        pass
if len(text_output) == 0:
    print("None")
else:
    print(text_output)
