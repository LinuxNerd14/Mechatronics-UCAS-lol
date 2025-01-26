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



draw = (('cirlce', 'red', 100, 50, 50),('other', 'yellow', 100, 10, 0, 12))
t.speed(0)
circledraw('yellow', 100, 10, 10)
squaredraw('green', 100, -40, -40)
stardraw('black', 100, 50, 0)
triangledraw('violet', 100, 100, 20)


lol = input("Press ENTER to quit")
