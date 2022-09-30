import random

print("What is my magic number (1 to 100) ?")
mynumber  = random.randint(1, 100)
ntries    = 1
yourguess = -1

while ntries < 7 and _______________________ :
    msg = str(ntries) + ">> "
    if (ntries == 6) :
        ___________________________
    yourguess = int(input(msg))
    if _____________________ :
        print("--> too high")
    ________________________ :
        print("--> too low")
    ntries += 1
    
if _______________________ :
    print("Yes! it's", mynumber)
else:
    print("Sorry! my number is", mynumber)
