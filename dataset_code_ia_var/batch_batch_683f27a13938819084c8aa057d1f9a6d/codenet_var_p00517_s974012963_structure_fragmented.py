def read_input():
    return list(map(int, input().split()))

def read_all_points(n):
    return [read_input() for _ in range(n)]

def is_first_point(i):
    return i == 0

def get_point(points, i):
    return points[i]

def get_dx(sx, gx):
    return gx - sx

def get_dy(sy, gy):
    return gy - sy

def dx_dy_nonnegative(dx, dy):
    return dx * dy >= 0

def max_abs(dx, dy):
    return max(abs(dx), abs(dy))

def sum_abs(dx, dy):
    return abs(dx) + abs(dy)

def move_cost(dx, dy):
    if dx_dy_nonnegative(dx, dy):
        return max_abs(dx, dy)
    else:
        return sum_abs(dx, dy)

def update_position(gx, gy):
    return gx, gy

def process_all_moves(points, n):
    ans = 0
    sx, sy = get_point(points, 0)
    for i in range(1, n):
        gx, gy = get_point(points, i)
        dx = get_dx(sx, gx)
        dy = get_dy(sy, gy)
        ans += move_cost(dx, dy)
        sx, sy = update_position(gx, gy)
    return ans

def main():
    W, H, N = read_input()
    points = read_all_points(N)
    result = process_all_moves(points, N)
    print(result)

main()