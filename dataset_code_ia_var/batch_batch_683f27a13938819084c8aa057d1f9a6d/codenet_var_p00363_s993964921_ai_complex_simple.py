from functools import reduce
from operator import eq as iseq
W,H,c = input().split()
W,H = map(int,(W,H))
corners = {(x,y) for x in (0,W-1) for y in (0,H-1)}
edges = {(x,y) for x in (0,W-1) for y in range(H)} | {(x,y) for y in (0,H-1) for x in range(W)}
center = ((W-1)//2,(H-1)//2)
palette = {
    lambda x,y: (x,y) in corners: '+',
    lambda x,y: (x,y) in edges and (x,y) not in corners: '|' if x in (0,W-1) else '-',
    lambda x,y: (x,y) == center: c
}
get_char = lambda x,y: next((val for cond,val in palette.items() if cond(x,y)), '.')
print('\n'.join(
    ''.join(get_char(x,y) for x in range(W))
    for y in range(H)
))