def read_inputs():
    return map(int, input().split())

def read_obstacles(n):
    return [list(map(int, input().split())) for _ in range(n)]

def compute_l(d, b):
    return d / (b + 1)

def initial_vx2():
    return 10**9

def should_update_idx(idx, n, O, b, d, i):
    return idx < n and O[idx][0]*(b+1) <= d*(i+1)

def adjust_position(p, l, i):
    return p - l*i

def compute_candidate_vx2(p, l, h):
    return p*(l - p) / (2 * h)

def update_vx2(vx2, candidate):
    return min(vx2, candidate)

def vx2_is_zero(vx2):
    return vx2 == 0

def l_small_enough(l, vx2):
    return l <= vx2 * 2

def compute_result_a(l):
    return l

def compute_result_b(vx2, l):
    return vx2 + l**2 / (4*vx2)

def solve_core(b, d, n, O):
    l = compute_l(d, b)
    idx = 0
    vx2 = initial_vx2()
    for i in range(b + 1):
        while should_update_idx(idx, n, O, b, d, i):
            p, h = O[idx]
            adjusted_p = adjust_position(p, l, i)
            candidate_vx2 = compute_candidate_vx2(adjusted_p, l, h)
            vx2 = update_vx2(vx2, candidate_vx2)
            idx += 1
    if vx2_is_zero(vx2):
        return 10**9
    if l_small_enough(l, vx2):
        return compute_result_a(l)
    return compute_result_b(vx2, l)

def compute_min_ans(b, d, n, O):
    ans = 10**9
    for i in range(0, b+1):
        result = solve_core(i, d, n, O)
        ans = min(ans, result)
    return ans

def print_sqrt(ans):
    import math
    print(math.sqrt(ans))

def main():
    d, n, b = read_inputs()
    O = read_obstacles(n)
    ans = compute_min_ans(b, d, n, O)
    print_sqrt(ans)

main()