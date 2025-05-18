import math
N = int(input())
ps = []
for i in range(N):
  x, y = map(int, input().split())
  ps.append((x, y, i))
ps.sort()

# i -> j のベクトル
def vec(pi, pj):
  return (pj[0] - pi[0], pj[1] - pi[1])
# i -> j 向きの外積
def det(vi, vj):
  return vi[0] * vj[1] - vi[1] * vj[0]

# 凸包を求める
cvx = []
for i in list(range(N)) + list(range(N-1))[::-1]:
  while len(cvx) >= 2 and det(vec(ps[cvx[-2]], ps[cvx[-1]]), vec(ps[cvx[-1]], ps
[i])) < 0:
    cvx.pop()
  cvx.append(i)

# 凸包の各頂点について、頂点から出る2辺のなす角を計算
ans = {}
pi = None
for i in cvx:
  x, y, j = ps[i]
  if pi is not None:
    px, py, pj = ps[pi]
    slope = math.atan2(y-py, x-px)
    if j not in ans: ans[j] = [0, 0]
    if pj not in ans: ans[pj] = [0, 0]
    ans[j][0] = slope
    ans[pj][1] = slope
  pi = i

for i in range(N):
  if i not in ans:
    print(0)
    continue
  v1, v2 = ans[i]
  if v2 < v1:
    v2 += 2*math.pi
  print(round((v2-v1) / (2*math.pi), 8))