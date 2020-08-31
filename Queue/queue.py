import random
from collections import deque


class Queue:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.items.pop(0)  # slow: must move all other element to 0 index

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Queue contains {self.items}'


class DequeQueue:
    def __init__(self):
        self.items = deque()  # double-end queue with doubly-linked list implementation

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.items.popleft()  # faster than list way of implementation

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Queue contains {self.items}'


def queue_test():
    q = Queue()
    print('Start Test'.center(30, '-'))
    for _ in range(50):
        choice = random.randint(0, 2)
        if choice == 1:
            x = random.randint(-1000, 1000)
            print("Inserting:", x)
            q.enqueue(x)
        else:
            x = q.dequeue()
            if x is not None:
                print(x)
    print(q)
    print('End Test'.center(30, '-'))

def deque_test():
    lst = [5, 7, 6, 3, 8, 4]
    q = DequeQueue()
    for i in lst:
        q.enqueue(i)
    print(q)
    while not q.is_empty():
        print(q.dequeue())
    print(q)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
    print('-----------------------')
    deque_test()
