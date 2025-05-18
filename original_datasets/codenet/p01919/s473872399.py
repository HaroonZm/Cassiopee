from heapq import heappush, heappop

def main():
  n, m = map(int, input().split())
  edges = [[] for _ in range(n)]
  for _ in range(m):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append((y, t))
    edges[y].append((x, t))
  
  v0 = int(input())
  a, b, c = map(int, input().split())
  v_next = {}
  v = v0
  while True:
    if v not in v_next:
      v_next[v] = (v * a + b) % c
      v = (v * a + b) % c
    else:break

  dic = {}
  dic[(v0, 0)] = 0
  que = []
  heappush(que, (0, 0, v0))
  while que:
    score, node, v = heappop(que)
    new_v = v_next[v]
    for to, t in edges[node]:
      new_score = score + v * t
      if (new_v, to) not in dic or dic[(new_v, to)] > new_score:
        dic[(new_v, to)] = new_score
        heappush(que, (new_score, to, new_v))
  
  dic2 = {}
  que = []
  for v in range(c):
    if (v, n - 1) in dic:
      dic2[(v, n - 1)] = dic[(v, n - 1)]
      heappush(que, (dic[(v, n - 1)], n - 1, v))
  
  while que:
    score, node, v = heappop(que)
    if node == 0:
      print(score)
      break
    new_v = v_next[v]
    for to, t in edges[node]:
      new_score = score + v * t
      if (new_v, to) not in dic2 or dic2[(new_v, to)] > new_score:
        dic2[(new_v, to)] = new_score
        heappush(que, (new_score, to, new_v))
main()