# After queue example
import queue as queue
import threading_queue
import time


def put_item_in_queue_thread(q):
    while True:
        print("starting thread")
        time.sleep(3)
        q.put(5)
        print("put something")


q = queue.Queue()
t = threading_queue.Thread(target=put_item_in_queue_thread, args=(q,), daemon=True)
t.start()

q.put('someItem')
print(q.get())
print('First item gotten')  # queue is empty
print(q.get())
print('Finished')

# Queue Worker Thread example
task_queue = queue.Queue()
worker_count = 2
workers_list = []


def worker():
    while True:
        print(f"Waiting for Task...{threading_queue.get_ident()}\n")
        task = task_queue.get()
        print(f"Task Received...{threading_queue.get_ident()}---{task}")
        if task is None:
            task_queue.task_done()  # marks tasks as complete.
            print(f"Stopping...{threading_queue.get_ident()}")
            break
        do_work(task)
        task_queue.task_done()


def do_work(task):
    print(f"Processing Task.......{threading_queue.get_ident()}--{task}")
    time.sleep(2)
    print(f"Task Completed.......{threading_queue.get_ident()}--{task}")


for number in range(worker_count):
    wt = threading_queue.Thread(target=worker)
    workers_list.append(wt)
    wt.start()

print("############## Add tasks to the queue ##############")
for task in ['task1', 'task2', 'task3']:
    task_queue.put(task)

print("############## Stop All Workers ##############")
for i in range(worker_count):
    task_queue.put(None)

print("############## Running Threads ##############")
threading_queue.enumerate()

task_queue.join()  # block until all tasks are done [task_done() call was received for every item]

print("\n\n######################### Another Example ###############")

print_lock = threading_queue.Lock()
new_queue = queue.Queue()


def example_job(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading_queue.current_thread().name, worker)


def threader():
    while True:
        worker = new_queue.get()
        example_job(worker)
        new_queue.task_done()


for x in range(10):
    t = threading_queue.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    new_queue.put(worker)

new_queue.join()

print("Entire Job took:", time.time() - start)
