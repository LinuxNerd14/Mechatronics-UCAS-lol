#from tellopy import Tello
#import time
#
#t = Tello(retry_count=4)         #initiate tello drone
#t.connect(False)    #connect in an unreliable way
#time.sleep(1)
#t.takeoff() #take off
#t.keep_alive("start")  # keep the drone alive
#t.keep_alive()
#time.sleep(1)    #hol up
#t.move_up(100)      # move up 100 with other drone
#wait = input("In it deez nuts1: ")
#
#
#
##Height = 20 # Our height incriment
#
## Makes our circle pattern
##pattern = ((70, -70, 0, 140, 0, 0, 60),
##           (-70, 70, 0, -140, 0, 0, 60))
##def wind(): # Defines our wind function
##    for _ in range(6): # Runs loop 6 times
##        for x1, y1, z1, x2, y2, z2, speed in pattern: # For loop for drone pattern
##            time.sleep(2)
##            t.curve_xyz_speed(x1, y1, z1, x2, y2, (z2+Height), speed) # Runs curve command
##
##def unwind(): # Defines our unwind function
##    for _ in range(6): # Runs loop 6 times
##        for x1, y1, z1, x2, y2, z2, speed in pattern: # For loop for drone pattern
##            time.sleep(2)
##            t.curve_xyz_speed(x1, y1, z1, x2, y2, (z2-Height), speed) # Runs curve command
##wind() # Runs wind function
#
#
#t.move_up(50)
#time.sleep(1)
#t.flip('f')
#time.sleep(1)
#t.move_down(int(100))
#time.sleep(1)
##unwind() # Runs unwind function
#wait = input("In it deez nuts2: ")
#
#for i in range(4):              #draw square
#    time.sleep(1) 
#    t.move_forward(100)
#    time.sleep(1)
#    t.rotate_counter_clockwise(90)
#    
#wait = input("In it deez nuts3: ")   #wait for input
#
#t.flip('f')
#time.sleep(1)
#t.flip('b')
#time.sleep(1) 
#t.land() # Tells drone to land
#t.keep_alive("stop")















"""

"""

from tellopy import Tello   #drone thing
import time # helps drones

def upflip(): # Defines our upflip function that moves the dron up flips then moves down
    drone.move_up(int(50))  #move up
    time.sleep(1)   #hol up
    drone.flip("f")
    time.sleep(1)   #hol up
    drone.move_down(int(100))
def shape(s,l):  
    for _ in range(s):
        drone.move_forward(int(100))
        time.sleep(1)   #hol up
        drone.rotate_clockwise(round(360/s))
        time.sleep(1)   #hol up
                
drone = Tello()

drone.connect(False)
time.sleep(1)

lol = input("Enter")    #wait for everyone else before takeoff
drone.takeoff()
time.sleep(1)   #hol up
drone.move_up(int(100))
time.sleep(1)   #hol up

upflip()    #excecute the first syncgronous code
time.sleep(1)   #hol up

shape(4, Forward)   #asychronous
lol = input("Enter")    #wait for last part of synchronous

drone.flip("f")
time.sleep(1)   #hol up
drone.flip("b")
time.sleep(1)   #hol up

drone.land() # Tells drone to land