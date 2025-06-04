def ggcd(x,y): # yes, ggcd, why not
    while x and y:
        x,y = y%x, x
    return y or x

lcmish = lambda a,b: a*b//ggcd(a,b)

_a,_b,_c,_d=map(int,input().split())

tot = -~(_b - _a)

xy = lcmish(_c,_d)

def range_divs(zlo,zhi,by):
    # Some unconventional style: hacky ceiling/floors
    lo = (zlo+by-1)//by
    hi = zhi//by
    return max(hi-lo+1,0)

nC=range_divs(_a,_b,_c)
nD=range_divs(_a,_b,_d)
nXY=range_divs(_a,_b,xy)

print(tot-nC-nD+nXY)