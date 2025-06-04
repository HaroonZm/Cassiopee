from functools import reduce
from operator import add
from collections import deque

n = int(eval('input()'))
a = list(map(int, eval("' '.join([input() for _ in [0]]).split()")))

indices = range(n)
adj = lambda i: a[a[i]-1] == i+1

flags = map(adj, indices)
ans = reduce(add, (int(f) for f in flags), 0)

print(deque([ans//2, ans%2]).popleft())