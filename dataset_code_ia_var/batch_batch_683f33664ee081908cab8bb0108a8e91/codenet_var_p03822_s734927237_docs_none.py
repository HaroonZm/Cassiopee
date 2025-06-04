from collections import defaultdict
import sys
sys.setrecursionlimit(110000)

def dfs(i):
    if i not in H:
        return 0
    if memo[i] >= 0:
        return memo[i]
    a = sorted(-dfs(e) for e in H[i])
    memo[i] = max(i + 1 - a[i] for i in range(len(a)))
    return memo[i]

N = int(sys.stdin.readline())
memo = [-1] * N
H = defaultdict(list)
for i in range(N - 1):
    H[int(sys.stdin.readline()) - 1].append(i + 1)
dfs(N // 2)
print(dfs(0))