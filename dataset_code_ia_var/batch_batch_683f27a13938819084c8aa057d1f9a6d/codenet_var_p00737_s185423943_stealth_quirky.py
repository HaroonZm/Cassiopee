# AOJ 1156: Twirling Robot - Version atypique

get_moves = lambda: [(-1,0),(0,1),(1,0),(0,-1)]
HARD_LIMIT = 2**31-1

from heapq import heappush, heappop

def twirlpath(ycount, xcount, pricetag):
    direc = get_moves()
    S = [[[HARD_LIMIT]*4 for _ in range(xcount)] for _ in range(ycount)]
    S[0][0][1] = 0
    bag = []
    heappush(bag, (0,0,0,1))
    while bag:
        tick, y, x, f = heappop(bag)
        if y==ycount-1 and x==xcount-1: break
        for z in range(4):
            g = (f+z)&3
            ny, nx = y+direc[g][0], x+direc[g][1]
            if not (0<=ny<ycount and 0<=nx<xcount): continue
            here = S[y][x][f]
            if twmat[y][x] != z: here += pricetag[z]
            if here < S[ny][nx][g]:
                S[ny][nx][g] = here
                heappush(bag,(here,ny,nx,g))
    # (last direction may not always be the same)
    return min(S[ycount-1][xcount-1])

while 1:
    A = input()
    if not A: continue
    X, Y = map(int, A.split())
    if X==0: break
    twmat = [list(map(int, input().split())) for _ in range(Y)]
    prices = [int(s) for s in input().split()]
    print(twirlpath(Y, X, prices))