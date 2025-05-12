from operator import itemgetter
import heapq
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
X.sort(key=itemgetter(0))
Y.sort(key=itemgetter(0))
G = [[] for _ in range(N)]
for i in range(N-1):
    G[X[i][1]].append((X[i+1][0]-X[i][0], X[i+1][1]))
    G[X[i+1][1]].append((X[i+1][0]-X[i][0], X[i][1]))
    G[Y[i][1]].append((Y[i+1][0]-Y[i][0], Y[i+1][1]))
    G[Y[i+1][1]].append((Y[i+1][0]-Y[i][0], Y[i][1]))

q = []
heapq.heapify(q)
for elem in G[0]:
    heapq.heappush(q, elem)
used = [False] * N
used[0] = True
ans = 0
while q:
    res = heapq.heappop(q)
    cost, nq = res
    if not used[nq]:
        used[nq] = True
        ans += cost
        for elem in G[nq]:
            heapq.heappush(q, elem)
print(ans)