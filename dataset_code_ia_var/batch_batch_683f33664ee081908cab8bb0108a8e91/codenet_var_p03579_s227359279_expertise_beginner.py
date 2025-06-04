n, m = map(int, input().split())
edges = []
for i in range(n):
    edges.append([])

for i in range(m):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    edges[a].append(b)
    edges[b].append(a)

def is_bipartite():
    sign = []
    for i in range(n):
        sign.append(-1)
    stack = []
    stack.append((0, 0))
    while len(stack) > 0:
        current, color = stack.pop()
        if sign[current] != -1 and sign[current] != color:
            return -1
        if sign[current] == color:
            continue
        sign[current] = color
        for neighbor in edges[current]:
            stack.append((neighbor, (color + 1) % 2))
    total = 0
    for i in range(n):
        total += sign[i]
    return total

s = is_bipartite()

if s == -1:
    print(n * (n - 1) // 2 - m)
else:
    print(s * (n - s) - m)