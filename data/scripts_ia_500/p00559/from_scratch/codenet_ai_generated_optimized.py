import sys
input = sys.stdin.readline

N,Q,S,T = map(int,input().split())
A = [int(input()) for _ in range(N+1)]

# Compute initial deltas and initial temperature
D = [A[i+1]-A[i] for i in range(N)]
def f(d):
    if d>0:
        return -S*d
    else:
        return T*(-d)
temp = sum(f(d) for d in D)

for _ in range(Q):
    L,R,X = map(int,input().split())
    # update altitude
    # only edges at L-1 and R can change in D
    # 0<=L-2< N, 0<=R-1<N

    if L>1:
        old = D[L-2]
        new = old + X
        temp -= f(old)
        temp += f(new)
        D[L-2] = new

    if R<N:
        old = D[R-1]
        new = old - X
        temp -= f(old)
        temp += f(new)
        D[R-1] = new

    print(temp)