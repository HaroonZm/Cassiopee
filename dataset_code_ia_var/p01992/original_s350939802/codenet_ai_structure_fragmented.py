from collections import deque

def get_input_size():
    return int(input())

def create_indices_list(size):
    return [deque() for _ in range(size)]

def char_to_index(c):
    return ord(c) - ord('a')

def get_char():
    return input()[0]

def populate_chars_and_indices(N, cs, idxs):
    for i in range(N):
        c = get_char()
        cs.append(c)
        ci = char_to_index(c)
        idxs[ci].append(i)

def initialize_dp(N):
    dp = [i for i in range(N)]
    dp[0] = 0
    return dp

def update_dp_at_position(i, dp):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)

def has_multiple_indices(ci, idxs):
    return len(idxs[ci]) >= 2

def pop_left_index(ci, idxs):
    idxs[ci].popleft()

def get_next_index(ci, idxs):
    return idxs[ci][0]

def set_dp_next_index(pi, i, dp):
    dp[pi] = dp[i]

def process_dp(N, cs, idxs, dp):
    for i in range(N):
        c = cs[i]
        ci = char_to_index(c)
        update_dp_at_position(i, dp)
        if not has_multiple_indices(ci, idxs):
            continue
        pop_left_index(ci, idxs)
        pi = get_next_index(ci, idxs)
        set_dp_next_index(pi, i, dp)

def print_result(dp):
    print(dp[-1] + 1)

def main():
    N = get_input_size()
    idxs = create_indices_list(26)
    cs = []
    populate_chars_and_indices(N, cs, idxs)
    dp = initialize_dp(N)
    process_dp(N, cs, idxs, dp)
    print_result(dp)

main()