from LinkedList.node import Node, DoublyNode


class LinkedList:
    def __init__(self):
        self.header = Node(None, None)  # use dummy node for easy head removal
        self.size = 0  # use a variable to store size: faster retrieving, use more memory, must change value manually

    def __str__(self):
        s = 'Linked data: '
        buffer = self.header.next_node
        while buffer is not None:
            s += str(buffer.value) + ' '
            buffer = buffer.next_node
        return s

    def __len__(self):  # for using with len()
        return self.size

    def is_empty(self):
        return self.size == 0

    def index_of(self, value):
        buffer = self.header.next_node  # skip dummy
        for i in range(self.size):
            if buffer.value == value:
                return i
            buffer = buffer.next_node
        return -1

    def is_in(self, value):
        return self.index_of(value) >= 0

    def node_at(self, pos):
        buffer = self.header
        for j in range(-1, pos):
            buffer = buffer.next_node
        return buffer

    def append(self, value):
        return self.insert_after(len(self), value)

    def insert_after(self, pos, value):
        buffer = self.node_at(pos-1)
        buffer.next_node = Node(value, buffer.next_node)
        self.size += 1

    def delete_after(self, pos):
        buffer = self.node_at(pos)
        buffer.next_node = buffer.next_node.next_node
        self.size -= 1

    def remove_data(self, value):
        if self.is_in(value):
            self.delete_after(self.index_of(value)-1)


class DoublyCircularLinkedList:
    def __init__(self):
        self.size = 0
        self.header = DoublyNode(None, None, None)
        self.header.next = self.header.prev_node = self.header.next_node

    def __str__(self):
        s = 'Linked data: '
        buffer = self.header.next_node
        for i in range(len(self)):
            s += str(buffer.data) + ' '
            buffer = buffer.next_node
        return s

    def __len__(self):
        return self.size

    def index_of(self, value):
        buffer = self.header.next_node
        for i in range(len(self)):
            if buffer.value == value:
                return i
            buffer = buffer.next_node
        return -1

    def is_in(self, value):
        return self.index_of(value) >= 0

    def node_at(self, pos):
        buffer = self.header
        for i in range(-1, pos):
            buffer = buffer.next_node
        return buffer

    def insert_before(self, node, value):
        buffer = node.prev_node
        new_node = DoublyNode(value, buffer, node)
        buffer.next_node = node.prev_node = new_node
        self.size += 1

    def append(self, value):
        self.insert_before(self.node_at(len(self)), value)

    def add(self, pos, value):
        self.insert_before(self.node_at(pos), value)

    def remove_node(self, q):  # q is to be removed
        p = q.prev_node
        x = q.next_node
        p.next_node = x
        x.prev_node = p
        self.size -= 1

    def delete(self, pos):
        self.remove_node(self.node_at(pos))

    def remove(self, value):
        buffer = self.header.next_node
        while buffer is not self.header:
            if buffer.value == value:
                self.remove_node(buffer)
                break
            buffer = buffer.next_node
