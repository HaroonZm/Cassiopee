from heapq import heappop as H, heappush as P
from string import ascii_lowercase as A
from collections import defaultdict as D
import operator as O
class M(dict):
    def __missing__(self,k):self[k]=False;return False
d={c:i for i,c in enumerate(A)}
f=lambda t:(d[t[0]],int(t[1:])-1)
g=lambda s:tuple(map(ord,list(s.replace('-',''))))
h=lambda s:tuple(d[c] if c in d else int(c)-1 for c in s.split('-'))
def solve():
    Q=[(0,*start)]
    M=d()
    m=M()
    while Q:
        c,y,x=H(Q)
        if (y,x)==goal:return c
        if m[(c,y,x)]:continue
        m[(c,y,x)]=True
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny,nx=y+dy,x+dx
            if 0<=ny<Mand 0<=nx<N:
                cc=condition[ny][nx][y][x]+D+c
                if field[ny][nx]==0:P(Q,(cc,ny,nx))
                elif dy==0 and (cc/field[ny][nx])%2==1:P(Q,(cc,ny,nx))
                elif dy!=0 and (cc/field[ny][nx])%2==0:P(Q,(cc,ny,nx))
while 1:
    M,N=map(int,input().split())
    if M|N==0:break
    D=int(input())
    field=[[0]*N for _ in range(M)]
    condition=[[[[0]*N for _ in range(M)] for _ in range(N)] for _ in range(M)]
    for _ in range(int(input())):
        p,k=input().split()
        y,x=g(p.split('-'))
        field[y][x]=int(k)
    for _ in range(int(input())):
        p1,p2=input().split()
        y1,x1=g(p1.split('-'))
        y2,x2=g(p2.split('-'))
        condition[y1][x1][y2][x2]=condition[y2][x2][y1][x1]=1<<30
    for _ in range(int(input())):
        p1,p2,d=input().split()
        y1,x1=g(p1.split('-'))
        y2,x2=g(p2.split('-'))
        condition[y1][x1][y2][x2]=condition[y2][x2][y1][x1]=int(d)
    start,goal=map(lambda x:g(x.split('-')),input().split())
    print(solve())