N, A = map(int, input().split())

ans = N

for i in range(1, 50):
    ok = 10 ** 20
    ng = 0

    while ok - ng > 1:
        mid = (ok + ng) // 2
        prod = 1
        for j in range(i):
            prod *= (mid + j) // i
        if prod >= N:
            ok = mid
        else:
            ng = mid

    ans = min(ans, A * (i - 1) + ok)

print(ans)