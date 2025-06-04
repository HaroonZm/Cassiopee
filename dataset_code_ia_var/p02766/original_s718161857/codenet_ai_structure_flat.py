N, K = list(map(int, input().split()))
tmp = K
cnt = 1
while tmp <= N:
    tmp = tmp * K
    cnt = cnt + 1
print(cnt)