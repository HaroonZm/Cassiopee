while True:
    n = int(raw_input())
    if n == 0:
        break
    a = [0]
    for i in range(n):
        a.append(int(raw_input()) + a[-1])
    mx = -100000
    for i in range(n):
        for j in range(i + 1, n + 1):
            mx = max(mx, a[j] - a[i])
    print mx