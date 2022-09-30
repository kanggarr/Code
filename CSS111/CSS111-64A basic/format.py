w = 4; h = 5
area = w * h

sentence = 'The area of {} x {} is {}.'.format(w, h, area)
print(sentence)

print('And {:.1f} x {:5.2f} is {:.4e}.'.format(w, h, area))