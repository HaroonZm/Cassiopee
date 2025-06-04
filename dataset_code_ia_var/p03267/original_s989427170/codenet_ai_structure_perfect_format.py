L = int(input())
edges = []

p2 = 1
N = 1

while L >= p2 * 2:
    N += 1
    p2 *= 2
    edges.append((N - 1, N, 0))
    edges.append((N - 1, N, 2 ** (N - 2)))

rest = L - p2
tmp = p2
for i in range(N, -1, -1):
    if (rest >> i) & 1:
        edges.append((i + 1, N, tmp))
        tmp += 2 ** i

M = len(edges)
print(N, M)
for edge in edges:
    print(*edge)