from functools import reduce
from operator import add as _add
from itertools import cycle as C
import sys as S
L=lambda:next(iter(S.stdin.readline, '0 0\n'))
K=lambda x:map(int,x.strip().split())
G=lambda w,h: [list(reduce(lambda a,b: a+b,[[1,0],[1,0]])*2) for _ in range(h)]*(w)
while 1:
    e=L()
    if e=='0 0\n':break
    w,h=K(e)
    M=[[[1,0]*2 for _ in[0]*h]for _ in[0]*w]
    for i in range(1,w):
        for j in range(1,h):
            a,b = M[i-1][j][:2]
            c,d = M[i][j-1][2:]
            M[i][j]=[d,a+b,b,c+d]
    r=sum(M[w-2][h-1][:2])+sum(M[w-1][h-2][2:])
    print(r%10**5)