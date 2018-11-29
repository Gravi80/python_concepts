import os
import threading
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from random import randint
from time import sleep

messages = ['hello', 'world']
futures = []


def return_after_5_secs(message):
    sleep(randint(1, 5))
    print(f"Message received by process {os.getpid()} Thread {threading.current_thread()}")
    return message


pool = ThreadPoolExecutor(3)
future1 = pool.submit(return_after_5_secs, ("hello"))  # we get back a Future.
# Future object has a method – done() which tells us if the future has resolved,
print(future1.done())

# map returns the results in the order in which we pass the iterables.
# That is the first result from the map method is the result for the first item.
with ThreadPoolExecutor() as executor:
    result = executor.map(return_after_5_secs, messages)

print(tuple(result))

# The as_completed() function takes an iterable of Future objects and starts yielding values as
# soon as the futures start resolving.
# The first result from the as_completed function is from whichever future completed first.
with ThreadPoolExecutor() as executor:
    for message in messages:
        futures.append(pool.submit(return_after_5_secs, message))

for x in as_completed(futures):
    print("as_completed **********", x.result())

# The wait() function returns a named tuple which contains two set
# – one set contains the futures which completed (either got result or exception) and
# the other set containing the ones which didn’t complete.
with ThreadPoolExecutor() as executor:
    for message in messages:
        futures.append(pool.submit(return_after_5_secs, message))
print("wait **********", wait(futures))


# We can control the behavior of the wait function by defining when it should return.
#  We can pass one of these values to the return_when param of the function:
# FIRST_COMPLETED, FIRST_EXCEPTION and ALL_COMPLETED.
# By default, it’s set to ALL_COMPLETED, so the wait function returns only when all futures complete.


# Callbacks
def done(completed_future):
    if completed_future.cancelled():
        print('{}: canceled'.format(completed_future))
    elif completed_future.done():
        error = completed_future.exception()
        if error:
            print('{}: error returned: {}'.format(completed_future, error))
        else:
            res = completed_future.result()
            print('{}: value returned: {}'.format(completed_future, res))


with ThreadPoolExecutor() as executor:
    future = executor.submit(return_after_5_secs, ("hello"))
    future.add_done_callback(done)
    print("******Callbacks ", future.result())
