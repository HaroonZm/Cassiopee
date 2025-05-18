n = int(input())
a = list(map(int, input().split()))
l, r = 1, n * 2
while r - l > 1:
    m = (l + r) // 2
    li = [0] * (2 * n - 1)
    for i in range(2 * n - 1):
        if a[i] >= m:
            li[i] = 1
    t = li[n - 1]
    for i in range(n - 1):
        if ((t + li[n + i] + i) & 1 == 0):
            if li[n + i] & 1:
                l = m
            else:
                r = m
            break
        if((t + li[n - i - 2] + i) & 1 == 0):
            if li[n - i - 2] & 1:
                l = m
            else:
                r = m
            break
    else:
        if (n + t) & 1:
            r = m
        else:
            l = m
print(l)