import math
N = int(input())
ps = []
for i in range(N):
    x, y = map(int, input().split())
    ps.append((x, y, i))
ps.sort()
cvx = []
i_list = list(range(N)) + list(range(N-1))[::-1]
det = lambda vi, vj: vi[0] * vj[1] - vi[1] * vj[0]
for i in i_list:
    while len(cvx) >= 2 and det((ps[cvx[-1]][0]-ps[cvx[-2]][0], ps[cvx[-1]][1]-ps[cvx[-2]][1]),
                                (ps[i][0]-ps[cvx[-1]][0], ps[i][1]-ps[cvx[-1]][1])) < 0:
        cvx.pop()
    cvx.append(i)
ans = {}
pi = None
for i in cvx:
    x, y, j = ps[i]
    if pi is not None:
        px, py, pj = ps[pi]
        slope = math.atan2(y - py, x - px)
        if j not in ans:
            ans[j] = [0, 0]
        if pj not in ans:
            ans[pj] = [0, 0]
        ans[j][0] = slope
        ans[pj][1] = slope
    pi = i
for i in range(N):
    if i not in ans:
        print(0)
        continue
    v1, v2 = ans[i]
    if v2 < v1:
        v2 += 2 * math.pi
    print(round((v2 - v1) / (2 * math.pi), 8))