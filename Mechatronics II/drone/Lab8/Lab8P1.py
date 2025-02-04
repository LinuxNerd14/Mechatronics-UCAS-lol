"""
 curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)

Fly to x2 y2 z2 in a curve via x2 y2 z2. Speed defines the traveling speed in cm/s.

    Both points are relative to the current position
    The current position and both points must form a circle arc.
    If the arc radius is not within the range of 0.5-10 meters, it raises an Exception
    x1/x2, y1/y2, z1/z2 can't both be between -20-20 at the same time, but can both be 0.
"""
#tello ssid == TELLO-62594A
from djitellopy import Tello
import time
tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
tello.takeoff()         #take off
time.sleep(1)           #all time commands from her on is to make sure the drone isn't being overloaded
tello.move_up(int(100)) #up 100cm
time.sleep(1)
tello.curve_xyz_speed(70, -70, 0, 140, 0, 0, 60)    #idk how this works
time.sleep(1)
tello.move_up(100)  #up another 100cm
time.sleep(5)
tello.curve_xyz_speed(70, -70, 0, 140, 0, 0, 60)    #idk how this works
time.sleep(1)
tello.rotate_counter_clockwise(180) #rotate left 180
time.sleep(1) 
tello.land()        #land