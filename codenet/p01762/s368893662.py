n = int(input())
c_lst = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n - 1):
  u, v, p = map(int, input().split())
  edges[u].append((v, p))
  edges[v].append((u, p))

INF = 10 ** 20
used = [False] * n
def cost(x):
  used[x] = True
  ret = 0
  pre_cost = 0 if x != 0 else INF
  for to, p in edges[x]:
    if used[to]:pre_cost = p
    else:
      ret += cost(to)
  if c_lst[x] == 0:return min(ret, pre_cost)
  else:return pre_cost

print(cost(0))