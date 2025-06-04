from sys import stdin
from collections import deque
from math import log2

def parse_bitset():
    n, *vals = map(int, stdin.readline().split())
    return sum(1 << (v - 1) for v in vals) if n else 0

results = []
while True:
    N, M = map(int, stdin.readline().split())
    if not (N | M):
        break
    a, b, c = (parse_bitset() for _ in range(3))

    visited = set()
    queue = deque([(0, a, b, c, None)])
    found = False

    while queue:
        cnt, a, b, c, prev = queue.popleft()
        state = (a, b, c, prev)
        if state in visited:
            continue
        visited.add(state)

        if cnt > M:
            results.append(-1)
            break
        if not (a | b) or not (b | c):
            results.append(cnt)
            found = True
            break

        slots = {'a': a, 'b': b, 'c': c}
        slotmax = {k: (int(log2(v)) if v else -1) for k, v in slots.items()}

        moves = []
        if slotmax['a'] > slotmax['b'] and prev != 'ba':
            moves.append(('ab', a - (1 << slotmax['a']), b + (1 << slotmax['a']), c))
        elif slotmax['a'] < slotmax['b'] and prev != 'ab':
            moves.append(('ba', a + (1 << slotmax['b']), b - (1 << slotmax['b']), c))
        if slotmax['c'] > slotmax['b'] and prev != 'bc':
            moves.append(('cb', a, b + (1 << slotmax['c']), c - (1 << slotmax['c'])))
        elif slotmax['c'] < slotmax['b'] and prev != 'cb':
            moves.append(('bc', a, b - (1 << slotmax['b']), c + (1 << slotmax['b'])))
        for m, na, nb, nc in moves:
            queue.append((cnt + 1, na, nb, nc, m))

print('\n'.join(map(str, results)))