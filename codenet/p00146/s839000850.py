n = int(input())
ids = []
dists = []
weights = []
for _ in range(n):
  s, d, v = map(int, input().split())
  ids.append(s)
  dists.append(d)
  weights.append(v * 20)

dic = {}
INF = 10 ** 20
def score(rest, pos, total_weight, order):
  if rest == 0:
    return 0, []
  if (rest, pos) in dic:
    return dic[(rest, pos)]

  mask = 1
  ret = (INF, [])
  for i in range(n):
    if rest & mask:
      temp = score(rest & ~mask, i, total_weight + weights[i], order)
      ret = min(ret, (temp[0] + abs(dists[pos] - dists[i]) / 2000 * (total_weight), [i] + temp[1]))
    mask <<= 1
  dic[(rest, pos)] = ret
  return ret

rest = 2 ** n - 1
print(*[ids[i] for i in min([score(rest, i, 70, []) for i in range(n)])[1]])