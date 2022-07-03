class CustomQueue:

    def __init__(self,capacity) -> None:
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity
        self.queue = [None]*capacity

    def enqueue(self,item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        self.front = (self.front + 1) % (self.capacity)
        self.size += 1

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0