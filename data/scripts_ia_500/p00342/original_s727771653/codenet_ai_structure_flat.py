n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        p = 0
        while p == i or p == j:
            p += 1
        q = 0
        while q == i or q == j or q == p:
            q += 1
        val = (A[p] + A[q]) / (A[i] - A[j])
        if val > ans:
            ans = val
print("%.6f" % ans)