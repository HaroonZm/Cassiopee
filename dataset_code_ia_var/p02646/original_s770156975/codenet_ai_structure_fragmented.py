def read_position_and_velocity():
    return list(map(int, input().split()))

def read_time():
    return int(input())

def get_velocity_difference(v1, v2):
    return v1 - v2

def get_location_difference(a, b):
    return abs(a - b)

def compute_reachable(loc_diff, vel_diff, t):
    return loc_diff - vel_diff * t

def is_reachable(result):
    return result <= 0

def print_result(is_yes):
    if is_yes:
        print('YES')
    else:
        print('NO')

def main():
    a, v = read_position_and_velocity()
    b, w = read_position_and_velocity()
    t = read_time()
    vel_diff = get_velocity_difference(v, w)
    loc_diff = get_location_difference(a, b)
    result = compute_reachable(loc_diff, vel_diff, t)
    reachable = is_reachable(result)
    print_result(reachable)

main()