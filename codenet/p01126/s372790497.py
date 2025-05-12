while True:
  n, m, a = map(int, input().split())
  if n == 0:
    break
  edges = [[] for _ in range(1001)]
  for _ in range(m):
    h, p, q = map(int, input().split())
    edges[h].append((p, q))
  
  for h in range(1000, -1, -1):
    if (a, a + 1) in edges[h]:
      a = a + 1
    elif (a - 1, a) in edges[h]:
      a = a - 1
  print(a)