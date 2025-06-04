from collections import Counter
from itertools import permutations
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def parse_int():
    return int(readline())

def parse_strings(N):
    return [readline().strip() for _ in range(N)]

def get_lengths(a, b):
    return len(a), len(b)

def init_dp_table(LA, LB):
    return [[10 ** 18] * (LB + 1) for _ in range(LA + 1)]

def set_dp_start(dp):
    dp[0][0] = 0

def update_dp_same_char(dp, i, j, v):
    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], v)

def update_dp_diff_char(dp, i, j, v):
    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], v + 1)

def update_dp_delete_from_a(dp, i, j, v):
    dp[i + 1][j] = min(dp[i + 1][j], v + 1)

def update_dp_delete_from_b(dp, i, j, v):
    dp[i][j + 1] = min(dp[i][j + 1], v + 1)

def update_dp_delete_rest_of_a(dp, i, LB):
    dp[i + 1][LB] = min(dp[i + 1][LB], dp[i][LB] + 1)

def update_dp_delete_rest_of_b(dp, LA, j):
    dp[LA][j + 1] = min(dp[LA][j + 1], dp[LA][j] + 1)

def levenshtein_distance(a, b):
    LA, LB = get_lengths(a, b)
    dp = init_dp_table(LA, LB)
    set_dp_start(dp)
    for i in range(LA):
        for j in range(LB):
            v = dp[i][j]
            if a[i] == b[j]:
                update_dp_same_char(dp, i, j, v)
            else:
                update_dp_diff_char(dp, i, j, v)
            update_dp_delete_from_a(dp, i, j, v)
            update_dp_delete_from_b(dp, i, j, v)
        update_dp_delete_rest_of_a(dp, i, LB)
    for j in range(LB):
        update_dp_delete_rest_of_b(dp, LA, j)
    return dp[LA][LB]

def is_length_diff_too_big(LA, LB, D):
    return abs(LA - LB) > D

def diff_indices_and_chars(a, b, LA):
    ra, rb, rp = [], [], []
    for i in range(LA):
        if a[i] != b[i]:
            rp.append(i)
            ra.append(a[i])
            rb.append(b[i])
    return ra, rb, rp

def is_transposition(rp, ra, rb):
    if len(rp) == 2 and rp[1] - rp[0] == 1:
        ra_reversed = list(ra)
        ra_reversed.reverse()
        if ra_reversed == rb:
            return True
    return False

def is_double_transposition(rp, ra, rb):
    if len(rp) == 4 and rp[1] - rp[0] == 1 and rp[3] - rp[2] == 1:
        new_ra = list(ra)
        new_ra[0], new_ra[1] = new_ra[1], new_ra[0]
        new_ra[2], new_ra[3] = new_ra[3], new_ra[2]
        if new_ra == rb:
            return True
    return False

def swap_adjacent(lst, i):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

def is_swap_inside_merging(a, b, LA, LB, D, dist_func):
    orig_a, orig_b = a, b
    if not LA < LB:
        LA, LB = LB, LA
        a, b = b[:], a[:]
    else:
        a = list(a)
        b = list(b)
    for i in range(LA - 1):
        swap_adjacent(a, i)
        if dist_func(a, b) <= D - 1:
            return True
        for j in range(LA - 1):
            swap_adjacent(a, j)
            if a == b:
                return True
            swap_adjacent(a, j)
        swap_adjacent(a, i)
    return False

def is_within_distance_D(a, b, D, dist_func):
    LA, LB = get_lengths(a, b)
    if is_length_diff_too_big(LA, LB, D):
        return False
    d = dist_func(a, b)
    if d <= D:
        return True
    if d == 2 and LA == LB:
        ra, rb, rp = diff_indices_and_chars(a, b, LA)
        if is_transposition(rp, ra, rb):
            return True
    if D == 2:
        if d == 4 and LA == LB:
            ra, rb, rp = diff_indices_and_chars(a, b, LA)
            if is_double_transposition(rp, ra, rb):
                return True
        if d == 3 and abs(LA - LB) < D:
            if is_swap_inside_merging(a, b, LA, LB, D, dist_func):
                return True
    return False

def collect_similar_pairs(S, N, D, dist_func):
    pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            if is_within_distance_D(S[i], S[j], D, dist_func):
                if S[i] < S[j]:
                    pairs.append((S[i], S[j]))
                else:
                    pairs.append((S[j], S[i]))
    return pairs

def output_pairs(ans):
    ans.sort()
    for e in ans:
        write("%s,%s\n" % e)
    write("%d\n" % len(ans))

def solve():
    N = parse_int()
    if N == 0:
        return False
    D = parse_int()
    S = parse_strings(N)
    ans = collect_similar_pairs(S, N, D, levenshtein_distance)
    output_pairs(ans)
    return True

def main_loop():
    while solve():
        ...

main_loop()