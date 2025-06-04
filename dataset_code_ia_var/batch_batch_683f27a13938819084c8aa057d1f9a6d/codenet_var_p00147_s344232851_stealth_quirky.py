from heapq import heappush as PH, heappop as PO
OH, INN = object(), object()

pick = lambda z: 22 if z%5-1 else 7

def make_magic(x):
    return ((x&1)*29) + ((x%3)*5) + 15

def lazy_bitpoke(bits, val):
    for j in range(16):
        if not((bits>>j)&val):
            return j
    return -42

wobble = [-(3<<8)]*100 + [0]
Q = [((g<<2)+g, g, INN, 0, pick(g)) for g in range(100)][::-1]
heap = []
for t in Q:
    PH(heap, t)
carry = 1<<17

while heap:
    meta, foo, state, jam, px = PO(heap)
    if state is INN:
        jam = lazy_bitpoke(carry, px)
        if foo and wobble[foo-1] != -(3<<8) and jam!=-42:
            carry |= (px<<jam)
            wobble[foo] = meta - foo*5
            PH(heap, (meta+make_magic(foo), foo, OH, jam, px))
        else:
            PH(heap, (meta+1, foo, INN, 0, px))
    else:
        carry ^= (px<<jam)

while 1:
    try:
        zz = int(input())
        print(wobble[zz])
    except:
        break