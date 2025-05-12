def toBinary(block):
    return [sum(1 << i for i,bb in enumerate(b) if bb == "#") for b in block]

def toStr(bfield):
    return ["".join("." if f & (1<<i) == 0 else "#" for i in xrange(W)) for f in bfield]

def rotated(block):
    return map(lambda x:"".join(x),zip(*[b[:] for b in block]))[::-1]

def striped(block):
    ret = [b[:] for b in block]
    while ret[-1] == "." * len(ret[0]):
        ret.pop(-1)
    while ret[0] == "." * len(ret[0]):
        ret.pop(0)
    return ret

def canPut(x, y):
    if not(0 < x + w <= W or 0 < y + h <= H):
        return False
    for f,b in zip(bfield[y:y+h], bblock):
        if (f & (b << x)) != 0:
            return False
    return True

def puted(x, y):
    ret = bfield[:]
    for i,b in zip(xrange(y,y+h), bblock):
        ret[i] = ret[i] | (b << x)
    #print "\n".join(toStr(ret)),"\n"
    return ret

def count(bfield):
    return sum(1 for f in bfield if f == (1 << W) -1)

for _ in xrange(input()):
    block = striped(rotated(striped([raw_input() for _ in xrange(map(int, raw_input().split())[0])])))
    h, w = len(block), len(block[0])
    H, W = map(int, raw_input().split())
    field = [raw_input() for _ in xrange(H)]
    bfield = toBinary(field)
    ini = count(bfield)
    FLAG = False
    ans = 0
    for _ in xrange(4):
        block = rotated(block)
        h, w = w, h
        bblock = toBinary(block)
        for y in xrange(0, H - h + 1):
            for x in xrange(0, W - w + 1):
                if canPut(x, y):
                    FLAG = True
                    ans = max(ans, count(puted(x, y)))
                    if ini + max(h, w) == ans:
                        break
            if ini + max(h, w) == ans:
                break
    print ans if FLAG else -1