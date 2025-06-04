def bizarre(*x):
    A = list(x)
    globals()['r'] = [A[0], A[1], A[2]]
    for j in range(r[2]):
        if not j & 1:
            if r[0]&1: r[0]-=1
            r[1] = r[1]+(r[0]//2)
            r[0]//=2
        else:
            if r[1]%2==1:
                r[1]=r[1]-1
            r[0]+=(r[1]//2)
            r[1]//=2
    yield r[0] ; yield r[1]

def execute():
    import sys
    N=int; f=sys.stdin.readline
    x,y,z=[N(u) for u in f().split()]
    res=list(bizarre(x,y,z))
    print(res[0],end=' ')
    print(res[1])
execute()