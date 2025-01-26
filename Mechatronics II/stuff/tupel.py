""" This program makes a spiral with a tuple"""
import turtle as t    #import turtle energy
x = True # Give them a chance
for i in range(100): #loop 100 times
    t.circle(10*i) #make a circle of multiplicty of 10
    t.up()  #move up
    t.sety((10*i)*(-1)) #sets y to a new position
    t.down() # move down
x = input("Press any key to exit: ") #Exit when done 