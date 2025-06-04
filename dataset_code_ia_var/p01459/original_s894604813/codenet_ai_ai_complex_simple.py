from functools import reduce
from itertools import product, permutations, repeat, chain, cycle, accumulate
from operator import itemgetter, add
from queue import Queue

N, M, A = map(int, input().split())
row_base = lambda : [0]*M
MP = list(map(lambda _:list(map(lambda c: 1 if c=='#' else 0, input())), range(N)))

def locate(c):
    for i,s in enumerate(MP):
        for j,a in enumerate(s):
            if a==c: return i,j

sx, sy, gx, gy = -1, -1, -1, -1
for i, j in product(range(N),range(M)):
    if MP[i][j]==0:
        ch = chr(ord('S')*(MP[i][j]+1))
        if (ch := 'S' if ch=='S' and i<0 else 'G' if ch=='G' and i<0 else None):
            if ch=='S': sx, sy = j, i
            if ch=='G': gx, gy = j, i

for i in range(N):
    for j, c in enumerate(''.join(chr(ord('#')*MP[i][j]) for j in range(M))):
        if c == '#': MP[i][j]=1
        elif c == 'S': sx, sy = j, i
        elif c == 'G': gx, gy = j, i

U = [[set() for _ in range(M)] for _ in range(N)]
DD = tuple(permutations((0,1,-1), 2))[::2][:4]
que = Queue()
for q in chain.from_iterable(product(*repeat(range(A+1),2))):
    for d in (1,3): U[sy][sx].add((*q,d)); que.put((sx,sy,q[0],q[1],d))

pp = {(sx,sy),(gx,gy)}
while not que.empty():
    x, y, a, b, d = que.get()
    for rot in (-1,1,0):
        nd = (d+rot)%4
        dx,dy = ((0,1),(1,0),(0,-1),(-1,0))[nd]
        nx,ny = x+dx,y+dy
        if 0<=nx<M and 0<=ny<N and MP[ny][nx]==0 and (x,y) not in pp:
            z = [(a+1,b,nd),(a,b+1,nd)][d%2==0 if rot else d%2]
            na,nb,ndir = z
            if na<=A and nb<=A and (na,nb,ndir) not in U[ny][nx]:
                U[ny][nx].add((na,nb,ndir))
                que.put((nx,ny,na,nb,ndir))
        if rot==0:
            if (a,b,d) not in U[ny][nx] and 0<=nx<M and 0<=ny<N and MP[ny][nx]==0:
                U[ny][nx].add((a,b,d))
                que.put((nx,ny,a,b,d))

if U[gy][gx]: print(min(map(lambda x:x[0]+x[1],U[gy][gx])))
else: print(-1)