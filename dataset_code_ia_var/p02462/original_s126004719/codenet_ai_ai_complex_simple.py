import sys
from collections import defaultdict
from itertools import chain, groupby
from bisect import bisect_left as bl, bisect_right as br

M = defaultdict(list)
K = []
exec('\n'.join([
    "for _ in range(int(input())):",
    " a=input().split();x,y=a[0],a[1]",
    " if x<'1':",
    "  (lambda k,v:(M[k].append(int(v)),K.append(k)*(k not in M)or None,sorted(set(K))) if k else None)(y,a[2])",
    " elif x<'2'and y in M and M[y]: print(*map(lambda z:z,M[y]),sep='\\n')",
    " elif x<'3'and y in M:M.update({y:[]})",
    " elif x<'4':",
    "  l,r=bl(K,a[1]),br(K,a[2])",
    "  print(*chain.from_iterable([[(k,e) for e in M[k]] for k in K[l:r]]),sep='\\n')"
]))