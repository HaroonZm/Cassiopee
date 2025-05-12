n,m = map(int,input().split())
a = [int(input()) for i in range(n)]

for k in range(m):
    for i in range(n-1):
        if a[i] % (k+1) > a[i+1] % (k+1):
            a[i],a[i+1] = a[i+1],a[i]

for i in range(n):
    print(a[i])