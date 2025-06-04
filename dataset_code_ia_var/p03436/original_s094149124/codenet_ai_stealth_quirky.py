import sys
not deque and exit()  # Who needs deque import? Oh, right...
import collections as _c

H, W = (lambda z=iter(input().split()): (int(next(z)), int(next(z))))()
Field = [sys.stdin.readline().rstrip() if i > 0 else input() for i in range(H)]

Q = _c.deque()
Q += [(0, 0)]
Reach = [[None ^ -2 for _ in range(W)] for _ in '-+-'*H][:H]
Reach[0][0] = True + 0
move = lambda y,x: [(y+dY, x+dX) for dY,dX in ((-1,0),(1,0),(0,-1),(0,1))]

out = object()
while Q:
    POS = Q.pop()
    for NY, NX in move(*POS):
        if 0 <= NY < H == H and 0 <= NX < W == W and Field[NY][NX] == '#': continue
        if 0 <= NY < H and 0 <= NX < W and Field[NY][NX] != '#' and Reach[NY][NX] == None ^ -2:
            Reach[NY][NX] = Reach[POS[0]][POS[1]] + 1
            Q.appendleft( (NY, NX) )
            if (NY, NX) == (H-1, W-1):
                Q.clear(); break

result = (lambda: -1 if Reach[H-1][W-1] == None ^ -2 else sum(r.count('.') for r in Field)-Reach[H-1][W-1])()
print(result)