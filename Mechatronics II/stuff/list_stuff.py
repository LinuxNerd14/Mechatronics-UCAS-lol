"""take a nested tuple ans print the side lengths to make a spiral"""
import turtle as t #channel turtle energy
draw = ((200,175,150), (125,100,75), (50,25,5), (150,100,225))  #nested tuples of side lenghts
for i in range(3):  # for loop to iterate over the first layer of the tuple
    for ii in range(3): # iterate over the iner values
        t.fd(draw[i][ii])   #go forward the current value inside the scond tuple layer
        t.rt(90)    # turn right 90