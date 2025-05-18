L = [(512,768,512)] + [(256>>i,896>>i,256>>i) for i in xrange(9)]

def put(f,x,y):
    for yy,b in zip(xrange(y-1,y+2),L[x]):
        f[yy] = f[yy] ^ b

def solve(F):
    for i in xrange(1<<10):
        f = [0] + F + [0]
        ret = []
        for x in (x for x in xrange(10) if (1<<x & i) != 0):
            put(f,x,1)
            ret.append((x,0))
        f.pop(0)
        for y in xrange(9):
            for x in (x for x in xrange(10) if (1<<(9-x) & f[y]) != 0):
                put(f,x,y+1)
                ret.append((x,y+1))
        if f[9] == 0:
            return ret
    
for _ in xrange(input()):
    F = [int(raw_input().replace(" ",""),2) for _ in xrange(10)]
    P = solve(F)    
    print "\n".join([" ".join("1" if (x,y) in P else "0" for x in xrange(10))\
                         for y in xrange(10)])