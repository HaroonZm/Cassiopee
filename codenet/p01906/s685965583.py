N, M = map(int, input().split())
As = list(map(int, input().split()))

rd = 0
c = 1
N_ = N * c
while(N_ % M != 0):
    c += 1
    N_ = c * N 
rd = N_ // M

As = As * (N_//N + 1)

ls = []
cnt = 0
for i in range(rd):
    lstmp = []
    for j in range(M):
        lstmp.append(As[cnt])
        cnt += 1
    ls.append(lstmp)

s = 0
for i in ls:
    s += max(i)-min(i)
print(s)