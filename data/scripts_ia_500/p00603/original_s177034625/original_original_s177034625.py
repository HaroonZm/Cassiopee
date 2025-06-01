try:
    while 1:
        N, R = map(int, input().split())
        *C, = map(int, input().split())
        *A, = range(N)
        for c in C:
            lb = N//2; la = N - lb
            TA = A[N//2:]
            TB = A[:N//2]
            A = []
            a = b = 0
            while a < la and b < lb:
                A.extend(TA[a:min(a+c, la)])
                a += c
                A.extend(TB[b:min(b+c, lb)])
                b += c
            if a < la:
                A.extend(TA[a:])
            if b < lb:
                A.extend(TB[b:])
        print(A[-1])
except EOFError:
    ...