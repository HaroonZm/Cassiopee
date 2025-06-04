from sys import stdin
from functools import reduce

n, m = map(int, stdin.readline().split())
parent = list(range(n))

def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while x != root:
        parent[x], x = root, parent[x]
    return root

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    parent[find(b - 1)] = find(a - 1)

groups = [find(i) for i in range(n)]
from collections import Counter
count = Counter(groups)

num_components = len(count)
num_singletons = sum(v == 1 for v in count.values())
num_nontrivial = num_components - num_singletons

print(abs(2 * num_nontrivial - num_singletons))