n, q, s, t = map(int, input().split())
a = [int(input()) for _ in range(n + 1)]
for i in range(1, n + 1)[::-1]:
    a[i] -= a[i - 1]
count = 0
for i in range(n + 1):
    count -= a[i] * s if a[i] > 0 else a[i] * t
for _ in range(q):
    l, r, x = map(int, input().split())
    count += a[l] * s if a[l] > 0 else a[l] * t
    a[l] += x
    count -= a[l] * s if a[l] > 0 else a[l] * t
    if r < n:
        count += a[r + 1] * s if a[r + 1] > 0 else a[r + 1] * t
        a[r + 1] -= x
        count -= a[r + 1] * s if a[r + 1] > 0 else a[r + 1] * t
    print(count)