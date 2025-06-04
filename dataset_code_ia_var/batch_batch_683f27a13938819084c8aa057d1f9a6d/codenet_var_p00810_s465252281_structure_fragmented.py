def read_int():
    return int(input())

def read_star():
    return list(map(float, input().split()))

def read_stars(n):
    return [read_star() for _ in range(n)]

def initial_center():
    return [0.0, 0.0, 0.0]

def initial_move():
    return 0.5

def distance2(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3))

def find_farthest_index(center, stars, n):
    max_dist2 = 0
    farthest_index = 0
    for i in range(n):
        dist2 = distance2(stars[i], center)
        if max_dist2 < dist2:
            max_dist2 = dist2
            farthest_index = i
    return farthest_index, max_dist2

def update_center(center, target, move):
    return [center[i] - (center[i] - target[i]) * move for i in range(3)]

def iterate(center, stars, move, n):
    for j in range(100):
        farthest_index, _ = find_farthest_index(center, stars, n)
        center = update_center(center, stars[farthest_index], move)
    return center

def optimize_center(center, stars, move, n):
    for _ in range(500):
        center = iterate(center, stars, move, n)
        move /= 2
    return center

def compute_max_distance2(center, stars, n):
    _, max_dist2 = find_farthest_index(center, stars, n)
    return max_dist2

def print_result(max_distance2):
    print(round(max_distance2 ** 0.5, 5))

def process_case(n):
    stars = read_stars(n)
    center = initial_center()
    move = initial_move()
    center = optimize_center(center, stars, move, n)
    max_distance2 = compute_max_distance2(center, stars, n)
    print_result(max_distance2)

def main_loop():
    while True:
        n = read_int()
        if not n:
            break
        process_case(n)

main_loop()