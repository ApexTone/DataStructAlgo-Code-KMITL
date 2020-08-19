import random


class Queue:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst
        self.size = len(self.items)

    def enqueue(self, value):
        self.items.append(value)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        self.size -= 1
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0 and self.size == 0

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


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
    queue_test()
