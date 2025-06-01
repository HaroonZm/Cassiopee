def cv(t):
    return t//100*60 + t%100

while True:
    n, p, q = map(int, input().split())
    if n == 0:
        break
    v = [0] * 1440
    for _ in range(n):
        k = int(input())
        a = list(map(int, input().split()))
        for j in range(k):
            for l in range(cv(a[2*j]), cv(a[2*j+1])):
                v[l] += 1
    m = c = 0
    for i in range(cv(p), cv(q)):
        if v[i] < n:
            c += 1
        else:
            c = 0
        m = max(m, c)
    print(m)