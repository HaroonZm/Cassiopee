a = [int(i) for i in raw_input().split()]
b = [int(i) for i in raw_input().split()]
c = [(a[i]/100.0,b[i]/100.0,(a[i]+b[i])/100.0,a[i]*1.0/(a[i]+b[i])) for i in range(len(a)) if a[i]+b[i]>0]
n = len(c)
c.sort(key=lambda item: item[3], reverse=True)
u = [0] * n
res = 1
for i in range(n):
    du = min(res / (c[i][2]), 1)
    u[i] = du
    res -= du * c[i][2]
    if res <=0:
        break
ans = 0
for i in range(n):
    ans += c[i][0] * u[i]

print ans