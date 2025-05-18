n = int(input())
a = list(map(int,input().split()))
q = int(input())
for _ in range(q):
    b, m, e = map(int,input().split())
    tmp = a[:]
    for k in range(e-b):
        t = b + ((k+(e-m)) % (e-b))
        a[t] = tmp[b+k]

print(*a)