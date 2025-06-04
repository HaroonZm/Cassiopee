import sys
from itertools import product

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def get_N():
    return int(input())

def get_S():
    return [0 if i == 'o' else 1 for i in input()]

def possible_patterns():
    return list(product(range(2), repeat=2))

def initialize_pattern(i, j, N):
    pat = [i, j] + [0]*(N - 2)
    return pat

def compute_pattern(pat, S, N):
    for k in range(2, N):
        pat[k] = calc_patern_element(S, pat, k)
    return pat

def calc_patern_element(S, pat, k):
    return (S[k - 1] - (pat[k - 1] + pat[k - 2])) % 2

def check_last(S, pat):
    return S[-1] == (pat[0] + pat[-1] + pat[-2]) % 2

def check_first(S, pat):
    return S[0] == (pat[1] + pat[0] + pat[-1]) % 2

def to_answer(pat, N):
    return ['S' if pat[k] == 0 else 'W' for k in range(N)]

def print_answer(ans):
    print(''.join(ans))

def print_fail():
    print(-1)

def try_one_pattern(i, j, N, S):
    pat = initialize_pattern(i, j, N)
    pat = compute_pattern(pat, S, N)
    if not check_last(S, pat):
        return False
    if not check_first(S, pat):
        return False
    ans = to_answer(pat, N)
    print_answer(ans)
    return True

def solve():
    N = get_N()
    S = get_S()
    pats = possible_patterns()
    for i, j in pats:
        if try_one_pattern(i, j, N, S):
            return None
    print_fail()

if __name__ == '__main__':
    solve()