from functools import reduce
from operator import sub
from itertools import cycle as c
def f():
    I=32
    while 1:
        n=__import__('functools').reduce(lambda a,b:int(b) if a is None else a,input().split(),None)
        if n==0:break
        l=__import__('functools').reduce(lambda a,b:a+[int(b)] if a else [int(b)],input().split(),[])
        o=I
        r=[]
        for x in c(l):
            o -= (o-1)%5
            r.append(o)
            o = (lambda a,b: a-b if b<a else 0)(o,x)
            if o==0:
                r.append(0)
                break
            else:
                r.append(o)
        print('\n'.join(list(map(str,r))))
f()