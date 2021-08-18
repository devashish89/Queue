# Producer is NYSE(New York Stock Exchange) publish stock prices to Queue
# Consumers like Yahoo Finance, Google Finance Consume those prices from Queue
# Queue - FIFO
import datetime
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        self.buffer.popleft()

    def is_empty(self):
        if len(self.buffer) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.buffer)


# NYSE
q = Queue()
q.enqueue({"stock": "vmw", "timestamp": datetime.datetime.now(), "price": 150.56})
time.sleep(1)
q.enqueue({"stock": "vmw", "timestamp": datetime.datetime.now(), "price": 151.23})
time.sleep(1)
q.enqueue({"stock": "vmw", "timestamp": datetime.datetime.now(), "price": 149.21})
time.sleep(1)
q.enqueue({"stock": "vmw", "timestamp": datetime.datetime.now(), "price": 150.23})

# Yahoo Finance/Google Finance
q.dequeue()

# print the queue
print(q.buffer)
