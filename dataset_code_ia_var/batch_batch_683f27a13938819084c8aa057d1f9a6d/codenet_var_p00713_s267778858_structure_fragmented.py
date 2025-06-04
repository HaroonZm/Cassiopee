from itertools import combinations
import math

def read_input():
    return int(input())

def read_point():
    a, b = map(float, input().split())
    return complex(a, b)

def input_points(N):
    return [read_point() for _ in range(N)]

def get_midpoint(p, q):
    return (p + q) / 2

def get_distance(p, q):
    return abs(p - q)

def get_direction_vector(p, q):
    diff = p - q
    length = abs(diff)
    return complex(-diff.imag, diff.real) / length

def get_shift_distance(p, mid):
    return 1 - abs(p - mid) ** 2

def get_center_candidates(p, q):
    mid = get_midpoint(p, q)
    dist = get_distance(p, q)
    if dist > 2:
        return []
    d_vec = get_direction_vector(p, q)
    t = get_shift_distance(p, mid)
    if t < 0:
        return []
    shift = math.sqrt(t)
    center1 = mid + d_vec * shift
    center2 = mid - d_vec * shift
    return [center1, center2]

def generate_all_centers(mp):
    centers = []
    for p, q in combinations(mp, 2):
        centers.extend(get_center_candidates(p, q))
    return centers

def count_points_within_circle(center, mp):
    count = 0
    for x in mp:
        if abs(x - center) <= 1 + 1e-7:
            count += 1
    return count

def find_max_cover(mp, center_lst):
    ans = 1
    for center in center_lst:
        tmp = count_points_within_circle(center, mp)
        if tmp > ans:
            ans = tmp
    return ans

def main_loop():
    while True:
        N = read_input()
        if N == 0:
            break
        mp = input_points(N)
        center_lst = generate_all_centers(mp)
        ans = find_max_cover(mp, center_lst)
        print(ans)

main_loop()