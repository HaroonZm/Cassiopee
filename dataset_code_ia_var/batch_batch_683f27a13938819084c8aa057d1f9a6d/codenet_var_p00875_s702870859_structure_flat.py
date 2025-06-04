from collections import deque

while True:
    n = int(input())
    if n == 0:
        break

    sub = []
    for _ in range(n):
        sub.append(input().split())
    gamma = input()
    delta = input()

    q = deque()
    q.append((gamma, 0))
    res = 10000
    while q:
        s, i = q.popleft()
        for rule in sub:
            alpha = rule[0]
            beta = rule[1]
            if alpha not in s:
                continue
            t = s.replace(alpha, beta)
            if t == delta:
                if i+1 < res:
                    res = i+1
                continue
            elif len(t) >= len(delta):
                continue
            q.append((t, i+1))
    if res == 10000:
        res = -1
    print(res)