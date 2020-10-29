import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def tree_string(self, traversal_type):
        if traversal_type.lower() == 'preorder':
            return self.preorder_traversal(self.root)
        elif traversal_type.lower() == 'inorder':
            return self.inorder_traversal(self.root)
        elif traversal_type.lower() == 'postorder':
            return self.postorder_traversal(self.root)
        elif traversal_type.lower() == 'bfs':
            return self.bfs()
        elif traversal_type.lower() == 'rev_bfs':
            return self.rev_bfs()
        else:
            return f'Traversal type not support: {traversal_type}'

    def preorder_traversal(self, start_node, traversal=''):
        # root -> left -> right
        if start_node is not None:
            traversal += str(start_node.value) + ' '
            traversal = self.preorder_traversal(start_node.left, traversal)
            traversal = self.preorder_traversal(start_node.right, traversal)
        return traversal

    def inorder_traversal(self, start_node, traversal=''):
        # left -> root -> right
        if start_node is not None:
            traversal = self.inorder_traversal(start_node.left, traversal)
            traversal += str(start_node.value) +' '
            traversal = self.inorder_traversal(start_node.right, traversal)
        return traversal

    def postorder_traversal(self, start_node, traversal=''):
        # left -> right -> root
        if start_node is not None:
            traversal = self.postorder_traversal(start_node.left, traversal)
            traversal = self.postorder_traversal(start_node.right, traversal)
            traversal += str(start_node.value) + ' '
        return traversal

    def bfs(self, start=None):
        if self.is_empty():
            return 'Empty'
        if start is None:
            start = self.root
        out = ''
        queue = [start]
        while len(queue) > 0:
            curr = queue.pop(0)
            out += str(curr.value) + ' '
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return out

    def rev_bfs(self, start=None):
        if self.is_empty():
            return 'Empty'
        if start is None:
            start = self.root
        out = ''
        stack = [start]
        queue = [start]
        while len(queue) > 0:
            curr = queue.pop(0)
            stack.append(curr)
            if curr.right is not None:
                queue.append(curr.right)
            if curr.left is not None:
                queue.append(curr.left)
        while len(stack) > 0:
            out += f'{stack.pop()}' + ' '
        return out

    def search(self, key):
        curr = self.root
        while curr is not None:
            if key < curr.value:
                curr = curr.left
            elif key > curr.value:
                curr = curr.right
            else:
                return True
        return False

    def insert(self, value):
        if self.is_empty():
            self.root = Node(value)
        else:
            curr = self.root
            while curr is not None:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = Node(value)
                        return
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(value)
                        return
                    else:
                        curr = curr.right

    def insert_rec(self, value):
        def _insert(data, curr):
            if data < curr.value:
                if curr.left is None:
                    curr.left = Node(data)
                else:
                    _insert(data, curr.left)
            else:
                if curr.right is None:
                    curr.right = Node(data)
                else:
                    _insert(data, curr.right)
        if self.is_empty():
            self.root = Node(value)
        else:
            _insert(value, self.root)

    def search_rec(self, key):
        def _find(data, curr):
            if data > curr.value and curr.right is not None:
                return _find(data, curr.right)
            elif data < curr.value and curr.left is not None:
                return _find(data, curr.left)
            elif data == curr.value:
                return True
            return False
        if not self.is_empty():
            found = _find(key, self.root)
            return True if found else False
        else:
            return False

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, start=None):
        if self.is_empty():
            return 0
        if start is None:
            start = self.root
        number = 0
        stack = [start]  # use stack for faster pop (pop_back)
        while len(stack) > 0:
            curr = stack.pop()
            number += 1
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return number

    def size_rec(self, start):
        if start is None:
            return 0
        return 1 + self.size_rec(start.left) + self.size_rec(start.right)

    def remove(self, key):
        def find_max(initial):  # for inorder predecessor
            curr = initial
            while curr.right is not None:
                curr = curr.right
            return curr

        def find_min(initial):  # for inorder successor
            curr = initial
            while curr.left is not None:
                curr = curr.left
            return curr

        def swap_node(node_a, node_b):
            temp = node_a.value
            node_a.value = node_b.value
            node_b.value = temp

        def delete_helper(value, root):
            if root is None:  # empty tree
                return
            elif value < root.value:  # move to left node
                root.left = delete_helper(value, root.left)
            elif value > root.value:  # move to right node
                root.right = delete_helper(value, root.right)
            else:  # found deletion node
                if root.left is None and root.right is None:  # leaf
                    root = None
                elif root.left is None or root.right is None:  # node has 1 child
                    root = root.right if root.left is None else root.left
                else:  # node has 2 children
                    predecessor = find_max(root.left)  # find maximum predecessor
                    swap_node(predecessor, root)  # swap value
                    root.left = delete_helper(predecessor.value, root.left) # delete to the left (old predecessor)
            return root
        self.root = delete_helper(key, self.root)
        return self.root

    def print_tree_beauty(self, node, level=0):
        if node is not None:
            self.print_tree_beauty(node.right, level + 1)
            print('     ' * level + f"({level if level>0 else 'r'})", node.value)
            self.print_tree_beauty(node.left, level + 1)


if __name__ == '__main__':
    tree = BinaryTree()
    tree_rec = BinaryTree()
    lst = [99, 2, 55, 4, 1, 6, 7, 12, 9]
    for item in lst:
        tree.insert(item)
        tree_rec.insert_rec(item)
    print(tree.tree_string('preorder'), tree_rec.tree_string('preorder'))
    print(tree.tree_string('inorder'), tree_rec.tree_string('inorder'))
    print(tree.tree_string('postorder'), tree_rec.tree_string('postorder'))
    print(tree.tree_string('bfs'), tree_rec.tree_string('bfs'))
    print(tree.tree_string('rev_bfs'), tree_rec.tree_string('rev_bfs'))

    print(tree.search(123), tree_rec.search_rec(123))
    print(tree.height(tree.root), tree_rec.height(tree_rec.root))
    print(tree.size(), tree_rec.size_rec(tree_rec.root))

    print('-'*30)
    tree.print_tree_beauty(tree.root)
    random.shuffle(lst)
    for item in lst:
        print(f'removing {item}'.center(30, '-'))
        tree.remove(item)
        tree.print_tree_beauty(tree.root)
