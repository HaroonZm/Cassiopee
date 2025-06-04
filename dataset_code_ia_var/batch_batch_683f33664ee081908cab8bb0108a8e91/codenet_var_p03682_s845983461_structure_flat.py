from operator import itemgetter
import heapq

N = int(input())
X = []
Y = []
i = 0
while i < N:
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    X.append((x, i))
    Y.append((y, i))
    i += 1

X.sort(key=itemgetter(0))
Y.sort(key=itemgetter(0))

G = []
i = 0
while i < N:
    G.append([])
    i += 1

i = 0
while i < N-1:
    cost_x = X[i+1][0] - X[i][0]
    a = X[i][1]
    b = X[i+1][1]
    G[a].append((cost_x, b))
    G[b].append((cost_x, a))

    cost_y = Y[i+1][0] - Y[i][0]
    c = Y[i][1]
    d = Y[i+1][1]
    G[c].append((cost_y, d))
    G[d].append((cost_y, c))
    i += 1

q = []
heapq.heapify(q)
i = 0
while i < len(G[0]):
    heapq.heappush(q, G[0][i])
    i += 1

used = []
i = 0
while i < N:
    used.append(False)
    i += 1
used[0] = True

ans = 0
while len(q) > 0:
    res = heapq.heappop(q)
    cost = res[0]
    nq = res[1]
    if not used[nq]:
        used[nq] = True
        ans += cost
        j = 0
        while j < len(G[nq]):
            heapq.heappush(q, G[nq][j])
            j += 1

print(ans)