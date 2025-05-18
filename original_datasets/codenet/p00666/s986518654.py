E = 10 ** -9
MOD = 100000007
fact_result = {}

while True:
  n = int(input())
  if n == 0: break
  plst = []
  wlst = []
  diff = []
  to = [None for _ in range(n)]
  for i in range(n):
    p, Id, w = input().split()
    to[i] = int(Id)
    plst.append(float(p))
    wlst.append(float(w))
    diff.append(1 / float(w) - 1 / float(p))

  def elapsed_time(group):
    ret = 0
    ret += 1 / plst[group[0]]
    for g in group[1:]:
      ret += 1 / wlst[g]
    return ret

  def init_comb(group):
    d = diff[group[0]]
    ret = 0
    for g in group:
      if abs(diff[g] - d) < E:
        ret += 1
    return ret

  def fact(n):
    if n == 0:
      return 1
    if n in fact_result:
      return fact_result[n]
    fact_result[n] = n * fact(n - 1)
    return fact_result[n]

  used = [False] * n
  time = 0
  comb = fact(n)
  group_cnt = 0
  for i in range(n):
    if used[i]: continue
    group_cnt += 1
    group = [i]
    used[i] = True
    nex = to[i]
    while not used[nex]:
      group.append(nex)
      used[nex] = True
      nex = to[nex]
    group.sort(key=lambda x:-diff[x])
    time += elapsed_time(group)
    comb //= fact(len(group))
    comb *= init_comb(group)
  print(time, comb % MOD)