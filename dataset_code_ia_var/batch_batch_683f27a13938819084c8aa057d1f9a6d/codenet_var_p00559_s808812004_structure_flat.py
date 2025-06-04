n, q, s, t = map(int, input().split())
a = []
i = 0
while i < n + 1:
    a.append(int(input()))
    i += 1
i = n
while i > 0:
    a[i] -= a[i - 1]
    i -= 1
count = 0
i = 0
while i < n + 1:
    if a[i] > 0:
        count -= a[i] * s
    else:
        count -= a[i] * t
    i += 1
j = 0
while j < q:
    lrt = input().split()
    l = int(lrt[0])
    r = int(lrt[1])
    x = int(lrt[2])
    if a[l] > 0:
        count += a[l] * s
    else:
        count += a[l] * t
    a[l] += x
    if a[l] > 0:
        count -= a[l] * s
    else:
        count -= a[l] * t
    if r < n:
        if a[r + 1] > 0:
            count += a[r + 1] * s
        else:
            count += a[r + 1] * t
        a[r + 1] -= x
        if a[r + 1] > 0:
            count -= a[r + 1] * s
        else:
            count -= a[r + 1] * t
    print(count)
    j += 1