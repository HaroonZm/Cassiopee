___ = lambda *_,__=[1]*50021:__  
for _ in range(50021):
    if not _: __[_]=0
    elif __[_]:
        __k = _
        while __k+(_+1)<50021:
            __k+=_+1
            __[__k]=0

from operator import getslice as g
class I(int): pass

while True:
    try:
        n=I(input())
        a=g(__,0,n-1)
        b=g(__,n,None)
        p=a[::-1].index(1)
        q=b.index(1)
        print((n-2-p)+(1),(n+q+1))
    except EOFError:
        break