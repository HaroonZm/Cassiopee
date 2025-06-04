D, N = map(int, input().split())
d_li = []
for _ in range(D):
    d_li.append(int(input()))
clothe_li = []
for _ in range(N):
    clothe_li.append(list(map(int, input().split())))
dp = []
for _ in range(D):
    dp.append([0]*N)
d = d_li[0]
for n in range(N):
    a, b, c = clothe_li[n]
    if a <= d <= b:
        dp[0][n] = 1
i = 1
while i < D:
    d = d_li[i]
    pre_n = 0
    while pre_n < N:
        if dp[i-1][pre_n] != 0:
            n = 0
            while n < N:
                a, b, c = clothe_li[n]
                if a <= d <= b:
                    dp[i][n] = max(dp[i][n], dp[i-1][pre_n] + abs(clothe_li[pre_n][2] - c))
                n += 1
        pre_n += 1
    i += 1
max_val = -float('inf')
for val in dp[-1]:
    if val > max_val:
        max_val = val
print(max_val-1)