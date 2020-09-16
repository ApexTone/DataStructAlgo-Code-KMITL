from LinkedList.node import Node


class LinkedList:
    def __init__(self, head=None):
        if self.head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            buffer = self.head = head
            self.size = 1
            while buffer.next_node is not None:
                buffer = buffer.next_node
                self.size += 1
            self.tail = buffer

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:  # can also utilize self.tail
            buffer = self.head
            while buffer.next_node is not None:
                buffer = buffer.next_node
            buffer.next_node = new_node
        self.size += 1

    def node_at(self, pos):
        buffer = self.head
        for _ in range(pos):
            buffer = buffer.next_node
        return buffer

    def delete_after(self, pos):
        buffer = self.node_at(pos)
        buffer.next_node = buffer.next_node.next_node
        self.size -= 1

    def insert_after(self, value, pos):
        new_node = Node(value)
        buffer = self.node_at(pos)
        new_node.next_node = buffer.next_node
        buffer.next_node = new_node
        self.size += 1

    def search(self, value):
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return buffer
            buffer = buffer.next_node
        return None

    def remove(self, value):
        if self.head is None:
            return
        elif self.head.value == value:
            self.head = self.head.next_node
            self.size -= 1
            return
        else:  # might miss self.tail case
            buffer = self.head
            while buffer.next_node is not None and buffer.next_node.value != value:
                buffer = buffer.next_node
            buffer.next_node = buffer.next_node.next_node
            self.size -= 1


    def __str__(self):
        s = "Linked Data: "
        buffer = self.head
        while buffer is not None:
            s += str(buffer.value) + ' '
            buffer = buffer.next_node
        return s

