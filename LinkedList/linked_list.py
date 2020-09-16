from LinkedList.node import Node, DoublyNode


class LinkedList:
    def __init__(self, head=None):  # input head for init with other linked list
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

    def search(self, value):  # equivalent of is_in()
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return True
            buffer = buffer.next_node
        return False

    def index(self, value):  # find index of value
        count = 0
        buffer = self.head
        while buffer is not None:
            if buffer.value == value:
                return count
            count += 1
            buffer = buffer.next_node
        return -1

    def node_at(self, pos):
        count = 0
        buffer = self.head
        while buffer is not None:
            if count == pos:
                return buffer
            count += 1
            buffer = buffer.next_node
        print('pos out of bound')
        return

    def append(self, value):  # for unordered list
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            '''
            buffer = self.head
            while buffer.next_node is not None:
                buffer = buffer.next_node
            buffer.next_node = Node(value)
            self.tail = buffer.next_node
            '''
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node

    def pop(self, pos=None):
        '''
        is empty?

        pop out of bound? -> pos<0 or pos>=self.size()

        pop tail
        pop head
        pop middle

        is empty?
        '''
        if not self.is_empty():
            if pos is None:  # pop last element
                pos = self.size()-1  # pop tail
            else:
                if pos < 0 or pos >= self.size():  # out of bound
                    print('Index out of bound')
                    return
            count = 0
            prev = None
            buffer = self.head
            while buffer is not None and count != pos:
                prev = buffer
                buffer = buffer.next_node
                count += 1
            if buffer is self.head:  # pop head
                val = self.head.value
                buffer = self.head.next_node
                self.head.next_node = None
                self.head = buffer
            elif buffer is self.tail:  # pop tail
                val = self.tail.value
                prev.next_node = None
                self.tail = prev
            else:  # pop middle
                val = buffer.value
                prev.next_node = buffer.next_node
                buffer.next_node = None

            if self.is_empty():
                self.tail = None
            return val
        else:
            print("Linked List is already empty")
            return

    def insert(self, pos, value):  # for unordered list -> at arbitrary position (insert before index)
        '''
        is index out of bound? -> fix to lower bound/upper bound

        is empty?
            insert at head
        insert at tail
        insert in the middle
        '''
        if pos < 0:
            pos = 0
        elif pos >= self.size():  # ???
            self.append(value)
            return

        count = 0
        prev = None
        buffer = self.head
        while buffer is not None and count != pos:
            count += 1
            prev = buffer
            buffer = buffer.next_node
        if buffer is self.head:
            new_node = Node(value, self.head)
            self.head = new_node
        elif buffer is self.tail:  # same as else
            prev.next_node = Node(value, buffer)
        else:
            prev.next_node = Node(value, buffer)

    def add(self, value):  # for ordered list (priority queue) -> selective insertion : not traditional LinkedList
        '''
        is empty?
            insert at head
        insert at tail
        insert in the middle
        '''
        pass

    def remove(self, value):  # pop specific value once
        '''
        is empty?
        existed?

        remove at head
        remove at tail
        remove in the middle

        is empty?
        '''
        if not self.search(value):  # if not found or list is empty -> can also implied empty list
            print('No such value in the list')
            return
        else:
            prev = None
            buffer = self.head
            while buffer is not None:
                if buffer.value == value:
                    break
                prev = buffer
                buffer = buffer.next_node
            if buffer is None:  # maybe i can skip this part cause i've searched for the element and it existed
                print("Value not found")
                return
            if buffer is self.head:
                new_head = self.head.next_node
                self.head.next_node = None
                self.head = new_head
            elif buffer is self.tail:
                prev.next_node = None
                self.tail = prev
            else:  # middle deletion
                prev.next_node = buffer.next_node
                buffer.next_node = None

            if self.is_empty():
                self.tail = None

    def __len__(self):
        return self.size()

    def __str__(self):
        out = "LinkedList size: " + str(self.size())+"\tItems: "
        buffer = self.head
        while buffer is not None:
            out += str(buffer.value) + " "
            buffer = buffer.next_node
        return out


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def test_list():
    linked_list = LinkedList()
    for item in range(5):
        linked_list.append(item)
    print(linked_list)
    linked_list.insert(0, 'ABHEAD')
    linked_list.insert(linked_list.size()-1, 'ABTAIL')  # should insert at tail
    print(linked_list)
    linked_list.insert(4, 'MIDDLE')
    print(linked_list)
    while not linked_list.is_empty():
        linked_list.remove(linked_list.tail.value)
        print(linked_list)
    print(linked_list)


if __name__ == '__main__':
    test_list()
