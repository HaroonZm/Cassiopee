import math
N=int(input())
data=[tuple(map(int,input().split())) for _ in range(N)]

def dist(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

res = {0: (-1,-1),1:(-1,-1)} # team: (max_dist, min_time)
for i in range(N-1):
    f1,a1,t1,x1,y1 = data[i]
    f2,a2,t2,x2,y2 = data[i+1]
    if t1 == t2 and a1 != a2: # different player same team
        d = dist(x1,y1,x2,y2)
        dt = (f2 - f1)/60
        maxd, mint = res[t1]
        if d > maxd or (abs(d - maxd) <= 1e-15 and dt < mint):
            res[t1] = (d, dt)

for t in [0,1]:
    d,tm = res[t]
    if d < 0:
        print(-1, -1)
    else:
        print(f"{d:.10f} {tm:.10f}")