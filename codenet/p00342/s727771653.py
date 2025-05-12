n = int(input())
*A, = map(int, input().split())
A.sort(reverse=1)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        p = q = 0
        while p in [i, j]:
            p += 1
        while q in [i, j, p]:
            q += 1
        ans = max(ans, (A[p]+A[q])/(A[i]-A[j]))
print("%.6f" % ans)