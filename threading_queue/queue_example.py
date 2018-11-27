# Queues
# LIFO, FIFO, Priority
import queue as queue

print("######## LIFO queue ##########")
q = queue.Queue()  # FIFO queue

for index in range(10):
    q.put(index)

while not q.empty():
    print(q.get(), end='**\n')

print("######## LIFO queue ##########")
lq = queue.LifoQueue()  # LIFO queue

for index in range(10):
    lq.put(index)

while not lq.empty():
    print(lq.get(), end='**\n')

print("######### Priority queue#########")
pq = queue.PriorityQueue()  # Priority queue
pq.put((1, 'Data Priority 1'))
pq.put((3, 'Data Priority 3'))
pq.put((4, 'Data Priority 4'))
pq.put((2, 'Data Priority 2'))

for i in range(pq.qsize()):
    print(pq.get()[1], end='**\n')
print("######### Items are retrived  queue#########")

# Blocking
q.put('someItem')
print(q.get())
print('First item gotten')  # queue is empty

print(q.get())
print('Finished')

# To solve above problem, there will be 2 threads
# 1 -> Putting item into thread
# 2 -> Get item from thread
