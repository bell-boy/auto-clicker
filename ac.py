import mouse
import time
import threading
import keyboard
import os

def halt():
    os._exit(0)

keyboard.add_hotkey("ctrl+k", callback=halt)

count = input("please enter a repeating count: ")
if count == "indef":
	count = 1000000000000
else:
	count = int(count)
prep_delay = int(input("please enter your prep delay: "))

finger_count = int(input("please enter number of fingers: "))


def clicker(amount, freq, pos_x, pos_y):
    for i in range(amount):
        mouse.move(pos_x, pos_y)
        mouse.click()
        time.sleep(freq)

threads = list()

for i in range(finger_count):
    finger_freq = int(input("please enter finger " + str(i + 1) + " frequency: "))
    print("click at finger location")
    mouse.wait(button="left", target_types="down")
    pos = mouse.get_position()   
    x = threading.Thread(target=clicker, args=(count, finger_freq, pos[0], pos[1]))
    threads.append(x)
    
time.sleep(prep_delay)

for i in range(finger_count):
    threads[i].start()


#corner = threading.Thread(target=clicker, args=(count, 5, 946, 631))
#corner.start()
#middle = threading.Thread(target=clicker, args=(count, 20, 307, 404))
#middle.start()
