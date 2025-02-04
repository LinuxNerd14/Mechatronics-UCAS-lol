#tello ssid == TELLO-62594A
from djitellopy import Tello
import time
tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
tello.takeoff()         #take off
tello.move_up(int(200))  #climb to altitude
shufly = ((200, 90, 30), (200, 90, 20), (200, 90, 30), (200, 90, 20))
def fly_direct(length, angle, height):
    tello.move_forward(int(length)) #forwad
    tello.rotate_counter_clockwise(int(angle))  # left
    tello.move_up(int(height))  #up
    return 1    #error handling

for i in range(len(shufly)):
    x = fly_direct(shufly[i][0], shufly[i][1], shufly[i][2])    #fly here
    if x == 1:
        pass    #if function work good pass
    else:       # if function excecutes bad land
        print("HELP ME I DONT KNOW WHAT THAT IS")
        tello.land()
tello.land()    #land