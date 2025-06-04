from itertools import product
from collections import Counter

# 各面の回転パターンを生成する関数
def rotations(box):
    box = tuple(box)
    patterns = set()
    # 回転操作
    rotate_x = lambda b: (b[0], b[3], b[1], b[4], b[2], b[5])
    rotate_y = lambda b: (b[3], b[1], b[0], b[5], b[4], b[2])
    rotate_z = lambda b: (b[1], b[5], b[2], b[3], b[0], b[4])
    b = box
    for _ in range(4):
        for _ in range(4):
            patterns.add(b)
            b = rotate_x(b)
        b = rotate_y(b)
    b = rotate_z(box)
    for _ in range(2):
        for _ in range(4):
            patterns.add(b)
            b = rotate_x(b)
        b = rotate_x(b)
        b = (b[5], b[4], b[2], b[3], b[1], b[0])
    return patterns

def threecheck(a, b, c):
    vals = {a, b, c}
    return 0 if len(vals) == 1 else 1 if len(vals) == 2 else 2

def fourcheck(lst):
    cnt = Counter(lst)
    mx = max(cnt.values())
    return {4: 0, 3: 1, 2: 2}.get(mx, 3)

def solve():
    if n == 1:
        return 0
    boxrots = [list(rotations(c)) for c in color]
    if n == 2:
        best = min(sum(a != b for a, b in zip(r1, r2))
                   for r1 in boxrots[0]
                   for r2 in boxrots[1])
    elif n == 3:
        best = min(sum(threecheck(a, b, c) for a, b, c in zip(r1, r2, color[2]))
                   for r1 in boxrots[0]
                   for r2 in boxrots[1])
    else:  # n==4
        best = min(
            sum(fourcheck([a, b, c, d]) for a, b, c, d in zip(r1, r2, r3, color[3]))
            for r1 in boxrots[0]
            for r2 in boxrots[1]
            for r3 in boxrots[2]
        )
    return best

while True:
    n = int(input())
    if n == 0:
        break
    color = [input().split() for _ in range(n)]
    # 色を数値に符号化
    all_colors = {col: idx for idx, col in enumerate({c for box in color for c in box})}
    color = [[all_colors[c] for c in box] for box in color]
    print(solve())