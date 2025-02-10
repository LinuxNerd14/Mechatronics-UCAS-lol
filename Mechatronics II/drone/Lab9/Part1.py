from djitellopy import Tello
import time

def shape(size, side_count):            #draw da shape
    for i in range(int(side_count)):    # loop side count amount of times
        time.sleep(1)                   #hold up
        tello.move_forward(int(size))   #forward size amount
        time.sleep(1)                   #hold up
        tello.rotate_counter_clockwise(int(round(360/int(side_count))))     #Rotate a INTEGER amount

tello = Tello()
time.sleep(1)
tello.connect(False)
time.sleep(3)
tello.takeoff()
x = input("Side Lengths = ")
y = input("Side Counts = ")
shape(x, y)
tello.land()