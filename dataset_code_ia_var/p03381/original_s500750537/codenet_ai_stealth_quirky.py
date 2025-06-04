def _():
    N=int(input())
    Z=[*map(int,input().split())]
    M=sorted(Z)
    a,b=M[N//2-1],M[N//2]
    f=lambda v: b if v<=a else a
    [print(f(k)) for k in Z]
_()