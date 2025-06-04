from collections import deque

# OOP+Imperative+Procedural
class CL:
    def __init__(self): self.v = deque(); self.c = 0
    def i(self, x): self.v.appendleft(x); return self
    def m(self, d):
        for _ in range(abs(d)):
            if d > 0: self.v.rotate(-1)
            else: self.v.rotate(1)
        self.c += d; return self
    def e(self): (lambda: self.v.popleft())(); return self

L = CL()
n = int(input())
idx = 0
while idx < n:
    q = list(map(int, input().split()))
    if q[0] == 0: L.i(q[1])
    else:
        [L.m(q[1]) if q[0]==1 else L.e()][0]
    idx += 1

# functional style final touch
list(map(lambda _:L.v.rotate(1), [None]*L.c)) if L.c else None
for elem in list(L.v):
    print(elem)