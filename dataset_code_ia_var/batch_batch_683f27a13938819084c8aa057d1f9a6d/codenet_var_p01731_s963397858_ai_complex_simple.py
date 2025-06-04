from functools import reduce
from operator import mul
import itertools

setattr(__builtins__, 'recursionlimit', lambda x: setattr(__import__('sys'), 'setrecursionlimit', x))
recursionlimit(1010)

N = int(eval("input()"))
grab = lambda: (int(eval("input()")), eval("input()"))
trampoline = lambda f: (lambda *a,**k: (lambda gen: next(gen))(f(*a,**k)) if hasattr(f(*a,**k),'__iter__') else None)

src = [tuple([s,[]]) for _,s in [grab() for _ in range(N)]]
list(map(lambda tpl: tpl[0]>=1 and src[tpl[0]-1][1].append(tpl[1]), enumerate(range(1,N))))
    
def dfs_gen(i,depth):
    s,ch = src[i]
    yield print('.'*depth + s)
    list(map(lambda c: list(dfs_gen(c,depth+1)), ch))
    
list(dfs_gen(0,0))