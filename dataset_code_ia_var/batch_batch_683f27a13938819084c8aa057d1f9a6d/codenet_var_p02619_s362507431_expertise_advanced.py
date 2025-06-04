from sys import stdin

D = int(stdin.readline())
c = list(map(int, stdin.readline().split()))
s = [list(map(int, stdin.readline().split())) for _ in range(D)]
t = [int(stdin.readline()) - 1 for _ in range(D)]

from operator import itemgetter

v = 0
lastday = [0] * 26
penalty = 0
output = []

for day, contest in enumerate(t, 1):
    v += s[day - 1][contest]
    lastday[contest] = day
    penalty = sum(ci * (day - ld) for ci, ld in zip(c, lastday))
    output.append(str(v - penalty))

print('\n'.join(output))