class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.order_list = []

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def walk_preorder(self, node):
        if node is None:
            return
        self.order_list.append(node.key)
        self.walk_preorder(node.left)
        self.walk_preorder(node.right)

    def walk_inorder(self, node):
        if node is None:
            return
        self.walk_inorder(node.left)
        self.order_list.append(node.key)
        self.walk_inorder(node.right)

    def print_nodes(self):
        self.order_list = []
        self.walk_inorder(self.root)
        inorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(inorder_str))
        self.order_list = []
        self.walk_preorder(self.root)
        preorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(preorder_str))

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

n = int(input())
tree = BinarySearchTree()
for _ in range(n):
    command = input().split(' ')
    if len(command) == 1:
        tree.print_nodes()
    else:
        opecode, operand = command[0], int(command[1])
        node = Node(operand)
        tree.insert(node)