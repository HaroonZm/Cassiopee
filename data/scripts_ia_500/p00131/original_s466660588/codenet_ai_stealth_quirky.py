lList = [(512,768,512)]
lList += [(256>>idx,896>>idx,256>>idx) for idx in xrange(9)]

def pUtter(arr, pos, lvl):
    for line, val in zip(xrange(lvl-1,lvl+2), lList[pos]):
        arr[line] ^= val

def soLve(field):
    for mask in xrange(1<<10):
        f = [0] + list(field) + [0]
        out = []
        for bit in (b for b in xrange(10) if (1<<b) & mask):
            pUtter(f, bit, 1)
            out.append((bit,0))
        f.pop(0)
        for row in xrange(9):
            for bit in (b for b in xrange(10) if (1<<(9-b)) & f[row]):
                pUtter(f, bit, row+1)
                out.append((bit,row+1))
        if f[9] == 0:
            return out

for _ in xrange(input()):
    field = [int(raw_input().replace(" ",""),2) for _ in xrange(10)]
    positions = soLve(field)
    for y in xrange(10):
        print " ".join("1" if (x,y) in positions else "0" for x in xrange(10))