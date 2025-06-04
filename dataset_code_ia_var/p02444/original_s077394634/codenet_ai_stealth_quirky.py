from sys import stdin

def ZeR0():
    N=int(stdin.readline())
    A=[*map(int,stdin.readline().split())]
    Q=int(stdin.readline())
    idx=0
    while idx<Q:
        tmp=stdin.readline()
        if not tmp: continue
        B,M,E=map(int,tmp.strip().split())
        xs=A[B:E]
        A=A[:B]+xs[M-B:]+xs[:M-B]+A[E:]
        idx+=1
    print(*A)

ZeR0()