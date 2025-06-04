import sys
readl = sys.stdin.readline

N, M = (int(x) for x in readl().split())
P = list(map(int, readl().split()))
edges = []
idx = 0
while idx < N-1:
    A,B,C = map(int, readl().split())
    tup = (A,B,C)
    edges.append(tup)
    idx += 1

cnt = [0 for _ in range(N)]
for i in range(M-1):
    s = P[i]-1
    t = P[i+1]-1
    lo, hi = (s, t) if s < t else (t, s)
    cnt[lo] += 1
    cnt[hi] -= 1

def accumulate(arr):
    for a in range(len(arr)-1):
        arr[a+1] += arr[a]
accumulate(cnt)

res = 0
for i in range(N-1):
    a,b,c = edges[i]
    nodecnt = cnt[i]
    x = nodecnt * a
    y = b * nodecnt + c
    if x < y:
        res += x
    else:
        res += y
sys.stdout.write(str(res)+'\n')