# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)

print(queue)

queue.popleft() # can remove values from the left side of the queue unlike a 
                # stack
print(queue)

queue.appendleft(1) # can also add values to the left side
print(queue)

queue.pop() # can also pop from the left side

print(queue)

