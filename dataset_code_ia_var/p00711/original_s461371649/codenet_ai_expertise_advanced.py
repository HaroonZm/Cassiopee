from sys import stdin

from collections import deque

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def explore(start, lb, ub, field):
    h, w = len(field), len(field[0])
    stack = [start]
    count = 0
    while stack:
        x, y = stack.pop()
        if not (lb[0] <= x < ub[0] and lb[1] <= y < ub[1]) or field[y][x] == "#":
            continue
        field[y][x] = "#"
        count += 1
        stack.extend(
            (nx, ny)
            for dx, dy in DIRECTIONS
            if 0 <= (nx := x + dx) < w and 0 <= (ny := y + dy) < h and field[ny][nx] != "#"
        )
    return count

def main():
    input_iter = iter(stdin.readline, '')
    while True:
        try:
            W_H = next(input_iter).split()
            W, H = map(int, W_H)
            if W == H == 0:
                break
            floor = [list(next(input_iter).rstrip()) for _ in range(H)]
            for y, row in enumerate(floor):
                if "@" in row:
                    start = (row.index("@"), y)
                    break
            print(explore(start, (0, 0), (W, H), floor))
        except StopIteration:
            break

if __name__ == "__main__":
    main()