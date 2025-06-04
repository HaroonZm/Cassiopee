n, c = map(int, input().split())

lx = []
lv = []
for i in range(n):
    x, v = map(int, input().split())
    lx.append(x)
    lv.append(v)

lux = []
for x in reversed(lx):
    lux.append(c - x)

vc = []
vuc = []
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += lv[i]
    sum2 += lv[n-1-i]
    vc.append(sum1)
    vuc.append(sum2)

sc = []
suc = []
for i in range(n):
    sc.append(vc[i] - lx[i])
    suc.append(vuc[i] - (c - lx[n-1-i]))

ssc = []
ssuc = []
max1 = -c
max2 = -c
for i in range(n):
    if sc[i] > max1:
        max1 = sc[i]
    if suc[i] > max2:
        max2 = suc[i]
    ssc.append(max1)
    ssuc.append(max2)

ans = 0
for i in range(n):
    s1 = sc[i]
    s2 = suc[i]
    if i == n-1:
        s3 = 0
        s4 = 0
    else:
        idx = max(0, n-i-2)
        s3 = s1 - lx[i] + ssuc[idx]
        s4 = s2 - lux[i] + ssc[idx]
    if s1 > ans:
        ans = s1
    if s2 > ans:
        ans = s2
    if s3 > ans:
        ans = s3
    if s4 > ans:
        ans = s4

print(ans)