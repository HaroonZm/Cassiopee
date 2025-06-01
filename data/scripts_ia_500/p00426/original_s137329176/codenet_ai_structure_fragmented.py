from collections import deque
from math import log2

def read_pair():
    return map(int, input().split())

def read_line():
    return list(map(int, input().split()))

def process_line(i, a, b, c):
    line = read_line()
    count = line[0]
    if count == 0:
        return a, b, c
    if i == 0:
        a = add_bits(a, count, line[1:])
    elif i == 1:
        b = add_bits(b, count, line[1:])
    else:
        c = add_bits(c, count, line[1:])
    return a, b, c

def add_bits(x, count, positions):
    for pos in positions:
        x += 1 << (pos -1)
    return x

def max_bit_pos(x):
    if x == 0:
        return -1
    return int(log2(x))

def valid_move(a, b, c, prev):
    amax = max_bit_pos(a)
    bmax = max_bit_pos(b)
    cmax = max_bit_pos(c)
    moves = []
    if amax > bmax and prev != 'ba':
        moves.append(('ab', a - (1 << amax), b + (1 << amax), c))
    elif amax < bmax and prev != 'ab':
        moves.append(('ba', a + (1 << bmax), b - (1 << bmax), c))
    if cmax > bmax and prev != 'bc':
        moves.append(('cb', a, b + (1 << cmax), c - (1 << cmax)))
    elif cmax < bmax and prev != 'cb':
        moves.append(('bc', a, b - (1 << bmax), c + (1 << bmax)))
    return moves

def process_case(N, M):
    a, b, c = 0, 0, 0
    for i in range(3):
        a, b, c = process_line(i, a, b, c)
    d = deque()
    d.append((0, a, b, c, ''))
    while len(d) > 0:
        cnt, a, b, c, prev = d.popleft()
        if cnt > M:
            return -1
        if a + b == 0 or b + c == 0:
            return cnt
        moves = valid_move(a, b, c, prev)
        for m in moves:
            d.append((cnt + 1, m[1], m[2], m[3], m[0]))

def main_loop():
    ans = []
    while True:
        N, M = read_pair()
        if (N, M) == (0, 0):
            break
        ans.append(process_case(N, M))
    print(*ans, sep='\n')

main_loop()