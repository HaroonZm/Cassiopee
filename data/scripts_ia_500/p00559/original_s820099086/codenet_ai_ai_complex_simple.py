from operator import itemgetter
from functools import reduce

N,Q,S,T=map(int,input().split())
A=[*map(int,[input()for _ in range(N+1)])]
diff=list(map(lambda x,y:(lambda z:z[1]-z[0])(x),zip(A,A[1:])))

def calc(v):
    return (lambda f,g,h,fv:fv(f,g,h))(lambda s,t,x:-s*x if x>0 else -t*x,S,T,v)

ret=reduce(lambda acc,i:acc+calc(i),diff,0)

def update_ret(pos,delta):
    global ret
    ret-=calc(diff[pos])
    diff[pos]+=delta
    ret+=calc(diff[pos])

for _ in range(Q):
    a,b,c=map(int,input().split())
    update_ret(a-1,c)
    if b!=N:
        update_ret(b,-c)
    print(ret)