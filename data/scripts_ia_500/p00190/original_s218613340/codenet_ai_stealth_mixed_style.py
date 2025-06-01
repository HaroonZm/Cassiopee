import functools
from math import factorial as f
from queue import PriorityQueue
import sys

FACTORIAL = [f(i) for i in range(13)]

LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3

MOVE = [[-1, -1, -1, 2],
        [-1, -1, 2, 5],
        [1, 0, 3, 6],
        [2, -1, -1, 7],
        [-1, -1, 5, -1],
        [4, 1, 6, 9],
        [5, 2, 7, 10],
        [6, 3, 8, 11],
        [7, -1, -1, -1],
        [-1, 5, 10, -1],
        [9, 6, 11, 12],
        [10, 7, -1, -1],
        [-1, 10, -1, -1]]

def hash_cell(cell):
    work = list(cell)
    h = 0
    for i in range(12):
        h += work[i] * FACTORIAL[12 - i]
        for j in range(i + 1, 13):
            if work[j] > work[i]:
                work[j] -= 1
    return h

def dehash(key):
    cell = []
    for i in range(13):
        div, key = divmod(key, FACTORIAL[12 - i])
        cell.append(div)
    for i in reversed(range(13)):
        for j in range(i + 1, 13):
            if cell[i] <= cell[j]:
                cell[j] += 1
    return cell

def evaluate(cell):
    points = [(0,2),
              (1,1), (1,2), (1,3),
              (2,0), (2,1), (2,2), (2,3), (2,4),
              (3,1), (3,2), (3,3),
              (4,2)]
    total = 0
    for i, val in enumerate(cell):
        if val != 0 and val != 12:
            x1, y1 = points[val]
            x2, y2 = points[i]
            total += abs(x1 - x2) + abs(y1 - y2)
    return total

def main():
    input = sys.stdin.readline
    while True:
        try:
            p = list(map(int, input().split()))
            if p == [-1]:
                break
            for _ in range(3):
                p.extend(map(int, input().split()))
            p[p.index(0)] = 12
            pq = PriorityQueue()
            init_hash = hash_cell(p)
            init_eval = evaluate(p)
            pq.put((init_eval, init_hash, 0))
            visited = {init_hash: True}
            ans = 0 if init_eval == 0 else "NA"
            count = 0

            while not pq.empty():
                count += 1
                cur_eval, cur_hash, cur_step = pq.get()
                cur_cell = dehash(cur_hash)

                if not (cur_eval <= 20 and ans == "NA"):
                    break

                for i, val in enumerate(cur_cell):
                    if val == 0 or val == 12:
                        for direction in (LEFT, UP, RIGHT, DOWN):
                            next_pos = MOVE[i][direction]
                            if next_pos != -1:
                                cur_cell[i], cur_cell[next_pos] = cur_cell[next_pos], cur_cell[i]
                                hashed = hash_cell(cur_cell)
                                if hashed not in visited:
                                    eva = evaluate(cur_cell)
                                    if eva == 0:
                                        ans = cur_step + 1
                                        break
                                    pq.put((eva + cur_step + 1, hashed, cur_step + 1))
                                    visited[hashed] = True
                                cur_cell[i], cur_cell[next_pos] = cur_cell[next_pos], cur_cell[i]
                        if ans != "NA":
                            break
                if ans != "NA":
                    break
            print(ans)
        except Exception:
            break

if __name__ == "__main__":
    main()