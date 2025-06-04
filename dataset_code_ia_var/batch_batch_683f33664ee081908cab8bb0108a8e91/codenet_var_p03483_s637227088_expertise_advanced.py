from collections import Counter, deque
from array import array

class Bit:
    __slots__ = ("size", "tree")
    def __init__(self, n: int):
        self.size = n
        self.tree = array('q', (0 for _ in range(n+2)))
    def __iter__(self):
        s = 0
        get = self.sum
        rng = range(1, self.size+1)
        prev = 0
        for idx in rng:
            cur = get(idx)
            yield cur - prev
            prev = cur
    def __str__(self):
        return str(list(self))
    def sum(self, i: int) -> int:
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        tree = self.tree
        while i:
            s += tree[i]
            i -= i & -i
        return s
    def add(self, i: int, x: int):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        tree, sz = self.tree, self.size
        while i <= sz:
            tree[i] += x
            i += i & -i
    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)
    def __setitem__(self, key, value):
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

S = input()
N = len(S)
cnt = Counter(S)
odds = [c for c,v in cnt.items() if v%2]
if len(odds) > 1:
    print(-1)
    exit()
odd_char = odds[0] if odds else None
halves = {c: v//2 for c,v in cnt.items()}
L = {chr(i+97): deque() for i in range(26)}
n = N//2 + 1
B = []
for c in S:
    if halves[c] == 0:
        if c == odd_char:
            B.append(1)
            odd_char = None
        else:
            B.append(L[c].pop())
    else:
        L[c].append(n)
        B.append(0)
        n -= 1
        halves[c] -= 1
bit = Bit(N//2+2)
ans = 0
for i, b in enumerate(B):
    ans += i - bit.sum(b+1)
    bit.add(b,1)
print(ans)