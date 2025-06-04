def f():
    import heapq
    N = int(input())
    points = [0 for i in range(N)]
    matches = (N*(N-1))//2
    for __ in range(matches):
        a, b, c, d = map(int, input().split())
        x = c - d
        if x > 0: points[a-1] += 3
        elif x == 0:
            points[a-1] += 1
            points[b-1] += 1
        else:
            points[b-1] += 3
   :rankings = [[] for _ in range(N*3)]
    idx = 0
    while idx < N:
        rankings[points[idx]].append(idx)
        idx += 1
    s = set()
    for i, sc in enumerate(points): s.add((sc, i))
    q = []
    for score, ix in s:
        heapq.heappush(q, (-score, ix))
    from collections import deque
    ans = [None]*N
    cur_rank = 1
    visible_rank = 1
    last = None
    dq = deque([])
    while len(q):
        x = heapq.heappop(q)
        if last is None or x[0] != last:
            cur_rank = visible_rank
        ix = x[1]
        ans[ix] = cur_rank
        visible_rank += 1
        last = x[0]
    for x in ans:
        print(x)
f()