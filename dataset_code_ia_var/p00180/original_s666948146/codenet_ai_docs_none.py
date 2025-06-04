class UnionFind:
  def __init__(self, size):
    self.table = [-1 for _ in xrange(size)]

  def find(self, x):
    while self.table[x] >= 0:
      x = self.table[x]
    return x

  def union(self, x, y):
    s1 = self.find(x)
    s2 = self.find(y)
    if s1 != s2:
      if self.table[s1] >= self.table[s2]:
        self.table[s1] += self.table[s2]
        self.table[s2] = s1
      else:
        self.table[s2] += self.table[s1]
        self.table[s1] = s2
      return True
    return False

def hash(n, s, g):
  return n*s+g

def dehash(n, hs):
  return [(hs-hs%n)/n, hs%n]

def kruskal(n, path):
  path = sorted(path.items(), key=lambda x: x[1])
  selected = {}
  union = UnionFind(n)
  for i in xrange(len(path)):
    k, v = path[i]
    s, g = dehash(n, k)
    if union.union(s, g):
      selected[k] = v
  return selected

while True:
  n, m = map(int, raw_input().split())
  if n == m == 0:
    break
  path = {}
  for _ in xrange(m):
    a, b, c = map(int, raw_input().split())
    path[hash(n, a, b)] = c
  result = kruskal(n, path)
  sumcost = 0
  for v in result.values():
    sumcost += v
  print sumcost