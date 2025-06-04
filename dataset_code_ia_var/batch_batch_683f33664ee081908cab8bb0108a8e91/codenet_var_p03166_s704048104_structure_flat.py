import numpy as np
import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    d[x - 1].append(y - 1)
dp = [0 for _ in range(N)]
Max = 0
for start in range(N):
    stack = [(start, 0)]
    visited = []
    scores = []
    while stack:
        now, score = stack.pop()
        if dp[now] == 0 and d[now]:
            all_done = True
            max_s = None
            for nxt in d[now]:
                if dp[nxt] == 0:
                    stack.append((now, score))
                    stack.append((nxt, score + 1))
                    all_done = False
                    break
            if all_done:
                _score = []
                for nxt in d[now]:
                    _score.append(dp[nxt] - score)
                dp[now] = max(_score)
                result = dp[now] + score
                if not visited or visited[-1] != (now, score):
                    visited.append((now, score, result))
            continue
        elif not d[now]:
            result = score
            dp[now] = 0
            if not visited or visited[-1] != (now, score):
                visited.append((now, score, result))
            continue
        else:
            result = dp[now] + score
            if not visited or visited[-1] != (now, score):
                visited.append((now, score, result))
    if visited:
        m = max(v[2] for v in visited if v[0] == start)
    else:
        m = 0
    if m > Max:
        Max = m
print(Max)