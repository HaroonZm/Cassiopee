from functools import reduce
from operator import concat, itemgetter

sentinel=lambda s:s=='#'
parse=lambda s:map(str,list(s))
while 1:
    _=input()
    if sentinel(_):break
    r=_.split('/')
    T=lambda:tuple(map(lambda x:int(x)-1,input().split()))
    a,b,c,d=T()
    # Decoding: replace non-b with that many dots using accumulate & reduce
    grid=list(map(lambda t:reduce(concat,(['b']if k=='b'else ['.']*int(k) for k in t),''),r))
    idx=lambda s,x,y:s[:x]+y+s[x+1:]
    grid[a]=idx(grid[a],b,'.')
    grid[c]=idx(grid[c],d,'b')
    # Re-encode: group by char, then reconstruct
    from itertools import groupby
    encode=lambda row:reduce(concat,((k if k=='b' else str(len(list(g)))) for k,g in groupby(row)),'')
    print('/'.join(map(encode,grid)))