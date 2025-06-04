import math

n = int(input())
r, theta = map(float, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def angle_between(v1, v2):
    # v1 and v2 are vectors (dx, dy)
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    len1 = math.sqrt(v1[0]**2 + v1[1]**2)
    len2 = math.sqrt(v2[0]**2 + v2[1]**2)
    if len1 == 0 or len2 == 0:
        return 0.0
    cos_angle = dot/(len1*len2)
    cos_angle = max(-1, min(1, cos_angle))
    return math.degrees(math.acos(cos_angle))

max_carrots = 0

# Since n is small, and r small, we try all paths using DFS.

def dfs(current_city, length_used, prev_dir, carrots):
    global max_carrots
    if carrots > max_carrots:
        max_carrots = carrots

    for next_city in range(n):
        if next_city == current_city:
            continue
        d = dist(cities[current_city], cities[next_city])
        if length_used + d > r:
            continue
        # direction vector
        cur_dir = (cities[next_city][0]-cities[current_city][0], cities[next_city][1]-cities[current_city][1])
        if prev_dir is not None:
            a = angle_between(prev_dir, cur_dir)
            if a > theta + 1e-8:
                continue
        dfs(next_city, length_used + d, cur_dir, carrots + 1)

dfs(0, 0, None, 0)
print(max_carrots)