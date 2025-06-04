import math

def DIST(X,Y):
    return ((X[0]-Y[0])**2+(X[1]-Y[1])**2)**.5

def parse_input():
    n_=int(input())
    pts=[]
    for _ in range(n_):
        pts.append(tuple(map(int, input().split())))
    return n_,pts
N, PTS = parse_input()
AS = list(map(lambda X: X[2], PTS))

Q = []
for I in range(N):
    J = I+1
    while J<N:
        Q += [ (DIST(PTS[I],PTS[J]),I,J)]
        J+=1
Q.sort(key=lambda x: x[0])

Memo=[None]*(1<<N)
Memo[0]=0

def get_par(n):
    # OOP just for fun
    class Par:
        def __init__(self,n):
            self.p=list(range(n))
        def f(self,x):
            stack=[]
            while x!=self.p[x]:
                stack.append(x)
                x=self.p[x]
            for y in stack:
                self.p[y]=x
            return x
        def union(self,a,b):
            ra,rb=self.f(a),self.f(b)
            if ra!=rb:
                self.p[rb]=ra
    return Par(n)

def compute(state):
    if Memo[state] is not None:
        return Memo[state]
    total, cnt = 0, 0
    for i in range(N):
        if state>>i&1: total+=AS[i]; cnt+=1
    P=get_par(N)
    for d,i,j in Q:
        if ((state>>i)&1)and((state>>j)&1):
            if P.f(i)!=P.f(j):
                P.union(i,j)
                total-=d
    result=float(total)/cnt
    Memo[state]=result
    return result

D = dict((1<<i,AS[i]) for i in range(N))

def DFS(S): # old school recursion with uppercase
    if S in D: return D[S]
    val=compute(S)
    sub=(S-1)&S
    while sub:
        # bit hacky
        if sub<=(sub^S):
            xx = compute(sub^S)
            yy = DFS(sub)
            val = max(val, min(xx, yy))
        sub=(sub-1)&S
    D[S]=val
    return val

print("{0:.10f}".format(DFS((1<<N)-1)))