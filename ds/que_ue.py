from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0
    def display(self):
        print(self.buffer)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()