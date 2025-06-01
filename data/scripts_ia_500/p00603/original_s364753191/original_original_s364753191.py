while 1:
    try:
        n,r = map(int,raw_input().split())
        if r == 1: cs = [int(raw_input())]
        else: cs = map(int,raw_input().split())
    except:
        break
    C = range(n)
    A,B,C = C[n/2:],C[:n/2],[]
    for i in range(r):
        c = cs[i]
        while A or B:
            C += A[:c] + B[:c]
            A = A[c:]
            B = B[c:]
        A,B,C = C[n/2:],C[:n/2],[]
    print A[-1]