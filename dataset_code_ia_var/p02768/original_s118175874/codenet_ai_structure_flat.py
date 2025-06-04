n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
N = 10 ** 6
inv_t = [0, 1]
for i in range(2, N):
    inv_t.append(inv_t[mod % i] * (mod - mod // i) % mod)
ret_a = 1
for i in range(1, a + 1):
    ret_a = (ret_a * (n - i + 1) * inv_t[i]) % mod
ret_b = 1
for i in range(1, b + 1):
    ret_b = (ret_b * (n - i + 1) * inv_t[i]) % mod
x = 2
k = n
res = 1
while k > 1:
    if k % 2 != 0:
        res = res * x % mod
    x = x * x % mod
    k //= 2
res = res * x % mod
result = (res - 1 - ret_a - ret_b) % mod
print(result)