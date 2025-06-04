k = int(raw_input())

l = 0
r = k
while r - l > 1:
    m = (l + r) / 2
    if m * (m + 1) < k:
        l = m
    else:
        r = m

b = l

ad = k - (b * (b + 1))

d = ((ad - 1) % (b + 1)) + 1

x = 2 * b + 1
y = 1

if ad - d > 0:
    x += 1

if d <= (b + 2) / 2:
    dd = d * 2 - 1
else:
    dz = (b + 1 - d)
    dd = dz * 2 + 2

x -= (dd - 1)
y += (dd - 1)

mod = 1000000007

def mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            res[i][j] = 0
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= mod
    return res

def fib(n):
    bt = [[1, 1], [1, 0]]
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            res = mul(res, bt)
        bt = mul(bt, bt)
        n = n // 2
    return res[0][0]

ans = fib(x - 1) * fib(y - 1)
ans = ans % mod
print ans