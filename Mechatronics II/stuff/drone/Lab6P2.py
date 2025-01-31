#tello ssid == TELLO-62594A
from djitellopy import Tello
import time
tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
tello.takeoff()         #take off
tello.move_up(300)  #climb to altitude
while True:
    x = input('Flip == ')
    if x == str("forward"): #flip forward
        tello.flip_forward()
    elif x == str("backward"):
        tello.flip_back()
    elif x == str('left'):  #Flip left
        tello.flip_left()
    elif x == str('right'): #Flip right
        tello.flip_right()
    else:   #panic
        print("IDK WHAT THAT IS HELP ME IDIOT") #help me pls
        tello.land()    #emergency land
        break   #stop
tello.land()    #land