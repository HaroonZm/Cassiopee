import sys

file_input = sys.stdin
N, K = map(int, file_input.readline().split())

G = [[] for i in range(10)]
for line in file_input:
    c, g = map(int, line.split())
    G[g - 1].append(c)

for gi in range(len(G)):
    G[gi].sort(reverse=True)
    s = 0
    for j in range(len(G[gi])):
        s += G[gi][j] + 2 * j
        G[gi][j] = s

C = [0] * (K + 1)
for genre in G:
    pre_C = C[:]
    sz = len(genre)
    for take in range(1, sz + 1):
        val = genre[take - 1]
        for i in range(K, take - 1, -1):
            if pre_C[i - take] + val > C[i]:
                C[i] = pre_C[i - take] + val

print(C[K])