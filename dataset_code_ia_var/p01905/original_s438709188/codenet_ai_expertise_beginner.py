N, M = map(int, input().split())

if M == 0:
    print(N - 1)
else:
    a = [False] * 256
    for i in range(M):
        x = int(input())
        a[x] = True

    def calc(l, n):
        if n == 2:
            if a[l] and a[l+1]:
                return [0, True]
            if a[l] or a[l+1]:
                return [0, False]
            return [1, False]
        m = n // 2
        t1 = calc(l, m)
        t2 = calc(l + m, m)
        if t1[1] and t2[1]:
            return [t1[0] + t2[0], True]
        if t1[1] or t2[1]:
            return [t1[0] + t2[0], False]
        return [t1[0] + t2[0] + 1, False]

    result = calc(0, N)
    print(result[0])