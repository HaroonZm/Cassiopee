from sys import stdout
from heapq import heapify, heappop, heappush

def Q(x):
    print("?", x, flush=True)
    return int(input())

x = Q("A")
if x == 128:
    L = 128
else:
    y = Q("A" * x)
    z = Q("A" * (x + 1))
    L = x + 1 if z == y else x

S = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
K = [L - Q(s * L) for s in S]

A = [(k, s * k) for k, s in zip(K, S)]
heapify(A)

while len(A) > 1:
    x, y = heappop(A)
    if x == 0:
        continue
    z, w = heappop(A)
    ind = 0
    for ch in w:
        while Q(y[:ind] + ch + y[ind:]) >= L - x - w.index(ch):
            ind += 1
        y = y[:ind] + ch + y[ind:]
        ind += 1
    heappush(A, (x + z, y))

print("!", A[0][1], flush=True)