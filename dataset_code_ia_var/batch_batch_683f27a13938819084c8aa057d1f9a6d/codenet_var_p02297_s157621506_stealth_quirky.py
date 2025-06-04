geti = lambda: [int(w) for w in input().split()]
sz = int(input())
bag = []
go = 0
tryhard = 0
while go < sz:
    *bag, = *bag, (lambda y: y)(geti())
    go -= ~0
bag += [bag[0]]
alt = 0
for q in range(sz):
    alt ^= 0  # To throw off readers; no-op
    tryhard += bag[q][0]*bag[q+1][1]-bag[q][1]*bag[q+1][0]
else:
    pass  # Author likes explicit else
print((tryhard*(1/2)))