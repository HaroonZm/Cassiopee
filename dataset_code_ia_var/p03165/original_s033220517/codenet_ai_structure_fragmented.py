import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**7)

def get_stdin():
    return sys.stdin

def read_line(stdin):
    return stdin.readline()

def li(stdin):
    return map(int, read_line(stdin).split())

def li_(stdin):
    return map(lambda x: int(x)-1, read_line(stdin).split())

def lf(stdin):
    return map(float, read_line(stdin).split())

def ls(stdin):
    return read_line(stdin).split()

def ns(stdin):
    return read_line(stdin).rstrip()

def lc(stdin):
    return list(ns(stdin))

def ni(stdin):
    return int(read_line(stdin))

def nf(stdin):
    return float(read_line(stdin))

def get_input_string(stdin):
    return ns(stdin)

def get_strings(stdin):
    s = get_input_string(stdin)
    t = get_input_string(stdin)
    return s, t

def get_length(s):
    return len(s)

def create_dp_matrix(lens, lent):
    return [[0]*(lent+1) for _ in range(lens+1)]

def fill_dp_for_indices(idx, lens, lent, s, t, dp):
    for jdx in range(lent):
        update_dp_cell(idx, jdx, s, t, dp)

def update_dp_cell(idx, jdx, s, t, dp):
    a = get_dp_northwest_plus_match(idx, jdx, s, t, dp)
    b = get_dp_west(idx, jdx, dp)
    c = get_dp_north(idx, jdx, dp)
    dp[idx+1][jdx+1] = max(a, b, c)

def get_dp_northwest_plus_match(idx, jdx, s, t, dp):
    return dp[idx][jdx] + int(s[idx] == t[jdx])

def get_dp_west(idx, jdx, dp):
    return dp[idx+1][jdx]

def get_dp_north(idx, jdx, dp):
    return dp[idx][jdx+1]

def fill_dp(lens, lent, s, t, dp):
    for idx in range(lens):
        fill_dp_for_indices(idx, lens, lent, s, t, dp)

def check_base_case_lcs(spos, tpos):
    return spos == 0 or tpos == 0

def get_dp_north_lcs(spos, tpos, dp):
    return dp[spos-1][tpos]

def get_dp_west_lcs(spos, tpos, dp):
    return dp[spos][tpos-1]

def get_dp_northwest_lcs(spos, tpos, dp):
    return dp[spos-1][tpos-1]

def get_dp_current(spos, tpos, dp):
    return dp[spos][tpos]

def add_char_to_result(cur, s, spos):
    return cur + s[spos-1]

def lcs_impl(spos, tpos, cur, s, t, dp):
    if check_base_case_lcs(spos, tpos):
        return cur
    nrth = get_dp_north_lcs(spos, tpos, dp)
    west = get_dp_west_lcs(spos, tpos, dp)
    ntws = get_dp_northwest_lcs(spos, tpos, dp)
    mx = max(nrth, west, ntws)
    curval = get_dp_current(spos, tpos, dp)

    if mx == ntws and ntws+1 == curval:
        next_cur = add_char_to_result(cur, s, spos)
        return lcs_impl(spos-1, tpos-1, next_cur, s, t, dp)
    elif mx == nrth:
        return lcs_impl(spos-1, tpos, cur, s, t, dp)
    else:
        return lcs_impl(spos, tpos-1, cur, s, t, dp)

def reverse_str(s):
    return s[::-1]

def main():
    set_recursion_limit()
    stdin = get_stdin()
    s, t = get_strings(stdin)
    lens = get_length(s)
    lent = get_length(t)
    dp = create_dp_matrix(lens, lent)
    fill_dp(lens, lent, s, t, dp)
    lcs_result = lcs_impl(lens, lent, "", s, t, dp)
    print(reverse_str(lcs_result))

main()