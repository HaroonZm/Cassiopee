from sys import stdin
from functools import partial

BIG_NUM = 2_000_000_000
HUGE_NUM = 99_999_999_999_999_999
MOD = 1_000_000_007
EPS = 1e-9

def solve_line(need, budget, aizu, normal, limit):
    left, right = 1, limit
    num_aizu = num_normal = 0
    while left <= right:
        mid = (left + right) >> 1
        rest = budget - mid * aizu
        tmp_normal = rest // normal
        if rest >= 0 and mid + tmp_normal >= need:
            num_aizu, num_normal = mid, tmp_normal
            left = mid + 1
        else:
            right = mid - 1
    return (num_aizu, num_normal) if num_aizu else None

for input_str in iter(partial(input, ''), ''):
    if input_str.strip() == "0":
        break
    try:
        need, budget, aizu, normal, limit = map(int, input_str.split())
    except ValueError:
        continue
    result = solve_line(need, budget, aizu, normal, limit)
    if result is None:
        print("NA")
    else:
        print(f"{result[0]} {result[1]}")