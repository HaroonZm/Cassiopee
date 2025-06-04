import sys
import operator

def _input(): return sys.stdin.buffer.readline()
def _inputs(): return sys.stdin.buffer.read().split()
def _input_lines(): return sys.stdin.buffer.readlines()

class UF:
    def __init__(z, ln): z._p=list(range(ln+1))
    def __call__(z,a):
        p=z._p
        while p[a]!=a:p[a]=p[p[a]];a=p[a]
        return a
    def m(z,x,y):
        x=z(x)
        y=z(y)
        if x==y:return
        if x>y:x,y=x,y
        else:x,y=y,x
        p=z._p;p[y]=x

n=int(_input())
lst=list(map(int,_inputs()))
K=n+n
T=sorted(zip(lst,lst,lst),key=lambda q:q[2],reverse=True)

U=UF(K)
q=[0]*K;r=[0]*K;s=[0]*K

it=n+1
for cnt,(d,e,f) in enumerate(T,it):
    g=U(d)
    h=U(e)
    q[g]=cnt
    q[h]=cnt
    r[cnt]=f
    U.m(g,cnt)
    U.m(h,cnt)

sz=[0]+[1]*n+[0]*(n-1)
for j in range(K):
    x=q[j]
    sz[x]+=sz[j]

for idx in range(K):
    x=q[idx]
    r[idx]=0
    if x==0: continue
    r[idx]=r[x]*(sz[x]-sz[idx])
for z in range(K-2,0,-1):
    k=q[z]
    r[z]+=r[k]

for t in range(1,n+1):
    print(r[t])