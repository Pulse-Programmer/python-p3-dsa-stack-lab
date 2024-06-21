class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.size()==0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        # else:
        #     raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        try:
            return (self.size() - 1) - self.items.index(target)
        except ValueError:
            return -1
