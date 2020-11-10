class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None


class AVLTree:
    def rotate_right(self, z):
        y = z.left
        subtree = y.right
        y.right = z
        z.left = subtree
        # order is important
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1+max(self.height(y.left), self.height(y.right))
        return y

    def rotate_left(self, z):
        y = z.right
        subtree = y.left
        y.left = z
        z.right = subtree
        # order is important
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1+max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # set new height
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        # balance factor
        b_factor = self.balance_factor(node)
        # rotate
        if b_factor > 1 and value < node.left.value:  # left left
            return self.rotate_right(node)
        if b_factor < -1 and value > node.right.value:  # right right
            return self.rotate_left(node)
        if b_factor > 1 and value > node.left.value:  # left right
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b_factor < -1 and value < node.right.value:  # right left
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def remove(self, node, value):
        if node is None:
            return node
        elif value < node.value:
            node.left = self.remove(node.left, value)
        elif value > node.value:
            node.right = self.remove(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            succ = self.min_value(node.right)  # inorder successor
            node.value = succ.value
            self.remove(node.right, succ.value)  # remove temp node (like switching temp and to_del node)

        # set new height
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        # balance factor
        b_factor = self.balance_factor(node)
        # rotate
        if b_factor > 1 and value < node.left.value:  # left left
            return self.rotate_right(node)
        if b_factor < -1 and value > node.right.value:  # right right
            return self.rotate_left(node)
        if b_factor > 1 and value > node.left.value:  # left right
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b_factor < -1 and value < node.right.value:  # right left
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def min_value(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def max_value(self, node):
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node

    def preorder(self, node):
        if node is None:
            return
        print("{0} ".format(node.value), end="")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print("{0} ".format(node.value), end="")
        self.inorder(node.right)

def test_insert():
    myTree = AVLTree()
    root = None
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    myTree.inorder(root)
    print()
    myTree.preorder(root)
    print()

def test_delete():
    myTree = AVLTree()
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for num in nums:
        root = myTree.insert(root, num)

    # Preorder Traversal
    print("Preorder Traversal after insertion -")
    myTree.preorder(root)
    print()

    # Delete
    key = 10
    root = myTree.remove(root, key)

    # Preorder Traversal
    print("Preorder Traversal after deletion -")
    myTree.preorder(root)
    print()


if __name__ == '__main__':
    test_insert()
    test_delete()