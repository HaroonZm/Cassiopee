import heapq
from itertools import accumulate, islice

def solve():
    n, *a = map(int, open(0).read().split())
    hq1 = a[:n]
    hq2 = [-x for x in a[-n:]]
    heapq.heapify(hq1)
    heapq.heapify(hq2)
    su1 = sum(hq1)
    su2 = -sum(hq2)
    mem1 = [su1]
    mem2 = [su2]
    for x in a[n:2*n]:
        y = heapq.heappop(hq1)
        if x > y:
            su1 += x - y
            heapq.heappush(hq1, x)
        else:
            heapq.heappush(hq1, y)
        mem1.append(su1)
    for x in reversed(a[n:2*n]):
        y = -heapq.heappop(hq2)
        if x < y:
            su2 -= (y - x)
            heapq.heappush(hq2, -x)
        else:
            heapq.heappush(hq2, -y)
        mem2.append(su2)
    print(max(map(lambda fb: fb[0] - fb[1], zip(mem1, reversed(mem2)))))

solve()