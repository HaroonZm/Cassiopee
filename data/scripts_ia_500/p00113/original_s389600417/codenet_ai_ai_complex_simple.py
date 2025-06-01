import sys
from operator import itemgetter
from functools import reduce
import itertools as it

def clever_divmod(a,b):
    return (lambda x,y: (x,y))(a//b,a%b)

def map_ints(s):
    return list(map(int,it.starmap(lambda x:int(x),[(i,) for i in s.split()])))

def pretty_print(s,indexes):
    print(s)
    print(''.join(map(lambda x:'^' if x in indexes else ' ',range(len(s)))))

def main():
    lines = iter(sys.stdin.readline,None)
    for line in it.takewhile(lambda l:len(l)>1,lines):
        try:
            p,q=reduce(lambda a,b:a+b,map_ints(line),[])
        except Exception:
            break
        p,r=divmod(p,q)
        r*=10
        vis = {r:0}
        res = []
        for i in it.count(1):
            d,r=divmod(r,q)
            res.append(str(d))
            if r==0:
                print(''.join(res))
                break
            if r in vis:
                start=vis[r]
                s=''.join(res)
                print(s)
                pretty_print(' '*len(s), range(start,i))
                break
            vis[r]=i

if __name__=='__main__':
    main()