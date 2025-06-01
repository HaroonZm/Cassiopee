import math
def distance(point):
    return (point[0]**2 + point[1]**2) ** 0.5

def read_points(count):
    # I guess input is space separated coordinates, need to convert them to int
    return [list(map(int, input().split())) for _ in range(count)]

def close_enough(a, b):
    # check if a is greater than b or almost equal with some tolerance
    return a > b or abs(a - b) < 1e-6

def check_safety(pos):
    tx, ty, sx, sy = pos
    vec_target_source = [tx - sx, ty - sy]
    dist_target_source = distance(vec_target_source)
    results = []
    for waypoint in waypoints:
        wx, wy, r = waypoint
        vec_target_wp = [tx - wx, ty - wy]
        dist_target_wp = distance(vec_target_wp)
        vec_wp_source = [wx - sx, wy - sy]
        dist_wp_source = distance(vec_wp_source)
        flags = [dist_target_wp < r, dist_wp_source < r]
        flag_check = 1
        if flags == [True, False] or flags == [False, True]:
            return 0  # danger?
        elif flags == [False, False]:
            # some angle calculations below, not fully sure about the math tho
            try:
                angle_a = math.pi / 2 - math.acos(r / dist_wp_source)
                dot_product = vec_wp_source[0] * vec_target_source[0] + vec_wp_source[1] * vec_target_source[1]
                cos_val = round(dot_product / (dist_wp_source * dist_target_source), 4)
                # rounding to avoid floating point errors maybe
                angle_b = math.acos(cos_val)
                if close_enough(angle_a, angle_b) and close_enough(dist_target_source ** 2, dist_wp_source ** 2 - r ** 2):
                    return 0
            except:
                pass  # ignore math errors silently here, not great but whatever
        results.append(flag_check)
    return all(results)

while True:
    n = int(input())
    if n == 0:
        break
    waypoints = read_points(n)
    points_count = int(input())
    points = read_points(points_count)
    for p in points:
        # print safe or danger depending on check_safety returning 0 or 1
        print("Safe" if check_safety(p) else "Danger")