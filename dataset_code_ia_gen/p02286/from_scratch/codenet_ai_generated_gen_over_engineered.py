import sys
import threading
from abc import ABC, abstractmethod
sys.setrecursionlimit(10**7)
threading.stack_size(1<<27)

class ITreapNode(ABC):
    @property
    @abstractmethod
    def key(self): pass
    @property
    @abstractmethod
    def priority(self): pass
    @property
    @abstractmethod
    def left(self): pass
    @property
    @abstractmethod
    def right(self): pass

    @left.setter
    @abstractmethod
    def left(self, node): pass

    @right.setter
    @abstractmethod
    def right(self, node): pass

class TreapNode(ITreapNode):
    __slots__ = ('_key', '_priority', '_left', '_right')
    def __init__(self, key, priority):
        self._key = key
        self._priority = priority
        self._left = None  # TreapNode or None
        self._right = None

    @property
    def key(self):
        return self._key

    @property
    def priority(self):
        return self._priority

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

class TreapOperations(ABC):
    @abstractmethod
    def insert(self, t: ITreapNode, key: int, priority: int) -> ITreapNode: pass
    @abstractmethod
    def delete(self, t: ITreapNode, key: int) -> ITreapNode: pass
    @abstractmethod
    def find(self, t: ITreapNode, key: int) -> bool: pass
    @abstractmethod
    def inorder(self, t: ITreapNode) -> list[int]: pass
    @abstractmethod
    def preorder(self, t: ITreapNode) -> list[int]: pass

class TreapAlgorithm(TreapOperations):
    NIL = None

    def rightRotate(self, t: ITreapNode) -> ITreapNode:
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def leftRotate(self, t: ITreapNode) -> ITreapNode:
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, t: ITreapNode, key: int, priority: int) -> ITreapNode:
        if t is self.NIL or t is None:
            return TreapNode(key, priority)
        if key == t.key:
            return t
        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.leftRotate(t)
        return t

    def find(self, t: ITreapNode, key: int) -> bool:
        while t is not self.NIL and t is not None:
            if key == t.key:
                return True
            if key < t.key:
                t = t.left
            else:
                t = t.right
        return False

    def delete(self, t: ITreapNode, key: int) -> ITreapNode:
        if t is self.NIL or t is None:
            return t
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            t = self._delete(t)
        return t

    def _delete(self, t: ITreapNode) -> ITreapNode:
        if (t.left is self.NIL or t.left is None) and (t.right is self.NIL or t.right is None):
            return self.NIL
        if t.left is self.NIL or t.left is None:
            t = self.leftRotate(t)
        elif t.right is self.NIL or t.right is None:
            t = self.rightRotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self.delete(t, t.key)

    def inorder(self, t: ITreapNode) -> list[int]:
        res = []
        def dfs(node):
            if node is self.NIL or node is None:
                return
            dfs(node.left)
            res.append(node.key)
            dfs(node.right)
        dfs(t)
        return res

    def preorder(self, t: ITreapNode) -> list[int]:
        res = []
        def dfs(node):
            if node is self.NIL or node is None:
                return
            res.append(node.key)
            dfs(node.left)
            dfs(node.right)
        dfs(t)
        return res

class TreapContext:
    def __init__(self):
        self._impl = TreapAlgorithm()
        self._root = None

    def insert(self, k: int, p: int) -> None:
        self._root = self._impl.insert(self._root, k, p)
    def delete(self, k: int) -> None:
        self._root = self._impl.delete(self._root, k)
    def find(self, k: int) -> bool:
        return self._impl.find(self._root, k)
    def print_tree(self) -> tuple[list[int], list[int]]:
        return self._impl.inorder(self._root), self._impl.preorder(self._root)

def main():
    input = sys.stdin.readline
    m = int(input())
    treap = TreapContext()
    output = []
    for _ in range(m):
        line = input().rstrip()
        if line == 'print':
            inorder, preorder = treap.print_tree()
            output.append(' ' + ' '.join(map(str,inorder)))
            output.append(' ' + ' '.join(map(str,preorder)))
        else:
            cmd, *args = line.split()
            if cmd == 'insert':
                k, p = map(int, args)
                treap.insert(k, p)
            elif cmd == 'find':
                k = int(args[0])
                output.append('yes' if treap.find(k) else 'no')
            elif cmd == 'delete':
                k = int(args[0])
                treap.delete(k)
    print('\n'.join(output))

threading.Thread(target=main).start()