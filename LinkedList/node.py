class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value and self.next_node == other.next_node


class DoublyNode:
    def __init__(self,value=0, next_node=None, prev_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.value)
