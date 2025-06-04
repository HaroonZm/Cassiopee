import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = (line.rstrip() for line in sys.stdin).__next__

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

flag = [0] * n

# Iterative DFS to avoid recursion:
stack = [(0, -1, 0)]
while stack:
    cur, par, f = stack.pop()
    flag[cur] = f
    stack.extend((to, cur, f ^ 1) for to in G[cur] if to != par)

one, two, three = (deque(range(x, n+1, 3)) for x in (1, 2, 3))
k = n // 3
a = sum(flag)
b = n - a
ans = [0] * n

groups = [one, two, three]

if k < a and k < b:
    for i, f in enumerate(flag):
        preferred = groups[1 if f else 2]
        secondary = groups[0]
        if preferred:
            ans[i] = preferred.popleft()
        else:
            ans[i] = secondary.popleft()
else:
    major_group, minor_group = (flag, 0) if k >= a else ([1-x for x in flag], 1)
    three_group = groups[2]
    for i, f in enumerate(flag):
        if f == minor_group:
            ans[i] = three_group.popleft()
    res = deque(one) + deque(two) + three_group
    for i, f in enumerate(flag):
        if f != minor_group:
            ans[i] = res.popleft()

print(*ans)