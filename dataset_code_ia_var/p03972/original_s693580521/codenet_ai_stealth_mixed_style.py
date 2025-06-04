from heapq import heappush as hpush, heappop as hpop

from sys import stdin

pq = list()
W_H = stdin.readline().split()
w = int(W_H[0])
h = int(W_H[1])
i = 0
while i < w:
    hpush(pq, (int(stdin.readline()), "W"))
    i = i + 1
[j for j in range(h) if not hpush(pq, (int(stdin.readline()), "H"))]

w += 1
h += 1

A = 0
def solve():
    global w, h, A
    while len(pq):
        e = hpop(pq)
        kind = e[1]
        val = e[0]
        match kind:
            case "W":
                A = A + val * h
                w -= 1
            case _:
                A += val * w
                h -= 1
solve()
print(A)