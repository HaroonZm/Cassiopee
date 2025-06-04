def read_input():
    return map(int, raw_input().split())

def is_termination_case(n, k, m):
    return n == 0 and k == 0 and m == 0

def create_stones_list(n):
    return list(range(1, n + 1))

def get_initial_indices(m, k):
    return m - 1, k - 1

def remove_stone(stones, m):
    stones.pop(m)

def update_index(m, k, length):
    return (m + k) % length

def solve_case(n, k, m):
    stones = create_stones_list(n)
    m_idx, k_val = get_initial_indices(m, k)
    while len(stones) != 1:
        remove_stone(stones, m_idx)
        m_idx = update_index(m_idx, k_val, len(stones))
    return stones[0]

def print_output(result):
    print result

def process_one_case():
    n, k, m = read_input()
    if is_termination_case(n, k, m):
        return False
    result = solve_case(n, k, m)
    print_output(result)
    return True

def main_loop():
    while process_one_case():
        continue

def main():
    main_loop()

main()