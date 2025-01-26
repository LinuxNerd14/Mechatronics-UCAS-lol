"""unpack a tuple and do carp with it"""
import turtle as t  #channel turtle energy
draw = ((130,104,50,'blue'),(200,164,60,"red"),(330,140,20,"green"),(30,144,40,'yellow'),(-90,94,100,'black')) #two layer list for the stars
for i in draw:  # iterte over the first layer to extract the information for each star
    x, y, size, color = i   #unpack the second layer into its respective values
    t.penup()   #Pen up for teleportation
    t.setposition(x, y) #set position for the start of the star
    t.pendown() #pend down to begin drawing ther star
    t.fillcolor(color)  #set the color to the appropriate color for the star
    t.begin_fill()  #begin filling the star with the right color
    for i in range(5):  #loop five times for each line in the star
        t.forward(size) #go forward the size amount specified in the unpacked tuple
        t.left(144) #go left 144 for the star
    t.end_fill()    #end the fill for teleportation
lol = input("Press ENTER to quit")  #exit