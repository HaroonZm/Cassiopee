import heapq
from itertools import accumulate, islice

def min_k_sum(seq, k):
    heap, total, res = [], 0, []
    for idx, val in enumerate(seq):
        heapq.heappush(heap, val)
        total += val
        if idx >= k:
            total -= heapq.heappop(heap)
        if idx >= k - 1:
            res.append(total)
    return res

N = int(input())
a = list(map(int, input().split()))

ltotal = min_k_sum(a, N)
rtotal = min_k_sum((-x for x in reversed(a)), N)
rtotal = [ -x for x in rtotal ]

ans = max(l + r for l, r in zip(ltotal, reversed(rtotal)))
print(ans)