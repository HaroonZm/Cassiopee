from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import *

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

class union_find:
  def __init__(self, n):
    self.par = [-1] * n
  def __repr__(self):
    return "union_find({0})".format(self.par)
  def unite(self, x, y):
    if self.root(x) != self.root(y):
      self.par[self.root(x)] = y
  def root(self, x):
    if self.par[x] == -1:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  def same(self, x, y):
    return self.root(x) == self.root(y)
  
N, M = reads()
p = reads()

uf = union_find(N)
for _ in range(M):
  x, y = reads()
  uf.unite(x-1, y-1)

d = defaultdict(set)
for i in range(N):
  d[uf.root(i)].add(i)
print(d, file=stderr)

ans = 0
for grp in d.values():
  ans += len(grp & {p[i]-1 for i in grp})
print(ans)