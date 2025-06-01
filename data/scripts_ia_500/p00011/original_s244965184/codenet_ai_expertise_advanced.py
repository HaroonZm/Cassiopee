from sys import stdin
n, m, *lines = map(str.rstrip, stdin)
edges = [tuple(map(int, line.split(','))) for line in lines[:int(m)]]
for i in range(1, int(n)+1):
    cur = i
    for a, b in reversed(edges):
        if cur == a: cur = b
        elif cur == b: cur = a
    print(cur)