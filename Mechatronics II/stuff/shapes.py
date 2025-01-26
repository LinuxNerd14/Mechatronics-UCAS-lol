""" takes user input to determin the size of shapes and how many sides that shape has"""
import turtle as t  # channel turtle energy
length = int(input("Side lengths == ")) #ask for length
sides = int(input("Side count == "))    # ask for the amount of sides
for i in range(sides):  #loop as many times as sides in order to close the shape
    t.fd(length)    # move forward desired length
    t.rt(360/sides) #turn right 360/n degrees