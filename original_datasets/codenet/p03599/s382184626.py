import bisect
a,b,c,d,e,f = map(int,input().split())
water = set()
sugar = set()
for i in range(301):
    for j in range(301):
        if 0 < (i*a + j*b)*100 <= f:
            water.add((i*a + j*b)*100)
for i in range(1500//d + 1):
    for j in range((1500 - (i*d))//c + 1):
        if i*d + j*c <= f//2 + 1:
            sugar.add(i*d + j*c)
sugar = sorted(list(sugar))
ans = [100*a, 0]
M = 0
for i in water:
    tmp = [i, sugar[bisect.bisect(sugar,min(f-i, i*e/100)) - 1]]
    if tmp[1]/sum(tmp) > ans[1]/ans[0]:
        ans = [sum(tmp), tmp[1]]
print(' '.join([str(i) for i in ans]))