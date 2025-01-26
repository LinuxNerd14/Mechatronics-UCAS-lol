"""takes a multui diomensialnal tuple and zips it up then move those value amounts"""
import turtle as t  #channel turtle energy 
x=(100,100,100,100) #table of first firward values
turn=(90,90,90,90)  #table of turn angles amounts for turning left
y=(125,135,145,155) #table of second forward values
for x, turn, y in zip(x,turn,y):    #zip x turn and y into a tuple then use those tuples to draw
    t.forward(x)    #GO FORWARD x amounts
    t.left(turn)    #turn left turn amounts
    t.forward(y)    #go forward y amount
lol = input("Press ENTER to quit")  #release the user