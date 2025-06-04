import math

def read_input():
    return map(int, input().split())

def read_obstacles(n):
    return [read_single_obstacle() for _ in range(n)]

def read_single_obstacle():
    return list(map(int, input().split()))

def get_l(d, b):
    return d / (b + 1)

def get_p_h(index):
    return O[index][0], O[index][1]

def compute_threshold(d, b, i):
    return d * (i + 1)

def position_in_segment(p, l, i):
    return p - l * i

def update_vx2(vx2, p, l, h):
    new_vx2 = min(vx2, p * (l - p) / (2 * h))
    return new_vx2

def vx2_zero_case():
    return 10 ** 9

def compute_l_case(l, vx2):
    if l <= 2 * vx2:
        return l
    return vx2 + l ** 2 / (4 * vx2)

def process_segment(i, b, d, n, l, vx2, idx):
    while idx < n and O[idx][0] * (b + 1) <= compute_threshold(d, b, i):
        p, h = get_p_h(idx)
        p = position_in_segment(p, l, i)
        vx2 = update_vx2(vx2, p, l, h)
        idx += 1
    return vx2, idx

def solve_single(b, d, n, O):
    l = get_l(d, b)
    idx = 0
    vx2 = 10 ** 9
    for i in range(b + 1):
        vx2, idx = process_segment(i, b, d, n, l, vx2, idx)
    if vx2 == 0:
        return vx2_zero_case()
    return compute_l_case(l, vx2)

def generate_b_list(b):
    return range(b + 1)

def min_solve(d, n, b, O):
    values = []
    for b_val in generate_b_list(b):
        values.append(solve_single(b_val, d, n, O))
    return min(values)

def print_result(result):
    print(math.sqrt(result))

def main():
    global d, n, b, O
    d, n, b = read_input()
    O = read_obstacles(n)
    result = min_solve(d, n, b, O)
    print_result(result)

main()