import sys
import math

def lcm(a, b):
    return a // math.gcd(a, b) * b

def all_lcms(arr):
    res = []
    def backtrack(i, curr_lcm):
        if i == len(arr):
            if curr_lcm != 1:
                res.append(curr_lcm)
            return
        # Include arr[i]
        new_lcm = lcm(curr_lcm, arr[i])
        if new_lcm <= n:
            backtrack(i + 1, new_lcm)
        # Exclude arr[i]
        backtrack(i + 1, curr_lcm)
    backtrack(0, 1)
    return res

input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    p = list(map(int, input().split()))
    # Inclusion-exclusion
    from itertools import combinations
    res = 0
    length = len(p)
    for size in range(1, length + 1):
        for comb in combinations(p, size):
            curr_lcm = 1
            for x in comb:
                curr_lcm = lcm(curr_lcm, x)
                if curr_lcm > n:
                    break
            else:
                cnt = n // curr_lcm
                if size % 2 == 1:
                    res += cnt
                else:
                    res -= cnt
    valid_count = n - res
    if valid_count == 0:
        print("0.0000000000")
        continue
    # Sum of all natural numbers from 1 to n
    total_sum = n * (n + 1) // 2
    # Sum of all multiples of each pi with inclusion-exclusion
    sum_excluded = 0
    for size in range(1, length + 1):
        for comb in combinations(p, size):
            curr_lcm = 1
            for x in comb:
                curr_lcm = lcm(curr_lcm, x)
                if curr_lcm > n:
                    break
            else:
                cnt = n // curr_lcm
                s = curr_lcm * cnt * (cnt + 1) // 2
                if size % 2 == 1:
                    sum_excluded += s
                else:
                    sum_excluded -= s
    valid_sum = total_sum - sum_excluded
    expected_value = valid_sum / valid_count
    print(f"{expected_value:.10f}")