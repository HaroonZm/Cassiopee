N, M = map(int, input().split())
As = list(map(int, input().split()))

rd = 0
c = 1
N_ = N * c
while N_ % M != 0:
    c += 1
    N_ = c * N
rd = N_ // M

repeat = (N_ // N) + 1
As = As * repeat

ls = []
cnt = 0
i = 0
while i < rd:
    lstmp = []
    j = 0
    while j < M:
        lstmp.append(As[cnt])
        cnt += 1
        j += 1
    ls.append(lstmp)
    i += 1

s = 0
i = 0
while i < len(ls):
    l = ls[i]
    mx = l[0]
    mn = l[0]
    k = 1
    while k < len(l):
        if l[k] > mx:
            mx = l[k]
        if l[k] < mn:
            mn = l[k]
        k += 1
    s += mx - mn
    i += 1

print(s)