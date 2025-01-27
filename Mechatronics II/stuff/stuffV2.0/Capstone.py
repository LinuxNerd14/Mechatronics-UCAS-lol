import turtle as t

def circledraw(color, size, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.fillcolor(str(color))
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()

def squaredraw(color, size, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.fillcolor(str(color))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()

def stardraw(color, size, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.fillcolor(str(color))
    t.begin_fill()
    for i in range(5):  #loop five times for each line in the star
        t.forward(size) #go forward the size amount specified in the unpacked tuple
        t.left(144) #go left 144 for the star
    t.end_fill()
    t.penup()

def triangledraw(color, size, x, y):
     t.penup()
     t.setposition(x, y)
     t.pendown()
     t.fillcolor(str(color))
     t.begin_fill()
     for i in range(3):
        t.forward(size)
        t.left(120)
     t.end_fill()
     t.penup()


t.hideturtle()
draw = (('cirlce', 'red', 100, 50, 50),('other', 'yellow', 100, 10, 0, 12))
t.speed(0)
for ii in range(13):
    for i in range(15):
        squaredraw('red', 100, (100*i)-600, (100*ii)-600)
for ii in range(5):
    for i in range(10):
        stardraw('blue', 40, (50*i)-500, (-50*ii)+400)
lol = input("Press ENTER to quit")
