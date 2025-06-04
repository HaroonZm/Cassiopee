from sys import stdin
from functools import partial

def parse_pos(s): return divmod(ord(s) - 65, 3)

mv = ((-1,0),(0,1),(1,0),(0,-1))
read = iter(stdin.read().split()).__next__

while True:
    n = int(read())
    if not n: break
    s, t, b = map(read, range(3))
    s_r, s_c = parse_pos(s)
    t_r, t_c = parse_pos(t)
    b_pos = ord(b) - 65

    # Use a rolling two-layer DP for space optimization
    from numpy import zeros
    f = zeros((2, 3, 3), dtype=float)
    f[0, s_r, s_c] = 1.0

    for j in range(1, n+1):
        f1 = f[(j-1)&1]
        f2 = f[j&1]
        f2.fill(0)
        for r in range(3):
            for c in range(3):
                prob = f1[r, c] / 4
                if prob == 0: continue
                for dr, dc in mv:
                    nr, nc = r + dr, c + dc
                    idx = 3 * nr + nc
                    if 0 <= nr < 3 and 0 <= nc < 3 and idx != b_pos:
                        f2[nr, nc] += prob
                    else:
                        f2[r, c] += prob
    print(f[n&1, t_r, t_c])