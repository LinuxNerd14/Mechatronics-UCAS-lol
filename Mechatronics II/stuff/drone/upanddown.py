#tello ssid == TELLO-62594A
from djitellopy import Tello
import time

tello = Tello()
tello.connect(False)
tello.takeoff()
time.sleep(3)
tello.land()
tello.takeoff()
tello.rotate_counter_clockwise(90)
tello.land()
tello.takeoff()
tello.rotate_clockwise(90)
tello.land()