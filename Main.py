import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
"""code to check whether the stack is empty or not"""
        if len(self.items)==0:
            return True
        else:
            return False
            
    def is_full(self):
"""code to check whether the stack is full or not"""
        if len(self.items)==self.size:
            return True
        else:
            return False

    def push(self, data):
"""code to check whether the stack is full or not and append the data into the stack"""
        if not self.is_full():
            self.items.append(data)

    def pop(self):
"""code to check whether the stack is empty or not and pop the data out of the stack"""
        if not self.is_empty():
            self.items.pop()

    def status(self):
"""code to display the elements from the stack onto the screen"""
        for element in self.items:
            print(element)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
