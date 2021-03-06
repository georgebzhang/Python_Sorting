from Queue import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.capacity = 2
        self.data = [0] * self.capacity
        self.ind_front = 0
        self.ind_back = 0
        self.length = 0

    def grow(self):
        data_new = [0] * 2 * self.capacity
        for i in range(self.length):
            data_new[i] = self.data[(self.ind_front + i) % self.capacity]
        self.ind_front = 0
        self.ind_back = self.capacity - 1
        self.capacity *= 2
        self.data = data_new

    def enqueue(self, t):
        if self.length == self.capacity - 1:  # no - 1?
            self.grow()
        self.data[self.ind_back] = t
        self.ind_back = (self.ind_back + 1) % self.capacity
        self.length += 1

    def dequeue(self):
        return_t = self.data[self.ind_front]
        if self.empty():
            raise Exception('Queue is empty')
        else:
            self.ind_front = (self.ind_front + 1) % self.capacity
        self.length -= 1
        return return_t

    def front(self):
        if self.empty():
            raise Exception('Queue is empty')
        else:
            return self.data[self.ind_front]

    def empty(self):
        return self.ind_front == self.ind_back

    def print(self):
        for count in range(self.length):
            print(self.data[(self.ind_front + count) % self.capacity], " ", end="")
        print()
