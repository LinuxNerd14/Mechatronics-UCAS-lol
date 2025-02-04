#tello ssid == TELLO-62594A
from djitellopy import Tello
import time

tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
tello.takeoff()         #take off
time.sleep(3)           #wait for the drone to be ready
tello.flip_left()       #flip to the left
time.sleep(3)           #wait for the drone to be ready
tello.flip_right()      #flip to the right
time.sleep(3)           #wait for the drone to be ready
tello.flip_forward()    #flip to the forward
time.sleep(3)           #wait for the drone to be ready
tello.flip_backward()   #flip to the back
time.sleep(3)           #wait for the drone to be ready
tello.land()            #land