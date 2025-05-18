N = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    sub = [0] * N
    for i in range(N):
        sub[i] = (a[i] - (N - 1) - 1) // N + 1
    sum_sub = sum(sub)
    if sum_sub == 0:
        break
    ans += sum_sub
    for i in range(N):
        a[i] -= N * sub[i] - (sum_sub - sub[i])

print(ans)