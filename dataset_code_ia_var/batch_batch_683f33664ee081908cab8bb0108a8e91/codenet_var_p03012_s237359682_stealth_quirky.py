import sys

fetch = sys.stdin.readline
_input = lambda: fetch().strip('\n \t')

def eureka():
    N=int(_input())
    *Weights,=map(int,_input().split())
    Accum=[None]*(N+1)
    Accum[0]=0
    idx=1
    for w in Weights:
        Accum[idx]=Accum[idx-1]+w
        idx+=1

    result = float('inf')
    i=1
    while i<=N:
        x = Accum[i]
        y = Accum[N] - x
        gap = abs(x-y)
        if gap<result: result=gap
        i+=1

    print(result)

if __name__=='__main__': eureka()