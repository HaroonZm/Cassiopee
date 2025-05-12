from heapq import heappush, heappop
INF = 10 ** 20

def main():
  n, m, x = map(int, input().split())
  tlst = [int(input()) for _ in range(n)]
  edges = [[] for _ in range(n)]
  for _ in range(m):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, d))
    edges[b].append((a, d))
  
  que = []
  heappush(que, (0, x, 0, 0)) #道のり、寒さ、暑さ、部屋番号
  dic = {}
  dic[(x, 0, 0)] = 0
  while que:
    total, ct, ht, node = heappop(que)
    for to, dist in edges[node]:
      new_ct = max(0, ct - dist)
      new_ht = max(0, ht - dist)
      t = tlst[to]
      if t == 1 or (t == 0 and new_ht == 0) or (t == 2 and new_ct == 0):
        new_total = total + dist
        if t == 0: new_ct = x
        if t == 2: new_ht = x
        if (new_ct, new_ht, to) not in dic or dic[(new_ct, new_ht, to)] > new_total:
          dic[(new_ct, new_ht, to)] = new_total
          heappush(que, (new_total, new_ct, new_ht, to))
  
  print(min([dic[(ct, ht, n - 1)] if (ct, ht, n - 1) in dic else INF for ct in range(x + 1) for ht in range(x + 1)]))

main()