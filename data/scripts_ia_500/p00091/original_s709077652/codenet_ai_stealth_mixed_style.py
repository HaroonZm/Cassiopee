B,M,S = 13,9,5
directions_x = [ 0, 0, 1, 0,-1, 1, 1,-1,-1, 0, 2, 0,-2]
directions_y = [ 0,-1, 0, 1, 0,-1, 1, 1,-1, 2, 0,-2, 0]

def is_within_bounds(x, y):
    if x < 0 or x >= 10:
        return False
    if y < 0 or y >= 10:
        return False
    return True

def apply_ink(cloth, x, y, ink, apply_subtract):
    for idx in range(ink):
        dx = directions_x[idx]
        dy = directions_y[idx]
        if apply_subtract:
            cloth[y+dy][x+dx] -= 1
        else:
            cloth[y+dy][x+dx] += 1

def can_apply_ink(cloth, x, y, ink):
    for idx in range(ink):
        nx = x + directions_x[idx]
        ny = y + directions_y[idx]
        if not is_within_bounds(nx, ny) or cloth[ny][nx] <= 0:
            return False
    return True

def recursive_search(cloth, inks, start):
    if not inks:
        return []
    pos = start
    while pos < 100 and cloth[pos // 10][pos % 10] != 0:
        pos += 1
    if pos >= 100:
        return False
    for ink in set(inks):
        for i in range(ink):
            cx = pos % 10 + directions_x[i]
            cy = pos // 10 + directions_y[i]
            if is_within_bounds(cx, cy) and cloth[cy][cx] > 0:
                if can_apply_ink(cloth, cx, cy, ink):
                    apply_ink(cloth, cx, cy, ink, True)
                    inks.remove(ink)
                    res = recursive_search(cloth, inks, pos)
                    if res is not False:
                        res.append([cx, cy, ink])
                        return res
                    inks.append(ink)
                    apply_ink(cloth, cx, cy, ink, False)
    return False

from sys import stdin
import itertools

n = int(stdin.readline())
cloth = [list(map(int, stdin.readline().split())) for _ in range(10)]

total_ink = sum(sum(row) for row in cloth)

possible_inks = [list(comb) for comb in itertools.combinations_with_replacement([0,B,M,S], n) if sum(comb) == total_ink]

result = False
for current_inks in possible_inks:
    inks_copy = current_inks[:]
    result = recursive_search(cloth, inks_copy, 0)
    if result is not False:
        break

mapping = {B:3, M:2, S:1}
if result:
    for x, y, ink_val in reversed(result):
        print(x, y, mapping[ink_val])