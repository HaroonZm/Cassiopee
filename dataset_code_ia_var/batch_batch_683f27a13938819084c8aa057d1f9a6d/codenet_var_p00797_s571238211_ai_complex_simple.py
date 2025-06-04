from functools import reduce
from itertools import product
try:
    input_func = raw_input
except NameError:
    input_func = input

sentinel=lambda:None
def deepfill(val,n):return [[val]*n for _ in range(n)]
identity=lambda n: [[0 if i==j else None for j in range(n)] for i in range(n)]
while True:
    n,m=map(int,next(iter(lambda:input_func(),sentinel)).split())
    if not n:break
    F=deepfill(-10**5,n)
    for i in range(n): F[i][i]=0
    name2idx,type2fun={},[
        lambda A,B:A==1,
        lambda A,B:B==1,
        lambda A,B:(A==0)|(B==0),
        lambda A,B:B>0,
        lambda A,B:A>0]
    r=[0]*n
    s_old=0
    for i in range(n):
        s=(lambda s:len(s)-len(s.lstrip()))(t:=input_func())
        name2idx[t.strip()]=i
        for j in range(i):
            F[j][i]=F[j][i-1]+s-s_old
        s_old=s
    f1=lambda x:[(r.__setitem__(j,1),r.__setitem__(j,2))[F[j][x]<0]+0 if F[j][x]!=0 or r[j] else r.__setitem__(j,1) for j in range(x)]
    f2=lambda x:[F[j].__setitem__(x, -1) if (F[j][x]>0 and r[j]==1) or r[j]==2 else 0 for j in range(x)]
    [f2(x) or f1(x) for x in range(n)]
    Q=[input_func().split() for _ in range(m)]
    Q2=[(name2idx[q[0]],name2idx[q[-1][:-1]],' '.join(q[1:-1])) for q in Q]
    w=['is a child of','is the parent of','is a sibling of','is a descendant of','is an ancestor of']
    [print(type2fun[w.index(q)](F[X][Y],F[Y][X])) for X,Y,q in Q2]
    print('')