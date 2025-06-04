from sys import stdin
from operator import itemgetter

DIRECTIONS = {'U': (0, 1, 0), 'D': (0, -1, 1), 'R': (1, 0, 2), 'L': (-1, 0, 3)}

def readints():
    return map(str, stdin.readline().split())

N = int(stdin.readline())
planes = []

for i in range(N):
    x, y, p = readints()
    x, y = int(x), int(y)
    dx, dy, p2 = DIRECTIONS[p]
    planes.append((x, y, x + y, x - y, p2))

def min_collision_time(planes):
    time = float('inf')
    # vertical collisions (same x)
    for sorted_planes in [sorted(planes, key=itemgetter(0,1))]:
        for prev, curr in zip(sorted_planes, sorted_planes[1:]):
            if curr[0] == prev[0]:
                # D(U=0 above D=1) or U below D above
                if curr[1] > prev[1]:
                    if curr[4] == 1 and prev[4] == 0:
                        t = (curr[1] - prev[1]) * 5
                        if t.is_integer():
                            time = min(time, t)
                else:
                    if curr[4] == 0 and prev[4] == 1:
                        t = (prev[1] - curr[1]) * 5
                        if t.is_integer():
                            time = min(time, t)
    # horizontal collisions (same y)
    for sorted_planes in [sorted(planes, key=itemgetter(1,0))]:
        for prev, curr in zip(sorted_planes, sorted_planes[1:]):
            if curr[1] == prev[1]:
                if curr[0] > prev[0]:
                    if curr[4] == 3 and prev[4] == 2:
                        t = (curr[0] - prev[0]) * 5
                        if t.is_integer():
                            time = min(time, t)
                else:
                    if curr[4] == 2 and prev[4] == 3:
                        t = (prev[0] - curr[0]) * 5
                        if t.is_integer():
                            time = min(time, t)
    # diagonal (x+y)
    for sorted_planes in [sorted(planes, key=itemgetter(2))]:
        for prev, curr in zip(sorted_planes, sorted_planes[1:]):
            if curr[2] == prev[2]:
                # They must head towards each other
                t = abs(curr[0] - prev[0]) * 10
                # L is two possible endpoints at collision moment
                L = {(max(curr[0], prev[0]), max(curr[1], prev[1])),
                     (min(curr[0], prev[0]), min(curr[1], prev[1]))}
                def move(x, y, d, t):
                    if d == 0: return x, y + t // 10
                    if d == 1: return x, y - t // 10
                    if d == 2: return x + t // 10, y
                    if d == 3: return x - t // 10, y
                cpos = move(*curr[:2], curr[4], t)
                ppos = move(*prev[:2], prev[4], t)
                if cpos in L and ppos in L and cpos == ppos:
                    time = min(time, t)
    # anti-diagonal (x-y)
    for sorted_planes in [sorted(planes, key=itemgetter(3))]:
        for prev, curr in zip(sorted_planes, sorted_planes[1:]):
            if curr[3] == prev[3]:
                t = abs(curr[0] - prev[0]) * 10
                L = {(max(curr[0], prev[0]), min(curr[1], prev[1])),
                     (min(curr[0], prev[0]), max(curr[1], prev[1]))}
                def move(x, y, d, t):
                    if d == 0: return x, y + t // 10
                    if d == 1: return x, y - t // 10
                    if d == 2: return x + t // 10, y
                    if d == 3: return x - t // 10, y
                cpos = move(*curr[:2], curr[4], t)
                ppos = move(*prev[:2], prev[4], t)
                if cpos in L and ppos in L and cpos == ppos:
                    time = min(time, t)
    return int(time) if time != float('inf') else "SAFE"

print(min_collision_time(planes))