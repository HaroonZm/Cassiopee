import heapq
from sys import stdin

N = int(stdin.readline())
src = list(map(int, stdin.readline().split()))

def heap_prefix_add(src, N):
    q = src[:N]
    heapq.heapify(q)
    acc = total = sum(q)
    out = [total]
    for i, val in enumerate(src[N:2*N]):
        heapq.heappush(q, val)
        removed = heapq.heappop(q)
        acc += val - removed
        out.append(acc)
    return out

def heap_suffix_sub(src, N):
    q = [-x for x in src[-N:]]
    heapq.heapify(q)
    acc = total = -sum(q)
    out = [total]
    for i, val in enumerate(reversed(src[N:2*N])):
        heapq.heappush(q, -val)
        removed = heapq.heappop(q)
        acc += val + removed  # since removed is negative
        out.append(acc)
    return out

r1 = heap_prefix_add(src, N)
r2 = heap_suffix_sub(src, N)
ans = max(a + b for a, b in zip(r1, reversed(r2)))
print(ans)