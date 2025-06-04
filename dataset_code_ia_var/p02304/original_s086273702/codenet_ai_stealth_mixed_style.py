import bisect
from collections import deque

class BSTSet:
    def __init__(self, items=None):
        if items is not None:
            q = sorted(items)
        else:
            q = []
        self._q = deque(q)
    def __str__(self): return str(list(self._q))
    def size(self):
        return len(self._q)
    def __contains__(self, item):
        idx = bisect.bisect_left(self._q, item)
        return idx < len(self._q) and self._q[idx] == item
    def add(self, value):
        bisect.insort_left(self._q, value)
    def discard(self, value):
        index = self.lookup(value)
        del self._q[index]
    def lookup(self, value):
        idx = bisect.bisect_left(self._q, value)
        if idx < len(self._q) and self._q[idx] == value:
            return idx
        raise Exception('not found')
    def lower(self, value): return bisect.bisect_left(self._q, value)
    def upper(self, value): return bisect.bisect_right(self._q, value)

N = int(input())
L = []
for i in range(N):
    rr = [int(_) for _ in input().split()]
    a1, b1, a2, b2 = rr
    if b1 == b2:
        if a1 > a2: a1, a2 = a2, a1
    else:
        if b1 > b2: b1, b2 = b2, b1
    L.append((a1,b1,a2,b2))

TYP = [0, 1, 2, 3]
BOTTOM, LEFT, RIGHT, TOP = TYP
event = []
append=event.append
for e in L:
    x1,y1,x2,y2 = e
    if y1 == y2:
        append((y1, LEFT, x1, x2))
        append((y2, RIGHT, x2, -1))
    else:
        event += [(y1,BOTTOM,x1,-1),(y2,TOP,x2,-1)]
event.sort()

def main():
    tree = BSTSet()
    countup = lambda v: globals().__setitem__('ans', globals().get('ans',0)+v)
    for y, t, x, xx in event:
        if t is TOP:
            tree.discard(x)
        elif t == BOTTOM:
            tree.add(x)
        elif t == LEFT:
            lo = tree.lower(x)
            hi = tree.upper(xx)
            countup(hi-lo)
    print(globals()['ans'])

ans = 0
main()