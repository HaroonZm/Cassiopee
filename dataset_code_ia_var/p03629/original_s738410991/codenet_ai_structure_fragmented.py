from bisect import bisect_left

def read_input():
    return [ord(i) - 97 for i in input()]

def append_range(A):
    return A + list(range(26))

def reverse_list(A):
    return A[::-1]

def initialize_dp():
    return [0] * 26

def initialize_key_val():
    return ([[] for _ in range(26)], [[] for _ in range(26)])

def process_A(A, dp, key, val):
    for i, a in enumerate(A):
        update_dp_key_val(i, a, dp, key, val)

def update_dp_key_val(i, a, dp, key, val):
    x = min(dp) + 1
    dp[a] = x
    key[a].append(i)
    val[a].append(x)

def find_min_index(dp):
    return dp.index(min(dp))

def compute_initial_x(dp):
    return dp[find_min_index(dp)] + 1

def compute_initial_pos():
    return 10**6

def main_loop(dp, key, val):
    ret = ''
    x = compute_initial_x(dp)
    pos = compute_initial_pos()
    while True:
        found, ret, x, pos = loop_once(key, val, ret, x, pos)
        if not found:
            break
    return ret

def loop_once(key, val, ret, x, pos):
    for i in range(26):
        if key[i] and key[i][0] < pos:
            j = bisect_left(key[i], pos) - 1
            if val[i][j] == x - 1:
                ret += chr(i + 97)
                pos = key[i][j]
                x -= 1
                return True, ret, x, pos
    return False, ret, x, pos

def print_result(ret):
    print(ret)

def main():
    A = read_input()
    A = append_range(A)
    A = reverse_list(A)
    dp = initialize_dp()
    key, val = initialize_key_val()
    process_A(A, dp, key, val)
    ret = main_loop(dp, key, val)
    print_result(ret)

main()