def read_input():
    return int(input())

def initialize_B(N):
    return [0] * N

def process_edges(N, B):
    for _ in range(N - 1):
        x, y, a = parse_edge_input()
        update_B_edges(B, x, y, a)

def parse_edge_input():
    return map(int, input().split())

def update_B_edges(B, x, y, a):
    apply_XOR(B, x, a)
    apply_XOR(B, y, a)

def apply_XOR(B, idx, a):
    B[idx] ^= a

def count_B_occurrences(B):
    D = {}
    for b in B:
        increment_dict_count(D, b)
    return D

def increment_dict_count(D, b):
    D[b] = D.get(b, 0) + 1

def reset_zero_occurrence(D):
    D[0] = 0

def compute_ans_and_first(D):
    ans = 0
    first = 0
    for b in D:
        ans = add_half(D, b, ans)
        if D[b]%2:
            first = update_first(first, b)
    return ans, first

def add_half(D, b, ans):
    return ans + D[b] // 2

def update_first(first, b):
    return first | (1 << b)

def initialize_A():
    size = 1 << 16
    A = [0] * size
    for i in range(1, size):
        bit = least_significant_bit(i)
        l = get_bit_index(bit)
        A[i] = A[i ^ bit] ^ l
    return A

def least_significant_bit(i):
    return i & -i

def get_bit_index(bit):
    return len(bin(bit)) - 3

def create_memo():
    return {0: 0}

def dfs_setup(A):
    memo = create_memo()
    def dfs(state):
        if state in memo:
            return memo[state]
        cur = state
        res = 10 ** 9 + 7
        while cur:
            if check_A_is_zero(A, cur):
                res = min(res, dfs(state ^ cur) + popcount(cur) - 1)
            cur = decrement_subset(cur, state)
        memo[state] = res
        return res
    return dfs

def check_A_is_zero(A, cur):
    return A[cur] == 0

def popcount(val):
    return bin(val).count('1')

def decrement_subset(cur, state):
    cur -= 1
    cur &= state
    return cur

def main():
    N = read_input()
    B = initialize_B(N)
    process_edges(N, B)
    D = count_B_occurrences(B)
    reset_zero_occurrence(D)
    ans, first = compute_ans_and_first(D)
    A = initialize_A()
    dfs = dfs_setup(A)
    ans += dfs(first)
    print(ans)

main()