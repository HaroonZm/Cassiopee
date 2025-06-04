while True:
  n = int(input())
  if n == 0:
    break
  edges = []
  score = []
  for _ in range(n):
    lst = input().split()
    score.append(float(lst[0]))
    edges.append([int(c)-1 for c in lst[2:]])
  rev_edges = [[] for _ in range(n)]
  for i in range(n):
    for e in edges[i]:
      rev_edges[e].append(i)
  
  visited = [False] * n
  order = []
  for x in range(n):
    stack = [x]
    to_visit = []
    while stack:
      node = stack.pop()
      if visited[node]:
        continue
      visited[node] = True
      to_visit.append(node)
      for to in edges[node]:
        if not visited[to]:
          stack.append(to)
    while to_visit:
      order.append(to_visit.pop())
  order = order[::-1]
  
  visited = [False] * n
  cycles = []
  for x in order:
    if not visited[x]:
      ret = []
      stack = [x]
      while stack:
        node = stack.pop()
        if visited[node]:
          continue
        visited[node] = True
        ret.append(node)
        for to in rev_edges[node]:
          if not visited[to]:
            stack.append(to)
      cycles.append(ret)
  
  visited = [False] * n
  ans = 1
  for x in order:
    if not visited[x]:
      for cycle in cycles:
        if x in cycle:
          acc = 1
          for node in cycle:
            stack = [node]
            while stack:
              nd = stack.pop()
              if visited[nd]:
                continue
              visited[nd] = True
              for to in edges[nd]:
                if not visited[to]:
                  stack.append(to)
            acc *= score[node]
          ans *= (1 - acc)
  print("{0:.7f}".format(ans))