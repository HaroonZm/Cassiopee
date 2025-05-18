#-------最強ライブラリ2-SAT(Python)------
#最強ライブラリSCC(Python)が必要

class two_sat:
  def __init__(s):
    s._n = 0
    s.scc = scc_graph(0)
  def __init__(s, n):
    s._n = n
    s._answer = [False] * n
    s.scc = scc_graph(2 * n)

  # クローズを足す
  # クローズってなに
  def add_clause(s, i, f, j, g):
    s.scc.add_edge(2 * i + (not f), 2 * j + (g))
    s.scc.add_edge(2 * j + (not g), 2 * i + (f))
  
  # 判定
  # O(n + m)
  def satisfiable(s):
    id = s.scc.scc_ids()[1]
    for i in range(s._n):
      if id[2 * i] == id[2 * i + 1]: return False
      s._answer[i] = id[2 * i] < id[2 * i + 1]
    return True

  # クローズを満たす割当を返す
  # satisfiableがTrueとなった後に呼ばないと意味ない
  # O(1だよね？）
  def answer(s): return s._answer

#-------最強ライブラリここまで------

#-------最強ライブラリSCC(Python) ver83025------
import sys
sys.setrecursionlimit(1000000)

class scc_graph:
  # n 頂点数
  def __init__(s, n): 
    s._n = n
    s.g = {}
  def num_vertices(s): return s._n
  # 辺を追加 frm 矢元 to 矢先
  # O(1)
  def add_edge(s, frm, to): 
    if frm in s.g: s.g[frm].append(to)
    else: s.g[frm] = [to]

  # グループの個数と各頂点のグループidを返す
  def scc_ids(s):
    now_ord = group_num = 0
    visited = []
    low = [0] * s._n
    ord = [-1] * s._n
    ids = [0] * s._n
    # 再帰関数 
    def dfs(self, v, now_ord, group_num):
      low[v] = ord[v] = now_ord
      now_ord += 1
      visited.append(v)
      if v in s.g:
        for to in s.g[v]:
          if ord[to] == -1:
            now_ord, group_num = self(self, to, now_ord, group_num)
            low[v] = min(low[v], low[to])
          else:
            low[v] = min(low[v], ord[to])
      if low[v] == ord[v]:
        while True:
          u = visited.pop()
          ord[u] = s._n
          ids[u] = group_num
          if u == v: break
        group_num += 1
      return now_ord, group_num

    for i in range(s._n):
      if ord[i] == -1: now_ord, group_num = dfs(dfs, i, now_ord, group_num)
    for i in range(s._n):
      ids[i] = group_num - 1 - ids[i]
    return group_num, ids

  # 強連結成分となっている頂点のリストのリスト トポロジカルソート済み
  # O(n + m)
  def scc(s):
    group_num, ids = s.scc_ids()
    counts = [0] * group_num
    for x in ids: counts[x] += 1
    groups = [[] for _ in range(group_num)]
    for i in range(s._n):
      groups[ids[i]].append(i)
    return groups

  class edge:
    def __init__(s, frm, to):
      s.frm = frm
      s.to = to

#-------最強ライブラリここまで------

def main():
  input = sys.stdin.readline

  N, D = list(map(int, input().split()))
  XY = [list(map(int, input().split())) for _ in range(N)]

  ts = two_sat(N)

  for i in range(N):
    for j in range(i + 1, N):
      xi, yi = XY[i]
      xj, yj = XY[j]
      # 距離がD未満の組み合わせに関して、
      # 少なくとも一つは使用しない
      # → 少なくとも一つは別の座標を使用する
      # というルールを追加する
      if (abs(xi - xj) < D):
        ts.add_clause(i, False, j, False)
      if (abs(xi - yj) < D):
        ts.add_clause(i, False, j, True)
      if (abs(yi - xj) < D):
        ts.add_clause(i, True, j, False)
      if (abs(yi - yj) < D):
        ts.add_clause(i, True, j, True)

  if not ts.satisfiable():
    print("No")
    exit()

  print("Yes")
  answer = ts.answer()
  for i in range(N):
    x, y = XY[i]
    if answer[i]:
      print(x)
    else:
      print(y)

main()