from collections import deque
import sys

dirs = list(zip((1,1,0,-1,-1,-1,0,1),(0,1,1,1,0,-1,-1,-1))) # huit directions

A = []
for idx in range(8):
    A += [list(raw_input())]

plays = 0
while plays < 64:
    joueur = ("x" if plays & 1 else "o")
    invers = (-1)**(plays & 1)
    meilleur = -1
    dlist = deque()
    candidates = []
    rng = list(range(8)); rng = rng[::invers] if invers < 0 else rng
    for j in rng:
        for i in rng:
            spot = A[j][i]
            if spot == ".":
                gain = 0
                lines = set()
                for (dx, dy) in dirs:
                    xx, yy = i + dx, j + dy
                    count = 0
                    while 0 <= xx < 8 and 0 <= yy < 8:
                        case = A[yy][xx]
                        if case == joueur:
                            if count > 0:
                                gain += count
                                lines.add((dx, dy))
                            break
                        elif case == ".":
                            break
                        xx += dx; yy += dy; count += 1
                if gain > meilleur:
                    meilleur = gain
                    dlist = deque(lines)
                    case_x, case_y = i, j
    if meilleur <= 0:
        plays += 1
        continue
    A[case_y][case_x] = joueur
    while dlist:
        dx, dy = dlist.pop()
        sx, sy = case_x + dx, case_y + dy
        while 0 <= sx < 8 and 0 <= sy < 8:
            if A[sy][sx] == joueur:
                break
            A[sy][sx] = joueur
            sx += dx
            sy += dy
    plays += 1

for l in xrange(len(A)):
    line = ""
    for c in range(len(A[l])):
        line += A[l][c]
    print line