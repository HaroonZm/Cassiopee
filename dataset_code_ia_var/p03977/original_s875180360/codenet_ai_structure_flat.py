for _ in range(int(input())):
    tmp = input().split()
    N = int(tmp[0])
    D = int(tmp[1])
    ans = 0
    i = 0
    while i < 7:
        q = D // 2
        m = D % 2
        if N % 2 != m:
            add = N - 1
        else:
            add = N
        ans += add * (2 ** i)
        D = q
        i += 1
    print(ans)