N, K = map(int, input().split())
MOD = 10 ** 9 + 7
i = 1
div = []
while i * i <= N:
    if N % i == 0:
        div.append(i)
        if N // i != i:
            div.append(N // i)
    i += 1
div.sort()
N1 = len(div)
num = [0] * (N1 + 1)
ans = 0
i = 0
while i < N1:
    d = div[i]
    num[i] = pow(K, (d + 1) // 2, MOD)
    j = 0
    while j < i:
        if d % div[j] == 0:
            num[i] = (num[i] - num[j] + MOD) % MOD
        j += 1
    if d % 2 == 0:
        ans = (ans + d * num[i] // 2) % MOD
    else:
        ans = (ans + d * num[i]) % MOD
    i += 1
print(ans)