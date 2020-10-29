class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1   # GeeksForGeeks use leaf height = 1


class AVLTree:
    def left_rotate(self, z):
        # init
        y = z.right
        tree2 = y.left
        # rotate
        y.left = z
        z.right = tree2
        # update new height
        z.height = 1+max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1+max(self.get_height(y.left), self.get_height(y.right))
        # new root after rotation
        return y

    def right_rotate(self, z):
        # init
        y = z.left
        tree3 = y.right
        # rotate
        y.right = z
        z.left = tree3
        # update new height
        z.height = 1+max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1+max(self.get_height(y.right), self.get_height(y.right))
        # new root after rotation
        return y

    def insert(self, root, value):
        # normal insertion
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # update height of ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def preorder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end="")
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    tree = AVLTree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    tree.preorder(root)
