M = 1000001

p = [1]*M
p[0] = p[1] = 0
for i in range(2, int(M**.5)+1):
    if p[i]:
        for j in range(i*i, M, i):
            p[j] = 0
cs = [0]*M
cur = 0
for i in range(M):
    if p[i]:
        cur += 1
    cs[i] = cur

while 1:
    N = int(input())
    if N == 0:
        break
    ans = 0
    for i in range(N):
        p, m = map(int, input().split())
        x = cs[min(p+m, M-1)] - cs[max(p-m-1, 0)]
        if x:
            ans += x-1
        else:
            ans -= 1
    print(ans)