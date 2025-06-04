while True:
    T, D, L = map(int, input().split())
    if T == 0:
        break
    a = []
    for i in range(T):
        x = int(input())
        if x >= L:
            a.append(i)
    T, ans = T - 1, 0
    for i in range(1, len(a)):
        x = D
        if T - a[i - 1] < D:
            x = T - a[i - 1]
        if a[i] - a[i - 1] < x:
            ans += a[i] - a[i - 1]
        else:
            ans += x
    if a:
        if a[-1] + D > T:
            ans += T - a[-1]
        else:
            ans += D
    print(ans)