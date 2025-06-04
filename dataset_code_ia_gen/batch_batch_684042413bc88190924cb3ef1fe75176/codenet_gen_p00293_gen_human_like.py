N,*h_m = map(int,input().split())
M,*k_g = map(int,input().split())
times = []
for i in range(N):
    h, m = h_m[2*i], h_m[2*i+1]
    times.append(h*60+m)
for i in range(M):
    k, g = k_g[2*i], k_g[2*i+1]
    times.append(k*60+g)
times = sorted(set(times))
res = []
for t in times:
    h = t//60
    m = t%60
    res.append(f"{h}:{m:02d}")
print(" ".join(res))