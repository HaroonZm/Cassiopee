n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ax = 0
ay = 0
i = 0
while i < n:
    val = (2 * i - n + 1) * x[i]
    val %= MOD
    ax = (ax + val) % MOD
    i += 1
i = 0
while i < m:
    val = (2 * i - m + 1) * y[i]
    val %= MOD
    ay = (ay + val) % MOD
    i += 1
result = (ax * ay) % MOD
print(int(result))