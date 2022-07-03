from custom_queue import CustomQueue

if __name__ == "__main__":

    q = CustomQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(4)
    print(q)