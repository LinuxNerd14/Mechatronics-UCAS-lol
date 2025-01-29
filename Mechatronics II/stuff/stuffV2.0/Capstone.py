""" Makes a list the size of your mom full of information for item type and parameters for said item.
    Then iterate over every item in that list of tuples and draw said items.
    The items included is a semi-accurate US flag and yellow and green triangles graphed in a exponetial form with a violet circle
    The perameters for the shapes/itmes are arranged as demonstrated
    (1, "color", size, x poition, y position)
    the very first Index is the chape identifyer
    1 == square, 2 == star, 3 == triangle, 4 == cirlce 
"""
import turtle as t
import random
import math
# takes standard parameters and draws a circle
def circledraw(color, size, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.fillcolor(str(color))
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()
#takes standard parameters and draws a square
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
#takes standard parameters and draws a star
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
# takes standard parameter and draws a triangle
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

# set up the turtle for sonic levels of speed and the stealth of your dad
t.hideturtle()
draw = []   #This is the bery big list
t.speed(0)


# assemble the great list of commands
# the commented out sections of code behind the "item" is a reference for the shapes setting themselves

#makes the red backround for the flag
# this section will show how the list of commands is made and so the other sections will have no comments
for ii in range(13):    # the amount of shapes in the Y direction
    for i in range(21): # the amount of shapes in the X direction
        #squaredraw('red', 20, (i*20)-300, (ii*20)+100) example of how I made the shapes
        item = (1, 'red', 20, (i*20)-300, (ii*20)+100) # pack the parameters into a tuple
        draw.append(item)   #append the tuple to the GREAT LIST

# puts the white strips on the flag
for ii in range(6):
    for i in range(21):
        #squaredraw('white', 20, (i*20)-300, (ii*20*2)+120)
        item = (1, 'white', 20, (i*20)-300, (ii*20*2)+120)
        draw.append(item)

# puts the blue backround in the top left
for ii in range(7):
    for i in range(10):
        #squaredraw('blue', 20, (20*i)-300, (20*ii)+220)
        item = (1,'blue', 20, (20*i)-300, (20*ii)+220)
        draw.append(item)

# puts the stars on the flag, all 50
for ii in range(5):
    for i in range(10):
        #stardraw('white', 19, (i*28)-160, (ii*20)+260)
        item = (2,'white', 20, (i*20)-300, (ii*28)+230)
        draw.append(item)

# makes the green and yellow triangles drawn in a exponential graph
for i in range(10):
    x = i % 2
    if int(x) == 0:
        y = 'green'         #alternate the color depending on the even or odd
    else:
        y = 'yellow'
    #triangledraw(y, i*10, -100+((i*5)^4), -100+((i*5)^8))
    item = (3, y, i*10, -100+(i*10), -100+((i*10)^i))
    draw.append(item)
#circledraw('violet', 100, -200, -200)
item = (4,'violet', 100, -200, -200)
draw.append(item)
yes = input("Special Mode?(y/n): ")
print(draw)

# special mode :)
if yes == 'y':
    random.shuffle(draw)
    for i in range(30):
        x = i % 2
        if int(x) == 0:
            y = 'black'         #alternate the color depending on the even or odd               #FUNZIE TIME
        else:
            y = 'pink'
        #triangledraw(y, i*10, -100+((i*5)^4), -100+((i*5)^8))
        item = (3, y, i*10, -100+(i*10), -100+(1.2**i))
        draw.append(item)
else:
    pass

# reads the great list and depending on the number on the front of the nested tuiple it will draw a certain shape and pass the parameters for it in
# 1 == square, 2 == star, 3 == triangle, 4 == cirlce
#if the first var in x index is a certain value it will make a certain shape. It then takes the rest of the parameters into the appropriate function
for i in range(len(draw)):
    print(str(draw[i]))
    if draw[i][0] == 1: #squaredraw
        squaredraw(str(draw[i][1]), draw[i][2], draw[i][3], draw[i][4])
    elif draw[i][0] == 2: #stardraw
        stardraw(str(draw[i][1]), draw[i][2], draw[i][3], draw[i][4])
    elif draw[i][0] == 3:   #triangledraw
        triangledraw(str(draw[i][1]), draw[i][2], draw[i][3], draw[i][4])
    elif draw[i][0] == 4:   #circledraw
        circledraw(str(draw[i][1]), draw[i][2], draw[i][3], draw[i][4])
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nIT DIDNT PRINT OR READ RIGHT HELP ME HERE IS THE TUPLE THAT I CANT READ\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")    #PANIC IF THE ITEM DOESN"T MATCH ANYTHING
        print("LIST INDEX: ")
        print(str(i))
        print(draw[i])
lol = input("Press ENTER to quit")
