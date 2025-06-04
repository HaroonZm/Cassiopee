import heapq

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    m = 2 * 10 ** 5
    infinity = 10 ** 18
    from collections import defaultdict
    table = []
    for _ in range(n+1):
        table.append([infinity]*(m+1))
    q = []
    heapq.heappush(q, (0, 0, 1))
    while len(q):
        cur = heapq.heappop(q)
        c, indx, val = cur[0], cur[1], cur[2]
        if indx == n:
            break
        if table[indx][val] < c - 1e-10:
            continue
        aa = arr[indx]
        # using functional style for the next step
        def go():
            for k in range(val, m+1, val):
                d2 = max(c, abs(k-aa)*1.0/aa)
                if table[indx+1][k] > d2:
                    table[indx+1][k] = d2
                    heapq.heappush(q, (d2, indx+1, k))
        go()
    # imperative min search
    best = infinity
    j = 0
    while j <= m:
        if table[n][j] < best:
            best = table[n][j]
        j += 1
    return best

print("{:.16f}".format(solve()))