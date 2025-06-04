from functools import reduce
from operator import itemgetter

n = int(input())
A = list(map(int, input().split()))

def fancy_heap_init(L, sign=1):
    h = list(map(lambda x: sign*x, L))
    heapq.heapify(h)
    return h

def fancy_accumulate(seq, start, end, func, heap_sign=1):
    h = fancy_heap_init(seq[start:end], heap_sign)
    h_sum = sum(map(lambda x: x*heap_sign, h))
    res = [0]*(end-start+1)
    idx = 0 if heap_sign == 1 else -1
    res[idx] = h_sum
    indices = range(end, 2*end) if heap_sign == 1 else range(2*end-1, end-1, -1)
    for i, z in zip(indices, func(indices)):
        val = (A[i]*heap_sign)
        popped = heapq.heappushpop(h, val)
        h_sum += (val - popped)*heap_sign
        idx = i-end+1 if heap_sign == 1 else i-end
        res[idx] = h_sum
    return res

pre = fancy_accumulate(A, 0, n, lambda r: r, 1)
suf = fancy_accumulate(A, 2*n, 3*n, lambda r: r[::-1], -1)

answer = max(map(lambda ic: ic[0]-ic[1], zip(pre, suf)))
print(answer)