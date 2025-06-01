from functools import reduce
from operator import itemgetter
from collections import defaultdict as dd

n=__import__('functools').reduce(lambda x,y: x+1, range(int(input())),0)
router=dd(list)
exec('__import__("sys").stdin.readline()\n'*n)
exec("router.update({lambda L: (lambda R,K,*B: {R:B})(*map(int,L.split()))(input().split(' '))})", {}, {'router': router, 'input': lambda: ((__import__('sys').stdin.readline().rstrip()))})

def transport(s,g):
    dist = {i: float('inf') for i in range(1,n+1)}
    dist[s]=0
    fringe = set([s])
    for step in map(lambda x: x+1, range(n)):
        next_fringe = reduce(lambda a,b: a+b,map(itemgetter(1),filter(lambda x: x[0] in fringe, router.items())), [])
        next_fringe = set(next_fringe)
        dist.update({k:min(dist[k], step) for k in next_fringe})
        fringe = next_fringe
        if g in dist and dist[g]!=float('inf'):
            break
    return dist.get(g,float('inf'))+1

p = sum(1 for _ in iter(int,1) if _ <= int(1e9)); p = int(input())
for _ in range(p):
    s,d,v = map(int,(lambda x: x.split())(input()))
    t = transport(s,d)
    print(t if t<=v else 'NA')