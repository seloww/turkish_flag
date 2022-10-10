import turtle as tos
win = tos.Screen()


win.setup(width=720,height=420)
win.bgcolor("red")
tos.speed(9999999999999999999)


# First circle

tos.up()
tos.goto(-100, -100)
tos.color("white")
tos.begin_fill()
for s in range(360):
    tos.forward(2)
    tos.left(1)
tos.end_fill()

# Second circle for cresent

tos.goto(-65,-70)
tos.color('red')
tos.begin_fill()
for s in range(360):
    tos.forward(1.5)
    tos.left(1)
tos.end_fill()

# Preparation for star
tos.goto(30, 40)
tos.fillcolor("white")
tos.begin_fill()

# Repeating triangle drawing for star
for i in range(5):
    tos.forward(120)
    tos.right(144)
tos.end_fill()
tos.done()