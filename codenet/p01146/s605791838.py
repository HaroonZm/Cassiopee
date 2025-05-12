import sys
import heapq

class Dijkstra(object):
  # def dijkstra(self, adj, start, goal=None):
  def dijkstra(self, num, path, start, goal=None):
    # num = len(adj)
    dist = [sys.maxint] * num
    prev = [sys.maxint] * num
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while len(q) != 0:
      prov_cost, src = heapq.heappop(q)
      if dist[src] < prov_cost: continue
      if src not in path: continue
      for dest,cost in path[src]:
        if dist[dest] > dist[src] + cost:
          dist[dest] = dist[src] + cost
          heapq.heappush(q, (dist[dest], dest))
          prev[dest] = src
      # for dest in range(num):
      #   cost = adj[src][dest]
      #   if cost != sys.maxint and dist[dest] > dist[src] + cost:
      #     dist[dest] = dist[src] + cost
      #     heapq.heappush(q, (dist[dest], dest))
      #     prev[dest] = src
    if goal is not None:
      return self.get_path(goal, prev)
    else:
      return dist

  def get_path(self, goal, prev):
    path = [goal]
    dest = goal
    while prev[dest] != sys.maxint:
      path.append(prev[dest])
      dest = prev[dest]
    return list(reversed(path))

while True:
  N,M,L,K,A,H=map(int,raw_input().split())
  if N==0: break
  # t(n,t) : minimum cost to remain t times and reach town n
  Ls=map(int,raw_input().split())
  # edge=[[sys.maxint]*(N*(M+1)) for _ in xrange(N*(M+1))]
  edge={}
  for l in Ls:
    for i in xrange(M):
      edge[l*(M+1)+i]=[(l*(M+1)+i+1,1)]
  for _ in xrange(K):
    s,g,c=map(int,raw_input().split())
    for i in xrange(c,M+1):
      if s*(M+1)+i not in edge: edge[s*(M+1)+i]=[]
      if g*(M+1)+i not in edge: edge[g*(M+1)+i]=[]
      edge[s*(M+1)+i].append((g*(M+1)+i-c,c))
      edge[g*(M+1)+i].append((s*(M+1)+i-c,c))
  cost=Dijkstra().dijkstra(N*(M+1), edge, A*(M+1)+M)
  minCost=sys.maxint
  for i in xrange(M+1):
    minCost=min(minCost,cost[H*(M+1)+i])
  if minCost==sys.maxint: print "Help!"
  else: print minCost