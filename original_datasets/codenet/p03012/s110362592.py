N = int(input())
W = list(map(int, input().split()))
sum_W = sum(W)

ans = 1000000000
for i in range(N):
    W_tmp = W[:i]
    sum_W_tmp = sum(W_tmp)
    if ans > abs(sum_W - 2 * sum_W_tmp):
        ans = abs(sum_W - 2 * sum_W_tmp)

print(ans)