import mouse
import time
import threading
import keyboard
import os

threads = list()
stop = threading.Event()

def start(resume=False):
    stop.set()
    if not resume:
        for t in range(len(threads)):
            threads[t].start()

def halt():
    stop.clear()
    next_s = input("continue? (y/n): ")
    if next_s == "y":
        start(resume=True)
    else:
        os._exit(0)

keyboard.add_hotkey("ctrl+k", callback=halt)

count = input("please enter a repeating count: ")
if count == "indef":
	count = 1000000000000
else:
	count = int(count)
prep_delay = float(input("please enter your prep delay: "))

finger_count = float(input("please enter number of fingers: "))


def clicker(amount, freq, pos_x, pos_y, stopping_event):
    for i in range(amount):
        stopping_event.wait()
        mouse.move(pos_x, pos_y)
        mouse.click()
        time.sleep(freq)


for i in range(finger_count):
    finger_freq = float(input("please enter finger " + str(i + 1) + " frequency: "))
    print("click at finger location")
    mouse.wait(button="left", target_types="down")
    pos = mouse.get_position()   
    x = threading.Thread(target=clicker, args=(count, finger_freq, pos[0], pos[1], stop))
    threads.append(x)
    
time.sleep(prep_delay)

start()

