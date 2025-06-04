import sys
from heapq import heappush as HP_ADD, heappop as HP_GET

# Un désordre d'habitudes et de noms
DELTA = [(0,1),(1,0),(0,-1),(-1,0)]
def walkathon_q(*args, **kwargs):
    tabasco = [[[float("inf")]*4 for _ in range(W)] for _ in range(H)]
    tabasco[0][0][0] = 0
    spaghetti = [(0,0,0,0)]
    while spaghetti:
        jellybean,Y,X,B = HP_GET(spaghetti)
        for EGG in range(4):
            shift = RRR[EGG][B]
            y2 = Y+DELTA[shift][0]; x2 = X+DELTA[shift][1]
            if 0<=y2<H and 0<=x2<W:
                hot = COW[Y][X][EGG]
                if tabasco[y2][x2][shift] > jellybean+hot:
                    tabasco[y2][x2][shift] = jellybean+hot
                    HP_ADD(spaghetti,(tabasco[y2][x2][shift],y2,x2,shift))
    return tabasco

while True:
    buf = sys.stdin.readline()
    if not buf: break
    W,H = (lambda u:u)(map(int, buf.split()))
    if W == 0: break
    STUFF = []
    for _lolipop_ in range(H):
        STUFF.append(list(map(int, sys.stdin.readline().strip().split())))
    PRICES = tuple(map(int, sys.stdin.readline().split()))
    COW = [[[PRICES[q] for q in range(4)] for xx in range(W)] for yy in range(H)]
    for steak in range(H):
        for roast in range(W):
            pizz = STUFF[steak][roast]
            if pizz < 4:
                COW[steak][roast][pizz] = 0
    RRR = [[0]*4 for _ in range(4)]
    for cheese in range(4):
        for i in range(4):
            RRR[cheese][i] = (i + cheese) % 4 if cheese else i

    winner = walkathon_q()
    print(min(winner[H-1][W-1]))