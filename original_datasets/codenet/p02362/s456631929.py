import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

INF = int(1e18)

class BellmanFord:
  N = -1
  edge = []
  
  def __init__(self, N):
    self.N = N
  
  def addEdge(self, a, b, cost):
    self.edge.append((a, b, cost))
  
  def addBiEdge(self, a, b, cost):
    self.addEdge(a, b, cost)
    self.addEdge(b, a, cost)

  def calc(self, start):
    dist = [INF] * self.N
    dist[start] = 0
    update = True
    cnt = 0
    while update:
      update = False
      cnt += 1
      if cnt > self.N:
        return -INF
      for a, b, cost in self.edge:
        ncost = dist[a] + cost
        if dist[a] == INF or ncost >= dist[b]:
          continue
        dist[b] = ncost
        update = True
    return dist

def main():
  v, e, r = na()
  BF = BellmanFord(v)
  for _ in range(e):
    BF.addEdge(*na())

  ans = BF.calc(r)
  if ans == -INF:
    print("NEGATIVE CYCLE")
  else:
    for i in range(v):
      print('INF' if ans[i] == INF else ans[i])

main()