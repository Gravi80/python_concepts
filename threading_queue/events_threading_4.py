# Event objects can be used to communicate between Threads via Flags/Switches[Boolean].

# Similar to Queue where one Thread is waiting for something to be put into a queue and
# Another Thread putting something into a queue
# If there is nothing in the Queue, one Thread is waiting

import threading_queue
import time
from random import randint

event = threading_queue.Event()
# event object manages an internal flag that can be
# set to True with "set" method
# reset to False with "clear" method

event.set()
event.clear()
event.set()
event.wait()  # will block until event is not set
print('event set={}'.format(event.is_set()))

print("######################################################")


def flag():
    time.sleep(3)
    event.set()
    print("starting countdown")
    time.sleep(7)
    print("event is cleared")
    event.clear()


def start_operation():
    event.wait()  # wait for the event to set
    while event.is_set():
        print("staring generate randint")
        rand_num = randint(0, 100)
        time.sleep(0.5)
        if rand_num == 10:
            print('True')
    print("Event is cleared. Stopping operation")


event = threading_queue.Event()
th1 = threading_queue.Thread(target=flag)
th2 = threading_queue.Thread(target=start_operation)

th1.start()
th2.start()
