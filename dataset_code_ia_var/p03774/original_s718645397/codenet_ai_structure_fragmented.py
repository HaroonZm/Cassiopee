def read_two_ints():
    return [int(i) for i in input().split()]

def read_point():
    x, y = read_two_ints()
    return [x, y]

def read_points(count):
    points = []
    for _ in range(count):
        points.append(read_point())
    return points

def calculate_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_min_distance_point(point, candidates):
    min_dist = float('inf')
    min_index = 0
    for idx in range(len(candidates)):
        current_dist = calculate_distance(point, candidates[idx])
        if current_dist < min_dist:
            min_dist = current_dist
            min_index = idx + 1
    return min_index

def process_points(points_a, points_b):
    for p in points_a:
        result = find_min_distance_point(p, points_b)
        print(result)

def main():
    n, m = read_two_ints()
    ab = read_points(n)
    cd = read_points(m)
    process_points(ab, cd)

main()