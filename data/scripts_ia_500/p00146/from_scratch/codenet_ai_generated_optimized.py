import sys
sys.setrecursionlimit(10**9)

n=int(sys.stdin.readline())
warehouses=[]
for _ in range(n):
    s,d,v=map(int,sys.stdin.readline().split())
    warehouses.append((s,d,v))

warehouses.sort(key=lambda x:x[1])

pos=[w[1] for w in warehouses]
boxes=[w[2] for w in warehouses]
ids=[w[0] for w in warehouses]

INF=float('inf')
dp=[[INF]*(n) for _ in range(1<<n)]
pre=[[-1]*n for _ in range(1<<n)]

for i in range(n):
    w = boxes[i]*20
    dist = abs(pos[i]-pos[i])
    speed = 2000/(70+w)
    dp[1<<i][i] = 0  # no initial move (start at warehouse i)

for mask in range(1<<n):
    for last in range(n):
        if not (mask & (1<<last)):
            continue
        cur_time=dp[mask][last]
        if cur_time==INF:
            continue
        load=sum(boxes[i]*20 for i in range(n) if (mask & (1<<i)))
        for nxt in range(n):
            if mask & (1<<nxt):
                continue
            dist = abs(pos[nxt]-pos[last])
            speed = 2000/(70+load)
            time=dist/speed
            nxt_mask=mask | (1<<nxt)
            new_time=cur_time+time
            if dp[nxt_mask][nxt]>new_time:
                dp[nxt_mask][nxt]=new_time
                pre[nxt_mask][nxt]=last

full=(1<<n)-1
min_time=INF
end=-1
for i in range(n):
    if dp[full][i]<min_time:
        min_time=dp[full][i]
        end=i

res=[]
mask=full
cur=end
while cur!=-1:
    res.append(ids[cur])
    nxt=pre[mask][cur]
    mask=mask^(1<<cur)
    cur=nxt
res.reverse()

print(*res)