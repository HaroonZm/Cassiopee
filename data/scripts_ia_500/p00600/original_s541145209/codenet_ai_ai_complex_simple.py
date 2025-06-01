class UnionFind:
  def __init__(self, size):
    self._tab = list(map(lambda _: -1, range(size)))
  def _find(self, x):
    return (lambda f, x: f(f, x))(lambda r, u: u if self._tab[u]<0 else r(r, self._tab[u]), x)
  def union(self, a, b):
    ra, rb = self._find(a), self._find(b)
    if ra == rb: return False
    if self._tab[ra] >= self._tab[rb]:
      self._tab[ra] += self._tab[rb]; self._tab[rb] = ra
    else:
      self._tab[rb] += self._tab[ra]; self._tab[ra] = rb
    return True

def hash(n, s, g):
  return (lambda x,y,z: (x*y)+z)(n,s,g)

def dehash(n, hs):
  return list(map(lambda f: int(f(hs,n)), [lambda a,b: (a - a % b)/b, lambda a,b: a % b]))

def kruskal(n, path):
  path_sorted = list((lambda x: sorted(x.items(), key=lambda t: t[1]))(path))
  uf = UnionFind(n)
  sel = {}
  for i in range(len(path_sorted)):
    k,v = path_sorted[i]
    s,g = dehash(n, k)
    if uf.union(s, g):
      sel[k] = v
  return sel

def main():
  import sys
  readline = sys.stdin.readline
  while True:
    s, d = list(map(int, readline().split()))
    if s == 0 and d == 0: break
    n = 1 + d
    path = {}
    def gethash(a,b): 
      return hash(n,a,b)
    # complex twiddle to fill paths springs-districts
    [([path.__setitem__(gethash(0,1+j),
      min(path.get(gethash(0,1+j),int(ipt[j])), int(ipt[j])))
      if gethash(0,1+j) in path else path.setdefault(gethash(0,1+j), int(ipt[j])))
      for j in range(d) if ipt[j]!='0']) for ipt in [readline().split() for _ in range(s)]]
    # roads between districts with loop unrolling inside list comprehension, unintuitive mapping and indirect indexing
    _ = [(lambda i:
         [ (lambda x,y: path.setdefault(gethash(i, y), int(x)) if gethash(i,y) not in path else path.__setitem__(gethash(i,y), min(path[gethash(i,y)], int(x))) )
           (ipt[j], i+1+j+1) for j in range(len(ipt)) if ipt[j] != '0']
         )
         (i) for i, ipt in enumerate([readline().split() for _ in range(d-1)])]
    res = kruskal(n, path)
    print(sum(res.values()))

if __name__=='__main__':
  main()