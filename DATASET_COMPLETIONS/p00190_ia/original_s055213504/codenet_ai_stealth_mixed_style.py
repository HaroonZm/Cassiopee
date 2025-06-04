from math import factorial as fact
from Queue import PriorityQueue
import sys

FACTORIAL = list(map(fact, range(13)))
LEFT, UP, RIGHT, DOWN = (0, 1, 2, 3)
MOVE = [[0] for _ in xrange(13)]
MOVE[0], MOVE[1], MOVE[2], MOVE[3] = [-1, -1, -1, 2], [-1, -1, 2, 5], [1, 0, 3, 6], [2, -1, -1, 7]
MOVE[4], MOVE[5], MOVE[6], MOVE[7] = [-1, -1, 5, -1], [4, 1, 6, 9], [5, 2, 7, 10], [6, 3, 8, 11]
MOVE[8], MOVE[9], MOVE[10], MOVE[11], MOVE[12] = [7, -1, -1, -1], [-1, 5, 10, -1], [9, 6, 11, 12], [10, 7, -1, -1], [-1, 10, -1, -1]

def hash(cell):
    work = cell[:]
    h = 0
    for i in xrange(12):
        h += work[i] * FACTORIAL[12 - i]
        for j in xrange(i+1,13):
            if work[j] > work[i]: work[j] -= 1
    return h

def dehash(k):
    res = []
    for i in xrange(13):
        f = FACTORIAL[12 - i]
        res.append(k // f)
        k %= f
    for i in range(12, -1, -1):
        for j in range(i+1, 13):
            if res[i] <= res[j]: res[j] += 1
    return res

def evaluate(cell):
    points = [(0,2),
              (1,1),(1,2),(1,3),
              (2,0),(2,1),(2,2),(2,3),(2,4),
              (3,1),(3,2),(3,3),
              (4,2)]
    val = 0
    for i in xrange(13):
        c = cell[i]
        if c != 0 and c != 12:
            val += abs(points[c][0]-points[i][0]) + abs(points[c][1]-points[i][1])
    return val

ANS_HASH = set([hash([0,1,2,3,4,5,6,7,8,9,10,11,12]),
                hash([12,1,2,3,4,5,6,7,8,9,10,11,0])])

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        p = [int(line.strip())]
        if p == [-1]:
            break
        for _ in xrange(4):
            p.extend(map(int, sys.stdin.readline().split()))
        idx0 = p.index(0)
        p[idx0] = 12

        pq = PriorityQueue()
        start_hash = hash(p)
        start_eval = evaluate(p)
        pq.put((start_eval, start_hash, 0))
        visited = {start_hash: True}
        ans = 0 if start_hash in ANS_HASH else "NA"

        while not pq.empty():
            eva, cur_hash, step = pq.get()
            if ans != "NA" or eva > 20:
                break
            cur_cell = dehash(cur_hash)
            for i in xrange(13):
                if cur_cell[i] == 0 or cur_cell[i] == 12:
                    for dir in (LEFT, UP, RIGHT, DOWN):
                        nxt = MOVE[i][dir]
                        if nxt != -1:
                            cur_cell[i], cur_cell[nxt] = cur_cell[nxt], cur_cell[i]
                            hkey = hash(cur_cell)
                            if hkey not in visited:
                                if hkey in ANS_HASH:
                                    ans = step + 1
                                    cur_cell[i], cur_cell[nxt] = cur_cell[nxt], cur_cell[i]
                                    break
                                v = evaluate(cur_cell) + step + 1
                                pq.put((v, hkey, step + 1))
                                visited[hkey] = True
                            cur_cell[i], cur_cell[nxt] = cur_cell[nxt], cur_cell[i]
                    if ans != "NA":
                        break
            if ans != "NA":
                break
        print ans

if __name__ == "__main__":
    main()