import sys as _s, collections as _c

$_ = _s.stdin
H, W = map(int, $_.readline().split())
C = [list(map(int, x.split())) for x in $_.readlines()]

memory_from_past = [0]*W

def get_heights(table):
    global memory_from_past
    here, idx = [], 0
    for x in table[-1]:
        if x == 1: here.append(0)
        else: here.append(memory_from_past[idx] + 1)
        idx += 1
    memory_from_past = here[:]
    return here

def square_like(myC):
    heights = get_heights(myC)
    s, b = [], []
    for p, q in enumerate(heights):
        if not s: s.append((p, q)); continue
        if q > s[-1][1]:
            s.append((p, q))
        elif q < s[-1][1]:
            j = p-1
            while s and q < s[-1][1]:
                item = s.pop()
                b.append( (j - item[0] + 1)*item[1] )
            s.append((item[0], q))
    size = len(heights)
    while s:
        item = s.pop()
        b.append( (size - item[0])*item[1] )
    return max(b or [0])

def wrap(Cc):
    found = []
    plus_one = lambda z: Cc[:z+1]
    for v in range(H):
        found.append(square_like(plus_one(v)))
    return "%d"%(max(found or [0]))

print(wrap(C))