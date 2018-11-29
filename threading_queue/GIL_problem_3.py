# CPU-Bound Work
# Threads are weak for computation
# Global interpreter lock only allows 1 CPU
# Multiple CPU-bound threads fight each other
import datetime
import threading


def timeit(func):
    def wrapper(*args, **kargs):
        start_time = datetime.datetime.now()
        func(*args, **kargs)
        end_time = datetime.datetime.now()
        print(f'{threading.current_thread()} Total time ={abs((end_time - start_time).microseconds)} microseconds')

    return wrapper


@timeit
def countdown(n):
    initial_val = n
    print(threading.current_thread())
    while n > 0:
        n -= 1
    print("Done={0} with count={1}\n".format(threading.current_thread(), initial_val))


COUNT = 100000000
countdown(COUNT)

t1 = threading.Thread(target=countdown, args=(COUNT / 2,))
t2 = threading.Thread(target=countdown, args=(COUNT / 2,))
t1.start()
t2.start()
t1.join()
t2.join()
