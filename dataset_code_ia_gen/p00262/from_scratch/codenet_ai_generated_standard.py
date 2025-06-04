def is_triangle_number(x):
    from math import sqrt
    n = int((sqrt(8 * x + 1) - 1) / 2)
    return n if n * (n + 1) // 2 == x else 0

def is_target(b):
    n = len(b)
    for i in range(n):
        if b[i] != i + 1:
            return False
    return True

def game(b):
    total = sum(b)
    k = is_triangle_number(total)
    if not k:
        return -1
    max_ops = 10000
    step = 0
    while step <= max_ops:
        if len(b) == k and is_target(b):
            return step
        if step == max_ops:
            return -1
        bottom = b[:]
        bottom_count = bottom[0]
        right_new = bottom_count
        # remove bottom layer (which is bottom[0] blocks)
        # drop rest by one
        rest = [x - bottom_count for x in bottom[1:] if x - bottom_count > 0]
        # append right_new block on the right side
        new_seq = rest + [right_new]
        # shift to left (remove zeros)
        b = [x for x in new_seq if x > 0]
        step += 1
    return -1

import sys
lines = sys.stdin.read().strip().split('\n')
i = 0
while True:
    if i >= len(lines):
        break
    N = int(lines[i])
    if N == 0:
        break
    i += 1
    b = list(map(int, lines[i].split()))
    i += 1
    print(game(b))