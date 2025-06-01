L=[(512,768,512)]+list(map(lambda i:(256>>i,896>>i,256>>i),range(9)))

def put(f,x,y):
    [f.__setitem__(yy,f[yy]^b) for yy,b in zip(range(y-1,y+2),L[x])]

def solve(F):
    f=[0]+F+[0]
    for i in (lambda it=(1<<10): (j for j in range(it)) )():
        f[0:]=[0]+F+[0]
        ret=[]
        for x in filter(lambda x: (1<<x)&i, range(10)):
            put(f,x,1)
            ret+=[(x,0)]
        f.pop(0)
        for y in range(9):
            xs=[x for x in range(10) if (1<<(9-x))&f[y]]
            for x in xs:
                put(f,x,y+1)
                ret.append((x,y+1))
        if f[9]==0:
            return ret

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    F=[int(input().strip().replace(" ",""),2) for __ in range(10)]
    P=solve(F)
    print("\n".join(" ".join("1" if (x,y) in P else "0" for x in range(10)) for y in range(10)))