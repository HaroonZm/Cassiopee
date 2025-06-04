import sys, collections
N, E = tuple(map(int, sys.stdin.readline().split()))
INF = float('inf')
distances = [[INF]*N for _ in range(N)]
for i in range(N):
    distances[i][i] = 0
for _ in range(E):
    s, d, w = map(int, sys.stdin.readline().rstrip().split())
    distances[s][d] = w
k = 0
while k < N:
    i = 0
    while i < N:
        j = 0
        while j < N:
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
            j += 1
        i += 1
    k += 1
i = 0
while i < N:
    if distances[i][i] < 0:
        print("NEGATIVE CYCLE")
        sys.exit()
    i += 1
i = 0
while i < N:
    j = 0
    s = []
    while j < N:
        if distances[i][j] == INF:
            s.append("INF")
        else:
            s.append(str(distances[i][j]))
        j += 1
    print(" ".join(s))
    i += 1