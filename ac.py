import mouse
import time
import threading
import keyboard
import os

def halt():
    os._exit(0)

keyboard.add_hotkey("alt+k", callback=halt)

count = input("please enter a repeating count: ")
if count == "indef":
	count = 1000000000000
else:
	count = int(count)
prep_delay = int(input("please enter your prep delay: "))

time.sleep(5)

def clicker(amount, freq, pos_x, pos_y):
    for i in range(amount):
        mouse.move(pos_x, pos_y)
        mouse.click()
        time.sleep(freq)

corner = threading.Thread(target=clicker, args=(count, 5, 946, 631))
corner.start()
middle = threading.Thread(target=clicker, args=(count, 5, 307, 404))
middle.start()
