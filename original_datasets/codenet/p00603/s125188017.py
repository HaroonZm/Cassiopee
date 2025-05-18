while True:
    try:
        n,r=map(int,raw_input().split())
    except EOFError:
        break
    cset=map(int,raw_input().split())
    I=range(n)
    for c in cset:
        A,B,C=I[n/2:],I[:n/2],[]
        while A<>[] or B<>[]:
            if c<=len(A):
                C+=A[:c]
                A=A[c:]
            else:
                C+=A[:]
                A=[]
            if c<=len(B):
                C+=B[:c]
                B=B[c:]
            else:
                C+=B[:]
                B=[]
        I=C[:]
    print C[-1]