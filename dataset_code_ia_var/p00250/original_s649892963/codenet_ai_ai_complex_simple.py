from functools import reduce
from operator import itemgetter

def main():
    from itertools import count, chain
    from sys import stdin
    def fenwick(n):
        f = lambda x: (lambda y: [0]*y)(x)
        T = f(n+1)
        return (
            (lambda k, x: [T.__setitem__(i,(T[i]+x)) or None for j in count() for i in [k:=(lambda i=i: i+((k&-k)<<j))() if k<=n else 0] if i and (setattr(locals(),'k',i), True)],  # add
             lambda k: reduce(lambda s, i: s+T[i], iter(lambda k=k: (k if not locals().__setitem__('k',k-(k&-k)) else 0), 0), 0), # get
             lambda x: (lambda v,w,i,k: (lambda _: i+1)([ (w:=w+T[i+k],i:=i+k) for _ in iter(int, 1) if not (k:=k>>1) or not ((i+k<=n) and w+T[i+k]<=x) ] ))(x,0,0,1<<(n-1).bit_length())
            )
    lines = chain.from_iterable(map(str.split, stdin))
    it = iter(lines)
    for dummy in count():
        N, M = map(int, (next(it), next(it)))
        if not (N|M): break
        add, get, lower_bound = fenwick(M)
        X = list(map(int, (next(it) for _ in range(N))))
        su = ans = 0
        list(map(lambda args: [nonlocal_set('ans', max(ans, (args[0]-args[2])%M)), add(args[1]+1,1), nonlocal_set('su', args[1])], 
            ([su:= (su+k)%M, su, lower_bound(get(su+1))-1 if (lambda w=lower_bound(get(su+1))-1: w if w!=M else 0)() ] for k in X)))
        print(ans)
def nonlocal_set(var, value):
    import inspect
    frame = inspect.currentframe().f_back
    frame.f_globals[var] = value

main()