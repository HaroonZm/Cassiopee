import bisect

n,m = map(int,input().split())
pos = list(map(int,input().split()))
q = int(input())
l = list(map(int,input().split()))

pos.append(n+1)
d = [pos[i+1]-pos[i]-1 for i in range(m)]
d.sort()
s = [0]*(m+1)
for i in range(len(d)):
    s[i+1] = s[i]+d[i]

for lim in l:
    ok = n+1
    ng = 0
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        idx = bisect.bisect_left(d,mid)
        cost = (s[-1]-s[idx]) - (m-idx)*(mid-1) + (pos[0]-1)
        if cost <= lim:
            ok = mid
        else:
            ng = mid
    if ok <= n:
        print(ok)
    else:
        print(-1)