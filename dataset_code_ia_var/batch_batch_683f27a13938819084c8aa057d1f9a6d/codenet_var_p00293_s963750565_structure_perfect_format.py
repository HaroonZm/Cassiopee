import sys
import itertools

f = sys.stdin

nhm, mkg = [list(map(int, f.readline().split())) for _ in range(2)]
n = nhm[0]
m = mkg[0]

goto_iimoriyama = list(zip(nhm[1::2], nhm[2::2]))
goto_turugajyo = list(zip(mkg[1::2], mkg[2::2]))

mixed = sorted(set(goto_iimoriyama + goto_turugajyo))
mixed = ['{}:{:02d}'.format(h, mi) for h, mi in mixed]

print(*mixed)