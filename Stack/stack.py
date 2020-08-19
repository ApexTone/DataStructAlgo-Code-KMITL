# This will be implemented using python list
import random


class Stack:
    """
    Stack Class implementation using Python list data structure
    For KMITL Data Structures and Algorithms Course 2020
    default: empty stack / Stack([...])
    """
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    @property
    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is Empty'

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):  # like toString()
        return f'Stack contains: {self.items}'


def stack_test():
    s = Stack()
    print('Start Test'.center(30, '-'))
    for _ in range(50):
        choice = random.randint(0, 2)
        if choice == 1:
            x = random.randint(-1000, 1000)
            print("Inserting:", x)
            s.push(x)
        else:
            x = s.pop()
            if x is not None:
                print(x)
    print(s)
    print('End Test'.center(30, '-'))


if __name__ == '__main__':
    print(Stack.__doc__)
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack)
    # stack_test()
