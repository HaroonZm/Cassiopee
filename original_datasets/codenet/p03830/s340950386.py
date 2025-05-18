def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if not arr:
        arr.append([n, 1])

    return arr

N = int(input())
MOD = 10 ** 9 + 7
x = dict()
for i in range(N, 1, -1):
    for f in factorization(i):
        if not f[0] in x:
            x[f[0]] = 1
        x[f[0]] += f[1]
ans = 1
for i in x.values():
    ans = (ans * i) % MOD
print(ans)