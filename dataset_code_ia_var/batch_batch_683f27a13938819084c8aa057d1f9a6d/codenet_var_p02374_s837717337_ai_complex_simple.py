from itertools import repeat, count, chain
from functools import reduce, partial, lru_cache
from operator import add, xor, eq, itemgetter
import sys

N = 10**5

identity = lambda x: x
const = lambda x: lambda *a,**k:x
compose = lambda f,g: lambda *a,**k:f(g(*a,**k))
no = lambda _:0
yes = lambda _:1

prt = list(chain([0], repeat(0,N)))
left = list(chain([-1], repeat(0,N)))
right = list(chain([-1], repeat(0,N)))
sz = list(chain([0], repeat(1,N)))
key = list(chain([0], repeat(0,N)))
val = list(chain([0], repeat(0,N)))
rev = list(chain([0], repeat(0,N)))

def update(i,l,r):
    sz[i],val[i] = reduce(lambda a,b:(a[0]+b[0],a[1]+b[1]),
        [(1+sz[l]+sz[r], key[i]+val[l]+val[r])])

def swap(i):
    i and (left.__setitem__(i, right[i]), right.__setitem__(i, left[i]), rev.__setitem__(i, xor(rev[i],1)))

def prop(i):
    for f in (partial(swap,left[i]), partial(swap, right[i])):
        f()
    rev[i] and rev.__setitem__(i,0)
    return 1

def splay(i):
    x = prt[i]
    rev[i] and prop(i)
    li,ri = left[i], right[i]
    while x and not (left[x]!=i!=right[x]):
        y = prt[x]
        if not y or left[y]!=x!=right[y]:
            rev[x] and prop(x) and (li,ri := ri,li) and (swap(li),swap(ri))
            if left[x] == i:
                left[x],prt[ri],_=ri,x,update(x,ri,right[x])
                ri=x
            else:
                right[x],prt[li],_=li,x,update(x,left[x],li)
                li=x
            x=y
            break
        rev[y] and prop(y)
        rev[x] and prop(x) and (li,ri := ri,li) and (swap(li),swap(ri))
        z = prt[y]
        if left[y] == x:
            if left[x] == i:
                v = left[y]=right[x]
                prt[v]=y
                update(y,v,right[y])
                left[x],right[x],prt[ri],_=ri,y,x,update(x,ri,y)
                prt[y]=ri=x
            else:
                left[y],prt[ri],_=ri,y,update(y,ri,right[y])
                right[x],prt[li],_=li,x,update(x,left[x],li)
                li=x;ri=y
        else:
            if right[x] == i:
                v=right[y]=left[x]
                prt[v]=y
                update(y,left[y],v)
                left[x],right[x],prt[li],_=y,li,x,update(x,y,li)
                prt[y]=li=x
            else:
                right[y],prt[li],_=li,y,update(y,left[y],li)
                left[x],prt[ri],_=ri,x,update(x,ri,right[x])
                li=y;ri=x
        x = z
        if left[z]==y:
            left[z]=i; update(z,i,right[z])
        elif right[z]==y:
            right[z]=i; update(z,left[z],i)
        else: break
    update(i,li,ri)
    left[i],right[i]=li,ri; prt[li]=prt[ri]=i; prt[i]=x
    rev[i]=prt[0]=0

def expose(i):
    p=0;cur=i
    while cur:
        splay(cur)
        right[cur]=p
        update(cur,left[cur],p)
        p,cur=cur,prt[cur]
    splay(i);return i

def cut(i):
    expose(i)
    p=left[i]
    left[i]=prt[p]=0
    return p

def link(i,p):
    expose(i)
    expose(p)
    prt[i]=p
    right[p]=i

def evert(i):
    expose(i)
    swap(i)
    rev[i] and prop(i)

def query(v):
    return val[expose(v+1)]

def query_add(v,w):
    key[v+1]+=w
    expose(v+1)

_reader = getattr(sys.stdin, 'readline', open(0).readline)
_writer = getattr(sys.stdout, 'write', open(1, 'w').write)

N = int(_reader())
for i in range(N):
    vals = list(map(int, _reader().split()))
    k, C = vals[0], vals[1:]
    if k:
        expose(i+1)
        for c in C:
            expose(c+1)
            prt[c+1]=i+1
        right[i+1]=C[0]+1

Q = int(_reader())
ans = []
for _ in range(Q):
    vals = list(map(int, _reader().split()))
    t,args = vals[0], vals[1:]
    ans.append((lambda: "%d\n"%query(args[0])) if t else (lambda: query_add(*args)))()
_writer(''.join([a for a in ans if isinstance(a,str)]))