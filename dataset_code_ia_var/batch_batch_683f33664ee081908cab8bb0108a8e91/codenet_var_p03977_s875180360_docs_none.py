def inpl(): return list(map(int, input().split()))
for _ in range(int(input())):
    N, D = inpl()
    ans = 0
    for i in range(7):
        D, m = divmod(D, 2)
        ans += (N - (N % 2 != m)) * (2 ** i)
    print(ans)