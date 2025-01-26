"""unpack a multi-verse tuple and use the distances to make a shape"""
import turtle as t  #channel turtle energy
draw = ((150,90,125),(100,-90,-75),(60,90,25),(-150,90,-25))    #multiverse tuplke
for i in range(3):  #Iterate over the first layer of the tuple
    (distance, angle, distance2) = draw[i]  #extract the juices from the inner tuple
    t.forward(distance) #move forward the value in the first index
    t.left(angle)   #turn left the value in the second index
    t.forward(distance2)    #go forward the amount in the third index
lol = input("press ENTER to quit")  #exit at users will