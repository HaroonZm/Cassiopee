from math import factorial as fct
from Queue import PriorityQueue

FACTORIAL=[fct(i) for i in xrange(13)]
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3
MOVE = [[0] * 4 for _ in xrange(13)]
MOVE[0]  = [-1,-1,-1, 2]
MOVE[1]  = [-1,-1, 2, 5]
MOVE[2]  = [ 1, 0, 3, 6]
MOVE[3]  = [ 2,-1,-1, 7]
MOVE[4]  = [-1,-1, 5,-1]
MOVE[5]  = [ 4, 1, 6, 9]
MOVE[6]  = [ 5, 2, 7,10]
MOVE[7]  = [ 6, 3, 8,11]
MOVE[8]  = [ 7,-1,-1,-1]
MOVE[9]  = [-1, 5,10,-1]
MOVE[10] = [ 9, 6,11,12]
MOVE[11] = [10, 7,-1,-1]
MOVE[12] = [-1,10,-1,-1]

def hash(cell):
    work = list(cell)
    h = 0
    for i in xrange(12):
        h += work[i] * FACTORIAL[12 - i]
        for j in xrange(i+1, 13):
            if work[j] > work[i]:
                work[j] -= 1
    return h

def dehash(key):
    cell = []
    for i in xrange(13):
        div, key = divmod(key, FACTORIAL[12 - i])
        cell.append(div)
    for i in xrange(11, -1, -1):
        for j in xrange(i+1, 13):
            if cell[i] <= cell[j]:
                cell[j] += 1
    return cell

def evaluate(cell):
    points = {
        0: [0, 2],
        1: [1, 1], 2: [1, 2], 3: [1, 3],
        4: [2, 0], 5: [2, 1], 6: [2, 2], 7: [2, 3], 8: [2, 4],
        9: [3, 1], 10: [3, 2], 11: [3, 3],
        12: [4, 2]
    }
    s = 0
    for i in xrange(13):
        if cell[i] not in (0, 12):
            dx = abs(points[cell[i]][0] - points[i][0])
            dy = abs(points[cell[i]][1] - points[i][1])
            s += dx + dy
    return s

answers = {hash(range(13)), hash([12] + range(1,12) + [0])}

while True:
    inp = input()
    if inp == -1:
        break
    p = [inp]
    for _ in xrange(4):
        p.extend(int(x) for x in raw_input().split())
    zero_pos = p.index(0)
    p[zero_pos] = 12

    pq = PriorityQueue()
    start_hash = hash(p)
    start_eval = evaluate(p)
    pq.put((start_eval, start_hash, 0))
    visited = {start_hash: True}
    ans = 0 if start_hash in answers else "NA"

    while not pq.empty():
        eva, curr_hash, steps = pq.get()
        if steps >= 20 or ans != "NA":
            break
        current = dehash(curr_hash)
        for i in xrange(13):
            if current[i] in (0, 12):
                for direction in (LEFT, UP, RIGHT, DOWN):
                    nxt = MOVE[i][direction]
                    if nxt != -1:
                        current[i], current[nxt] = current[nxt], current[i]
                        nhash = hash(current)
                        if nhash not in visited:
                            if nhash in answers:
                                ans = steps + 1
                                current[i], current[nxt] = current[nxt], current[i]
                                break
                            score = evaluate(current) + steps + 1
                            pq.put((score, nhash, steps + 1))
                            visited[nhash] = True
                        current[i], current[nxt] = current[nxt], current[i]
                if ans != "NA":
                    break
    print ans