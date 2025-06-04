import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def readints():
    return map(int, input().split())

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = readints()
    tree[a].append((b, c))
    tree[b].append((a, c))

ans = [-1] * (n + 1)
ans[1] = 0
que = deque([1])

while que:
    node = que.popleft()
    cur_col = ans[node]
    for neighbor, weight in tree[node]:
        if ans[neighbor] == -1:
            ans[neighbor] = (cur_col + weight) & 1
            que.append(neighbor)

print(*ans[1:], sep="\n")