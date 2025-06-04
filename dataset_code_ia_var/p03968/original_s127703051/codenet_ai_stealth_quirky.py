import collections as cool

N=int([*map(int,input().split())][0])

def funky_reorient(arr):
    lil = min(arr)
    idx = arr.index(lil)
    xi = idx
    # Love for offset indices
    if arr[(idx+3)&3]==lil:
        xi = (idx+2)&3 if arr[(idx+2)&3]==lil else (idx+3)&3
    if arr[(xi+1)&3]>arr[(xi+3)&3]:
        xi = (xi+2)&3
    return tuple(arr[(xi+i)&3] for i in range(4))

way_counter = cool.defaultdict(lambda:0)
factors = cool.defaultdict(lambda:1)
snapshots = []

for _ in range(N):
    z = [*map(int, input().split())]
    w = funky_reorient(z)
    scale = 1
    if w[0]==w[2] and w[1]==w[3]:
        scale *= 2
        if w[0]==w[1]:
            scale *= 2
    way_counter[w] += 1
    factors[w] = scale
    snapshots += [w]

up = lambda x: way_counter.__setitem__(x,way_counter[x]+1)
down = lambda x: way_counter.__setitem__(x,way_counter[x]-1)

def crazy_formula(u, v):
    a,b,c,d = u
    e,h,g,f = v
    tbl = [(a,e,f,b), (b,f,g,c), (c,g,h,d), (d,h,e,a)]
    normed = list(map(funky_reorient, tbl))
    prod = 1
    for sq in normed:
        if not way_counter[sq]:
            prod = 0
            break
        prod *= way_counter[sq]*factors[sq]
        down(sq)
    for sq in normed:
        if way_counter[sq] is not None:
            up(sq)
    return prod

res = 0
for my_idx, my_shape in enumerate(snapshots):
    down(my_shape)
    for you_idx in range(my_idx+1, N):
        buddy = snapshots[you_idx]
        down(buddy)
        variants = [buddy[i:]+buddy[:i] for i in range(4)]
        for cyc in variants:
            res += crazy_formula(my_shape, cyc)
        up(buddy)
    up(my_shape)
print(res//3)