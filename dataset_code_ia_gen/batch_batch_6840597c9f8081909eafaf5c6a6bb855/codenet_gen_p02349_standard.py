import sys
input = sys.stdin.readline

n, q = map(int, input().split())
bit = [0]*(n+1)

def add(i, x):
    while i <= n:
        bit[i] += x
        i += i & (-i)

def sum_(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        _, s, t, x = query
        add(s, x)
        if t+1 <= n:
            add(t+1, -x)
    else:
        _, i = query
        print(sum_(i))