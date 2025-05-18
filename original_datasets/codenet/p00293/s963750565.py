import sys
import itertools
f = sys.stdin

nhm, mkg = [map(int, f.readline().split()) for _ in range(2)]
n = next(nhm)
m = next(mkg)

goto_iimoriyama = list(zip(*[nhm]*2))
goto_turugajyo = list(zip(*[mkg]*2))

mixed = sorted(list(set(goto_iimoriyama + goto_turugajyo)))

mixed = ['{}:{:02d}'.format(h, m) for h,m in mixed]
print(*mixed)