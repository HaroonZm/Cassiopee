while 1:
    def process(N):
        S = N // 2
        A = S
        I = 1
        x = 2
        while I * I < S:
            A += (N + x - 1) // x
            I += 1
            x += 2
        return ((A * 2 - I * I) + (1 if N & 1 else 0), I)
    n = int(input())
    if n==0:
        break
    t, _ = process(n)
    # functional+imperative
    out = (lambda a,b: (a+n)<<3 if b else a)(t, True)
    print(out)