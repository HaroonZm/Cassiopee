from heapq import heappush, heappop
n, m, k, p = map(int, input().split())
p -= 1
edges = [[] for _ in range(n)]
for _ in range(m):
  x, y, w = map(int, input().split())
  x -= 1
  y -= 1
  edges[x].append((y, w))
  edges[y].append((x, w))

point = []
for _ in range(k):
  s, t = map(int, input().split())
  s -= 1
  t -= 1
  point.append(s)
  point.append(t)

INF = 10 ** 20
def dist(x):
  mem = [INF] * n
  mem[x] = 0
  que = []
  heappush(que, (0, x))
  while que:
    total, node = heappop(que)
    for to, cost in edges[node]:
      new_total = total + cost
      if new_total < mem[to]:
        mem[to] = new_total
        heappush(que, (new_total, to))
  return mem

dist_dic = [[None] * (2 * k) for _ in range(2 * k)]
for i in range(2 * k):
  mem = dist(point[i])
  for j in range(2 * k):
    dist_dic[i][j] = mem[point[j]]

start_mem = dist(p)
start_cost = []
for i in range(2 * k):
  start_cost.append(start_mem[point[i]])

dic = {}
end = 2 ** (2 * k) - 1
def min_cost(stat, pos):
  if (stat, pos) in dic:
    return dic[(stat, pos)]
  if stat == end:
    dic[(stat, pos)] = 0
    return 0

  ret = INF
  mask = 1
  for i in range(2 * k):
    if stat & mask or (i % 2 == 1 and not (stat & (mask >> 1))):
      mask <<= 1
      continue
    ret = min(ret, dist_dic[pos][i] + min_cost(stat | mask, i))
    mask <<= 1
  dic[(stat, pos)] = ret
  return ret

ans = INF
for i in range(0, k * 2, 2):
  ans = min(ans, start_cost[i] + min_cost(2 ** i, i))
if ans == INF:
  print("Cannot deliver")
else:
  print(ans)