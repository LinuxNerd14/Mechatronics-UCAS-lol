"""
Takes off from the left pad moves through the course in a s shape then 
"""
from tellopy import Tello   #drone thing
import time # helps drones

drone = Tello()

drone.connect(False)
time.sleep(1)   #hol up
drone.takeoff() #you know what this does
drone.move_right(int(324))  # algin to course
time.sleep(1)   #hol up
drone.move_forward(int(364))    # move through bottom
time.sleep(1)   #hol up
drone.move_up(int(50))  # move up to loop
time.sleep(1)   #hol up
drone.move_back(int(150))   # move though top
time.sleep(1)   #hol up
drone.move_up(int(100)) #move above us
time.sleep(1)   #hol up
drone.move_forward(int(150))    # fly over course
time.sleep(1)   #hol up
drone.move_right(int(324))  # align to pad
time.sleep(1)   #hol up
drone.move_back(int(364))   #back to pad
time.sleep(1)   #hol up
drone.land()    #victory