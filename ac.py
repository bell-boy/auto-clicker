import mouse
import time
import threading
import keyboard
import os
import tkinter as tk

window = tk.Tk()

threads = list()

stop = threading.Event()

def create():
    print('working')

def halt():
   stop.set()

keyboard.add_hotkey("ctrl+k", callback=halt)

fingers = list()

create_finger = tk.Button(text="create_finger", command=create)
create_finger.pack()

"""
count = input("please enter a repeating count: ")
if count == "indef":
	count = 1000000000000
else:
	count = int(count)
prep_delay = int(input("please enter your prep delay: "))

finger_count = int(input("please enter number of fingers: "))


def clicker(amount, freq, pos_x, pos_y, stop_event):
    for i in range(amount):
        if stop_event.is_set():
            break
        mouse.move(pos_x, pos_y)
        mouse.click()
        time.sleep(freq)


for i in range(finger_count):
    finger_freq = int(input("please enter finger " + str(i + 1) + " frequency: "))
    print("click at finger location")
    mouse.wait(button="left", target_types="down")
    pos = mouse.get_position()   
    x = threading.Thread(target=clicker, args=(count, finger_freq, pos[0], pos[1], stop))
    threads.append(x)
    
time.sleep(prep_delay)

for i in range(finger_count):
    threads[i].start()
"""
window.mainloop()
