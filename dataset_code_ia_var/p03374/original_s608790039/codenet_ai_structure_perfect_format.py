n, c = map(int, input().split())

lx = []
lv = []

for _ in range(n):
    tmpx, tmpv = map(int, input().split())
    lx.append(tmpx)
    lv.append(tmpv)

lux = [c - x for x in reversed(lx)]

vc = []
vuc = []
tmpv1 = 0
tmpv2 = 0
for i in range(n):
    tmpv1 += lv[i]
    tmpv2 += lv[n - 1 - i]
    vc.append(tmpv1)
    vuc.append(tmpv2)

sc = []
suc = []
for i in range(n):
    sc.append(vc[i] - lx[i])
    suc.append(vuc[i] - (c - lx[n - 1 - i]))

ssc = []
ssuc = []
tmp = -c
tmpu = -c
for i in range(n):
    tmp = max(tmp, sc[i])
    tmpu = max(tmpu, suc[i])
    ssc.append(tmp)
    ssuc.append(tmpu)

ans = 0
for i in range(n):
    s1 = sc[i]
    s2 = suc[i]
    if i == n - 1:
        s3 = 0
        s4 = 0
    else:
        s3 = s1 - lx[i] + ssuc[max(0, n - i - 2)]
        s4 = s2 - lux[i] + ssc[max(0, n - i - 2)]
    ans = max(ans, s1, s2, s3, s4)

print(ans)