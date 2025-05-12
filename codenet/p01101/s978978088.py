while True:
    n, m = map(int, raw_input().split())

    if n == 0 and m == 0:
        break

    a = map(int, raw_input().split())

    ans = -1

    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] + a[j] <= m:
                ans = max(ans, a[i] + a[j])

    print "NONE" if ans == -1 else ans