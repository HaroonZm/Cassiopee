import sys
readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
L = [0] * N
D = [0] * N
i = 0
while i < N:
    l, d = readline().split()
    L[i] = +(l == 'y')
    D[i] = int(d)
    i += 1
ans = 0
I = list(range(N))
I.sort(key=lambda x: D[x])
U = [0] * N
i = 0
while i < N:
    idx = I[i]
    if not L[idx] or U[idx]:
        i += 1
        continue
    d = D[idx]
    U[idx] = 1
    ans += 1
    k = idx - 1
    while k >= 0 and (L[k] or D[k] < d):
        if L[k]:
            U[k] = 1
        k -= 1
    k = idx + 1
    while k < N and (L[k] or D[k] < d):
        if L[k]:
            U[k] = 1
        k += 1
    i += 1
write("%d\n" % ans)