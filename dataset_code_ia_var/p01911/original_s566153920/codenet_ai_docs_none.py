from heapq import heappush, heappop

def main():
  n, m, s, g = map(int, input().split())
  s -= 1
  g -= 1
  edges = [[] for _ in range(n)]
  for _ in range(m):
    u, v, t, c = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((t, t + c, v))
  score = {}
  score[(0, 0)] = 0
  que = []
  heappush(que, (0, 0, s))
  while que:
    total, time, node = heappop(que)
    if node == g:
      print(total)
      break
    for start, end, to in edges[node]:
      if start < time:
        continue
      new_total = total + (start - time)
      if (to, end) not in score or score[(to, end)] > new_total:
        score[(to, end)] = new_total
        heappush(que, (new_total, end, to))

main()