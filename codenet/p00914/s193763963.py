def rec(n, u, k, s):
    if k == 1:
        if u < s <= n:
            return 1
        else:
            return 0

    ret = 0
    for i in range(u + 1, n - k + 2):
        ret += rec(n, i, k - 1, s - i)

    return ret

while True:
    n, k, s = map(int, input().split())
    if n == k == s == 0:
        break

    print(rec(n, 0, k, s))