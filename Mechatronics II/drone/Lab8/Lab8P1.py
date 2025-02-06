"""
 curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)

Fly to x2 y2 z2 in a curve via x2 y2 z2. Speed defines the traveling speed in cm/s.

    Both points are relative to the current position
    The current position and both points must form a circle arc.
    If the arc radius is not within the range of 0.5-10 meters, it raises an Exception
    x1/x2, y1/y2, z1/z2 can't both be between -20-20 at the same time, but can both be 0.
"""
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
time.sleep(1)
tello.curve_xyz_speed(-70, 70, 0, -140, 0, 0, 60)    #idk how this works
time.sleep(1)
tello.rotate_counter_clockwise(180) #rotate left 180
time.sleep(1) 
tello.land()        #land

#   Figure 8 Pattern

tello.takeoff()

def figure8():                                          #flys a figure 8 when called
    tello.curve_xyz_speed(70, -70, 0, 140, 0, 0, 60)
    time.sleep(1)
    tello.curve_xyz_speed(-70, 70, 0, -140, 0, 0, 60)
    time.sleep(1)
    tello.curve_xyz_speed(-70, 70, 0, -140, 0, 0, 60)
    time.sleep(1)
    tello.curve_xyz_speed(70, -70, 0, 140, 0, 0, 60)
    time.sleep(1)
    
figure8()
tello.move_up(100)
tello.rotate_counter_clockwise(180) #rotate left 180
tello.land()
    """
    
    
"""
from djitellopy import Tello
import time
x1=(70,70,70,70)
y1=(70,70,70,70)
z1=(0,0,0,0)
x2=(140,140,140,140)
y2=(0,0,0,0)
z2=(0,0,0,0)
s=(60,60,60,60)
#listy = zip(x1, y1, z1, x2, y2, z2, s)
tello = Tello()         #initiate tello drone
tello.connect(False)    #connect in an unreliable way
time.sleep(1)
tello.takeoff()         #take off
for i in zip(x1, y1, z1, x2, y2, z2, s):    #loope over zip while zipping it
    X1, Y1, Z1, X2, Y2, Z2, S = i   #unpack the zip that was just done
    time.sleep(3.5) #give the drone time to figure itself out
    tello.curve_xyz_speed(X1, Y1, Z1, X2, Y2, Z2, S)    #excecute curve based on tuple
print("HERE")   #Land mark for progress
time.sleep(1)   #wait
tello.land()    #land
"""
from djitellopy import Tello
import time
tello = Tello()
def windup():
    for i in range(6):
        time.sleep(1)
        tello.move_forward(100)
        time.sleep(1)
        tello.move_up(20)
        time.sleep(1)
        tello.move_left(100)
        time.sleep(1)
        tello.move_up(20)
        time.sleep(1)
        tello.move_backward(100)
        time.sleep(1)
        tello.move_up(20)
        time.sleep(1)
        tello.right(100)
        time.sleep(1)
        tello.move_up(20)
        time.sleep(1)
def winddown():
    for i in range(6):
        time.sleep(1)
        tello.move_forward(100)
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.move_left(100)
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.move_backward(100)
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.right(100)
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
tello.connect(False)    #connect in an unreliable way
time.sleep(1)
tello.takeoff()         #take off
time.sleep(1)
windup()
winddown()
time.sleep(1)
tello.land()