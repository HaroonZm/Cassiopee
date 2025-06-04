from functools import reduce, lru_cache, partial
from itertools import chain, count, islice, tee, accumulate as acc
from operator import add, itemgetter
from types import SimpleNamespace
from collections import deque, defaultdict
from copy import deepcopy
from random import random
import sys
input = lambda: sys.stdin.readline()

def identity(x): return x
def k_combinator(x): return lambda _: x
def S(f): return lambda g: lambda x: f(x)(g(x))

def nested_getitem(obj, idxs):
    return reduce(lambda o, idx: o[idx], idxs, obj)

def traverse_in_order(node, acc=[]):
    if node and hasattr(node, '__getitem__'):
        traverse_in_order(node[0], acc)
        acc.append(node[2])
        traverse_in_order(node[1], acc)
    return acc

def traverse_pre_order(node, acc=[]):
    if node and hasattr(node, '__getitem__'):
        acc.append(node[2])
        traverse_pre_order(node[0], acc)
        traverse_pre_order(node[1], acc)
    return acc

def build_path(node, pred):
    path = []
    while node and pred(node):
        path.append(node)
        node = node[1 if pred(node) else 0]
    return path

class Treap:
    class _Node(list):
        __slots__ = ()
        def __init__(self, l, r, k, p, d, s): super().__init__([l, r, k, p, d, s])
        def __repr__(self): return f"({self[2]},p={self[3]})"

    def __init__(self, iterable=None):
        self.root = None
        self.node = Treap._Node
        if iterable:
            reduce(lambda _, x: self.insert(x), iterable, None)

    @staticmethod
    @lru_cache(None)
    def _count(node): return node[4] if node else 0

    @staticmethod
    def _agg_sum(node): return node[5] if node else 0

    @staticmethod
    def _update(node):
        if node:
            node[4] = 1 + Treap._count(node[0]) + Treap._count(node[1])
            node[5] = node[2] + Treap._agg_sum(node[0]) + Treap._agg_sum(node[1])
        return node

    def _rotate(self, node, dir):
        opp = 1 - dir
        child = node[opp]
        if not child: return node
        node[opp], child[dir] = child[dir], node
        self._update(node)
        self._update(child)
        return child

    def __contains__(self, key):
        traverse = lambda n: False if not n else key == n[2] or traverse(n[key > n[2]])
        return traverse(self.root)

    def __getitem__(self, i):
        node = self.root
        N = self._count(node)
        i = i + N if i < 0 else i
        if i >= N or i < 0: raise IndexError
        while node:
            l = self._count(node[0])
            if i == l: return node[2]
            node = node[1] if i > l else node[0]
            i -= l + 1 if i > l else 0

    def __repr__(self):
        q, out = deque([(self.root, 0)]), []
        while q:
            n, d = q.popleft()
            if n: out.append((d, n[2], round(n[3], 4))); q.extend((n[0], d+1)); q.extend((n[1], d+1))
        return "Treap(" + str(out) + ")"

    def sort(self):
        return traverse_in_order(self.root, [])

    def bisect(self, key):
        idx, node = 0, self.root
        while node:
            left = node[0]
            if key >= node[2]:
                idx += self._count(left) + 1
                node = node[1]
            else:
                node = left
        return idx

    def insert(self, key, priority=None):
        priority = random() if priority is None else priority
        path = []; node = self.root
        while node:
            dir = key >= node[2]
            path.append((node, dir))
            node = node[dir]
        newn = self.node(None, None, key, priority, 1, key)
        while path:
            p, dir = path.pop()
            p[dir] = newn
            self._update(p)
            if p[3] >= newn[3]: newn = p; continue
            newn = self._rotate(p, 1 - dir)
        self.root = newn
        return self

    def delete(self, key):
        def descend(node):
            pth = []
            while node and node[2] != key:
                dir = key > node[2]
                pth.append((node, dir))
                node = node[dir]
            return node, pth
        node, path = descend(self.root)
        if not node: return self
        while any(node[:2]):
            l, r = node[0], node[1]
            dir = (not r) or (l and l[3] > r[3])
            node = self._rotate(node, dir)
            path.append((node, dir))
            node = node[dir]
        node = None
        while path:
            p, d = path.pop()
            p[d] = node
            self._update(p)
            node = p
        self.root = node
        return self

    def merge(self, other):
        def _merge(a, b):
            if not a or not b: return a or b
            if a[3] > b[3]:
                a[1] = _merge(a[1], b)
                return self._update(a)
            else:
                b[0] = _merge(a, b[0])
                return self._update(b)
        self.root = _merge(self.root, other.root)
        return self

    def split(self, i):
        def _split(node, k):
            if not node: return (None, None)
            if k <= self._count(node[0]):
                l, r = _split(node[0], k)
                node[0] = r
                return (l, self._update(node))
            else:
                l, r = _split(node[1], k - self._count(node[0]) - 1)
                node[1] = l
                return (self._update(node), r)
        x, y = _split(self.root, i)
        self.root = x
        other = Treap()
        other.root = y
        return other

def print_treap(tr):
    pre, ino = traverse_pre_order(tr.root, []), traverse_in_order(tr.root, [])
    print(' ' + ' '.join(map(str, ino)))
    print(' ' + ' '.join(map(str, pre)))

m = int(input())
tr = Treap()
for _ in range(m):
    query, *args = input().split()
    if query == 'insert':
        k, p = map(int, args)
        tr.insert(k, p)
    elif query == 'find':
        print('yes' if int(args[0]) in tr else 'no')
    elif query == 'delete':
        tr.delete(int(args[0]))
    else:
        print_treap(tr)