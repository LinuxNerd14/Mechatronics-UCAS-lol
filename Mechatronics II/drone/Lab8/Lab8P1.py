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
"""
from djitellopy import Tello
import time
tello = Tello()
time.sleep(1)
def windup():                       # moves up slowley whilst drawing a a square: repeats 6 times
    for i in range(3):
        time.sleep(3)               #sleep before every command to the drone
        tello.move_forward(50*(i+1))     #squre draw
        time.sleep(1)
        tello.move_up(20)           #move up
        time.sleep(1)
        tello.move_left(50*(i+1))        #square draw
        time.sleep(1)
        tello.move_up(20)           #move up
        time.sleep(1)
        tello.move_back(50*(i+1))    #square draw
        time.sleep(1)
        tello.move_up(20)           #move up
        time.sleep(1)
        tello.move_right(50*(i+1))            #square draw
        time.sleep(1)
        tello.move_up(20)           #move up
        time.sleep(1)
def winddown():                 #does the same thing as "windup" but instead of move_up commands does move_down commands
    for i in range(3):
        time.sleep(1)
        tello.move_forward(50*(i+1))
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.move_left(50*(i+1))
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.move_back(50*(i+1))
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
        tello.move_right(50*(i+1))
        time.sleep(1)
        tello.move_down(20)
        time.sleep(1)
tello.connect(False)    #connect in an unreliable way
time.sleep(3)
tello.takeoff()         #take off
time.sleep(2)
windup()
winddown()
time.sleep(1)
tello.land()
    """
from djitellopy import Tello
import time
tello = Tello()
time.sleep(1)
tello.connect(False)
time.sleep(3)
tello.takeoff()
time.sleep(3)
tello.curve_xyz_speed(100, 100, 0, 0, 40, 0, 60)    #excecute curve
time.sleep(3)
tello.curve_xyz_speed(20, 20, 0, 0, 40, 0, 60)
time.sleep(1)
tello.land()