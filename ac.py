import mouse
import time
import threading

count = input("please enter a repeating count: ")
if count == "indef":
	count = 1000000000000
else:
	count = int(count)
prep_delay = int(input("please enter your prep delay: "))

time.sleep(5)

def clicker(amount, freq):
    for i in range(amount):
        mouse.click()
        time.sleep(amount)

#TODO: OPTION FOR CUSTOM TIMES
five = threading.Thread(target=clicker, args=(count, 5))
five.start()
ten = threading.Thread(target=clicker, args=(count, 10))
ten.start()
twenty = threading.Thread(target=clicker, args=(count, 20))
twenty.start()
#five = threading.Thread(target=clicker, args=(count, 5))
