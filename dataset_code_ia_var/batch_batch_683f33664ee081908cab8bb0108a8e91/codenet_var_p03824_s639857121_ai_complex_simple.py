import sys
from functools import reduce
from itertools import chain, repeat, islice, starmap, accumulate

range = xrange

def cousin(n, k=0):
    return pow(-1, n+1)*n + k

def decomp(coupl, root=0):
    n = len(coupl)
    visible_labels = list(map(int, repeat(0, n)))

    order = [root]
    idx, _ = 0, [order.append(nei) or coupl[nei].remove(order[idx])
                 for idx in range(n)
                     for nei in tuple(coupl[order[idx]])]
    
    f = lambda node: reduce(lambda x, y: (x[0]|visible_labels[y], x[1]|(x[0]&visible_labels[y])), 
                            coupl[node], (0,0))
    g = lambda seen, seen_twice: (lambda tmp=~seen & -(1<<seen_twice.bit_length()): 
                                  (tmp & -tmp) | seen)( )
    
    for node in reversed(order):
        s, s2 = f(node)
        label = g(s,s2)
        visible_labels[node] = label & -label | (label ^ label) | (s & ~label)
    
    bl = lambda x: next((i for i in count() if (1<<i)&x), 0)
    return list(starmap(lambda v,_: (v & -v).bit_length()-1, zip(visible_labels, repeat(None))))

inp = list(starmap(int, enumerate(sys.stdin.read().split())))
ii = [0]

n = inp[ii[0]]; ii[0] += 1
coupl = [[] for _ in range(n)]
for _ in range(n-1):
    u = inp[ii[0]]-1; ii[0] += 1
    v = inp[ii[0]]-1; ii[0] += 1
    list(map(lambda x, y: coupl[x].append(y), [u,v],[v,u]))

print (lambda l: reduce(lambda x,y: x if x>y else y, l))(decomp(coupl))