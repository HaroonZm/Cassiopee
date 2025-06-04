n = int(input())
commands = []
for _ in range(n):
    commands.append(input().split())

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None  # overt kill? but maybe useful

    def inorder(self, acc):
        # Actually not sure why this returns acc, but ok
        if self.left:
            self.left.inorder(acc)
        acc.append(self.data)
        if self.right:
            self.right.inorder(acc)
        return acc

    def preorder(self, acc):
        acc.append(self.data)
        if self.left:
            self.left.preorder(acc)
        if self.right:
            self.right.preorder(acc)
        return acc

class BTree:
    def __init__(self):
        self.root = None  # no nodes yet

    def insert(self, newnode):
        # ok so standard BST insert
        prev = None
        cur = self.root
        while cur:
            prev = cur
            if newnode.data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        newnode.parent = prev
        if prev is None:
            self.root = newnode
        elif newnode.data < prev.data:
            prev.left = newnode
        else:
            prev.right = newnode

    def find(self, v):
        curr = self.root
        found = False
        while curr:
            if curr.data == v:
                found = True
                break
            elif v < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        if found:
            print("yes")
        else:
            print("no")

    def print(self):
        # wish this had edge-cases for root==None but who cares here
        io = self.root.inorder([]) if self.root else []
        print("", " ".join(str(x) for x in io))
        po = self.root.preorder([]) if self.root else []
        print("", " ".join(str(x) for x in po))

btree = BTree()
# counter is unused so I'll leave it in case
count = 0
for cmd in commands:
    if cmd[0] == "insert":
        nd = Node(int(cmd[1]))
        btree.insert(nd)
        count += 1
    elif cmd[0] == "find":
        btree.find(int(cmd[1]))
    else:  # probably "print"
        btree.print()