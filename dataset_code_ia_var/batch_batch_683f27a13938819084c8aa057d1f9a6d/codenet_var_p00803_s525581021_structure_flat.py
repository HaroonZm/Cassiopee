a = [0]
b = [0]
i = 0
while i < 100:
    a.append(i * i * i)
    b.append((i * (i - 1) * (i - 2)) / 6)
    i += 1
while True:
    n = int(raw_input())
    if n == 0:
        break
    ans = 1 << 30
    i = 0
    while i < len(b):
        if b[i] > n:
            break
        if n - b[i] < ans:
            ans = n - b[i]
        i += 1
    i = 0
    while i < len(a):
        if a[i] > n:
            break
        if n - a[i] < ans:
            ans = n - a[i]
        j = 0
        while j < len(b):
            if a[i] + b[j] > n:
                break
            if n - (a[i] + b[j]) < ans:
                ans = n - (a[i] + b[j])
            j += 1
        i += 1
    print n - ans