n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
while k < m:
    i = 0
    while i < n - 1:
        if a[i] % (k+1) > a[i+1] % (k+1):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
        i += 1
    k += 1
i = 0
while i < n:
    print(a[i])
    i += 1