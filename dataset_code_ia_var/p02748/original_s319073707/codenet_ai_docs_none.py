mi = lambda : map(int, input().split())
li = lambda : list(map(int, input().split()))

a, b, m = mi()
av = li()
bv = li()

avs = av.copy()
bvs = bv.copy()
avs.sort()
bvs.sort()

ans = avs[0] + bvs[0]

for _ in range(m):
    q = li()
    tmp = av[q[0]-1] + bv[q[1]-1] - q[2]
    ans = min(ans, tmp)

print(ans)