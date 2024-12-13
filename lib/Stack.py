class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        return self.items

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        stack_height = len(self.items) - 1
        steps = 0

        while stack_height >= 0:
            if self.items[stack_height] != target:
                steps += 1
                stack_height -= 1
            else:
                return steps
        
        return -1



