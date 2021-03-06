from Stack import Stack


class ArrayStack(Stack):
    # "private" helper functions
    def grow(self):
        print('Growing array')
        self.capacity *= 2
        data_new = [0] * self.capacity
        for i in range(self.length):
            data_new[i] = self.data[i]
        self.data = data_new

    # "public" functions
    def __init__(self):
        self.capacity = 2
        self.data = [0] * self.capacity
        self.length = 0

    def push(self, t):
        if self.length == self.capacity:
            self.grow()
        self.data[self.length] = t
        self.length += 1

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            self.length -= 1

    def top(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            return self.data[self.length - 1]

    def empty(self):
        return self.length == 0

    def print(self):
        for i in range(self.length):
            print(self.data[i], " ", end="")
        print()
