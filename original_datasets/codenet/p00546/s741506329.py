from collections import deque
import heapq

N,M,K,S = map(int,input().split())
# - N nodes, M edges, K zombie nodes
# - S本以下の道路を使って到達できる街 = 危険な街

P,Q = map(int,input().split())
# - P: not dangerous
# - Q: dangerous

C = []
for _ in range(K):
  C.append(int(input()))
# C[i] = zombie cities

# M rows
adj = [ [] for _ in range(N+1) ]
for _ in range(M):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)

expensive_cities = set()
for c in C:
  q = deque([c])
  step = 0
  visited = [False] * (N+1)

  while q and step <= S:
    l = len(q)
    new_q = deque()

    for _ in range(l):
      node = q.popleft()
      visited[node] = True

      for nei in adj[node]:
        if visited[nei]: continue
        if nei in q or nei in new_q: continue
        if nei in C: continue
        new_q.append(nei)
    
    q = new_q
    step += 1

  for i in range(1, N+1):
    if visited[i] and i not in C:
      expensive_cities.add(i)

# print(expensive_cities)

adj2 = [ [] for _ in range(N+1) ]
for i in range(1, N+1):
  for city in adj[i]:
    if city in C: continue
    if city in expensive_cities:
      adj2[i].append((city,Q))
    else:
      adj2[i].append((city,P))

# print(adj2)

pq = [(0,1)]
dist = [float('inf')] * (N+1)
visited = [False] * (N+1)
dist[1] = 0
while pq:
  d,n = heapq.heappop(pq)
  if n==N: break
  visited[n] = True

  for nei,nd in adj2[n]:
    # import pdb; pdb.set_trace()
    if visited[nei]: continue
    if d+nd < dist[nei]:
      dist[nei] = d+nd
      heapq.heappush(pq, (d+nd,nei))

# print(dist)
d = dist[N]
if N in expensive_cities:
  print(d-Q)
else:
  print(d-P)