from sys import stdin
from math import hypot
from itertools import pairwise

N = int(stdin.readline())
data = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

team, player = data[0][2], data[0][1]
stats = {0: {'max_dist': 0, 'min_time': float('inf')}, 1: {'max_dist': 0, 'min_time': float('inf')}}

for (prev, curr) in pairwise(data):
    curr_team, curr_player = curr[2], curr[1]
    if curr_team == team and curr_player != player:
        dist = hypot(curr[3] - prev[3], curr[4] - prev[4])
        time_diff = (curr[0] - prev[0]) / 60
        s = stats[team]
        if dist > s['max_dist'] or (dist == s['max_dist'] and time_diff < s['min_time']):
            s['max_dist'], s['min_time'] = dist, time_diff
    player, team = curr_player, curr_team

for t in (0, 1):
    if stats[t]['max_dist'] == 0:
        print(-1, -1)
    else:
        print(stats[t]['max_dist'], stats[t]['min_time'])