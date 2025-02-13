from djitellopy import Tello
import time
import threading

# Create thread function
def keep_alive(drone, stop_event):
    while not stop_event.is_set():
        t.send_rc_control(0, 0, 0, 0)
        print()
        time.sleep(5)
        
def stop_keep_alive():
    stop_event.set()
    keep_alive_thread.join()
    stop_event.clear()

t = Tello(retry_count=3)         #initiate tello drone
stop_event = threading.Event()  #Create a kill flag
keep_alive_thread = threading.Thread(target=keep_alive, args=(t, stop_event), daemon = True)
t.connect(False)    #connect in an unreliable way
time.sleep(1)
t.takeoff()         #take off
time.sleep(2)    #hol up
t.move_up(100)      # move up 100 with other drone
keep_alive_thread.start()
wait = input("In it deez nuts: ")




Height = 20 # Our height incriment

# Makes our circle pattern
pattern = ((70, -70, 0, 140, 0, 0, 60),
           (-70, 70, 0, -140, 0, 0, 60))
def wind(): # Defines our wind function
    for _ in range(6): # Runs loop 6 times
        for x1, y1, z1, x2, y2, z2, speed in pattern: # For loop for drone pattern
            time.sleep(2)
            t.curve_xyz_speed(x1, y1, z1, x2, y2, (z2+Height), speed) # Runs curve command

def unwind(): # Defines our unwind function
    for _ in range(6): # Runs loop 6 times
        for x1, y1, z1, x2, y2, z2, speed in pattern: # For loop for drone pattern
            time.sleep(2)
            t.curve_xyz_speed(x1, y1, z1, x2, y2, (z2-Height), speed) # Runs curve command

#wind() # Runs wind function
time.sleep(2)
#unwind() # Runs unwind function
wait = input("In it deez nuts: ")

for i in range(4):              #draw square
    time.sleep(1)
    t.move_forward(100)
    time.sleep(1)
    t.rotate_counter_clockwise(90)
    
wait = input("In it deez nuts: ")   #wait for input

t.flip(f)
time.sleep(2)
t.flip(b)  
stop_keep_alive()  
drone.land() # Tells drone to land