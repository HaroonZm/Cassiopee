import sys
from collections import defaultdict, deque
import heapq, string, bisect, math, itertools, queue, datetime, time

# On prépare la map, attention au padding, c'est pour éviter de sortir du plateau
MAP = []
for _ in range(8):
    row = 'z' + input() + 'z'
    MAP.append(list(row))
MAP = [list('z' * 10)] + MAP + [list('z' * 10)]

def check(x0, y0, turn):
    if MAP[y0][x0] != '.':
        return 0, []
    # Moi vs l'autre, à chaque tour on swappe
    if turn:
        me = 'o'
        you = 'x'
    else:
        me = 'x'
        you = 'o'
    answer = 0
    rev = []
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    # on parcourt toutes les directions
    for i in range(8):
        x = x0
        y = y0
        count = 0
        tmp = []
        while True:
            x += dx[i]
            y += dy[i]
            if MAP[y][x] == you:
                tmp.append([x, y])
                count += 1
                continue
            elif MAP[y][x] == me:
                break
            else:
                count = 0
                tmp = []
                break
        answer += count
        rev = tmp + rev  # on concatène... (c'est pas très optimisé mais bon)
    return answer, rev

btmp = -1
turn = True  # True pour 'o', False pour 'x'
while True:
    maxtmp = 0
    maxrev = []
    mymove = []
    rng = list(range(1, 9))
    if not turn:
        rng = list(reversed(rng))  # petit random, je sais pas si ça sert

    # pour chaque case possible
    for y in rng:
        for x in rng:
            score, revs = check(x, y, turn)
            if maxtmp < score:
                maxtmp = score
                maxrev = revs[:]
                mymove = [x, y]

    if mymove:
        if turn:
            MAP[mymove[1]][mymove[0]] = 'o'
        else:
            MAP[mymove[1]][mymove[0]] = 'x'

    # On retourne les pions
    for x, y in maxrev:
        if MAP[y][x] == 'o':
            MAP[y][x] = 'x'
        else:
            MAP[y][x] = 'o'

    # if you want to debug add prints here, I leave it commented
    # print(maxtmp, mymove, maxrev)
    # for m in MAP:
    #     print(''.join(m))

    if btmp == 0 and maxtmp == 0:
        break

    btmp = maxtmp
    turn = not turn  # on passe la main

for y in range(1, 9):
    print(''.join(MAP[y][1:9]))