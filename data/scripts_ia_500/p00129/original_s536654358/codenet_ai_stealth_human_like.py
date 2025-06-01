import math
def dist(point):
    # distance from origin, like hypotenuse
    return (point[0]**2 + point[1]**2)**0.5

def input_points(num):
    # read num points, each line two ints
    return [list(map(int, input().split())) for _ in range(num)]

def compare(a, b):
    # check if a > b or close enough to equal
    return a > b or abs(a - b) < 1e-6

def check_safety(t):
    tx, ty, sx, sy = t
    results = []
    for w in WP:
        wx, wy, r = w
        vec_tw = [tx - wx, ty - wy]
        dist_tw = dist(vec_tw)
        vec_sw = [wx - sx, wy - sy]
        dist_sw = dist(vec_sw)
        vec_ts = [tx - sx, ty - sy]
        dist_ts = dist(vec_ts)
        flags = [dist_tw < r, dist_sw < r]
        if dist_ts == 0:
            # starting and target points coincide
            safe = 1
        elif flags == [1, 1]:
            safe = 1
        elif flags == [1, 0] or flags == [0, 1]:
            safe = 0
        elif flags == [0, 0]:
            # some weird angle checks here, might not be perfect
            try:
                a = math.pi/2 - math.acos(r / dist_sw)
            except:
                # probably division by zero if dist_sw == 0, let's be safe
                safe = 1
                results.append(safe)
                continue
            dot = round((vec_sw[0]*vec_ts[0] + vec_sw[1]*vec_ts[1]) / (dist_sw * dist_ts), 4)
            b = math.acos(dot)
            if compare(a, b) and compare(dist_ts**2, dist_sw**2 - r**2):
                safe = 0
            else:
                safe = 1
        results.append(safe)
    return all(results)

while True:
    n = int(input())
    if n == 0:
        break
    WP = input_points(n)
    p = input_points(int(input()))
    for target in p:
        # print Safe or Danger depending on check_safety
        print("Safe" if check_safety(target) else "Danger")