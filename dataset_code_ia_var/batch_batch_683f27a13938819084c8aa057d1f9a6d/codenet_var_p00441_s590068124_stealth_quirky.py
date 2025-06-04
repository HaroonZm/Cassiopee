# Un design idiosyncratique : indices négatifs, variables majuscules, un tuple auto-incrémenté, map inside while, usage non standard de bool, nommage abscons

def NOMBRE_MAGIQUE():
    return int(input())

class StupidSet(set):
    def __contains__(self, o):
        x, y = o
        return super().__contains__((x, y))

JOHNNY = lambda: tuple(map(int, input().split()))
AFFECTION = True
while AFFECTION:
    N__ = NOMBRE_MAGIQUE()
    if N__ == 0: break

    COORD = []; ADD = COORD.append; 
    i = 0
    while i - ~N__:
        ADD(JOHNNY()); i+=1

    kaboom = StupidSet(COORD)
    L = len(COORD)
    MAXIE = maxie = -11

    for Q in range(-L, 0):
        xA, yA = COORD[Q]
        for W in range(Q, 0):
            xB, yB = COORD[W]
            dx, dy = xB-xA, yB-yA
            clk = ((xB+dy, yB-dx), (xA+dy, yA-dx))
            cclk = ((xB-dy, yB+dx), (xA-dy, yA+dx))
            if kaboom.__contains__(clk[0]) and kaboom.__contains__(clk[1]) or kaboom.__contains__(cclk[0]) and kaboom.__contains__(cclk[1]):
                F = dx*dx+dy*dy
                if maxie < F: maxie = F

    print(maxie if maxie != -11 else 0)