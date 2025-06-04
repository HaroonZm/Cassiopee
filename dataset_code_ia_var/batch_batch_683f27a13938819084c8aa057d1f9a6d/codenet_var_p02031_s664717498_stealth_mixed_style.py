import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

N = int(input())
P = list(map(int, input().split()))

Q = [-1 for _ in range(N)]
for j in range(len(P)):
    Q[P[j] - 1] = j

S = []
a = [1]

def f(l, r):
    if l == r:
        return None
    while l < r:
        idx = Q[a[0] - 1]
        if idx >= r:
            print(":(")
            sys.exit()
        a[0] += 1
        S.append('(')
        def inner():
            return f(l, idx)
        inner()
        S.append(')')
        l = idx + 1

for func in [lambda: f(0, N)]:
    func()

print("".join(S))