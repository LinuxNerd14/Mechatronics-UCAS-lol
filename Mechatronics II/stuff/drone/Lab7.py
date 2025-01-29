#tello ssid == TELLO-62594A
from djitellopy import Tello
import time

tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
tello.takeoff()         #take off
time.sleep(1)           #allow the drone to process
tello.move_up(200)
time.sleep(1)           #allow the drone to process
tello.move_forward(300)
time.sleep(1)           #allow the drone to process
tello.move_left(300)
time.sleep(1)           #allow the drone to process
tello.move_back(300)
time.sleep(1)           #allow the drone to process
tello.move_right(300)
tello.land()            #land