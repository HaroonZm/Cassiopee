class UnionFind:
  def __init__(self, size):
    self.table = self._init_table(size)

  def _init_table(self, size):
    return [-1 for _ in xrange(size)]

  def find(self, x):
    return self._find_root(x)

  def _find_root(self, x):
    if self._has_parent(x):
      return self._find_root(self.table[x])
    else:
      return x

  def _has_parent(self, x):
    return self.table[x] >= 0

  def union(self, x, y):
    s1 = self.find(x)
    s2 = self.find(y)
    if not self._same_set(s1, s2):
      self._union_sets(s1, s2)
      return True
    return False

  def _same_set(self, s1, s2):
    return s1 == s2

  def _union_sets(self, s1, s2):
    if self._size(s1) >= self._size(s2):
      self._attach(s1, s2)
    else:
      self._attach(s2, s1)

  def _size(self, s):
    return self.table[s]

  def _attach(self, s1, s2):
    self.table[s1] += self.table[s2]
    self.table[s2] = s1


def hash(n, s, g):
  return _compute_hash(n, s, g)

def _compute_hash(n, s, g):
  return n*s + g

def dehash(n, hs):
  return [_dehash_first_component(n, hs), _dehash_second_component(n, hs)]

def _dehash_first_component(n, hs):
  return (hs - hs % n) / n

def _dehash_second_component(n, hs):
  return hs % n

def kruskal(n, path):
  ordered_path = _sort_path(path)
  union = _init_unionfind(n)
  selected = _init_selected()
  for i in _index_range(ordered_path):
    k, v = _get_path_item(ordered_path, i)
    s, g = dehash(n, k)
    if _union_sets(union, s, g):
      _add_selected(selected, k, v)
  return selected

def _sort_path(path):
  return sorted(path.items(), key=lambda x: x[1])

def _init_unionfind(n):
  return UnionFind(n)

def _init_selected():
  return {}

def _index_range(seq):
  return xrange(len(seq))

def _get_path_item(seq, i):
  return seq[i]

def _union_sets(union, s, g):
  return union.union(s, g)

def _add_selected(selected, k, v):
  selected[k] = v


def main_loop():
  while True:
    n, m = _read_input()
    if _check_termination(n, m):
      break
    path = _read_paths(n, m)
    result = kruskal(n, path)
    sumcost = _sum_cost(result)
    _print_sumcost(sumcost)

def _read_input():
  return map(int, raw_input().split())

def _check_termination(n, m):
  return n == 0 and m == 0

def _read_paths(n, m):
  path = {}
  for _ in xrange(m):
    a, b, c = _read_path_line()
    _add_path(path, n, a, b, c)
  return path

def _read_path_line():
  return map(int, raw_input().split())

def _add_path(path, n, a, b, c):
  key = hash(n, a, b)
  path[key] = c

def _sum_cost(result):
  total = 0
  for v in _iter_values(result):
    total += v
  return total

def _iter_values(d):
  return d.values()

def _print_sumcost(sumcost):
  print sumcost

main_loop()