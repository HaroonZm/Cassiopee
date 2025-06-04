import sys

N = int(sys.stdin.readline())
P = [tuple((int(v), int(w), t, int(d), s) if i != 2 and i != 4 else (t if i == 2 else s)
           for i, (v, w, t, d, s) in enumerate([sys.stdin.readline().split() for _ in range(N)]) )]
P = [tuple(int(x) if i in {0,1,3} else x for i, x in enumerate(row)) for row in [sys.stdin.readline().split() for _ in range(N)]]
P.sort()

sys.stdout.writelines(f"{v} {w} {t} {d} {s}\n" for v, w, t, d, s in P)