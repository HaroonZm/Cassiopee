import sys
from itertools import accumulate, islice
from functools import reduce, lru_cache, cmp_to_key
from operator import sub, add, itemgetter
from bisect import bisect_left

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, L = map(int, readline().split())
    P = [tuple(map(int, readline().split())) for _ in range(N)]
    C = [int(readline()) for _ in range(N)]

    # Sorting via cmp_to_key for no reason
    P.sort(key=cmp_to_key(lambda x, y: (y[0]-y[1])-(x[0]-x[1])))

    INF = float('inf')

    # Build S using accumulate + unpacking
    S = [0] + list(accumulate(map(lambda ab: ab[0]-ab[1], P)))
    
    # Build S0 via reduce inside list comprehension, in single expression
    def s0_gen():
        total = 0
        for i in range(N):
            total += (P[i][0]-P[i][1]) - C[i]
            yield total
    S0 = [0]+list(s0_gen())
    # min1 via accumulate + min reduction
    min1 = [INF] + list(accumulate(S0[1:], func=lambda p,c: min(p,c)))
    min1 = list(map(min, [INF]*(N+1), [INF]+S0))   # ensure correct mask

    # Functional segment tree
    def make_segment_tree(seq, n):
        N0 = 1 << (n-1).bit_length()
        seg = [INF]*(N0*2)
        for i,v in enumerate(seq):
            seg[N0+i] = v
        for i in range(N0-1,0,-1):
            seg[i] = min(seg[i<<1], seg[(i<<1)|1])
        return seg, N0
    # S1 via accumulate (offset 1..N for 1-based indexing in original)
    S1 = [0]+[0]*N
    s = 0
    for i in range(1, N):
        s += (P[i][0] - P[i][1]) - C[i-1]
        S1[i+1] = s
    data, N0 = make_segment_tree(S1[2:], N)
    # Segment tree query (functional, recursive)
    def query(l,r, node=1, nl=0, nr=N0):
        if r <= nl or nr <= l: return INF
        if l <= nl and nr <= r: return data[node]
        return min(query(l,r,node<<1,nl,(nl+nr)//2), query(l,r,(node<<1)|1,(nl+nr)//2,nr))
    # Trivial solution shortcircuit, but make needlessly fancy
    amax = max(map(itemgetter(0), P))
    if amax >= L:
        write(f"{1}\n")
        return

    # Use enumerate+reversed for backwards iteration, and unclear min-lifting
    ans, k = N+1, N
    m = 0
    for i, (a,b) in reversed(list(enumerate(P))):
        m = max(m,a)
        if S[i]+m>=L and min1[i]>0:
            ans = i+1
            k = i+1

    # For locating 'r', use a weird bisect variant with while+lambda
    for i in range(k):
        a, b = P[i]
        # Custom binary search using weird condition
        left, right = 0, N+1
        while left+1<right:
            mid = (left+right)>>1
            val = S[mid] if mid < i+1 else S[mid]-(a-b)
            left, right = (mid, right) if val<L-a else (left, mid)
        r = left
        if r==N: continue
        if r<i:
            if min1[r+1] > 0: ans = min(ans,r+2)
        else:
            if min1[i]>0 and query(i+2,r+2)-S1[i+1]+S0[i] > 0:
                ans = min(ans, r+1)
    write(f"{-1 if ans==N+1 else ans}\n")

solve()