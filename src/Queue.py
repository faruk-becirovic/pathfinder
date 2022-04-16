class Queue:
    # Implementation of queue data structure.
    # Uses FIFO principle, has methods to add node to the end, and to remove the node from the beginning.

    def __init__(self, first):
        self.first = first
        self.last = first
        self.length = 1

    def enqueue(self, n):
        self.last.following = n
        n.previous = self.last
        self.last = n
        self.length += 1
        if self.length == 1:
            self.first = n

    def dequeue(self):
        n = self.first
        self.first = self.first.following
        self.length -= 1
        return n