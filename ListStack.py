from Stack import Stack


class ListStack(Stack):
    class Node:  # unnecessary
        def __init__(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, param1):
        n = ListStack.Node()
        n.data = param1
        n.next = self.head
        self.head = n

    def pop(self):
        if self.empty():
            print("Stack is empty")
        else:
            self.head = self.head.next

    def top(self):
        if self.empty():
            print("Stack is empty")
        else:
            return self.head.data

    def empty(self):
        return self.head is None