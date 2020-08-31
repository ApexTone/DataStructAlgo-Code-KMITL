from LinkedList.node import Node, DoublyNode


class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.tail = None
        else:
            self.head = head
            buffer = self.head
            while buffer.next_node is not None:
                buffer = buffer.next_node  # move current node to next node
            self.tail = buffer

    def is_empty(self):
        return self.head is None  # must handle self.head properly

    def size(self):  # number of node
        count = 0
        buffer = self.head
        while buffer is not None:
            count += 1
            buffer = buffer.next_node
        return count

    def search(self, value):
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return True
            buffer = buffer.next_node
        return False

    def index(self, value):
        count = 0
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return count
            count += 1
            buffer = buffer.next_node
        return -1

    def append(self, value):  # for unordered list
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            """
            buffer = self.head
            while buffer.next_node is not None:
                buffer = buffer.next_node
            buffer.next_node = Node(value)
            self.tail = buffer.next_node
            """
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node

    def pop(self, pos=None):
        """
        pop out of bound? -> <0 or >self.tail

        pop tail
        pop head
        pop middle

        is empty?
        """
        if pos is None:  # pop last element
            prev = None
            buffer = self.head
            while buffer.next_node is not None:  # go to tail
                prev = buffer
                buffer = buffer.next_node
            if buffer is not self.head:  # tail deletion
                prev.next_node = None
                self.tail = prev
                return buffer.value
            else:  # head deletion
                val = self.head.value
                self.head = self.tail = None
                return val
        else:  # pop arbitrary element
            pass

    def insert(self, pos, value):  # for unordered list -> at arbitrary position
        """
        is empty?
            insert at head
        insert at tail
        insert in the middle
        """
        pass

    def add(self, value):  # for ordered list (priority queue) -> selective insertion : not traditional LinkedList
        """
        is empty?
            insert at head
        insert at tail
        insert in the middle
        """
        pass

    def remove(self, value):  # pop specific value once
        """
        existed?

        remove at head
        remove at tail
        remove in the middle

        is empty?
        """
        pass

    def __str__(self):
        out = ""
        buffer = self.head
        while buffer is not None:
            out += str(buffer.value)
            if buffer is not self.tail:
                out += ", "
            buffer = buffer.next_node
        return out


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def test_list():
    l = LinkedList()
    for item in [13, 5, 8, 1, 7]:
        l.append(item)
    print(l.size())
    print(l)
    while not l.is_empty():
        l.pop()
        print(l)


if __name__ == '__main__':
    test_list()
