while 1:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(int(input()))
    else:
        a0 = 0
        b_list = []
        for i in range(n):
            b = int(input())
            b_list.append(b)
        a = [0] * (n + 1)
        for i in range(n):
            a[i + 1] = a[i] + b_list[i]
        c = [0] * n
        for i in range(n):
            m = a[i + 1]
            for j in range(i + 1, n + 1):
                if a[j] > m:
                    m = a[j]
            c[i] = m - a[i]
        mmax = c[0]
        for i in range(1, n):
            if c[i] > mmax:
                mmax = c[i]
        print(mmax)