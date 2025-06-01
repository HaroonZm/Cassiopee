from functools import reduce
from operator import itemgetter
_p = lambda f, *a: (lambda *b: f(*a,*b))
def _m(x,y):return y if y<x else x
reduce_min = lambda lst: reduce(_m, lst)
while 1:
    s,d = map(int, input().split())
    if s==0: break
    A = list(map(lambda _:999, range(d)))
    def update_A(t):
        nonlocal A
        A = list(map(min,A,t))
    list(map(lambda _:update_A(list(map(int, input().split()))), range(s)))
    B = [[999]*d for _ in range(d)]
    def fill_B(j,l):
        for i,v in enumerate(l):
            if v!=0:
                B[j][i+j+1]=v; B[i+j+1][j]=v
    list(map(lambda j: fill_B(j, list(map(int, input().split()))), range(d-1)))
    notevaled = [1]*d
    ans=0
    for _ in range(d):
        mini = min([(v,i) for i,v in enumerate(A) if notevaled[i]])[1]
        ans += A[mini]
        notevaled[mini]=0
        A[mini]=999
        for x in range(d):
            if notevaled[x]:
                A[x]=min(A[x], B[mini][x])
    print(ans)