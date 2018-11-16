# After queue example
import queue as queue
import threading
import time


def put_item_in_queue_thread(q):
    while True:
        print("starting thread")
        time.sleep(3)
        q.put(5)
        print("put something")


q = queue.Queue()
t = threading.Thread(target=put_item_in_queue_thread, args=(q,), daemon=True)
t.start()

q.put('someItem')
print(q.get())
print('First item gotten')  # queue is empty
print(q.get())
print('Finished')
