import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
edges = set()
for _ in range(m):
    i_, j_ = map(int, input().split())
    adj[i_].append(j_)
    indeg[j_] += 1
    edges.add((i_, j_))

from collections import deque

# Topological sort with uniqueness check
q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

res = []
unique = True
while q:
    if len(q) >= 2:  # multiple choices => multiple topological orders possible
        unique = False
    u = q.popleft()
    res.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

# Check if topological order is complete
if len(res) < n:
    # This means input contradicts info, but problem does not specify what then
    # Still, output any order and 0 to satisfy format (or could print nothing or error)
    # But problem assumes consistent input, so no cycle expected
    pass

# The problem expects order by ranks from 1 to n.
# According to the problem, the team ranked a should beat team ranked b if a < b.
# The topological order gives an order where edges i->j means i ranked higher than j.
# So just print res as rank order.

print('\n'.join(map(str, res)))
print(0 if unique else 1)