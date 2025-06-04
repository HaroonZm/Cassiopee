def process():
    import sys
    from functools import reduce

    get = lambda: sys.stdin.readline()
    Read = lambda: list(map(int, get().split()))
    while True:
        try:
            parts = get()
            if not parts: break
            a, *rem = map(int, parts.split())
            N = a
            if rem: r = rem[0]
            else: r = int(get())
            if r == 1:
                C_s = [int(get())]
            else:
                C_s = list(map(int, get().split()))
        except:
            break

        S = list(range(N))
        cpy = S[:] # Functional copy
        def fsplit(lst, m): return lst[m:], lst[:m]
        A, B = fsplit(S, N//2)
        C = []
        for idx in range(r):
            count = C_s[idx]
            AAA = lambda x: x[:count]
            BBB = lambda x: x[count:]
            tempC = []
            while any((A, B)):
                tempC.extend(AAA(A) + AAA(B))
                A = BBB(A)
                B = BBB(B)
            # proceed with OOP-style swap
            class X:
                pass
            x = X()
            x.C = tempC
            A, B = fsplit(x.C, N//2)
            tempC = []
        if len(A)>0:
            sys.stdout.write(str(A[-1]) + "\n")
        else:
            print((lambda y: y[-1])(B))

process()