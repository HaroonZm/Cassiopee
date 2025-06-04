import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder(self, u, res):
        if u is None:
            return
        self.inorder(u.left, res)
        res.append(u.key)
        self.inorder(u.right, res)

    def preorder(self, u, res):
        if u is None:
            return
        res.append(u.key)
        self.preorder(u.left, res)
        self.preorder(u.right, res)

bst = BST()
m = int(input())
for _ in range(m):
    line = input().split()
    if line[0] == "insert":
        k = int(line[1])
        node = Node(k)
        bst.insert(node)
    else:
        inorder_res = []
        preorder_res = []
        bst.inorder(bst.root, inorder_res)
        bst.preorder(bst.root, preorder_res)
        print(" " + " ".join(map(str, inorder_res)))
        print(" " + " ".join(map(str, preorder_res)))