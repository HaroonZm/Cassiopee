n = int(input())
A = sorted(map(int, input().split()), reverse=True)

ans = max(
    (A[p] + A[q]) / (A[i] - A[j])
    for i in range(n)
    for j in range(i + 1, n)
    for p in range(n) if p not in (i, j)
    for q in range(p + 1, n) if q not in (i, j)
)

print(f"{ans:.6f}")