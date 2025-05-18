n, k = map(int, raw_input().split())
a = [input() for i in range(n+k)]
c = [0]*n
for i in range(n,n+k):
    for j in range(n):
        if a[i] >= a[j]:
            c[j] += 1
            break
print c.index(max(c)) + 1