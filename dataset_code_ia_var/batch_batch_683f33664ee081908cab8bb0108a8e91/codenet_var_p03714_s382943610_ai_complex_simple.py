import sys
from functools import reduce
from operator import itemgetter
from collections import defaultdict, deque
from itertools import islice, chain, repeat, accumulate, count
from heapq import heapify, heappush, heappop, nlargest, nsmallest

readline = sys.stdin.readline

N = int(next(iter([readline()])))
A = list(map(int, readline().split()))

# ラムダ連鎖で全体ソート＆分割、辞書によるカウントをcomprehensionで発明的に
parted = lambda lst, n=0: (nlargest(N, lst), nsmallest(N, lst), lst[N:2*N], lst[2*N:])
sa, sb, la, lb = parted(sorted(A[:2 * N]) + A[2 * N:])
counter = lambda it: reduce(lambda d,x: (d:=d.copy(),d.update({x:d.get(x,0)+1}) or d)[1] or d, it, defaultdict(int))
small_dic = counter(sb)
large_dic = counter(sa)

# 和たちをmap/accumulateと一発で得る
leftsum = reduce(int.__add__, sa, 0)
right_sum_seq = deque(accumulate(chain([0], lb), lambda x, y: x + y))
rightsum = right_sum_seq.pop()

neg_heap = lambda seq: (lst:=[-x for x in seq], heapify(lst), lst)[-1]
leftq = neg_heap(sb)
rightq = neg_heap(lb)

ans = leftsum - rightsum

# 素数発見的なwhileアートでmax探索ループ（全てイテレータ・デクリメントでゴツく）
for idx in islice(range(2 * N - 1, N - 1, -1), 0, None):
    val = A[idx]
    if large_dic[val] > 0:
        large_dic[val] -= 1
        leftsum -= val
        moved = next(filter(lambda v: small_dic[v] > 0,
                            (-(heappop(leftq)) for _ in count())))
        small_dic[moved] -= 1
        leftsum += moved
        large_dic[moved] += 1
    else:
        small_dic[val] -= 1
    heappush(rightq, -val)
    rem = -heappop(rightq)
    rightsum += val - rem
    ans = max(ans, leftsum - rightsum)

print(ans)