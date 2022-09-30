import turtle
x = turtle.Turtle()
def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle + 15)
for i in range(24):
    square(90)
turtle.done()
#input('Press [Enter] to quit')