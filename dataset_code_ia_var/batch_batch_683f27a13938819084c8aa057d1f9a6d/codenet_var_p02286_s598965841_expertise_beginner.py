import sys
import random

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1

def node_size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = 1 + node_size(node.left) + node_size(node.right)

class Treap:
    def __init__(self):
        self.root = None

    def rotate_left(self, node):
        r = node.right
        node.right = r.left
        r.left = node
        update_size(node)
        update_size(r)
        return r

    def rotate_right(self, node):
        l = node.left
        node.left = l.right
        l.right = node
        update_size(node)
        update_size(l)
        return l

    def _insert(self, node, key, priority):
        if node is None:
            return TreapNode(key, priority)
        if key < node.key:
            node.left = self._insert(node.left, key, priority)
            update_size(node)
            if node.left.priority > node.priority:
                node = self.rotate_right(node)
        else:
            node.right = self._insert(node.right, key, priority)
            update_size(node)
            if node.right.priority > node.priority:
                node = self.rotate_left(node)
        update_size(node)
        return node

    def insert(self, key, priority=None):
        if priority is None:
            priority = random.random()
        self.root = self._insert(self.root, key, priority)

    def _find(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def __contains__(self, key):
        return self._find(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # The node to be deleted is found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.priority > node.right.priority:
                    node = self.rotate_right(node)
                    node.right = self._delete(node.right, key)
                else:
                    node = self.rotate_left(node)
                    node.left = self._delete(node.left, key)
        update_size(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(str(node.key))
            self._inorder(node.right, result)

    def _preorder(self, node, result):
        if node:
            result.append(str(node.key))
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def print_treap(self):
        inorder = []
        preorder = []
        self._inorder(self.root, inorder)
        self._preorder(self.root, preorder)
        print(' ' + ' '.join(inorder))
        print(' ' + ' '.join(preorder))

input = sys.stdin.readline

m = int(input())
tr = Treap()
for _ in range(m):
    parts = input().split()
    if not parts:
        continue
    cmd = parts[0]
    if cmd == "insert":
        key = int(parts[1])
        priority = int(parts[2])
        tr.insert(key, priority)
    elif cmd == "find":
        key = int(parts[1])
        print("yes" if key in tr else "no")
    elif cmd == "delete":
        key = int(parts[1])
        tr.delete(key)
    else:
        tr.print_treap()