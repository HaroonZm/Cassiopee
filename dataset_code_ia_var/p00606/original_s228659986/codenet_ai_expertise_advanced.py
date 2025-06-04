import sys

to = (
    (0, 0, 1, 3), (0, 1, 2, 4), (1, 2, 2, 5),
    (0, 3, 4, 6), (1, 3, 5, 7), (2, 4, 5, 8),
    (3, 6, 6, 7), (4, 6, 7, 8), (5, 7, 8, 8)
)
base = ord('A')

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    s, t, b = sys.stdin.readline().split()
    blank = ord(b) - base
    target = ord(t) - base
    start = ord(s) - base

    dp_prev = [0.0] * 9
    dp_prev[start] = 1.0

    for _ in range(n):
        dp_next = [0.0] * 9
        for x in range(9):
            c = dp_prev[x] * 0.25
            for nex in to[x]:
                if nex == blank:
                    dp_next[x] += c
                else:
                    dp_next[nex] += c
        dp_prev = dp_next

    print(dp_prev[target])