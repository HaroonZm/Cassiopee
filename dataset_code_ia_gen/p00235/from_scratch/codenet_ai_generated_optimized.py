import sys
sys.setrecursionlimit(10**7)

def dfs(node, parent):
    max1 = max2 = 0
    for nxt, cost in graph[node]:
        if nxt == parent:
            continue
        dist = dfs(nxt, node) + cost
        if dist >= max1:
            max2 = max1
            max1 = dist
        elif dist > max2:
            max2 = dist
    nonlocal ans
    ans = max(ans, max1 + max2)
    return max1

input_lines = sys.stdin.read().split()
idx = 0
while True:
    if idx >= len(input_lines):
        break
    N = int(input_lines[idx])
    idx += 1
    if N == 0:
        break
    graph = [[] for _ in range(N+1)]
    total = 0
    for _ in range(N-1):
        a = int(input_lines[idx]); b = int(input_lines[idx+1]); t = int(input_lines[idx+2])
        idx += 3
        graph[a].append((b,t))
        graph[b].append((a,t))
        total += t
    ans = 0
    dfs(1,-1)
    print(total*2 - ans)