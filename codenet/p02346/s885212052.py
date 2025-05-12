class BIT:
  def __init__(self, size):
    self.tree = [0] * (size + 1)
    self.size = size
  
  def sum(self, a):
    res = 0
    a += 1
    while a:
      res += self.tree[a]
      a -= a & -a
    return res
  def add(self, a, x):
    a += 1
    while a < len(self.tree):
      self.tree[a] += x
      a += a & -a

import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

def main():
  n, q = na()
  bit = BIT(n)
  for _ in range(q):
    t, x, y = na()
    if t == 0:
      bit.add(x - 1, y)
    else:
      print(bit.sum(y - 1) - bit.sum(x - 2))

main()