def read_input():
    import sys
    input = sys.stdin.readline
    n, m = parse_nm(input)
    ks = read_ks(m, input)
    p = read_p(input)
    return n, m, ks, p

def parse_nm(input):
    return list(map(int, input().rstrip('\n').split()))

def read_ks(m, input):
    return [parse_ks_line(input) for _ in range(m)]

def parse_ks_line(input):
    return list(map(int, input().rstrip('\n').split()))

def read_p(input):
    return list(map(int, input().rstrip('\n').split()))

def generate_switch_states(n):
    import itertools
    return itertools.product([True, False], repeat=n)

def evaluate_switch_state(v, ks, p):
    for j, vv in enumerate(ks):
        cnt = count_on_switches(v, vv)
        if not is_correct_parity(cnt, p[j]):
            return False
    return True

def count_on_switches(v, vv):
    count = 0
    for i in range(vv[0]):
        idx = get_switch_index(vv, i)
        if is_switch_on(v, idx):
            count += 1
    return count

def get_switch_index(vv, i):
    return vv[i+1] - 1

def is_switch_on(v, idx):
    return v[idx]

def is_correct_parity(cnt, expected_parity):
    return cnt % 2 == expected_parity

def increment_counter_if_valid(v, ks, p, a_cnt):
    if evaluate_switch_state(v, ks, p):
        a_cnt[0] += 1

def solve_logic(n, m, ks, p):
    a_cnt = [0]
    for v in generate_switch_states(n):
        increment_counter_if_valid(v, ks, p, a_cnt)
    return a_cnt[0]

def print_result(result):
    print(result)

def slove():
    n, m, ks, p = read_input()
    result = solve_logic(n, m, ks, p)
    print_result(result)

if __name__ == '__main__':
    slove()