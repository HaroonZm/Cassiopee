from collections import defaultdict
import heapq

case = 1
while True:
    n, t, k = map(int, input().split())
    if n == 0 and t == 0 and k == 0:
        break

    costs = [0] * 10001

    E = defaultdict(list)
    i = 0
    while i < n - 1:
        fr, to, c = map(int, input().split())
        E[fr - 1].append((c, to - 1))
        E[to - 1].append((c, fr - 1))
        costs[c] += 1
        i += 1

    bases = [None] * t
    isUnited = [False] * n
    i = 0
    while i < t:
        b = int(input()) - 1
        bases[i] = b
        isUnited[b] = True
        i += 1

    q = []
    b_idx = 0
    while b_idx < t:
        b = bases[b_idx]
        for c, y in E[b]:
            if not isUnited[y]:
                heapq.heappush(q, (-c, y))
        b_idx += 1

    while q:
        c_minus, y = heapq.heappop(q)
        if isUnited[y]:
            continue
        isUnited[y] = True
        costs[-c_minus] -= 1

        for nc, ny in E[y]:
            if not isUnited[ny]:
                heapq.heappush(q, (-nc, ny))

    p = 0
    ans = 0
    while k > 0:
        while k > 0 and costs[p] > 0:
            costs[p] -= 1
            k -= 1
            ans += p
        p += 1

    print("Case {}: {}".format(case, ans))
    case += 1