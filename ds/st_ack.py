from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container) == 0

st = Stack()
st.push(10)
st.push(20)
st.push(30)
print(st.size())
print(st.peek())