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

    def inorder(self, x, res):
        if x is not None:
            self.inorder(x.left, res)
            res.append(x.key)
            self.inorder(x.right, res)

    def preorder(self, x, res):
        if x is not None:
            res.append(x.key)
            self.preorder(x.left, res)
            self.preorder(x.right, res)

def main():
    import sys
    input = sys.stdin.readline
    m = int(input())
    T = BST()
    for _ in range(m):
        line = input().strip()
        if line.startswith("insert"):
            _, k = line.split()
            k = int(k)
            node = Node(k)
            T.insert(node)
        elif line == "print":
            inorder_res = []
            preorder_res = []
            T.inorder(T.root, inorder_res)
            T.preorder(T.root, preorder_res)
            print(" ".join(str(x) for x in inorder_res))
            print(" ".join(str(x) for x in preorder_res))

if __name__ == "__main__":
    main()