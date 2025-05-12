while True:
  n = int(input())
  if n == 0:break
  to = []
  fr = [[] for _ in range(n * n)]
  for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
      x, y = line[2 * j:2 * j + 2]
      to.append(y * n + x)
      fr[y * n + x].append(i * n + j)
  
  order = []
  used = [False] * (n * n)
  def dfs(x):
    if used[x]:return
    used[x] = True
    dfs(to[x])
    order.append(x)
  
  for i in range(n * n):
    dfs(i)
  order.reverse()
  
  def dfs2(x, used, group):
    if used[x]:return False
    if x in group:return True
    group.append(x)
    ret = False
    ret = ret or dfs2(to[x], used, group)
    return ret
  
  used = [False] * (n * n)
  ans = 0
  for i in order:
    group = []
    if not used[i]:
      if dfs2(i, used, group):ans += 1
    for g in group:used[g] = True
  print(ans)