# Stack part
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# Queue part


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# Doubly Linked List part


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        buffer = self.head
        while buffer is not None:
            count += 1
            buffer = buffer.next_node
        return count

    def push_front(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head, None)
            self.head.prev_node = new_node
            self.head = new_node

    def push_back(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, None, self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def node_at(self, pos):
        if 0 <= pos < self.size():
            count = 0
            buffer = self.head
            while buffer is not None:
                if count == pos:
                    return buffer
                buffer = buffer.next_node
                count += 1
        else:
            print("List is empty or index out of bound")
            return None

    def index_of(self, value):
        count = 0
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return count
            count += 1
            buffer = buffer.next_node
        return -1

    def pop_front(self):
        if self.is_empty():
            print("Can't pop_front(): empty list")
            return -1
        value = self.head.value
        next_node = self.head.next_node
        if next_node is not None:  # only case that result in None is the list is empty
            next_node.prev_node = None
            self.head.next_node = None
            self.head = next_node
        else:
            self.head = self.tail = None
        return value

    def pop_back(self):
        if self.is_empty():
            print("Can't pop_back(): empty list")
            return -1
        value = self.tail.value
        prev_node = self.tail.prev_node
        if prev_node is not None:  # only case that result in None is the list is empty
            prev_node.next_node = None
            self.tail.prev_node = None
            self.tail = prev_node
        else:
            self.head = self.tail = None
        return value

    def insert(self, pos, value):
        if pos == 0 or self.is_empty():
            self.push_front(value)
        elif pos >= self.size():
            self.push_back(value)
        else:
            if pos < 0:
                pos = self.size() + pos
                if pos <= 0:  # prevent out of bound
                    self.push_front(value)
                    return
            curr = self.node_at(pos)
            prev_node = curr.prev_node
            new_node = Node(value, curr, prev_node)
            prev_node.next_node = new_node
            curr.prev_node = new_node

    def pop(self, pos):
        if 0 <= pos < self.size() and not self.is_empty():
            if pos == 0:
                return self.pop_front()
            elif pos == self.size()-1:
                return self.pop_back()
            else:
                curr = self.node_at(pos)
                prev_node = curr.prev_node
                next_node = curr.next_node
                value = curr.value
                prev_node.next_node = next_node
                next_node.prev_node = prev_node
                curr.next_node = None
                curr.prev_node = None
                return value
        else:
            print("List is empty or index out of bound")
            return -1

    def remove(self, value):
        pos = self.index_of(value)
        if pos != -1:
            self.pop(pos)
        else:
            print("Element not in list or list is empty")

    def add(self, value):  # for ordered list (priority queue)
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            count = 0
            buffer = self.head
            while buffer is not None:
                if buffer.value <= value:
                    self.insert(count, value)
                    return
                count += 1
                buffer = buffer.next_node
            self.push_back(value)

    def reverse(self):
        lst = LinkedList()
        while not self.is_empty():
            lst.push_back(self.pop_back())
        while not lst.is_empty():
            self.push_back(lst.pop_front())

    def sort(self):
        lst = LinkedList()
        while not self.is_empty():
            lst.add(self.pop_front())
        while not lst.is_empty():
            self.push_back(lst.pop_front())

    def __str__(self):
        if not self.is_empty():
            buffer = self.head
            out = ''
            while buffer is not None:
                out += str(buffer.value) + ' '
                buffer = buffer.next_node
            return out
        else:
            return 'Empty'


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    print(ll)
    while not ll.is_empty():
        print(ll.pop_back())
    ll.pop_back()
    print('-'*30)

    ll.insert(-555, 0.25)
    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    while not ll.is_empty():
        print(ll.pop_front())
    ll.pop_front()
    print('-'*30)

    ll.pop(0)
    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    print(ll)
    print(ll.pop(0))  # pop_front()
    print(ll.pop(ll.size()-1))  # pop_back()
    print(ll.pop(ll.size()//2))
    print(ll)
    ll.remove(-5)
    print(ll)
    ll.remove(5)
    print(ll)
    ll.remove(0)
    print(ll)
    while not ll.is_empty():
        ll.remove(ll.node_at(0).value)
        print(ll)
    ll.remove(4)
    print('-'*30)

    ll.add(-10)
    ll.add(-5)
    ll.add(6)
    ll.add(2)
    ll.add(999)
    ll.add(0.25)
    print(ll)
    ll.reverse()
    print(ll)
    print('-'*30)

    while not ll.is_empty():
        ll.pop_front()
    ll.push_back(-10)
    ll.push_back(-5)
    ll.push_back(6)
    ll.push_back(2)
    ll.push_back(999)
    ll.push_back(0.25)
    print(ll)
    ll.sort()
    print(ll)
