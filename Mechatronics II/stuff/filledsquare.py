"""make a square that is filled blue with side lengths 100"""
import turtle as t # channel turtle energy
t.fillcolor('blue') # get ready to fill blue
t.begin_fill()  #start filling the square
for i in range(4): # loop four times to make the sides of the square
        t.fd(100)   # side lengths == 100
        t.rt(90)    #turn right 90 degrees
t.end_fill() #end filling the square