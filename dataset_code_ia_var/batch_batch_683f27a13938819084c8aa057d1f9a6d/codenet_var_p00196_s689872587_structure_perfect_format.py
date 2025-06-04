import sys
import operator

f = sys.stdin

while True:
    n = int(f.readline())
    if n == 0:
        break
    teams = [f.readline().split() for i in range(n)]
    teams = [
        (t[0], -t.count('0'), t.count('1'), i)
        for i, t in enumerate(teams)
    ]
    teams.sort(key=operator.itemgetter(1, 2, 3))
    print('\n'.join([t[0] for t in teams]))