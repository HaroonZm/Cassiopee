import sys, heapq, functools, operator

n, *rest = list(map(int, sys.stdin.read().split()))
a = rest[:n]
	
r = functools.reduce(
    lambda acc, i: acc + (
        [] if functools.reduce(lambda l, j: l or a[j]!=a[n-1-j], range(i), False) else [i]
    ),
    range(1, n+1),
    []
)

print(*r)